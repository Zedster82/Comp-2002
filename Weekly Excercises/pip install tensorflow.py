import numpy as np
import tensorflow as tf
from tensorflow.keras import layers

inputs = tf . keras . Input ( shape =( 784 ,) )

dense = layers . Dense ( 64 , activation =" relu ")
x = dense ( inputs )

x = layers . Dense (64 , activation =" relu ")( x)
outputs = layers . Dense ( 10 )( x)

model = tf . keras . Model ( inputs = inputs , outputs = outputs , name =" mnist_model ")
model . summary ()

( x_train , y_train ) ,( x_text , y_test )=tf . keras . datasets . mnist . loaddata ()
x_train = x_train.reshape ( 60000 , 784 ). astype (" float32 ")/ 255
x_test = x_test.reshape ( 10000 , 784 ). astype (" float32 ")/ 255

model . complie (
loss =tf . keras . losses . SparseCategoricalCrossentropy ( from_logits = True ) ,
optimizer =tf . keras . optimizers . RMSprop () ,
metrics =[" accruacy "],
)
history = model . fit ( x_train , y_train , batch_size =64 , epochs =2 , validation_split =0.2)
test_scores = model . evalute ( x_test , y_test , verbose =2)
print (" Test accuracy :", test_scores[1])
