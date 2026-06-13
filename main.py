from extract import extract_team_standings
from transform import transform_team_strength
from predict import predict_winner
from load import load_to_postgres

def main():
    print("Strating World cup Prediction Pipeline")
    print("\nExtracting Data...")
    raw_df = extract_team_standings(source="csv")
    print(raw_df.head())

    print("\nTransforming Data...")
    transformed_df = transform_team_strength(raw_df)
    
    print(
        transformed_df[
            [
                "team_name",
                "strength_score"
            ]
        ].head()
    )

    print("\nPredicting Winner...")
    predictions_df = predict_winner(transformed_df)

    print("\nLoading To PostgreSQL...")
    load_to_postgres(
        predictions_df,
        "team_strength_predictions"
    )

    print("\nPipeline Completed Successfully")


if __name__ == "__main__":
    main()