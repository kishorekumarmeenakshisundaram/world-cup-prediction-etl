import os
import requests
import pandas as pd
from dotenv import load_dotenv
BASE_URL = "https://v3.football.api-sports.io"


def get_api_headers():
    load_dotenv()
    api_key=os.getenv("API_FOOTBALL_KEY")
    print("API key loaded:", api_key is not None)
    if not api_key:
        raise ValueError("API_FOOTBALL_KEY is missing in .env file")
    return{
        "x-apisports-key":api_key,
        "x-rapidapi-host": "v3.football.api-sports.io"
        }


def extract_Standings_json():
    load_dotenv()
    league_id =os.getenv("LEAGUE_ID")
    season =os.getenv("SEASON")
    if not league_id or not season:
        raise ValueError(
            "LEAGUE_ID or SEASON is missing in .env file"
        )
    url =f"{BASE_URL}/standings"
    params={
        "league":league_id,
        "season":season
    }
    response = requests.get(
        url,
        headers=get_api_headers(),
        params=params,
        timeout=30
    )
    response.raise_for_status()
    data=response.json()
    if data.get("errors"):
        raise ValueError(
            f"API returned errors:{data.get('errors')}"
        )
    if not data.get("response"):
        raise ValueError(
            "API returned no standings data."
        )
    return data
def convert_standings_json_to_dataframe(data):
    league_data = data["response"][0]["league"]
    league_id = league_data.get("id")
    league_name= league_data.get("name")
    season =league_data.get("season")
    standings_groups = league_data.get("standings",[])
    rows=[]
    for group in standings_groups:
        for team_row in group:
            team=team_row.get("team",{})
            all_stats = team_row.get("all",{})
            goals=all_stats.get("goals",{})

            rows.append({
                "league_id":league_id,
                "league_name":league_name,
                "season": season,
                "rank": team_row.get("rank"),
                "team_id": team.get("id"),
                "team_name": team.get("name"),
                "group_name": team_row.get("group"),
                "points": team_row.get("points"),
                "goals_diff": team_row.get("goalsDiff"),
                "form": team_row.get("form"),
                "played": all_stats.get("played"),
                "won": all_stats.get("win"),
                "drawn": all_stats.get("draw"),
                "lost": all_stats.get("lose"),
                "goals_for": goals.get("for"),
                "goals_against": goals.get("against")

            })
    
    df =pd.DataFrame(rows)

    return df

def extract_team_standings(source="csv"):
    if source == "api":
        data = extract_Standings_json()
        df = convert_standings_json_to_dataframe(data)
        return df

    if source == "csv":
        df = pd.read_csv("team_stats.csv")
        return df

    raise ValueError("Invalid source. Use 'api' or 'csv'.")