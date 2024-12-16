def print_opportunities(opportunities: list):
    if not opportunities:
        print("No arbitrage opportunities found.")
    else:
        for opp in opportunities:
            print(f"Match: {opp['match_id']}")
            outcome1, outcome2 = opp['outcomes']
            best_odds = opp['best_odds']
            
            print(f"Outcome 1: {outcome1}, Best Odds: {best_odds[outcome1]['odds']} (from {best_odds[outcome1]['bookmaker']})")
            print(f"Outcome 2: {outcome2}, Best Odds: {best_odds[outcome2]['odds']} (from {best_odds[outcome2]['bookmaker']})")
            print(f"Profit Margin: {opp['profit_margin_percent']:.2f}%")
            print("------")
