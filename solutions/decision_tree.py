dt = DecisionTreeClassifier()
dt.fit(X_train, y_train)
print("Training error",
      dt.score(X_train, y_train),
      "Validation error",
      dt.score(X_val, y_val))