function p = predictOneVsAll(all_theta, X)
%PREDICT Predict the label for a trained one-vs-all classifier. The labels 
%are in the range 1..K, where K = size(all_theta, 1). 
%  p = PREDICTONEVSALL(all_theta, X) will return a vector of predictions
%  for each example in the matrix X. Note that X contains the examples in
%  rows. all_theta is a matrix where the i-th row is a trained logistic
%  regression theta vector for the i-th class. You should set p to a vector
%  of values from 1..K (e.g., p = [1; 3; 1; 2] predicts classes 1, 3, 1, 2
%  for 4 examples) 

m = size(X, 1);
num_labels = size(all_theta, 1);

% You need to return the following variables correctly 
p = zeros(size(X, 1), 1);

% Add ones to the X data matrix
X = [ones(m, 1) X];

% ====================== YOUR CODE HERE ======================
% Instructions: Complete the following code to make predictions using
%               your learned logistic regression parameters (one-vs-all).
%               You should set p to a vector of predictions (from 1 to
%               num_labels).
%
% Hint: This code can be done all vectorized using the max function.
%       In particular, the max function can also return the index of the 
%       max element, for more information see 'help max'. If your examples 
%       are in rows, then, you can use max(A, [], 2) to obtain the max 
%       for each row.
%       

%A = [1, 2, 6; 4, -7, 0];
%B = max(A, [], 1);    -> B=[4 2 6]  column wise max 1*3
%C = max(A, [], 2); 	-> C= [6; 4]  row wise max 2*1 


% one line to calculate the sigmoid() of the product of X and all_theta. X is (m x n), and all_theta 
% is (num_labels x n), so you'll need a transposition to get a result of (m x num_labels) 

h=sigmoid(X*all_theta');   % it will be 5000*10 vector

% one line to return the classifier which has the max value. The size will be (m x 1)
% max function return max value and its index as [max_value index]
[max_value p]= max(h, [], 2);

% =========================================================================


end
