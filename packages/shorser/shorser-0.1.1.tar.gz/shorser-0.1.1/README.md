# shorser

Shorter serializer. Helpful if you are using `sqlitedict` / `filecache` to store key value pairs.

## Usage

To use shorser with std json backend:

``` py
from shorser import jdump, jload

bytes_buf = jdump(obj)
obj = jload(bytes_buf)
```

## Compare with JSON

| Value        | JSON (utf-8 encoded) | shorser (with JSON backend)                                  | Saved bytes |
| ------------ | -------------------- | ------------------------------------------------------------ | ----------- |
| `None`       | `b'null'`            | `None`                                                       | 4           |
| `True`       | `b'true'`            | `b'y'`                                                       | 3           |
| `False`      | `b'false'`           | `b'n'`                                                       | 3           |
| `100`        | `b'100'`             | `b'id'` (store integer in little order bytes, with prefix `i`) | a lot       |
| `'vnais'`    | `b'"vnais"'`         | `b'svnais'`                                                  | 1           |
| `b'dsads15'` | Not Support          | `b'bdsads15'`                                                |             |
| `{'a': 10}`  | `b'{"a": 10}'`       | `b'u{"a": 10}'`                                              | -1          |

- shorser is support `bytes` type;
- integer type is unreadable;
- in most cases, shorser is smaller than backend (like JSON);
- in most cases, shorser is faster than backend (like JSON);
