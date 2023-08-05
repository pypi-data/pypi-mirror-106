# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['clattr']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'clattr',
    'version': '0.0.1',
    'description': 'Construct a comand line interface based on a function or class',
    'long_description': '# clattr\n\nEasily make a command line interface from any interface in your code. How easily? This easy:\n\n```\nimport clattr\n\ndef my_program(a: int, b: str = "not provided"):\n  print(f"Running some code with: a={a}, b={b}")\n\nif __name__ == "__main__":\n  clattr.call(my_program)\n```\n\nThat\'s all it takes. Clattr will inspect your function and collect the values it needs it from command line arguments, environment variables, or config files, and then call it.\n\n```\npython examples/function --a 1\n```\n```\nRunning some code with: a=1, b=not provided\n```\n\n\nIf you want to think in a more data oriented design, you can have clattr construct a data object for you and use it as you please. \n\n```\nimport attr\nimport clattr\n\n\n@attr.s(auto_attribs=True, frozen=True)\nclass Basic:\n    a: int\n    b: str = "not provided"\n\ndef my_program(data: Basic):\n    # Your actual program will go here. For this example we just print the input.\n    print(data)\n\n\nif __name__ == "__main__":\n    data = clattr.call(Basic)\n    my_program(data)\n```\n\nThis could be invoked as\n```\npython examples/basic.py --a 1 --b hi\n```\nclattr will construct this object\n```\nBasic(a=1, b=\'hi\')\n```\nWhich you can then pass into the rest of your code as you please. The example simply prints it and then exits.\n\nOr if you have environment variables defined\n\n```\nexport A=1\nexport B=hi\npython example.py\n```\nagain yields\n```\nBasic(a=1, b=\'hi\')\n```\n\n`clattr` also supports nested objects (or functions taking complex objects as inputs)\n\n```\nfrom typing import Optional\nimport datetime as dt\n\nimport attr\nimport clattr\n\n\n@attr.s(auto_attribs=True, frozen=True)\nclass Foo:\n    a: dt.datetime\n    b: Optional[str] = None\n\n\n@attr.s(auto_attribs=True, frozen=True)\nclass Bar:\n    f: Foo\n    c: int\n\ndef my_program(data: Bar):\n    print(data)\n\nif __name__ == "__main__":\n    bar = clattr.call(Bar)\n    my_program(bar)\n```\n\nYou specify values for the fields in the nested class by referring to them with a their field name in the outer class\n\n```\npython examples/advanced.py --c 1 --f.a 2020-01-01 --f.b hi\n```\n```\nBar(f=Foo(a=1, b=\'hi\'), c=1)\n```\n\nYou can also supply one or more `json` formatted `config` files. Provide the name(s) of these files as positional arguments. `clattr`` will search them, last file first, for any keys fields that are not provided at the command line before searching the environment.\n\n```\npython examples/advanced.py --c 1 examples/foo.json\n```\n```\nBar(f=Foo(a=1, b=\'str\'), c=1)\n```\n\n`clattr` is inspired by [clout](https://github.com/python-clout/clout), but I wanted to try being a bit more opinionated to make both the library and code using it simpler.\n\n\n',
    'author': 'Tom Dimiduk',
    'author_email': 'tom@dimiduk.net',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6',
}


setup(**setup_kwargs)
