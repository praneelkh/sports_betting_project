from odds_data_fetcher import fetch_odds_from_api
from odds_parser import parse_odds
from arbitrage_calculator import find_arbitrage_opportunities
from print_output import print_opportunities

def main():
    # Step 1: Fetch data from The Odds API
    # Example: English Premier League soccer odds
    raw_data = fetch_odds_from_api()
    
    # Step 2: Parse & Standardize
    matches = parse_odds(raw_data)
    
    # Step 3: Find arbitrage
    opportunities = find_arbitrage_opportunities(matches)
    
    # Step 4: Print results
    print_opportunities(opportunities)

if __name__ == "__main__":
    main()
