# Applied Machine Learning in Python

### Useful Function of Scikit Learning for Binary-Class Evaluation

- **train_test_split** - Used to split the data in train and test
  > from sklearn.model_selection import train_test_split  
  > X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)   
  
- **DummyClassifier** - Used to make prediction by ignoring input data and using simple rule which serves as a baseline for comparision  
  > from sklearn.dummy import DummyClassifier  
  > dummy_majority = DummyClassifier(strategy = 'most_frequent').fit(X_train, y_train)  
  > y_dummy_predictions = dummy_majority.predict(X_test)  
  > dummy_majority.score(X_test, y_test)  
  
- **Confusion Matrices** - Used to describe the performance of a classification model on a set of test data for which the true values are known.  
  > from sklearn.metrics import confusion_matrix  
  > confusion_matrix(y_test, y_predicted)  
  
- **Accuracy**: For what fraction of all instances is the classifier's prediction correct(for either positive or negative class)   
  > Accuracy = TP + TN / (TP + TN + FP + FN)  
  > from sklearn.metrics import precision_score    
  > print('Accuracy: {:.2f}'.format(accuracy_score(y_test, y_predicted)))  

 
- **Classification error**: For what fraction of all instances is the classifier's prediction incorrect(1 - Accuracy)   
  
- **Recall or True positive Rate or Sensivity**: what fraction of all positive instances does the classifier predicts correctly   
OR  
The recall is intuitively the ability of the classifier to find all the positive samples.  
  > Recall = TP / (TP + FN)   
  > from sklearn.metrics import recall_score   
  > print('Recall: {:.2f}'.format(recall_score(y_test, y_predicted)))  


- **Precision**: What fraction of positive prediction are correct  
OR  
The precision is intuitively the ability of the classifier not to label as positive a sample that is negative.   
  > Precision = TP / (TP + FP)  
  > from sklearn.metrics import precision_score   
  > print('Precision: {:.2f}'.format(precision_score(y_test, y_predicted)))    

  
- **False Postive Rate or Specificity**: What fraction of all negative instances does the classifier incorrectly identify as positive  

- **F1 Score**: Used to combines precision and recall into a single number  
  > F1 = 2 * Precision * Recall / (Precision + Recall)  
  > from sklearn.metrics import f1_score    
  > print('F1: {:.2f}'.format(f1_score(y_test, y_predicted)))    

- **classification_report** - Used to get combined report of all the scores  
  > from sklearn.metrics import classification_report   
  >  print(classification_report(y_test, y_predicted, target_names=['not 1', '1']))    
  
- **decision_function** - Each classifier score value per test point indicates how confidently the classifier predicts the positive class or negative class   
  > X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)  
  > y_scores_model = model.fit(X_train, y_train).decision_function(X_test)  
  > y_score_list = list(zip(y_test[0:20], y_scores_model[0:20])) # for 20 records  
  
- **predict_proba** - It is the probability of the data instance belonging to each class. This is called a probability prediction where given a new instance, the model returns the probability for each outcome class as a value between 0 and 1.  
  > X_train, X_test, y_train, y_test = train_test_split(X, y_binary_imbalanced, random_state=0)    
  > y_proba_model = model.fit(X_train, y_train).predict_proba(X_test)  
  > y_proba_list = list(zip(y_test[0:20], y_proba_model[0:20,1])) # probability of positive class for first 20 instances    
  
- **precision_recall_curve** - used to draw precision-recall curve  
  > from sklearn.metrics import precision_recall_curve  
  > precision, recall, thresholds = precision_recall_curve(y_test, y_scores_model)  
  > closest_zero = np.argmin(np.abs(thresholds)) # argmin return index and abs return mod of value  
  > closest_zero_p = precision[closest_zero]  
  > closest_zero_r = recall[closest_zero]  
  > plt.figure()  
  > plt.xlim([0.0, 1.01])  
  > plt.ylim([0.0, 1.01])  
  > plt.plot(precision, recall, label='Precision-Recall Curve')  
  > plt.plot(closest_zero_p, closest_zero_r, 'o', markersize = 12, fillstyle = 'none', c='r', mew=3)  
  > plt.xlabel('Precision', fontsize=16)  
  > plt.ylabel('Recall', fontsize=16)  
  > plt.axes().set_aspect('equal')  
  > plt.show()  
 
- **ROC curves, Area-Under-Curve (AUC)** - It illustrate the performance of a binary classifier.(receiver operating characteristic curves). More the area under curve and better is the classifier. We need a classifer which maximize the True positive rate and minimize the False Positive Rate.  
  > from sklearn.metrics import roc_curve, auc   
  > X_train, X_test, y_train, y_test = train_test_split(X, y_binary_imbalanced, random_state=0)  
  > y_score_model = model.fit(X_train, y_train).decision_function(X_test)  
  > fpr_model, tpr_model, _ = roc_curve(y_test, y_score_model)  
  > roc_auc_model = auc(fpr_model, tpr_model) # It is the area under curve value  


