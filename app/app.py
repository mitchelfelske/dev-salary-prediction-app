from flask import Flask, request
import pickle

# create an app instance
app = Flask(__name__)

# load the model & label encoding files
model_file = pickle.load(open('../resources/model.pkl', 'rb'))

country_mapping = model_file['country_mapping']
education_mapping = model_file['education_mapping']
devtype_mapping = model_file['devtype_mapping']

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

    # Label encoding - mapping categorical to numerical values
    data['country'] = country_mapping[data['country']]
    data['education'] = education_mapping[data['education']]
    data['devtype'] = devtype_mapping[data['devtype']]
    data['yearscode'] = float(data['yearscode'])
    return data

# run the flask app
if __name__ == "__main__":
    app.run()
