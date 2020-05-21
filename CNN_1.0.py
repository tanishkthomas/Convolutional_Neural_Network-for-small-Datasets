import numpy as np
from keras import layers
from keras.layers import Input, Dense, Activation, ZeroPadding2D, BatchNormalization, Flatten, Conv2D
from keras.layers import MaxPooling2D
from keras.models import Model
from keras.preprocessing import image

#Everyone has a different dataset so data can be loaded by referring to Keras documentation 
X_train_orig, Y_train_orig, X_test_orig, Y_test_orig, classes = load_dataset()

# Normalize image vectors
X_train = X_train_orig/255.
X_test = X_test_orig/255.

# Reshape
Y_train = Y_train_orig.T
Y_test = Y_test_orig.T

def CNN_Model_1(input_shape): 
    X_input = Input(input_shape)
    
    X = ZeroPadding2D((3, 3))(X_input)
    X = Conv2D(32, (7, 7), strides=(1, 1), kernel_initializer='glorot_uniform',  name='conv0')(X)
    X = BatchNormalization(axis = 3, name = 'bn0')(X)
    X = Activation('relu')(X)
    X = MaxPooling2D(pool_size=(2, 2), strides=(1, 1))(X)
    
    X = Conv2D(16, (5, 5), strides=(1, 1), name='conv1')(X)
    X = BatchNormalization(axis = 3, name = 'bn1')(X)
    X = Activation('relu')(X)
    X = MaxPooling2D(pool_size=(2, 2), strides=(1, 1))(X)
    
    X = Flatten()(X)
    
    X = Dense(1, activation='sigmoid', name='fc1')(X)
    
    model = Model(inputs = X_input, outputs = X, name='HappyModel')    
    return model

#Creating the model
SmileModel = CNN_Model_1(X_train.shape[1:])

#Compiling the model
SmileModel.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])

#Fitting the model to the training set
SmileModel.fit(x=X_train, y=Y_train, epochs=50, batch_size=16) 

#Model evaluation
preds = SmileModel.evaluate(x = X_test, y = Y_test)