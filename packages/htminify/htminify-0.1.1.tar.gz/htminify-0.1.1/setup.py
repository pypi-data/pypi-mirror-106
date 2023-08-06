# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['htminify']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'htminify',
    'version': '0.1.1',
    'description': 'A lightweight html minifier for all Python web frameworks and WSGI apps.',
    'long_description': 'HTMinify\n========\nA lightweight HTML minifier for *all* Python web frameworks and WSGI apps.\n\nFeatures\n________\n\n* Using a web framework, like django, flask, and pyramid? We got you covered.\n* Or you\'re feeling adventurous and you\'re building your own wsgi app? We got you covered there too. This will work with any program that complies with the WSGI specification\n* Using an encoding that is not UTF-8? Just pass an argument,and we\'ll take it from there. 😉   \n* Mixing Javascript and html? We\'ll try to minify that too, without judging you too much. (No promises though😜).\n* No external dependencies.\n\nInstallation\n____________\nWith pip \n\n.. code-block:: bash\n\n    $ pip install htminify\n\nWith poetry\n\n.. code-block:: bash\n\n    $ poetry add htminify\n\n\nUsage\n_____\n\n**For Django**\n\nThe middleware goes in your ``wsgi.py`` file. An example ``wsgi.py`` will look like this.\n\n.. code-block:: Python\n\n    # wsgi.py\n    import os\n\n    from django.core.wsgi import get_wsgi_application\n    from htminify.wsgi import StripWhitespaceMiddleware # add this!\n    os.environ.setdefault(\'DJANGO_SETTINGS_MODULE\', \'website.settings\')\n\n    application = get_wsgi_application()\n    application = StripWhitespaceMiddleware(application) # add this too!\n    \n\n\n**For Flask**\n\nFlask provides access to its wsgi app, which you can pass as an argument to the middleware. \nYou are essentially wrapping the middleware around the wsgi application.\nAn example flask file would be like this.\n\n.. code-block:: Python\n\n    # app.py\n    from flask import Flask\n    from htminify.wsgi import StripWhitespaceMiddleware # add this!\n\n    app = Flask(__name__)\n    app.wsgi_app = StripWhitespaceMiddleware(app.wsgi_app) # add this too!\n    \n    @app.route(\'/\')\n    def hello():\n        return "Hello, world."\n\n    if __name__=="__main__":\n        app.run()\n\n\nNote that we are wrapping the ``app.wsgi_app`` object and not the ``app`` object.\n\n**For any other wsgi framework**\n\n\nA similar procedure can be followed to integrate the middleware with other wsgi-Python web frameworks.\nJust wrap the middleware around the wsgi app.\n\n.. code-block:: Python\n\n    # app.py\n    from htminify.wsgi import StripWhitespaceMiddleware # add this!\n    wsgi_app = StripWhitespaceMiddleware(wsgi_app) # wrap around \n    \n\n\nConfiguration\n_____________\n\n**if you don\'t want to minify when debug is true**\n\nYou can do something like this\n\n.. code-block:: Python\n\n    # app.py\n    if not debug:\n        wsgi_app = StripWhitespaceMiddleware(wsgi_app) \n    \n**If you\'re using encoding other than UTF-8**\n\nPass the encoding-type to the middleware when wrapping the app.\n\n.. code-block:: Python\n\n    # app.py\n    from htminify.wsgi import StripWhitespaceMiddleware # add this!\n    wsgi_app = StripWhitespaceMiddleware(wsgi_app, "UTF-16") # pass the encoding\n\n\nTODO\n____\n\n*New Features*\n\n#. Minify Json content.\n#. Add ASGI support.\n\n*Documentation*\n\n* Generate Documentation and push to read the docs.\n* Add information for contributing.\n\n*Testing*\n\n* Improve test suite for wsgi middleware.\n',
    'author': 'Abhinav Omprakash',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/AbhinavOmprakash/py-htminify',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
