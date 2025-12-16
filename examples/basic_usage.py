#!/usr/bin/env python3
"""
Basic usage examples for the Braid Formula.

Run: python examples/basic_usage.py
"""

from braid_formula import settle, quick_settle


def main():
    print("=" * 60)
    print("BRAID FORMULA - Basic Examples")
    print("=" * 60)
    
    # Example 1: Simple profitable event
    print("\n📈 Example 1: Profitable Event")
    print("-" * 40)
    
    result = settle(
        revenue=1000,
        collaborators=[
            {"name": "Alice", "split_percent": 60, "expenses": 200},
            {"name": "Bob", "split_percent": 40, "expenses": 100},
        ]
    )
    
    print(f"Revenue: ${result.revenue}")
    print(f"Total Expenses: ${result.total_expenses}")
    print(f"Net Profit: ${result.net_profit}")
    print(f"Status: {'PROFIT' if result.is_profitable else 'LOSS'}")
    print("\nPayouts:")
    for c in result.collaborators:
        print(f"  {c.name}: ${c.payout}")
    
    # Example 2: Loss scenario
    print("\n📉 Example 2: Loss Scenario")
    print("-" * 40)
    
    result = settle(
        revenue=120,
        collaborators=[
            {"name": "J", "split_percent": 50, "expenses": 151.15},
            {"name": "Z", "split_percent": 50, "expenses": 90.49},
        ]
    )
    
    print(f"Revenue: ${result.revenue}")
    print(f"Total Expenses: ${result.total_expenses}")
    print(f"Net Profit: ${result.net_profit}")
    print(f"Status: {'PROFIT' if result.is_profitable else 'LOSS'}")
    print("\nPayouts:")
    for c in result.collaborators:
        print(f"  {c.name}: ${c.payout}")
    
    # Example 3: Quick settle
    print("\n⚡ Example 3: Quick Settle (One-liner)")
    print("-" * 40)
    
    payouts = quick_settle(
        revenue=500,
        splits={"Lead": 70, "Support": 30},
        expenses={"Lead": 100, "Support": 50}
    )
    
    print(f"Payouts: {payouts}")
    
    # Example 4: Three-way split
    print("\n👥 Example 4: Three-Way Split")
    print("-" * 40)
    
    result = settle(
        revenue=3000,
        collaborators=[
            {"name": "Founder", "split_percent": 50, "expenses": 500},
            {"name": "Partner A", "split_percent": 30, "expenses": 200},
            {"name": "Partner B", "split_percent": 20, "expenses": 100},
        ]
    )
    
    print(f"Revenue: ${result.revenue}")
    print(f"Net Profit: ${result.net_profit}")
    print("\nPayouts:")
    for c in result.collaborators:
        print(f"  {c.name} ({c.split_percent}%): ${c.payout}")
    
    # Example 5: JSON output
    print("\n📋 Example 5: JSON Output")
    print("-" * 40)
    
    import json
    result = settle(
        revenue=1000,
        collaborators=[
            {"name": "A", "split_percent": 50, "expenses": 100},
            {"name": "B", "split_percent": 50, "expenses": 100},
        ]
    )
    
    print(json.dumps(result.to_dict(), indent=2))
    
    print("\n" + "=" * 60)
    print("Done!")


if __name__ == "__main__":
    main()
