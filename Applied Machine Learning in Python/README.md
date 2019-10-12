# Applied Machine Learning in Python

### pitfalls to avoid, important issues to focus on, and answers to common questions

### Learning = Representation + Evaluation + Optimization

**Representation** 
'''
A classifier must be represented in some formal language that the computer can handle.
Conversely, choosing a representation for a learner is tantamount to choosing the set of classifiers that it
can possibly learn. This set is called the hypothesis space of the learner. If a classifier is not in the hypothesis space, it cannot be learned. A related question, that I address later, is how to represent the input, in other words,what features to use.
'''

**Evaluation**
'''An evaluation function (also called objective function or scoring function) is needed to distinguish good classifiers from bad ones. The evaluation function used internally by the algorithm may differ from the external one that we want the classifier to optimize, for ease of optimization and due to the issues I
will discuss.
'''

**Optimization**
'''
Finally, we need  method to search among the classifiers in the language for the highest-scoring one. The choice of optimization technique is key to the efficiency of the learner, and also helps determine the classifier produced if the evaluation function has more than one optimum. It is common for new learners to start out using off-the-shelf optimizers, which are later replaced by custom-designed ones.
'''

Q Holding out data reduces the amount available for training?
'''
This can be mitigated by doing cross-validation: randomly dividing your training data into (say) 10 subsets, holding out each one while training on the rest, testing each learned classifier on the examples it
did not see, and averaging the results to see how well the particular parameter setting does.
'''

**Overfitting Has Many Faces**
One way to understand overfitting is by decomposing generalization error into bias and variance.
- Cross-validation can help to combat overfitting
- The most popular one is adding a regularization term to the evaluation function to combat overfitting
- Perform a statistical significance test like chi-square before adding new structure, to decide whether the distribution of the class really is different with and without this structure.

**curse of dimensionality**
