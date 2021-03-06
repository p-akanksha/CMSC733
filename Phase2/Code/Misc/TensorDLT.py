import tensorflow as tf
import numpy as np
# import tensorflow.compat.v1 as tf
# tf.disable_v2_behavior()


# Auxiliary matrices used to solve DLT
Aux_M1  = np.array([
          [ 0 , 0 , 0 , 0  , 0 , 0 , 0 , 0 ],
          [ 1 , 0 , 0 , 0  , 0 , 0 , 0 , 0 ],
          [ 0 , 0 , 0 , 0  , 0 , 0 , 0 , 0 ],
          [ 0 , 0 , 1 , 0  , 0 , 0 , 0 , 0 ],
          [ 0 , 0 , 0 , 0  , 0 , 0 , 0 , 0 ],
          [ 0 , 0 , 0 , 0  , 1 , 0 , 0 , 0 ],
          [ 0 , 0 , 0 , 0  , 0 , 0 , 0 , 0 ],
          [ 0 , 0 , 0 , 0  , 0 , 0 , 1 , 0 ]], dtype=np.float64)

Aux_M2  = np.array([
          [ 0 , 0 , 0 , 0  , 0 , 0 , 0 , 0 ],
          [ 0 , 1 , 0 , 0  , 0 , 0 , 0 , 0 ],
          [ 0 , 0 , 0 , 0  , 0 , 0 , 0 , 0 ],
          [ 0 , 0 , 0 , 1  , 0 , 0 , 0 , 0 ],
          [ 0 , 0 , 0 , 0  , 0 , 0 , 0 , 0 ],
          [ 0 , 0 , 0 , 0  , 0 , 1 , 0 , 0 ],
          [ 0 , 0 , 0 , 0  , 0 , 0 , 0 , 0 ],
          [ 0 , 0 , 0 , 0  , 0 , 0 , 0 , 1 ]], dtype=np.float64)

Aux_M3  = np.array([
          [0],
          [1],
          [0],
          [1],
          [0],
          [1],
          [0],
          [1]], dtype=np.float64)



Aux_M4  = np.array([
          [-1 , 0 , 0 , 0  , 0 , 0 , 0 , 0 ],
          [0 , 0 , 0 , 0  , 0 , 0 , 0 , 0 ],
          [0 , 0 ,-1 , 0  , 0 , 0 , 0 , 0 ],
          [0 , 0 , 0 , 0  , 0 , 0 , 0 , 0 ],
          [0 , 0 , 0 , 0  ,-1 , 0 , 0 , 0 ],
          [0 , 0 , 0 , 0  , 0 , 0 , 0 , 0 ],
          [0 , 0 , 0 , 0  , 0 , 0 ,-1 , 0 ],
          [0 , 0 , 0 , 0  , 0 , 0 , 0 , 0 ]], dtype=np.float64)


Aux_M5  = np.array([
          [0 ,-1 , 0 , 0  , 0 , 0 , 0 , 0 ],
          [0 , 0 , 0 , 0  , 0 , 0 , 0 , 0 ],
          [0 , 0 , 0 ,-1  , 0 , 0 , 0 , 0 ],
          [0 , 0 , 0 , 0  , 0 , 0 , 0 , 0 ],
          [0 , 0 , 0 , 0  , 0 ,-1 , 0 , 0 ],
          [0 , 0 , 0 , 0  , 0 , 0 , 0 , 0 ],
          [0 , 0 , 0 , 0  , 0 , 0 , 0 ,-1 ],
          [0 , 0 , 0 , 0  , 0 , 0 , 0 , 0 ]], dtype=np.float64)

Aux_M6  = np.array([
          [-1 ],
          [ 0 ],
          [-1 ],
          [ 0 ],
          [-1 ],
          [ 0 ],
          [-1 ],
          [ 0 ]], dtype=np.float64)

Aux_M71 = np.array([
          [0 , 1 , 0 , 0  , 0 , 0 , 0 , 0 ],
          [1 , 0 , 0 , 0  , 0 , 0 , 0 , 0 ],
          [0 , 0 , 0 , 1  , 0 , 0 , 0 , 0 ],
          [0 , 0 , 1 , 0  , 0 , 0 , 0 , 0 ],
          [0 , 0 , 0 , 0  , 0 , 1 , 0 , 0 ],
          [0 , 0 , 0 , 0  , 1 , 0 , 0 , 0 ],
          [0 , 0 , 0 , 0  , 0 , 0 , 0 , 1 ],
          [0 , 0 , 0 , 0  , 0 , 0 , 1 , 0 ]], dtype=np.float64)

Aux_M72 = np.array([
          [1 , 0 , 0 , 0  , 0 , 0 , 0 , 0 ],
          [-1 , 0 , 0 , 0  , 0 , 0 , 0 , 0 ],
          [0 , 0 , 1 , 0  , 0 , 0 , 0 , 0 ],
          [0 , 0 ,-1 , 0  , 0 , 0 , 0 , 0 ],
          [0 , 0 , 0 , 0  , 1 , 0 , 0 , 0 ],
          [0 , 0 , 0 , 0  ,-1 , 0 , 0 , 0 ],
          [0 , 0 , 0 , 0  , 0 , 0 , 1 , 0 ],
          [0 , 0 , 0 , 0  , 0 , 0 ,-1 , 0 ]], dtype=np.float64)

