# Football World Cup ETL Pipeline

## About

This project is a personal data engineering project where I built a simple end-to-end ETL pipeline using Python, PostgreSQL and Docker.

The pipeline reads football team statistics from a CSV file, performs data cleaning and transformation, calculates a custom team strength score, and stores the final predictions in PostgreSQL.

The main purpose of this project was to understand how a typical ETL pipeline is structured and how different components work together.

---

## Technologies

- Python
- Pandas
- PostgreSQL
- SQLAlchemy
- Docker
- Docker Compose

---

## Pipeline Flow

1. Extract football team data from a CSV file.
2. Transform the raw data by creating additional KPIs.
3. Calculate a team strength score.
4. Load the processed data into PostgreSQL.

---

## Project Structure

```
extract.py      -> Reads the dataset

transform.py    -> Cleans and transforms the data

predict.py      -> Calculates team strength

load.py         -> Loads data into PostgreSQL

main.py         -> Runs the complete pipeline
```

---

## Running the Project

Clone the repository and run:

```bash
docker compose up --build
```

The pipeline will automatically load the processed data into PostgreSQL.

---

## What I Learned

While building this project I learned:

- How ETL pipelines are structured.
- Working with PostgreSQL using SQLAlchemy.
- Containerizing Python applications using Docker.
- Managing multiple services with Docker Compose.
- Organizing Python code into reusable modules.

---

## Pipeline Execution

![Pipeline](images/pipeline-success.png)

---

## Docker Containers

![Docker](images/docker-containers.png)

---

## PostgreSQL Output

![Postgres](images/postgres_table_1.png)

![Postgres](images/postgres_table_2.png)


## Future Improvements

- Replace the CSV dataset with football APIs.
- Use Apache Airflow for orchestration.
- Store raw data in AWS S3.
- Build dashboards using Power BI or Streamlit.
- Improve the prediction logic using machine learning.
