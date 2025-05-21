from software_simulations import project_manager_sim, ntask_sim
from analytical_techniques import risk_register, swot_analysis, probability_impact_matrix, root_cause_analysis
from financial_risk_models import value_at_risk, stress_testing, monte_carlo_sim, credit_scoring_sim
import numpy as np

def demonstrate_project_manager_sim():
    print("\n--- Demonstrating ProjectManager Simulation ---")
    risk_card1 = project_manager_sim.create_risk_card(
        risk_name="Supplier Delay",
        description="Key supplier might fail to deliver components on time.",
        impact="High",
        likelihood="Medium",
        priority="High",
        response_plan="Identify alternative suppliers and stock critical components."
    )
    project_manager_sim.add_risk_to_project("Alpha Project", risk_card1)
    project_manager_sim.set_risk_alert(
        risk_name="Supplier Delay",
        condition="Delivery overdue by >2 days",
        recipient="Logistics Lead"
    )

def demonstrate_ntask_sim():
    print("\n--- Demonstrating nTask Risk Matrix Simulation ---")
    project_risks = [
        ("Scope Creep", 3, 4),  # (name, likelihood_score 1-5, impact_score 1-5)
        ("Budget Overrun", 2, 5),
        ("Team Member Unavailable", 4, 3),
        ("Technology Failure", 1, 5)
    ]
    ntask_sim.create_risk_matrix(project_risks)

def demonstrate_risk_register():
    print("\n--- Demonstrating Risk Register ---")
    my_register = risk_register.create_risk_register()
    
    my_register = risk_register.add_risk_to_register(
        register=my_register,
        risk_id="R001",
        name="Data Breach",
        description="Sensitive customer data could be exposed due to a security vulnerability.",
        category="Cybersecurity",
        likelihood="Medium",
        impact="High",
        owner="IT Security Team",
        mitigation_plan="Conduct regular security audits, implement multi-factor authentication.",
        contingency_plan="Activate incident response plan, notify affected customers and authorities."
    )
    my_register = risk_register.add_risk_to_register(
        register=my_register,
        risk_id="R002",
        name="Market Competition",
        description="New competitor enters the market with a similar product at a lower price.",
        category="Market",
        likelihood="High",
        impact="Medium",
        owner="Marketing Dept",
        mitigation_plan="Enhance product features, run loyalty programs.",
        contingency_plan="Offer promotional discounts, targeted marketing campaigns."
    )
    risk_register.display_risk_register(my_register)
    my_register = risk_register.update_risk_status(my_register, "R001", "In Progress")
    risk_register.display_risk_register(my_register)

def demonstrate_swot():
    print("\n--- Demonstrating SWOT Analysis ---")
    strengths = ["Experienced development team", "Strong brand reputation"]
    weaknesses = ["Limited marketing budget", "Reliance on a single supplier"]
    opportunities = ["Growing market demand for our product type", "Potential for international expansion"]
    threats = ["Upcoming regulatory changes", "Price wars from competitors"]
    swot_analysis.perform_swot_analysis(strengths, weaknesses, opportunities, threats)

def demonstrate_probability_impact_matrix():
    print("\n--- Demonstrating Probability and Impact Matrix ---")
    likelihood_scale = ['Very Low', 'Low', 'Medium', 'High', 'Very High'] # 0-4
    impact_scale = ['Negligible', 'Minor', 'Moderate', 'Significant', 'Severe'] # 0-4

    risks_for_matrix = [
        {"name": "Critical System Failure", "likelihood_score": 2, "impact_score": 4}, # Medium, Severe
        {"name": "Project Funding Cut", "likelihood_score": 1, "impact_score": 3},    # Low, Significant
        {"name": "Key Staff Departure", "likelihood_score": 3, "impact_score": 2},     # High, Moderate
        {"name": "Minor Feature Delay", "likelihood_score": 4, "impact_score": 0}      # Very High, Negligible
    ]
    probability_impact_matrix.create_probability_impact_matrix(risks_for_matrix, likelihood_scale, impact_scale)

# New demonstrations for FRM-related tools
def demonstrate_value_at_risk():
    print("\n--- Demonstrating Value at Risk (VaR) Calculations ---")
    
    # Sample historical returns data (as decimals, not percentages)
    returns = np.array([0.01, -0.02, 0.005, 0.008, -0.01, 0.02, -0.03, 0.015, -0.005, 0.012,
                       -0.008, 0.01, -0.015, 0.007, -0.012, 0.018, -0.022, 0.01, 0.003, -0.018])
    
    # Calculate historical VaR
    historical_var = value_at_risk.calculate_historical_var(
        returns=returns,
        confidence_level=0.95,
        investment_value=1000000
    )
    
    # Calculate parametric VaR
    parametric_var = value_at_risk.calculate_parametric_var(
        mean_return=np.mean(returns),
        std_dev=np.std(returns),
        confidence_level=0.95,
        investment_value=1000000,
        time_horizon=1
    )
    
    # Calculate Conditional VaR (Expected Shortfall)
    cvar = value_at_risk.calculate_conditional_var(
        returns=returns,
        confidence_level=0.95,
        investment_value=1000000
    )

