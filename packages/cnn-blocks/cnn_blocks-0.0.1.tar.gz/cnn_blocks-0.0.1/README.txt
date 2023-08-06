# How to use this library?
This library containts all famous CNN blocks like VGG Block , residual block , inception modules etc implemented in keras.
Blocks are constructed in a function so that one can simply write a function call and construct a CNN block.
Various CNN blocks can be sequentially joined with one another to construct an entire architecture.
Implementation of popular architectures like VGG16 , ResNet-50 , Inception-v4 are already present in the repository.
One can also create there own architecture by stacking varoius CNN blocks and have fun while learning 😉.

# Why this library?
It is sometimes difficult to understand how such deeper networks like inception-v4 or resnets are implemented.
Most of the times we simple load a pre-trained model available in keras which is good for practical implementation
but hinders the educational process. Using this repository one can understand in depth how each and every block of
CNN architecture is implemented and how these blocks are stacked together to form a large network.
One can also use this repository to create new architectures using various CNN blocks present.
If these blocks are not enough, one can create new cnn blocks in a similar fashion as given in this repository. 
