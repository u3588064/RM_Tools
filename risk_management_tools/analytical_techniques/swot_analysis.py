def perform_swot_analysis(strengths, weaknesses, opportunities, threats):
    \"\"\"
    Performs and displays a SWOT analysis.

    Args:
        strengths (list): List of strings describing strengths.
        weaknesses (list): List of strings describing weaknesses.
        opportunities (list): List of strings describing opportunities.
        threats (list): List of strings describing threats.

    Returns:
        dict: A dictionary containing the SWOT analysis.
    \"\"\"
    swot_data = {
        "Strengths": strengths,
        "Weaknesses": weaknesses,
        "Opportunities": opportunities,
        "Threats": threats
    }

    print("\n--- SWOT Analysis ---")
    for category, items in swot_data.items():
        print(f"\n{category}:")
        if items:
            for item in items:
                print(f"  - {item}")
        else:
            print("  (No items listed)")
    print("-" * 20)
    print("SWOT Analysis complete.")
    return swot_data 