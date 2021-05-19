<<<<<<< HEAD
=======
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from LinearRegression import MyLR
from gradientDescent import LinearRegressionGD
from SGDRegressor import SGD

X,y=datasets.load_diabetes(return_X_y=True)

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=1)

#Batch Gradient Descent-->

reg=LinearRegressionGD(epochs=10000,learning_rate=0.1)

reg.fit(X_train,y_train)

y_pred= reg.predict(X_test)

from sklearn.metrics import r2_score
print('Batch GD',r2_score(y_test,y_pred))

#Stokastic Gradient Descent-->

sgd=SGD(epochs=10000,learning_rate=0.1)

sgd.fit(X_train,y_train)

y_pred1=sgd.predict(X_test)

print('SGD',r2_score(y_test,y_pred1))

#Mini-batch Gradient Descent-->



#OLE:

# print(X_train.shape)
# print(y_train.shape)

# reg=LinearRegression()

# reg1=MyLR()
#
# reg1.fit(X_train,y_train)
#
# y_pred=reg1.predict(X_test) #Needed

# reg.fit(X_train,y_train)

# y_pred=reg.predict((X_test))

# from sklearn.metrics import r2_score
# print(r2_score(y_test,y_pred)) #Needed

# print(reg.coef_)
# print(reg.intercept_)


#Assignment:
#Mini batch implementation to be done
>>>>>>> e0eef2396e87ff962e1d1c36b1c66370956b9211
