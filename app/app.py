from flask import Flask, request, render_template
import pickle

# create an app instance
app = Flask(__name__)

# load the model & label encoding files
model_file = pickle.load(open('../resources/model.pkl', 'rb'))
model = model_file['model']
country_mapping = model_file['country_mapping']
education_mapping = model_file['education_mapping']
devtype_mapping = model_file['devtype_mapping']

# load the scaler
scaler = pickle.load(open('../resources/scaler.pkl', 'rb'))

# at the end point /, call method hello
@app.route("/")
def home():
    return render_template('home.html')

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

    # Feature scaling
    # The wrapped brackets are used to convert the data into a 2D array (lines, columns)
    standardized_data = scaler.transform([list(data.values())])

    # Model prediction
    prediction = model.predict(standardized_data)

    return "$ {} [valor anual]".format(round(prediction[0], 2))

# run the flask app
if __name__ == "__main__":
    app.run()
