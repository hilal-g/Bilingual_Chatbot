import os
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
    print("Training already done. Chatbot is ready!")

else:

    model.fit(training, 
            output, 
            n_epoch=1000, 
            batch_size=8,
            show_metric=True)

    model.save("model.tflearn")