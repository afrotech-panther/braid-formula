#!/usr/bin/env python3
"""
Real Example: The Floral Workshop

J and Z collaborated on a floral arrangement workshop.
This is the settlement calculation that inspired the Braid Formula.
"""

from braid_formula import settle

# The real numbers
REVENUE = 120.00

COLLABORATORS = [
    {
        "name": "J",
        "split_percent": 50,
        "expenses": 151.15,  # Flowers, supplies, marketing
    },
    {
        "name": "Z", 
        "split_percent": 50,
        "expenses": 90.49,   # Venue, refreshments
    },
]


def main():
    print("=" * 60)
    print("THE FLORAL WORKSHOP SETTLEMENT")
    print("=" * 60)
    print()
    
    print("INPUTS:")
    print(f"  Revenue: ${REVENUE:,.2f}")
    print()
    print("  Collaborators:")
    for c in COLLABORATORS:
        print(f"    {c['name']}: {c['split_percent']}% split, ${c['expenses']:,.2f} expenses")
    print()
    
    # Calculate settlement
    result = settle(revenue=REVENUE, collaborators=COLLABORATORS)
    
    print("CALCULATION:")
    print(f"  Total Expenses: ${result.total_expenses:,.2f}")
    print(f"  Net Profit:     ${result.net_profit:,.2f}")
    print(f"  Status:         {'PROFIT' if result.is_profitable else 'LOSS'}")
    print()
    
    print("BREAKDOWN:")
    for c in result.collaborators:
        print(f"  {c.name}:")
        print(f"    Expenses paid:    ${c.expenses:,.2f}")
        print(f"    Profit/Loss share: ${c.profit_share:,.2f}")
        print(f"    PAYOUT:           ${c.payout:,.2f}")
        print()
    
    print("VERIFICATION:")
    total_payouts = sum(c.payout for c in result.collaborators)
    print(f"  Total payouts: ${total_payouts:,.2f}")
    print(f"  Matches revenue: {total_payouts == result.revenue}")
    print()
    
    print("=" * 60)
    print("RESULT: J receives $90.33, Z receives $29.67")
    print("The loss is shared equally according to the 50/50 split.")
    print("=" * 60)


if __name__ == "__main__":
    main()
