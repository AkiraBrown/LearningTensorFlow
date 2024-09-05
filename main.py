import tensorflow as tf

string = tf.Variable("this is a string", tf.string)
number = tf.Variable(324, tf.int16)
floating = tf.Variable(3.567, tf.float64)

tensor1 = tf.ones([1,2,3]) #Creates a shape comprised of ones
tensor2 = tf.reshape(tensor1, [2,3,1]) # reshape existing data to shape [2,3,1]
tensor3 = tf.reshape(tensor2, [3,-1]) # -1 tells tensor to calculate the size of the dimension in that place
                                    # this will reshape the tensor to [3,2]
                                    # To figure how how many elements are in a shape 3*2 = 6
# print(tensor1)
# print(tensor2)
# print(tensor3)
# print(tensor1,tensor2,tensor3)


tensor4  = tf.constant([[1,2,3,4],[5,6,7,8]])
print(tensor4.shape)# Result is (2,4): 2 lists and 4 tensors in each list.
print(tensor4.dtype) # dtype reports back the datatype for each tensor in the shape. In this case we're using int32 because 
                    # each of the entries fall within the range of a 32 bit integer
