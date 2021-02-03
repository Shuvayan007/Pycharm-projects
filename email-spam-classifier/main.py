from flask import Flask,render_template,request
import pickle
import numpy as np

cv=pickle.load(open('imports/vectorizer.pkl','rb'))
clf=pickle.load(open('imports/classifier.pkl','rb'))

app=Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/predict',methods=['post'])
def predict():
    email= request.form.get("email")

    input_email=cv.transform(np.array([email])).toarray()
    print(input_email.shape)

    y_pred=clf.predict(input_email)

    print(y_pred)

    return render_template("index.html",label=y_pred[0])

if __name__=='__main__':
    app.run(debug=True)