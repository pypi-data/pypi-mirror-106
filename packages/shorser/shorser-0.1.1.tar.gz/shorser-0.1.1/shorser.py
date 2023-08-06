# -*- coding: utf-8 -*-
#
# Copyright (c) 2021~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

from typing import Any, Optional
import functools
import json

TYPE_TRUE           = ord(b'y')
TYPE_FALSE          = ord(b'n')
TYPE_BYTES          = ord(b'b')
TYPE_INT            = ord(b'i')
TYPE_STRING         = ord(b's')
TYPE_USER_BYTES     = ord(b'u')
TYPE_USER_STRING    = ord(b'x')

def _byte(val: int) -> bytes:
    return val.to_bytes(1, 'little')

_LOAD_CONVS = {
    TYPE_FALSE:  lambda _: False,
    TYPE_TRUE:   lambda _: True,
    TYPE_BYTES:  lambda v: v,
    TYPE_INT:    lambda v: int.from_bytes(v, 'little', signed=True),
    TYPE_STRING: lambda v: v.decode('utf-8'),
}

_DUMP_CONVS = {
    type(None): lambda _: None,
    bool:   lambda v: _byte(TYPE_TRUE if v else TYPE_FALSE),
    bytes:  lambda v: _byte(TYPE_BYTES)  + v,
    int:    lambda v: _byte(TYPE_INT)    + v.to_bytes((v.bit_length() + 7) // 8, 'little', signed=True),
    str:    lambda v: _byte(TYPE_STRING) + v.encode('utf-8')
}

def load(value: Optional[bytes], base_load) -> Any:
    if base_load is None: raise TypeError
    if not value:
        return None
    v0 = value[0]
    if v0 == TYPE_USER_BYTES:
        return base_load(value[1:])
    elif v0 == TYPE_USER_STRING:
        return base_load(value[1:].decode('utf-8'))
    try:
        conv = _LOAD_CONVS[v0]
    except KeyError:
        raise NotImplementedError
    else:
        return conv(value[1:])

def dump(value: Any, base_dump) -> bytes:
    if base_dump is None: raise TypeError
    try:
        conv = _DUMP_CONVS[type(value)]
    except KeyError:
        pass
    else:
        return conv(value)
    rv = base_dump(value)
    if isinstance(rv, str):
        return _byte(TYPE_USER_STRING) + rv.encode('utf-8')
    else:
        return _byte(TYPE_USER_BYTES) + rv

def wrap_load(base_load):
    return functools.update_wrapper(
        functools.partial(load, base_load=base_load),
        base_load
    )

def wrap_dump(base_dump):
    return functools.update_wrapper(
        functools.partial(dump, base_dump=base_dump),
        base_dump
    )

# for json
jload = wrap_load(lambda b: json.loads(b.decode('utf-8')))
jdump = wrap_dump(lambda v: json.dumps(v).encode('utf-8'))

__all__ = [
    'load', 'dump',
    'wrap_load', 'wrap_dump',
    'jload', 'jdump',
]
