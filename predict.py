def predict_winner(df):
    if df.empty:
        raise ValueError(
            "Prediction failed because Dataframe is empty"
            )
    predictions = df.sort_values(
        "strength_score",
        ascending=False
    ).copy()

    winner=predictions.iloc[0]
    print("\nPredicted Winner")
    print("-----------------")
    print(f"Team:{winner['team_name']}")
    print(f"Strength Score:{winner['strength_score']}"
          
    )
    print("\nTop 5 Teams")
    print("--------------")
    print(predictions[[
        "predicted_rank",
        "team_name",
        "points",
        "goals_diff",
        "strength_score"
    ]].head(5))

    return predictions