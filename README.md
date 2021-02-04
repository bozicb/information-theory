# information-theory

This repository consists of Python scrips for calculating information theory metrics and functions. There is no claim of mathematical identity to the functions, but they could be used as helper functions for studying information theory or reused in code for Machine Learning algorithms.

In the following functions are classified by the area of information theory they target. Every module covers one part of information theory that we use for our machine learning classes.

## entropy.py
The entropy module covers concepts such as entropy, information gain, etc. Here is how to use the different functions.

### entropy(list)
The entropy function takes a list of probabilities and uses it to calculate entropy for a descriptive feature or overall entropy for a target. A list `x` would be used as follows: ![equation1](https://latex.codecogs.com/gif.latex?\dpi{400}H(Feature,\mathcal{D})=-\sum_{i}^{n}x_i*log(x_i))

### ig(DataFrame)
