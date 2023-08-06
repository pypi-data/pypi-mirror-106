# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['shorser']
setup_kwargs = {
    'name': 'shorser',
    'version': '0.1.1',
    'description': 'a shorter serializer',
    'long_description': '# shorser\n\nShorter serializer. Helpful if you are using `sqlitedict` / `filecache` to store key value pairs.\n\n## Usage\n\nTo use shorser with std json backend:\n\n``` py\nfrom shorser import jdump, jload\n\nbytes_buf = jdump(obj)\nobj = jload(bytes_buf)\n```\n\n## Compare with JSON\n\n| Value        | JSON (utf-8 encoded) | shorser (with JSON backend)                                  | Saved bytes |\n| ------------ | -------------------- | ------------------------------------------------------------ | ----------- |\n| `None`       | `b\'null\'`            | `None`                                                       | 4           |\n| `True`       | `b\'true\'`            | `b\'y\'`                                                       | 3           |\n| `False`      | `b\'false\'`           | `b\'n\'`                                                       | 3           |\n| `100`        | `b\'100\'`             | `b\'id\'` (store integer in little order bytes, with prefix `i`) | a lot       |\n| `\'vnais\'`    | `b\'"vnais"\'`         | `b\'svnais\'`                                                  | 1           |\n| `b\'dsads15\'` | Not Support          | `b\'bdsads15\'`                                                |             |\n| `{\'a\': 10}`  | `b\'{"a": 10}\'`       | `b\'u{"a": 10}\'`                                              | -1          |\n\n- shorser is support `bytes` type;\n- integer type is unreadable;\n- in most cases, shorser is smaller than backend (like JSON);\n- in most cases, shorser is faster than backend (like JSON);\n',
    'author': 'Cologler',
    'author_email': 'skyoflw@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/Cologler/shorser-python',
    'py_modules': modules,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
