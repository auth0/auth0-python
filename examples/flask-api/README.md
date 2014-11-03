# Auth0 + Python + Flask API Seed
This is the seed project you need to use if you're going to create a Python + Flask API. You'll mostly use this API either for a SPA or a mobile app. If you just want to create a regular Python web app, please check [this other seed project](https://github.com/auth0/auth0-python/tree/master/examples/flask-webapp)

This example is deployed to Heroku at http://auth0-python-flaskapi-sample.herokuapp.com/ping

# Running the example
In order to run the example you need to have `python` and `pip` installed.

You also need to set the client ID and secret from your Auth0 app as enviroment variables with the following names respectively: `AUTH0_CLIENT_ID` and `AUTH0_CLIENT_SECRET`.

For that, if you just create a file named `.env` in the directory and set the values like the following, the app will just work:

````bash
# .env file
AUTH0_CLIENT_SECRET=myCoolSecret
AUTH0_CLIENT_ID=myCoolClientId
````

Once you've set those two enviroment variables, just run `python server.py` and try calling [http://localhost:3001/ping](http://localhost:3001/ping)

You can then try to do a GET to [http://localhost:3001/secured/ping](http://localhost:3001/secured/ping) which will throw an error if you don't send the JWT in the header.
