types = pd.get_dummies(df_ml['Type 1'], prefix='Type') + pd.get_dummies(df_ml['Type 2'], prefix='Type')
types_opponents = pd.get_dummies(df_ml['Type 1_opponent'], prefix='Opponent_Type') + pd.get_dummies(df_ml['Type 2_opponent'], prefix='Opponent_Type')
df_ml = pd.concat((df_ml, types, types_opponents), axis=1).drop(['Type 1', 'Type 2', 'Type 1_opponent', 'Type 2_opponent'], axis=1)