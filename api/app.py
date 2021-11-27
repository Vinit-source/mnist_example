from flask import Flask
# from flask_restx import Resource, Api

# app = Flask(__name__)
# api = Api(app)

# @api.route('/hello')
# class HelloWorld(Resource):
#     def get(self):
#         return {'hello': 'world'}

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, request
import numpy as np
from joblib import load

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/svm_predict", methods=["POST"])
def svm_predict():
    best_model_path = "mnist_example/models/best_model_SVC/model.joblib"
    clf = load(best_model_path)
    print("Model loaded.")
    input_json = request.json
    image = input_json['image']
    print(image)
    image = np.array(image).reshape(1, -1)
    predicted = clf.predict(image)
    return str(predicted[0])


@app.route("/tree_predict", methods=["POST"])
def tree_predict():
    best_model_path = "mnist_example/models/best_model_DecisionTreeClassifier/model.joblib"
    clf = load(best_model_path)
    print("Model loaded.")
    input_json = request.json
    image = input_json['image']
    print(image)
    image = np.array(image).reshape(1, -1)
    predicted = clf.predict(image)
    return str(predicted[0])

'''
curl http://localhost:5000/predict -X POST  -H 'Content-Type: application/json' -d '{"image": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59", "60", "61", "62", "63", "64"]}'
'''