This is a simple flask web service that outputs Hello with a date time.
It contains a Dockerfile that means the project can be served in a docker.

Please following the following process to serve the web service and test the docker:

Download the source code by git.

```
git clone ..

```

Then command into the directory where the source code is downloaded, run the following command to create docker container

```
docker build -t pythonhello .
```

Then start the docker

```
docker run -p 5000:5000 pythonhello
```

At this point you should see the following output in your command windows, this means the service is hosted successfully in the docker container:

```
_ Environment: production
WARNING: This is a development server. Do not use it in a production deployment.
Use a production WSGI server instead.
_ Debug mode: off \* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
```

And now you can connect to the API in the browser with the following URL:

```http://localhost:5000/hello/Andrew
```

You should see something similiar to the following in your browser:
￼
`
Hello there, Andrew! It's Saturday, 21 November, 2020 at 16:31:14.
`

For a full tutorial of creating a flask web service, please follow this tutorial,  

`https://code.visualstudio.com/docs/python/tutorial-flask`

The following are the issues I ran into for this tutorial, hopefully this will help you.
