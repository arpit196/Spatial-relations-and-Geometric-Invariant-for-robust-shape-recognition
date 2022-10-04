# Geometric Invariant Networks
A neural network that learns invariant representations of shapes
In this work, we show that geometric invariant features such as curvatures and higher order derivatives, and spatial relations between parts such as relative locations and orientations extracted from boundaries or contours of objects provides a robust description of shape which is invariant to rigid motions (such as translation and rotations), and is more robust to convolutional operations when these augmentations are applied. Moreover, we show through experiments that the shallow networks trained over these features outperform deep convolutional neural network such as the VGG network models both in test accuracy and in robustness to different augmentations performed on the test set.

![alt text](https://i.ibb.co/6JgVJ10/Fig2-1.jpg)

We also proposed a variant of the above model which we call the hierarchical deformable parts where the probability of presence of a part is given as the summation of the probability of each of its subpart and is inversely proportional to the deformation of parts, or the relative distances of the parts from each other. This deformation energy is invariant to rotations, translations but not to scaling transformations. However, it can be made scale invariant by normalizing the distance between pair of parts such that if the distance between two parts is scaled by factor s, the normalization divides it by the distances of the other pairs which are all scaled by s. Hence, the model becomes invariant to scaling if it is normalized properly.

The performance of the different models on the test set of the smallNORB dataset is summarised in the table below and as can be observed, our geometric invariants and hierarchical deformable model outperforms convolutional neural networks and even the deeper variants of the convolutional model such as the VGG-16 model.

![alt text](https://i.ibb.co/yQnYj8q/Norbaccuracy.png)

Next, we evaluated the robustness of the model by testing the drop in accuracy on the test performance when the images in test set is augmented by the corresponding augmentations such as rotations, translations, scaling or affine transformations. The result for the robustness of the different models are compared in table below.

![alt text](https://i.ibb.co/VJG4Rn6/Robustness.png)

As can be observed from the table above, our Geometric invariant network is highly robust to rotation transformations and suffers a drop in test performance of only $2%$ for a $20^{0}$ rotation compared to a $63%$ drop in test accuracy by convolutional network and a $11.3%$ drop for VGG networks.

On the other hand, the geometric invariant models are not invariant to shearing transformations and suffer a large drop in performance for even a small shear. On the other hand, our hierarchical deformable parts model is highly robust to shearing transformations than both, the convolutional networks or the VGG networks.
