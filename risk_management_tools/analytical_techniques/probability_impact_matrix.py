def create_probability_impact_matrix(risks_data, likelihood_scale, impact_scale):
    \"\"\"
    Creates and displays a probability and impact matrix.

    Args:
        risks_data (list of dicts): Each dict should have 'name', 'likelihood_score', 'impact_score'.
                                   Scores are indices into the provided scales.
        likelihood_scale (list): Descriptions for likelihood levels (e.g., ['Very Low', 'Low', 'Medium', 'High', 'Very High']).
        impact_scale (list): Descriptions for impact levels (e.g., ['Negligible', 'Minor', 'Moderate', 'Significant', 'Severe']).

    Returns:
        list: A list of processed risks with their matrix categorization.
              Each item will have: name, likelihood, impact, likelihood_score, impact_score, risk_level
    \"\"\"
    if not risks_data:
        print("No risk data provided for the matrix.")
        return []

    print("\n--- Probability and Impact Matrix ---")
    
    # Initialize matrix display (optional, could be more visual with libraries like matplotlib or a GUI)
    # For console, we can list risks and their assessed levels.

    processed_risks = []
    for risk in risks_data:
        l_score = risk['likelihood_score'] # Expecting 0-indexed score
        i_score = risk['impact_score']     # Expecting 0-indexed score

        likelihood = likelihood_scale[l_score] if 0 <= l_score < len(likelihood_scale) else "Invalid Likelihood"
        impact = impact_scale[i_score] if 0 <= i_score < len(impact_scale) else "Invalid Impact"

        # Simplified risk level calculation (can be customized based on a predefined matrix logic)
        # Example: Low-Low, Low-Med, Med-Med, Med-High, High-High etc.
        risk_level_score = l_score + i_score # A simple sum for demonstration
        
        risk_level = "Low"
        if risk_level_score >= (len(likelihood_scale) + len(impact_scale) -2) * 0.75: # Top 25% severity
            risk_level = "Critical"
        elif risk_level_score >= (len(likelihood_scale) + len(impact_scale) -2) * 0.5: # 50-75% severity
            risk_level = "High"
        elif risk_level_score >= (len(likelihood_scale) + len(impact_scale) -2) * 0.25: # 25-50% severity
            risk_level = "Medium"
        
        processed_risk = {
            "name": risk["name"],
            "likelihood": likelihood,
            "impact": impact,
            "likelihood_score": l_score,
            "impact_score": i_score,
            "risk_level": risk_level
        }
        processed_risks.append(processed_risk)
        
        print(f"Risk: {risk['name']}\n  Likelihood: {likelihood} (Score: {l_score})\n  Impact: {impact} (Score: {i_score})\n  Assessed Risk Level: {risk_level}\n")

    print("-" * 40)
    print("Probability and Impact Matrix processing complete.")
    return processed_risks 