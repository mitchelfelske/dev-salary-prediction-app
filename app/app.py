from flask import Flask, request

# create an app instance
app = Flask(__name__)

# at the end point /, call method hello
@app.route("/")
def hello():
    return "Hello World!"

@app.route("/predict", methods=["POST"])
def predict():
    data = {
        'country': request.form['country'],
        'education': request.form['education'],
        'devtype': request.form['devtype'],
        'yearscode': request.form['yearscode']
    }
    return data

# run the flask app
if __name__ == "__main__":
    app.run()
