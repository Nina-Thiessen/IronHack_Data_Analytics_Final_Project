# IronHack_Data_Analytics_Final_Project
by Nina Thiessen

## Data

Downloaded from UCI Machine Learning Repository  
https://archive.ics.uci.edu/ml/datasets/in-vehicle+coupon+recommendation

Collected via a survey on Amazon Mechanical Turk

12,684 records

23 features, all categorical, including:
* driver personal info (age, gender, education, occupation)
* coupon type & expiration time
* distance & direction to restaurant/… on coupon
* typical number of weekly visits to bar/restaurant/coffee house/takeaway
* trip info (destination type, passenger details)
* weather, temperature, time of day

### Data source

Wang, Tong, Cynthia Rudin, Finale Doshi-Velez, Yimin Liu, Erica Klampfl, and Perry MacNeille. 'A bayesian framework for learning rule sets for interpretable classification.' The Journal of Machine Learning Research 18, no. 1 (2017): 2357-2393.

## Binary Classification Task

Predict whether a person driving a car will accept a recommended coupon in different scenarios.

Use resulting model to determine which factors most influence the 5 different coupon types to be accepted.

Coupon types:
1. Restaurant(<$20)
1. Restaurant($20-$50)
1. Coffee House
1. Carry out & Take away
1. Bar

### Analysis Plan

Explore...
* Ordinal vs Nominal feature encoding
* Options for filling missing values in ordinal features
* Upsampling with SMOTE to handle yes/no imbalance
* Classifier models: RandomForest (Decision Trees), KNN, Logistic Regression
* Optimising hyperparameters with grid search cross validation
* Evaluating performance with AUC-ROC (validation and test sets)
