# World Cup Prediction ETL Pipeline

## Overview

This project is an end-to-end Data Engineering pipeline that predicts the strongest football teams using historical team performance data.

The pipeline extracts football team statistics from a CSV file, transforms the raw data into analytical KPIs, calculates a custom team strength score, ranks teams, and loads the final results into PostgreSQL.

## Architecture

```text
CSV Dataset
    ↓
Extract
    ↓
Transform KPIs
    ↓
Predict Team Strength
    ↓
Load to PostgreSQL
```

## Tech Stack

- Python
- Pandas
- PostgreSQL
- SQLAlchemy
- Git
- GitHub

## Project Structure

```text
world_cup_prediction/
│
├── data/
│   └── team_stats.csv
│
├── images/
│   ├── pipeline_success.png
│   └── postgres_output.png
│
├── extract.py
├── transform.py
├── predict.py
├── load.py
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

## KPIs Created

The transformation layer creates the following metrics:

- Win Rate
- Points Per Game
- Goals Per Game
- Conceded Per Game
- Form Score
- Strength Score
- Predicted Rank

## Strength Score Logic

The strength score is a rule-based metric calculated using:

```text
points_per_game
win_rate
goal_difference
goals_per_game
conceded_per_game
form_score
```

Higher strength score means a stronger predicted team.

## Output

The pipeline predicted **Brazil** as the strongest team based on the current scoring logic.

## PostgreSQL Table

Final output is loaded into:

```text
team_strength_predictions
```

## How to Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Run pipeline:

```bash
python main.py
```

## Sample Output

```text
Predicted Winner
----------------
Team: Brazil
Strength Score: 179.0

Pipeline Completed Successfully
```

## Future Improvements

- Replace CSV source with a working football API
- Add real FIFA ranking data
- Add historical World Cup match results
- Improve prediction model using machine learning
- Add Airflow orchestration
- Add dashboard using Power BI or Streamlit