Aux_M8  = np.array([
          [0 , 1 , 0 , 0  , 0 , 0 , 0 , 0 ],
          [0 ,-1 , 0 , 0  , 0 , 0 , 0 , 0 ],
          [0 , 0 , 0 , 1  , 0 , 0 , 0 , 0 ],
          [0 , 0 , 0 ,-1  , 0 , 0 , 0 , 0 ],
          [0 , 0 , 0 , 0  , 0 , 1 , 0 , 0 ],
          [0 , 0 , 0 , 0  , 0 ,-1 , 0 , 0 ],
          [0 , 0 , 0 , 0  , 0 , 0 , 0 , 1 ],
          [0 , 0 , 0 , 0  , 0 , 0 , 0 ,-1 ]], dtype=np.float64)
Aux_Mb  = np.array([
          [0 ,-1 , 0 , 0  , 0 , 0 , 0 , 0 ],
          [1 , 0 , 0 , 0  , 0 , 0 , 0 , 0 ],
          [0 , 0 , 0 , -1  , 0 , 0 , 0 , 0 ],
          [0 , 0 , 1 , 0  , 0 , 0 , 0 , 0 ],
          [0 , 0 , 0 , 0  , 0 ,-1 , 0 , 0 ],
          [0 , 0 , 0 , 0  , 1 , 0 , 0 , 0 ],
          [0 , 0 , 0 , 0  , 0 , 0 , 0 ,-1 ],
          [0 , 0 , 0 , 0  , 0 , 0 , 1 , 0 ]], dtype=np.float64)

def TensorDLT(H4pt, C4A , MiniBatchSize):
    
  pts_1_tile = tf.expand_dims(C4A, [2]) # BATCH_SIZE x 8 x 1
    
  # Solve for H using DLT
  pred_h4p_tile = tf.expand_dims(H4pt, [2]) # BATCH_SIZE x 8 x 1
  # 4 points on the second image
  pred_pts_2_tile = tf.add(pred_h4p_tile, pts_1_tile)


  # Auxiliary tensors used to create Ax = b equation
  M1_tile = tf.tile(tf.expand_dims(tf.constant(Aux_M1,tf.float32),[0]),[MiniBatchSize,1,1])
  M2_tile = tf.tile(tf.expand_dims(tf.constant(Aux_M2,tf.float32),[0]),[MiniBatchSize,1,1])
  M3_tile = tf.tile(tf.expand_dims(tf.constant(Aux_M3,tf.float32),[0]),[MiniBatchSize,1,1])
  M4_tile = tf.tile(tf.expand_dims(tf.constant(Aux_M4,tf.float32),[0]),[MiniBatchSize,1,1])
  M5_tile = tf.tile(tf.expand_dims(tf.constant(Aux_M5,tf.float32),[0]),[MiniBatchSize,1,1])
  M6_tile = tf.tile(tf.expand_dims(tf.constant(Aux_M6,tf.float32),[0]),[MiniBatchSize,1,1])
  M71_tile = tf.tile(tf.expand_dims(tf.constant(Aux_M71,tf.float32),[0]),[MiniBatchSize,1,1])
  M72_tile = tf.tile(tf.expand_dims(tf.constant(Aux_M72,tf.float32),[0]),[MiniBatchSize,1,1])
  M8_tile = tf.tile(tf.expand_dims(tf.constant(Aux_M8,tf.float32),[0]),[MiniBatchSize,1,1])
  Mb_tile = tf.tile(tf.expand_dims(tf.constant(Aux_Mb,tf.float32),[0]),[MiniBatchSize,1,1])

  # Form the equations Ax = b to compute H
  # Form A matrix
  A1 = tf.matmul(M1_tile, pts_1_tile) # Column 1
  A2 = tf.matmul(M2_tile, pts_1_tile) # Column 2
  A3 = M3_tile                   # Column 3
  A4 = tf.matmul(M4_tile, pts_1_tile) # Column 4
  A5 = tf.matmul(M5_tile, pts_1_tile) # Column 5
  A6 = M6_tile                   # Column 6
  A7 = tf.matmul(M71_tile, pred_pts_2_tile) *  tf.matmul(M72_tile, pts_1_tile)# Column 7
  A8 = tf.matmul(M71_tile, pred_pts_2_tile) *  tf.matmul(M8_tile, pts_1_tile)# Column 8

  A_mat = tf.transpose(tf.stack([tf.reshape(A1,[-1,8]),tf.reshape(A2,[-1,8]),\
                                 tf.reshape(A3,[-1,8]),tf.reshape(A4,[-1,8]),\
                                 tf.reshape(A5,[-1,8]),tf.reshape(A6,[-1,8]),\
                                 tf.reshape(A7,[-1,8]),tf.reshape(A8,[-1,8])],axis=1), perm=[0,2,1]) # BATCH_SIZE x 8 (A_i) x 8


  print('--Shape of A_mat:', A_mat.get_shape().as_list())
  # Form b matrix
  b_mat = tf.matmul(Mb_tile, pred_pts_2_tile)
  print('--shape of b:', b_mat.get_shape().as_list())

  # Solve the Ax = b
  H_8el = tf.matrix_solve(A_mat , b_mat)  # BATCH_SIZE x 8.
  print('--shape of H_8el', H_8el)


  # Add ones to the last cols to reconstruct H for computing reprojection error
  h_ones = tf.ones([MiniBatchSize, 1, 1])
  H_9el = tf.concat([H_8el,h_ones],1)
  H_flat = tf.reshape(H_9el, [-1,9])
  H_mat = tf.reshape(H_flat,[-1,3,3])   # BATCH_SIZE x 3 x 3

  return H_mat