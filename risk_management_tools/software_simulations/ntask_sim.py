def create_risk_matrix(risks):
    \"\"\"
    Simulates creating a risk matrix like in nTask.
    Risks should be a list of tuples: (risk_name, likelihood_score, impact_score)
    Likelihood/Impact scores are e.g., 1-5 (Low to High).
    \"\"\"
    if not risks:
        print("No risks provided to create a matrix.")
        return None

    print("\n--- Risk Matrix ---")
    print("{:<20} | {:<10} | {:<10} | {:<10}".format("Risk Name", "Likelihood", "Impact", "Severity"))
    print("-" * 60)

    matrix = []
    for risk_name, likelihood, impact in risks:
        severity_score = likelihood * impact # Simple severity calculation
        severity_label = ""
        if severity_score >= 15:
            severity_label = "Very High"
        elif severity_score >= 10:
            severity_label = "High"
        elif severity_score >= 5:
            severity_label = "Medium"
        else:
            severity_label = "Low"
        
        matrix.append({
            "name": risk_name,
            "likelihood": likelihood,
            "impact": impact,
            "severity_score": severity_score,
            "severity_label": severity_label
        })
        print("{:<20} | {:<10} | {:<10} | {:<10}".format(risk_name, likelihood, impact, severity_label))
    
    print("-" * 60)
    print("Matrix generation complete.")
    return matrix 