# World Cup Prediction ETL Pipeline

## Project Overview

This project predicts the strongest football teams using a custom strength score formula.

The pipeline:

CSV Data
→ Extract
→ Transform
→ Predict
→ Load to PostgreSQL

## Technologies Used

- Python
- Pandas
- PostgreSQL
- SQLAlchemy
- Git
- GitHub

## Features

- Extract football team statistics
- Calculate KPIs
- Generate strength scores
- Predict top teams
- Store results in PostgreSQL

## Project Structure

world_cup_prediction/

├── extract.py
├── transform.py
├── predict.py
├── load.py
├── main.py
├── team_stats.csv

## Output

Top Predicted Team:

Brazil

Strength Score:

179.0