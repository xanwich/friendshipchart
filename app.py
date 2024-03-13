from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy


print("Friendship chart starting")

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

from routes import *  # NOQA

if __name__ == "__main__":
    app.logger.critical("start")
    app.run(debug=True, port=5777)
