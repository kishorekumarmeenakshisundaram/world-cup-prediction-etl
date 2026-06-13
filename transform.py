import pandas as pd
def calculate_form_score(form):
    if pd.isna(form):
        return 0
    score = 0
    for result in str(form):
        if result=="W":
            score+=3
        elif result=="D":
            score+=1
        elif result=="L":
            score+=0
    return score

def transform_team_strength(df):
    df=df.copy()

    numeric_columns=[
        "points",
        "goals_diff",
        "played",
        "won",
        "drawn",
        "lost",
        "goals_for",
        "goals_against"
    ]    
    for col in numeric_columns:
        df[col]=pd.to_numeric(df[col],errors="coerce").fillna(0)

    df = df[df["played"]>0]
    df["win_rate"] = (df["won"]/df["played"]).round(2)
    df["points_per_game"]=(
        df["points"]/df["played"]
        ).round(2)
    df["goals_per_game"] = (
        df["goals_for"] / df["played"]
    ).round(2)

    df["conceded_per_game"] = (
        df["goals_against"] / df["played"]
    ).round(2)

    df["form_score"] = df["form"].apply(
        calculate_form_score
    )
    df["strength_score"] = (
        (df["points_per_game"] * 40)
        + (df["win_rate"] * 25)
        + (df["goals_diff"] * 2)
        + (df["goals_per_game"] * 10)
        - (df["conceded_per_game"] * 5)
        + (df["form_score"] * 2)
    ).round(2)
    df= df.sort_values(
        "strength_score",
        ascending=False
    )
    df["predicted_rank"]=range(1,len(df)+1)
    return df
