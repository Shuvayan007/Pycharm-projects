from flask import Flask,render_template,request
import pickle
import numpy as np

app=Flask(__name__)

# status_encoder=pickle.load(open('model/status_encoder.pkl','rb'))
# transaction_encoder=pickle.load(open('model/transaction_encoder.pkl','rb'))
# type_encoder=pickle.load(open('model/type_encoder.pkl','rb'))

ohe=pickle.load(open('model/ohe.pkl','rb'))
locality_df=pickle.load(open('model/locality_df.pkl','rb'))

#Predictioon model
reg=pickle.load(open('model/model.pkl','rb'))

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/predict',methods=['POST'])
def predict():
    # recieve form data here
    area=request.form.get('area')
    bhk = int(request.form.get('bhk'))  #Type casting
    bathrooms = float(request.form.get('bathrooms'))    #Type casting
    status = request.form.get('status')
    transaction = request.form.get('transaction')
    property = request.form.get('property')
    locality = request.form.get('locality')

    per_sqft=locality_df[locality_df['Locality']==locality]['Per_Sqft'].mean()

    # Onehot encode bhk and bathroom

    X_trans=ohe.transform(np.array([[bhk,bathrooms]])).toarray()

    # Label encode status, transaction and property

    ##Automated encoding
    # status=status_encoder.transform(status)
    # transaction=transaction_encoder.transform(transaction)
    # property=type_encoder.transform(property)

    # Derive per_sqft value from locality

    #Mannual encoder: (Label encoding)
    if status=='Ready_to_move':
        status=1
    else:
        status=0

    if transaction=='New_Property':
        transaction=0
    else:
        transaction=1

    if property=='Builder_Floor':
        property=1
    else:
        property=0

    X=np.array([[area,status,transaction,property,per_sqft]])

    # print(area)
    # print(bhk)
    # print(bathrooms)
    # print(status)
    # print(transaction)
    # print(property)
    # print(locality)

    # print(X_trans)
    X=np.asarray(X, dtype='float64')

    X=np.hstack((X,X_trans))

    y_pred=reg.predict(X)

    # print(X)

    print(y_pred[0])

    return render_template('index.html',price=y_pred[0])

if __name__=="__main__":
    app.run(debug=True)