# GeometricInvariantNetworks
A neural network that learns invariant representations of shapes
In this work, we show that geometric invariant features such as curvatures and higher order derivatives, and spatial relations between parts such as relative locations and orientations extracted from boundaries or contours of objects provides a robust description of shape which is invariant to rigid motions (such as translation and rotations), and is more robust to convolutional operations when these augmentations are applied. Moreover, we show through experiments that the shallow networks trained over these features outperform deep convolutional neural network such as the VGG network models both in test accuracy and in robustness to different augmentations performed on the test set.

![alt text](https://i.ibb.co/6JgVJ10/Fig2-1.jpg)

We also proposed a variant of the above model which we call the hierarchical deformable parts where the probability of activation of a part is given as the summation of the probability of appearance of each part and is inversely proportional to the deformation of parts, or the relative distances of the parts from each other. 
