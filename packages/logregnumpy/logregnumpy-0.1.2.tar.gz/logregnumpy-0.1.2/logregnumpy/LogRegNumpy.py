"""
Logistic Regression based on Numpy.

This is a small pet project. It consists of two ideas. 
The first one is to implement a basic logistic regressor, build only with Numpy. 
The second one is to learn, how to deploy a self-made python library.
"""

import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm


# some helper functions for inner processing 
def _encoding(label):
    """
    Encode integer labels into a binary array with a length of unique class numbers.
    
    Parameters
    ----------
    label : array-like of shape (n_samples,)
        Target vector relative to X.
        
    Returns
    -------
    binary_labels : ndarray of shape (n_samples, n_classes)
        Array of arrays.
    """
    num_classes = len(set(label))
    binary_labels = np.zeros((len(label), num_classes))
    
    for i in range(len(label)):    
        binary_label = np.zeros(num_classes)
        binary_label[label[i]] = 1
        binary_labels[i] = binary_label
        
    return binary_labels


def _softmax(x):
    """
    Calculate the softmax function.
    
    Parameters
    ----------
    x : array-like of float of shape (M, N)
        Argument to the logistic function.
    
    Returns
    -------
    out : ndarray of shape (M, N)
        Softmax function evaluated at every point in x.
        Array of arrays.
    """
    # this step prevents exponent overflow
    e = np.exp(x - np.max(x))  
    
    if e.ndim == 1:
        return e / np.sum(e, axis=0)
    else:  
        return e / np.array([np.sum(e, axis=1)]).T  # ndim = 2
          

class LogRegNumpy(object):
    """
    Logistic Regressor Classifier.
    
    Performs a gradient descent method for a loss minimizing.
    
    Works with binary and multiclass targets. 
    
    Parameters
    ----------
    lr : float, default=1e-3
        Learning rate (size) for each step of an gradient descent.
        
    l2_reg : float, default=0.2
        Degree of L2 penalty.
        
    epochs : int, default=100
        Number of gradient descent iterations.
    
    Examples
    --------
    >>> from sklearn.datasets import load_iris
    >>> import LogRegNumpy
    >>> X, y = load_iris(return_X_y=True)
    >>> model = LogRegNumpy(l2_reg=0.1, epochs=1000)
    >>> model.fit(X, y)
    >>> model.predict(X)
    array([0, 0, 0])
    >>> model.predict_proba(X)[:3]
    array([[9.69584306e-01, 3.04018742e-02, 1.38198704e-05],
           [9.32753885e-01, 6.71844981e-02, 6.16165599e-05],
           [9.57931295e-01, 4.20313028e-02, 3.74027136e-05]])
    """
    def __init__(self, lr=0.001, l2_reg=0.2, epochs=100):
        
        self.l2_reg = l2_reg
        self.lr = lr
        self.epochs = epochs     

        
    def negative_log_likelihood(self):
        """
        Performs a cross entropy calculation.
        
        Parameters
        ----------
        self 
            Inner parameters.
            
        Returns
        -------
        cross_entropy : float
            Loss value in the end of each iteration.
        """
        softmax_activation = _softmax(np.dot(self.x, self.W) + self.b)
        cross_entropy = - np.mean(
                                  np.sum(self.y * np.log(softmax_activation) + 
                                  (1 - self.y) * np.log(1 - softmax_activation),
                                  axis=1))
        return cross_entropy

    
    def fit(self, X=None, y=None, verbose=False, plot=False):
        """
        Fit the model according to a given data.
        
        Parameters
        ----------
        X : array-like of shape (n_samples, n_features)
            Training vector, where n_samples is the number of samples and
            n_features is the number of features.
        y : array-like of shape (n_samples,)
            Target vector relative to X.
        verbose : bool, default=False
            If true, returns array with loss values on each iteration.
        plot : bool, default=False
            If true, returns a loss value graph. 
            
        Returns 
        -------
        self
            Fitted estimator.
        """
        self.x = X
        self.y = _encoding(y)   
        # set starting weights to zero
        self.W = np.zeros((self.x.shape[1], self.y.shape[1]))  
        # set starting bias to zero
        self.b = np.zeros(self.y.shape[1])
               
        loss_array = []
        
        for epoch in tqdm(range(self.epochs)):
            # calculate the difference between predicted classes and true labels
            p_y_given_x = _softmax(np.dot(self.x, self.W) + self.b)
            d_y = self.y - p_y_given_x
        
            # update weights with current learning rate value. Apply a l2 regularization
            self.W += self.lr * np.dot(self.x.T, d_y) - self.lr * self.l2_reg * self.W
            self.b += self.lr * np.mean(d_y, axis=0)
            
            # loss calculaculation
            loss = self.negative_log_likelihood()           
            loss_array.append(loss)
            
            # update learning rate
            self.lr *= 0.995   
        
        # return array of loss values if needed
        if verbose == True:    
            return loss_array
        
        # plot loss values graph if needed
        if plot == True:
            plt.figure(figsize=(9,4))
            plt.plot(loss_array, c='royalblue', linewidth=2)
            plt.xlabel('Epochs')
            plt.ylabel('Negative Log Likelyhood')
            plt.grid(True)
            plt.title('Loss', size=14);

             
    def predict(self, x):
        """
        Fit the model according to a given data.
        
        Parameters
        ----------
        X : array-like of shape (n_samples, n_features)
            Training vector, where n_samples is the number of samples and
            n_features is the number of features.
        y : array-like of shape (n_samples,)
            Target vector relative to X.
        verbose : bool, default=False
            If true, returns array with loss values on each iteration.
        plot : bool, default=False
            If true, returns a loss value graph. 
            
        Returns 
        -------
        self
            Fitted estimator.
        """
        
        output = _softmax(np.dot(x, self.W) + self.b)
        prediction = []

        for i in range(len(output)):
            y_i = np.argmax(output[i])
            prediction.append(y_i)
        
        return prediction
    
       
    def predict_proba(self, x):
        """
        Probability estimates.
        
        The returned estimates for all classes are ordered by the
        label of classes.
        
        Parameters
        ----------
        x : array-like of shape (n_samples, n_features)
            Vector to be scored, where `n_samples` is the number of samples and
            `n_features` is the number of features.
        
        Returns
        -------
        output : array-like of shape (n_samples, n_classes)
            Returns the probability of the sample for each class in the model,
            where classes are ordered from min to max labels, i.e. from 0 to 5.
        """
        output = _softmax(np.dot(x, self.W) + self.b)
        
        return output
    
    
    def __repr__(self):
        """
        Print model name and they parameters.
        
        Parameters
        ----------
        self 
            Inner parameters
            
        Returns
        -------
        out : str
            Model name and set parameters
        
        """
        return(f'LogRegNumpy(lr={self.lr}, l2_reg={self.l2_reg}, epochs={self.epochs})')
