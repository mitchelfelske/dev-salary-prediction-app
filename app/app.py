from flask import Flask

# create an app instance
app = Flask(__name__)

# at the end point /, call method hello
@app.route("/")
def hello():
    return "Hello World!"

# run the flask app
if __name__ == "__main__":
    app.run()