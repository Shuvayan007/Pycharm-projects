from flask import Flask,request,jsonify
#from flask_cors import CORS
import pickle
import pandas as pd
import numpy as np

fuel_encoder=pickle.load(open('models/fuel_encoder.pkl','rb'))
owner_encoder=pickle.load(open('models/owner_encoder.pkl','rb'))
brand_encoder=pickle.load(open('models/brand_encoder.pkl','rb'))
seller_encoder=pickle.load(open('models/seller_encoder.pkl','rb'))
transmission_encoder=pickle.load(open('models/transmission_encoder.pkl','rb'))
ohe=pickle.load(open('models/ohe.pkl','rb'))
rf_reg=pickle.load(open('models/rf_reg.pkl','rb'))
scaler=pickle.load(open('models/scaler.pkl','rb'))

app=Flask(__name__)
#CORS(app) #Added for a particular error, doesn't needed for me

@app.route('/')
def hello():
    return 'Hello'

@app.route('/predict',methods=['POST'])
def index():
    brand = request.form.get('brand')
    fuel = request.form.get('fuel')
    owner = request.form.get('owner')
    seller = request.form.get('seller')
    transmission = request.form.get('transmission')
    kms = int(request.form.get('kms'))
    old = 2020-int(request.form.get('year'))

    data=[[kms,fuel,seller,transmission,owner,brand,old]]

    df=pd.DataFrame(data,columns=['km','fuel','seller','transmission','owner','brand','old'])

    #Doing label encoding
    df['fuel'] = fuel_encoder.transform(df['fuel'])
    df['seller'] = seller_encoder.transform(df['seller'])
    df['transmission'] = transmission_encoder.transform(df['transmission'])
    df['owner'] = owner_encoder.transform(df['owner'])
    df['brand'] = brand_encoder.transform(df['brand'])

    #One hot encoding
    X_temp = ohe.transform(df[['owner', 'brand']]).toarray()

    X = df.drop(['owner', 'brand'], axis=1).values

    X=np.hstack((X, X_temp))

    X=scaler.transform(X)

    y_pred=rf_reg.predict(X)
    print(y_pred[0])
    dict={'price':y_pred[0]}
    return jsonify(dict)

if __name__=='__main__':
    app.run(debug=True)