# Friendship Chart <3

I wanted to make a family tree of all my friends because I was confused about how we all knew each other. This is more or less what I came up with. It's a little flask app where you can type in your friends and how they know each other, and it'll make a little graph for you.

## Installation

1. Install requirements in an environment with `venv` and `pip`, or with `conda`; activate your environment
1. Add a secret key to your .env file, or just rename `example.env` --> `.env` and change the key inside.
1. Create a local database with `python models.py`
1. Run locally with `python app.py` or with flask via `FLASK_APP=app FLASK_ENV=development flask run --port=5777`
1. Navigate to localhost:5777 to see your app

## Deployment

This app is setup to be launched easily with fly.io - follow [fly's instructions](https://fly.io/docs/languages-and-frameworks/python/#launch-your-fly-app) to use `flyctl` to create and deploy an app. Don't forget to create an attached postgres instance! You'll additionally need to set your secret key using `flyctl secrets`.

### Automated Deploys

This app is also setup to deploy automatically to fly.io upon push to the `main` branch. To set this up, after launching the app, create a deployment API token with `fly tokens create deploy` and add it to your GitHub actions secrets. See [this guide](https://fly.io/docs/app-guides/continuous-deployment-with-github-actions/) for more info. To skip this entirely, delete the `.github/workflows/fly.yml` file.
