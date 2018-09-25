rf_cv_scores = cross_val_score(RandomForestClassifier(), X, y, cv=10) 
dt_cv_scores = cross_val_score(DecisionTreeClassifier(), X, y, cv=10)

print(f'Average accuracy for Decision Trees {dt_cv_scores.mean()} with a standard deviation of {dt_cv_scores.std()}')
print(f'Average accuracy for Random Forests {rf_cv_scores.mean()} with a standard deviation of {rf_cv_scores.std()}')
