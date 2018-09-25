pd.DataFrame(data=dt.feature_importances_, index=df_ml.columns[1:],
             columns=['Feature importance']).sort_values(by="Feature importance", ascending=False)
