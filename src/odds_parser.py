def parse_odds(api_data: list):
    """
    Converts the data from The Odds API into a standardized format.
    """
    standardized_matches = []
    for event in api_data:
        home_team = event["home_team"]
        away_team = event["away_team"]
        
        # Create a unique match_id. This is arbitrary; you can refine.
        match_id = f"{home_team}_vs_{away_team}_{event['commence_time']}"
        
        odds_dict = {}
        for bookmaker in event.get("bookmakers", []):
            sportsbook_key = bookmaker["key"]
            # Assuming H2H market
            for market in bookmaker.get("markets", []):
                if market["key"] == "h2h":
                    # There should be two outcomes for a typical moneyline
                    outcome_odds = {}
                    for outcome in market["outcomes"]:
                        outcome_odds[outcome["name"]] = outcome["price"]
                    # Add this bookmaker’s odds
                    odds_dict[sportsbook_key] = outcome_odds
        
        # Only add if we have odds
        if odds_dict:
            standardized_matches.append({
                "match_id": match_id,
                "odds": odds_dict
            })
    
    return standardized_matches
