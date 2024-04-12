from flask import Flask
from ml import predict_image #il faut impoter la fonction de l'autre fichier pour pouvoir l'appeler dans l'api 

app = Flask(__name__)

@app.route("/predict", methods= ["GET"])
def home():
    result = predict_image(None) #on appele notre fonction dans l'api
    return result 


if __name__ == '__main__':
    app.run(host= "0.0.0.0", port=8081)
