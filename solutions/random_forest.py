rf = RandomForestClassifier()
rf.fit(X_train, y_train)
print("Training error",
      rf.score(X_train, y_train),
      "Validation error",
      rf.score(X_val, y_val))
