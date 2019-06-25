function [all_theta] = oneVsAll(X, y, num_labels, lambda)
%ONEVSALL trains multiple logistic regression classifiers and returns all
%the classifiers in a matrix all_theta, where the i-th row of all_theta 
%corresponds to the classifier for label i
%   [all_theta] = ONEVSALL(X, y, num_labels, lambda) trains num_labels
%   logistic regression classifiers and returns each of these classifiers
%   in a matrix all_theta, where the i-th row of all_theta corresponds 
%   to the classifier for label i

% Some useful variables
m = size(X, 1);    % training examples
n = size(X, 2);     % 400 no of columns or features 20*20 pixels

% You need to return the following variables correctly 
all_theta = zeros(num_labels, n + 1);   % matrix of 10*401 i.e. 10 is output label and 401 is features including Xo=1

% Add ones to the X data matrix
X = [ones(m, 1) X];    % column with all ones is added to incorporate Xo=1

% ====================== YOUR CODE HERE ======================
% Instructions: You should complete the following code to train num_labels
%               logistic regression classifiers with regularization
%               parameter lambda. 
%
% Hint: theta(:) will return a column vector. of 4010*1
%
% Hint: You can use y == c to obtain a vector of 1's and 0's that tell you
%       whether the ground truth is true/false for this class.
%The "y == c" statement creates a vector of 0's and 1's for each value of 'c' as you iterate 
%from 1 to num_labels. Those are the effective 'y' values that are used for training to detect each label.
%
% Note: For this assignment, we recommend using fmincg to optimize the cost
%       function. It is okay to use a for-loop (for c = 1:num_labels) to
%       loop over the different classes.
%
%       fmincg works similarly to fminunc, but is more efficient when we
%       are dealing with large number of parameters.
%
% Example Code for fmincg:
%
%     % Set Initial theta
%     initial_theta = zeros(n + 1, 1);
%     
%     % Set options for fminunc
%     options = optimset('GradObj', 'on', 'MaxIter', 50);
% 
%     % Run fmincg to obtain the optimal theta
%     % This function will return theta and the cost 
%     [theta] = ...
%         fmincg (@(t)(lrCostFunction(t, X, (y == c), lambda)), ...
%                 initial_theta, options);
%		a = 1:10; 
% 		b = 3; a == b return 10*1 vector 0 0 1 0 0 0 0 0 0 0 
%		
%		y is a 5000*1 vector which has values of 0,1,2,3,4,5,6,7,8,9 for classes
%

initial_theta=zeros(n+1,1);
options=optimset('GradObj','on','MaxIter',50);

% When training the classiﬁer for class k belongs{1,...,K}, you will want a m-dimensional vector of labels y,
% where yj belongs 0,1 indicates whether the j-th training instance belongs to class k (yj = 1), or 
% if it belongs to a diﬀerent class (yj = 0).

% training multiple regularized logistic regression classiﬁers, one for each of the K=10=new_labels classes in our dataset 
for c=1:num_labels
	
	% Each call to fmincg() returns a theta vector 
	% y==c will return vector of 5000*1 where only one class is present and others are not.
	[theta] = fmincg (@(t)(lrCostFunction(t, X, (y == c), lambda)),initial_theta, options);
	% copy theta vector into a row of all_theta where each row correspond to one class of output.
	all_theta(c,:)=theta;
end






% =========================================================================


end