### Useful Function of Scikit Learning for Multi-Class Evaluation  

- Multi-Class evaluation is an extension of binary case  
	- A collection of true vs predicted binary outcomes, one per class  
	- Confusion matrices are especially useful  
	- Classification report  

- Overall evaluation matrices are average across classes  
	- But there are different ways to avarage multi-class result  
	- The support(no of instances) for each class is important to consider e.g. in case of imbalanced classes  


- **Multi-class Confusion Matrices**  
  > X_train_mc, X_test_mc, y_train_mc, y_test_mc = train_test_split(X, y, random_state=0)  
  > svm = SVC(kernel = 'linear').fit(X_train_mc, y_train_mc)  
  > svm_predicted_mc = svm.predict(X_test_mc)  
  > confusion_mc = confusion_matrix(y_test_mc, svm_predicted_mc)  
  > df_cm = pd.DataFrame(confusion_mc, index = [i for i in range(0,10)], columns = [i for i in range(0,10)])    
  
- **Multi-class classification report**   
  > print(classification_report(y_test_mc, svm_predicted_mc))  
  
  
### Useful Function of Scikit Learn for Regression Evaluation   

- Typically R2_score is enough  
	- Reminder: cumputes how well future instance will be predicted  
	- Best possible score is 1.0  
	- Constant prediction score is 0.0  
- Alternative metrics include  
	- mean_absolute_error (absolute(mod) difference of target and predicted value)  
	- mean_squared_error (squared difference of target and predicted value)  
	- median_absolute_error (robust to outlier)  

- mean_absolute_error and mean_squared_error does not distinguish between over and under estimates  
- you can use the median_absolute_error score, which is robust with the presence of outliers because it uses the median of the error distribution rather than the mean   


- **DummyRegressor** - Used to make prediction by ignoring input data and using simple rule which serves as a baseline for comparision  
  > from sklearn.dummy import DummyRegressor  
  > model_dummy_mean = DummyRegressor(strategy = 'mean').fit(X_train, y_train)  
  > y_predict_dummy_mean = model_dummy_mean.predict(X_test)  
  > print("Mean squared error (dummy): {:.2f}".format(mean_squared_error(y_test, y_predict_dummy_mean)))  
  > print("r2_score (dummy): {:.2f}".format(r2_score(y_test, y_predict_dummy_mean)))  

### Some Useful Example  

- **Cross-validation example**  
  > from sklearn.model_selection import cross_val_score  
  > from sklearn.svm import SVC  
  > model = SVC(kernel='linear', C=1)  
  > print('Cross-validation (accuracy)', cross_val_score(model, X, y, cv=5)) # accuracy is the default scoring metric    
  > print('Cross-validation (AUC)', cross_val_score(model, X, y, cv=5, scoring = 'roc_auc')) # use AUC as scoring metric    
  > print('Cross-validation (recall)', cross_val_score(model, X, y, cv=5, scoring = 'recall')) # use recall as scoring metric   

- **Grid Search example**  
  > from sklearn.svm import SVC  
  > from sklearn.model_selection import GridSearchCV  
  > from sklearn.metrics import roc_auc_score  
  > model = SVC(kernel='rbf')  
  > grid_values = {'gamma': [0.001, 0.01, 0.05, 0.1, 1, 10, 100]}  
  >  
  > ** default metric to optimize over grid parameters: accuracy**  
  > grid_model_acc = GridSearchCV(clf, param_grid = grid_values)  
  > grid_model_acc.fit(X_train, y_train)  
  > y_decision_fn_scores_acc = grid_model_acc.decision_function(X_test)   
  > print('Grid best parameter (max. accuracy): ', grid_model_acc.best_params_)  
  > print('Grid best score (accuracy): ', grid_model_acc.best_score_)  
  >  
  > **alternative metric to optimize over grid parameters: AUC**  
  > grid_model_auc = GridSearchCV(clf, param_grid = grid_values, scoring = 'roc_auc')  
  > grid_model_auc.fit(X_train, y_train)  
  > y_decision_fn_scores_auc = grid_model_auc.decision_function(X_test)   
  > print('Test set AUC: ', roc_auc_score(y_test, y_decision_fn_scores_auc))  
  > print('Grid best parameter (max. AUC): ', grid_model_auc.best_params_)  
  > print('Grid best score (AUC): ', grid_model_auc.best_score_)  

- **Evaluation metrics supported for model selection**  
  > from sklearn.metrics.scorer import SCORERS  
  > print(sorted(list(SCORERS.keys())))  
  
### Training, Validation and Test Framework for Model Selection and Evaluation  
- Use three data split  
	1. Training Set (model building)  
	2. Validation Set (model selection)  
	3. Test Set (final evaluation)   
- In practice  
	- Create an initail training/test split  
	- Do cross validation on training data for model/parameter selection  
	- Save the held out test set for final model selection  
	
