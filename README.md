# Convolutional_Neural_Network-for-small-Datasets

This particular CNN Architechture is inspired by the famous CNN LeNet 5 architechure and three layers.
Firstly, an initial padding is done after which the first convolutional layer is applied followed by a second convolutional layer and finally a fully connected layer. The problem in hand was a binary classification of smile detection hence a sigmoid function as used in the output layer but, if it was a multi-class classification problem then softmax function be used thereby. The CNN is compiled using an adam optimizer(since it combines the concept of RMSprop and Momentum) and a binary_crossentropy loss function(since the problem I was dealing with was a binary classification problem), if the problem in hand is of multi-class classification then, crossentropy loss function can be used instead.
Keras is used to build this Neural Network architecture, which make it very easy to understand the architecture and its working.
