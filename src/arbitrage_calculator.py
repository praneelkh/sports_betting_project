def find_arbitrage_opportunities(matches: list):
    opportunities = []
    for match in matches:
        match_id = match["match_id"]
        odds = match["odds"]  # {sportsbookName: {teamA: x.xx, teamB: x.xx}, ... }
        
        # Identify the outcomes
        any_sportsbook = next(iter(odds.values()))
        outcomes = list(any_sportsbook.keys())
        if len(outcomes) != 2:
            continue
        outcome1, outcome2 = outcomes
        
        # Find best odds and track which sportsbook provided them
        best_odds_outcome1, best_book_outcome1 = None, None
        best_odds_outcome2, best_book_outcome2 = None, None
        
        for bookmaker, outcome_odds in odds.items():
            # Check if this bookmaker has a better odd for outcome1
            if best_odds_outcome1 is None or outcome_odds[outcome1] > best_odds_outcome1:
                best_odds_outcome1 = outcome_odds[outcome1]
                best_book_outcome1 = bookmaker
            
            # Check if this bookmaker has a better odd for outcome2
            if best_odds_outcome2 is None or outcome_odds[outcome2] > best_odds_outcome2:
                best_odds_outcome2 = outcome_odds[outcome2]
                best_book_outcome2 = bookmaker
        
        # Check for arbitrage
        inverse_sum = (1 / best_odds_outcome1) + (1 / best_odds_outcome2)
        if inverse_sum < 1:
            profit_percent = (1 - inverse_sum) * 100
            opportunities.append({
                "match_id": match_id,
                "outcomes": (outcome1, outcome2),
                "best_odds": {
                    outcome1: {"odds": best_odds_outcome1, "bookmaker": best_book_outcome1},
                    outcome2: {"odds": best_odds_outcome2, "bookmaker": best_book_outcome2}
                },
                "profit_margin_percent": profit_percent
            })
    return opportunities
