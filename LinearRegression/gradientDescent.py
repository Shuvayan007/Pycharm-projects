import numpy as np

class LinearRegressionGD:
    def __init__(self,learning_rate=0.001,epochs=10000):

        self.coef_=None
        self.intercept_=None
        self.learning_rate=learning_rate
        self.epochs=epochs

    def fit(self,X_train,y_train):
        #Start with random values of beta:
        self.intercept_=0
        self.coef_=np.ones(X_train.shape[1])
        print('_________________________________________________________________')

        #update
        for epoch in range(self.epochs):

            y_hat=np.dot(X_train,self.coef_)+self.intercept_

            i_der=-2*np.mean(y_train - y_hat)
            self.intercept_=self.intercept_-self.learning_rate*i_der

            c_der=-2*(np.dot(y_train - y_hat,X_train)/X_train.shape[0])

            self.coef_=self.coef_-self.learning_rate * c_der

            # print(self.intercept_)
            # print(self.coef_)

            #Calculate the loss
            # loss=np.dot(y_train-y_hat,y_train-y_hat)/X_train.shape[0]
            #
            # print(loss)


    def predict(self,X_test):

        y_pred = np.dot(X_test, self.coef_) + self.intercept_
        return y_pred