'''
Create the scaffolding for a Flask-like framework.

>>> app = WebApp()
>>> @app.route("/")
... def index():
...     return 'Index Page'
...
>>> @app.route("/contact/")
... def contact():
...     return 'Contact Page'
...
>>> app.get("/")
'Index Page'
>>> app.get("/contact/")
'Contact Page'
>>> app.get("/no-such-page/")
'ERROR - no such page'


'''

# Write your code here:
class WebApp:
    def __init__(self):
        self.cache = dict()

    def route(self, endpoint):
        def wrapper(func):
            self.cache[endpoint] = func
            return func
        return wrapper

    def get(self, endpoint):
        try:
            return self.cache[endpoint]()
        except:
            return "ERROR - no such page"





# Do not edit any code below this line!

if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Copyright 2015-2016 Aaron Maxwell. All rights reserved.
