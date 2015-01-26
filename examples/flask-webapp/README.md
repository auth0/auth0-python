#Auth0 + Python WebApp Seed
This is the seed project you need to use if you're going to create a Regular WebApp with Python. If you want to build a Python API that will be used with a SPA or a Mobile device, please check this [other seed project](https://github.com/auth0/auth0-python/tree/master/examples/flask-api)

#Running the example
In order to run the example you need to have `python` and `pip` installed.

You also need to set the ClientSecret, ClientId, Domain and CallbackURL for your Auth0 app as enviroment variables with the following names respectively: AUTH0_CLIENT_SECRET, AUTH0_CLIENT_ID, AUTH0_DOMAIN and AUTH0_CALLBACK_URL.

For that, if you just create a file named .env in the directory and set the values like the following, the app will just work:

````bash
# .env file
AUTH0_CLIENT_SECRET=myCoolSecret
AUTH0_CLIENT_ID=myCoolClientId
AUTH0_DOMAIN=samples.auth0.com
AUTH0_CALLBACK_URL=http://localhost:3000/auth/auth0/callback
````
Once you've set those 4 enviroment variables, just run `python server.py` and try calling [http://localhost:3000/](http://localhost:3000/)
