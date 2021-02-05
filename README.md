# flask-api-docs
Interface automation document based on flash


# Installation

It is possible to install the tool with pip:

```
pip install xt-FlaskAPIDocs
```

# Usage

Sample usage:

```python
from flask import Flask

from flask_api_demo.test.HelloWorld import HelloWorld
from flask_docs import BluePrint, Docs

app = Flask(__name__)

a = BluePrint('hello', __name__)

a.add_url_rule('/hello', 'hello', HelloWorld().hello_world, methods=['GET'], args={"test1": 'str', "test2": 'int'})
a.add_url_rule('/bye', 'bye', HelloWorld().bye_world, methods=['GET'], args={"test1": 'str', "test2": 'int'})
app.register_blueprint(a)
Docs(app, hide_docs=True)
```