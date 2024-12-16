import os
import requests
from dotenv import load_dotenv

load_dotenv()  # loads variables from .env into the environment

def fetch_odds_from_api(sport: str = "basketball_nba", region: str = "us", market: str = "h2h"):
    """
    Fetches odds data from The Odds API for a given sport, region, and market.
    sport: The sport key (e.g. 'soccer_epl', 'soccer_uefa_champs_league', 'basketball_nba', etc.)
    region: The region of the sportsbooks (au, uk, us, eu)
    market: The type of odds market (h2h, spreads, totals)
    """
    api_key = os.getenv("ODDS_API_KEY")
    if not api_key:
        raise ValueError("ODDS_API_KEY not found in environment. Please set it in .env.")
    
    url = "https://api.the-odds-api.com/v4/sports/{sport}/odds".format(sport=sport)
    params = {
        "apiKey": api_key,
        "regions": region,
        "markets": market,
        "oddsFormat": "decimal",
        "dateFormat": "iso"
    }
    
    response = requests.get(url, params=params)
    if response.status_code != 200:
        print("Error fetching odds:", response.text)
        return []
    
    data = response.json()
    return data
