import os
import sys
import tflearn 
import tensorflow.compat.v1 as tf

from preprocess import training, output

tf.reset_default_graph()

net = tflearn.input_data(shape=[None, len(training[0])])
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, 
                              len(output[0]), 
                              activation="softmax")
net = tflearn.regression(net)

model = tflearn.DNN(net)

if os.path.exists("model.tflearn" + ".meta"):
    model.load("model.tflearn")

else:

    print('\033[1m' + '\n'
          "Chatbot is not ready. " 
          + "Please train the model first by running 'python3 train.py'." 
          + '\n' + '\033[0m')

    sys.exit()

    