def demonstrate_stress_testing():
    print("\n--- Demonstrating Stress Testing ---")
    
    # Define a portfolio
    portfolio = {
        "US Equities": 500000,
        "European Equities": 300000,
        "US Bonds": 400000,
        "Cash": 100000
    }
    
    # Define a historical scenario (2008 Financial Crisis simplified)
    financial_crisis = stress_testing.define_historical_scenario(
        scenario_name="2008 Financial Crisis",
        description="Simulates market conditions similar to the 2008 global financial crisis",
        asset_shocks={
            "US Equities": -0.40,  # 40% drop
            "European Equities": -0.45,  # 45% drop
            "US Bonds": 0.05,  # 5% increase (flight to safety)
            "Cash": 0.00  # No change
        }
    )
    
    # Apply the scenario to the portfolio
    stress_results = stress_testing.apply_scenario_to_portfolio(
        portfolio=portfolio,
        scenario_shocks=financial_crisis["asset_shocks"]
    )

def demonstrate_monte_carlo_sim():
    print("\n--- Demonstrating Monte Carlo Simulation ---")
    
    # Simulate a single asset price
    asset_sim = monte_carlo_sim.simulate_asset_price_monte_carlo(
        initial_price=100,
        mu=0.08,  # 8% expected annual return
        sigma=0.2,  # 20% annual volatility
        days=252,  # One trading year
        simulations=1000,
        percentile=5,
        plot=False  # Set to True to see a plot if running in an environment that supports it
    )

def demonstrate_credit_scoring():
    print("\n--- Demonstrating Credit Scoring and Risk ---")
    
    # Calculate a credit score
    credit_score_result = credit_scoring_sim.simple_credit_score(
        income=75000,
        debt=25000,
        payment_history=90,  # 90/100 score for payment history
        credit_utilization=30,  # 30% of available credit is used
        credit_history_length=5  # 5 years of credit history
    )
    
    # Calculate credit risk parameters
    credit_risk = credit_scoring_sim.calculate_pd_lgd_ead(
        credit_score=credit_score_result["credit_score"],
        loan_amount=200000,
        collateral_value=180000,  # e.g., house value for a mortgage
        loan_term=360  # 30-year mortgage in months
    )
    
    # Analyze a small loan portfolio
    loans = [
        {
            "pd": 0.02,  # 2% probability of default
            "lgd": 0.4,  # 40% loss given default
            "ead": 150000  # Exposure at default
        },
        {
            "pd": 0.05,
            "lgd": 0.6,
            "ead": 75000
        },
        {
            "pd": 0.01,
            "lgd": 0.3,
            "ead": 250000
        }
    ]
    portfolio_risk = credit_scoring_sim.calculate_loan_portfolio_risk(loans)

def demonstrate_root_cause_analysis():
    print("\n--- Demonstrating Root Cause Analysis Techniques ---")
    
    # Demonstrate 5 Whys with predefined answers (normally would be interactive)
    whys = [
        {"question": "Why #1: Why did the project miss its deadline?", 
         "answer": "The final testing phase took longer than expected."},
        {"question": "Why #2: Why did testing take longer than expected?", 
         "answer": "We found more bugs than anticipated."},
        {"question": "Why #3: Why were there more bugs than anticipated?", 
         "answer": "Code reviews were rushed during development."},
        {"question": "Why #4: Why were code reviews rushed?", 
         "answer": "The development team was under pressure to meet intermediate milestones."},
        {"question": "Why #5: Why was there pressure to meet intermediate milestones?", 
         "answer": "The project schedule was too aggressive and didn't account for adequate quality assurance."}
    ]
    
    five_whys_result = root_cause_analysis.perform_5whys(
        problem_statement="The project missed its deadline",
        whys=whys  # Providing predefined answers to avoid interactive input
    )
    
    # Demonstrate Fishbone Diagram data with predefined categories
    fishbone_categories = {
        "People": ["Insufficient training", "High turnover", "Understaffed QA team"],
        "Process": ["Inadequate testing procedures", "Rushed code reviews", "No regression testing"],
        "Technology": ["Outdated development tools", "Incompatible systems", "Technical debt"],
        "Environment": ["Distracting work environment", "Remote work challenges"]
    }
    
    fishbone_result = root_cause_analysis.create_fishbone_diagram_data(
        problem_statement="Excessive software defects",
        categories=fishbone_categories  # Providing predefined categories to avoid interactive input
    )
    
    # Demonstrate Barrier Analysis with predefined barriers
    barriers = [
        {"name": "Data Encryption", "effectiveness": "High", "status": "Intact"},
        {"name": "Access Controls", "effectiveness": "Medium", "status": "Breached"},
        {"name": "Employee Training", "effectiveness": "Medium", "status": "Intact"},
        {"name": "Intrusion Detection", "effectiveness": "High", "status": "Missing"}
    ]
    
    barrier_result = root_cause_analysis.perform_barrier_analysis(
        hazard="Data Breach",
        target="Customer Personal Information",
        barriers=barriers  # Providing predefined barriers to avoid interactive input
    )

if __name__ == "__main__":
    # Original demonstrations
    demonstrate_project_manager_sim()
    demonstrate_ntask_sim()
    demonstrate_risk_register()
    demonstrate_swot()
    demonstrate_probability_impact_matrix()
    
    # New FRM-related demonstrations
    demonstrate_value_at_risk()
    demonstrate_stress_testing()
    demonstrate_monte_carlo_sim()
    demonstrate_credit_scoring()
    demonstrate_root_cause_analysis() 