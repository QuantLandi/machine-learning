# Importing a few necessary libraries
import numpy as np
import matplotlib.pyplot as pl
from sklearn import datasets
from sklearn.tree import DecisionTreeRegressor

# Create our client's feature set for which we will be predicting a selling price
CLIENT_FEATURES = [[11.95, 0.00, 18.100, 0, 0.6590, 5.6090, 90.00, 1.385, 24, 680.0, 20.20, 332.09, 12.13]]

# Load the Boston Housing dataset into the city_data variable
city_data = datasets.load_boston()

# Initialize the housing prices and housing features
housing_prices = city_data.target
housing_features = city_data.data

print "Boston Housing dataset loaded successfully!"

# Number of houses in the dataset
total_houses = housing_prices.shape[0]

# Number of features in the dataset
total_features = housing_features.shape[1]

# Minimum housing value in the dataset
minimum_price = np.min(housing_prices)

# Maximum housing value in the dataset
maximum_price = np.min(housing_prices)

# Mean house value of the dataset
mean_price = np.mean(housing_prices)

# Median house value of the dataset
median_price = np.median(housing_prices)

# Standard deviation of housing values of the dataset
std_dev = np.std(housing_prices)

# Show the calculated statistics
print "Boston Housing dataset statistics (in $1000's):\n"
print "Total number of houses:", total_houses
print "Total number of features:", total_features
print "Minimum house price:", minimum_price
print "Maximum house price:", maximum_price
print "Mean house price: {0:.3f}".format(mean_price)
print "Median house price:", median_price
print "Standard deviation of house price: {0:.3f}".format(std_dev)

from sklearn import cross_validation
from sklearn.utils import shuffle

def shuffle_split_data(X, y):
    """ Shuffles and splits data into 70% training and 30% testing subsets,
    then returns the training and testing subsets. """
    
    # Shuffle and split the data
    X_train, X_test, y_train, y_test = cross_validation.train_test_split(
        X, y, test_size = 0.3)
    
    # Return the training and testing data subsets
    return X_train, y_train, X_test, y_test

X_train, y_train, X_test, y_test = shuffle_split_data(housing_features, housing_prices)

try:
    X_train, X_test, y_train, y_test = shuffle_split_data(housing_features, housing_prices)
    print "Successfully shuffled and split the data!"
except:
    print "Something went wrong with shuffling and splitting the data."

from sklearn import metrics

def performance_metric(y_true, y_predict):
    """ Calculates and returns the total error between true and predicted values
    based on a performance metric chosen by the student. """
    
    error = metrics.mean_squared_error(y_true, y_predict)
    return error

# Test performance_metric
try:
    total_error = performance_metric(y_train, y_train)
    print "Successfully performed a metric calculation!"
except:
    print "Something went wrong with performing a metric calculation."



# Put any import statements you need for this code block
from sklearn import grid_search

def fit_model(X, y):
    """ Tunes a decision tree regressor model using GridSearchCV on the input data X 
    and target labels y and returns this optimal model. """
    
    # Create a decision tree regressor object
    regressor = DecisionTreeRegressor()
    
    # Set up the parameters we wish to tune
    parameters = {'max_depth':(1,2,3,4,5,6,7,8,9,10)}
    
    # Make an appropriate scoring function
    scoring_function = metrics.make_scorer(metrics.mean_squared_error)
    
    # Make the GridSearchCV object
    reg = grid_search.GridSearchCV(regressor, parameters, scoring=scoring_function)
    
    # Fit the learner to the data to obtain the optimal model with tuned parameters
    reg.fit(X, y)
    
    # Return the optimal model
    return reg.best_estimator_


# Test fit_model on entire dataset
try:
    reg = fit_model(housing_features, housing_prices)
    print "Successfully fit a model!"
except:
    print "Something went wrong with fitting a model."
