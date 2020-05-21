# Convolutional_Neural_Network-for-small-Datasets

This particular CNN Architechture is inspired by the famous CNN LeNet 5 architechure and three layers.
Firstly, an initial padding is done after which the first convolutional layer is applied followed by a second convolutional layer and finally a fully connected layer. The problem in hand was a binary classification of smile detection hence a sigmoid function as used in the output layer but, if it was a multi-class classification problem then softmax function be used thereby. The CNN is compiled using an adam optimizer(since it combines the concept of RMSprop and Momentum) and a binary_crossentropy loss function(since the problem I was dealing with was a binary classification problem), if the problem in hand is of multi-class classification then, crossentropy loss function can be used instead. The MaxPooling layer is used in such a way that the length and breadth dimensions of the image are reduced to half, there by reducing variance as well as computation.
Keras is used to build this Neural Network architecture, which make it very easy to understand the architecture and its working.
This CNN works in a way that can be related to our very fundamental linear regression, i.e., Z = W.A + b, and A' = g(Z), so, a lot of intuition can be derived.

# Few of the ending epochs of my model
...
Epoch 37/50
600/600 [==============================] - 33s - loss: 0.0574 - acc: 0.9900    
Epoch 38/50
600/600 [==============================] - 34s - loss: 0.1299 - acc: 0.9750    
Epoch 39/50
600/600 [==============================] - 34s - loss: 0.1681 - acc: 0.9733    
Epoch 40/50
600/600 [==============================] - 34s - loss: 0.1089 - acc: 0.9767    
Epoch 41/50
600/600 [==============================] - 34s - loss: 0.1308 - acc: 0.9767    
Epoch 42/50
600/600 [==============================] - 34s - loss: 0.0635 - acc: 0.9867    
Epoch 43/50
600/600 [==============================] - 34s - loss: 0.1302 - acc: 0.9783    
Epoch 44/50
600/600 [==============================] - 34s - loss: 0.1153 - acc: 0.9750    
Epoch 45/50
600/600 [==============================] - 34s - loss: 0.1275 - acc: 0.9817    
Epoch 46/50
600/600 [==============================] - 34s - loss: 0.0457 - acc: 0.9900    
Epoch 47/50
600/600 [==============================] - 33s - loss: 0.0465 - acc: 0.9883    
Epoch 48/50
600/600 [==============================] - 33s - loss: 0.0283 - acc: 0.9983    
Epoch 49/50
600/600 [==============================] - 33s - loss: 0.0228 - acc: 0.9983      
Epoch 50/50
600/600 [==============================] - 33s - loss: 0.0105 - acc: 0.9950    


# Finally the test accuracy
150/150 [==============================] - 3s     

Loss = 0.0530788719375
Test Accuracy = 0.986666666667
