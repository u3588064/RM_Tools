import numpy as np
import pandas as pd

def simple_credit_score(income, debt, payment_history, credit_utilization, credit_history_length):
    """
    Calculate a simple credit score based on common factors.
    
    Args:
        income (float): Annual income in dollars.
        debt (float): Total debt in dollars.
        payment_history (float): Score from 0-100 representing payment history (higher is better).
        credit_utilization (float): Percentage of available credit being used (0-100, lower is better).
        credit_history_length (int): Length of credit history in years.
        
    Returns:
        dict: Dictionary containing credit score and component scores.
    """
    # Calculate debt-to-income ratio (DTI)
    dti = (debt / income) * 100 if income > 0 else 100
    
    # Component scores (0-100 scale)
    dti_score = max(0, min(100, 100 - dti))
    payment_history_score = payment_history  # Already on 0-100 scale
    utilization_score = max(0, min(100, 100 - credit_utilization))
    
    # Credit history length score (0-100 scale)
    if credit_history_length >= 10:
        history_score = 100
    elif credit_history_length <= 0:
        history_score = 0
    else:
        history_score = (credit_history_length / 10) * 100
    
    # Calculate weighted score (300-850 scale, similar to FICO)
    weighted_score = (
        0.35 * payment_history_score +
        0.30 * utilization_score +
        0.25 * dti_score +
        0.10 * history_score
    )
    
    # Scale to 300-850 range
    credit_score = int(300 + (weighted_score / 100) * 550)
    
    # Determine credit rating
    if credit_score >= 800:
        rating = "Excellent"
    elif credit_score >= 740:
        rating = "Very Good"
    elif credit_score >= 670:
        rating = "Good"
    elif credit_score >= 580:
        rating = "Fair"
    else:
        rating = "Poor"
    
    # Print results
    print("\n--- Credit Score Assessment ---")
    print(f"Credit Score: {credit_score} ({rating})")
    print("\nComponent Scores (0-100 scale):")
    print(f"  Payment History (35%): {payment_history_score:.1f}")
    print(f"  Credit Utilization (30%): {utilization_score:.1f}")
    print(f"  Debt-to-Income (25%): {dti_score:.1f}")
    print(f"  Credit History Length (10%): {history_score:.1f}")
    print(f"\nDebt-to-Income Ratio: {dti:.1f}%")
    
    return {
        "credit_score": credit_score,
        "rating": rating,
        "components": {
            "payment_history": payment_history_score,
            "credit_utilization": utilization_score,
            "debt_to_income": dti_score,
            "credit_history_length": history_score
        },
        "dti_ratio": dti
    }

def calculate_pd_lgd_ead(credit_score, loan_amount, collateral_value=0, loan_term=12):
    """
    Calculate Probability of Default (PD), Loss Given Default (LGD), and Exposure at Default (EAD).
    
    Args:
        credit_score (int): Credit score (300-850 scale).
        loan_amount (float): Amount of the loan.
        collateral_value (float): Value of any collateral securing the loan.
        loan_term (int): Term of the loan in months.
        
    Returns:
        dict: Dictionary containing PD, LGD, EAD, and expected loss.
    """
    # Calculate PD based on credit score (simplified model)
    if credit_score >= 800:
        pd = 0.001  # 0.1% probability of default
    elif credit_score >= 740:
        pd = 0.005  # 0.5% probability of default
    elif credit_score >= 670:
        pd = 0.02   # 2% probability of default
    elif credit_score >= 580:
        pd = 0.10   # 10% probability of default
    else:
        pd = 0.30   # 30% probability of default
    
    # Calculate LGD based on collateral (simplified model)
    recovery_rate = min(1.0, collateral_value / loan_amount) if loan_amount > 0 else 0
    lgd = 1 - recovery_rate
    
    # Calculate EAD (simplified as loan amount)
    ead = loan_amount
    
    # Calculate expected loss
    expected_loss = pd * lgd * ead
    
    # Print results
    print("\n--- Credit Risk Parameters ---")
    print(f"Probability of Default (PD): {pd:.2%}")
    print(f"Loss Given Default (LGD): {lgd:.2%}")
    print(f"Exposure at Default (EAD): ${ead:,.2f}")
    print(f"Expected Loss: ${expected_loss:,.2f}")
    print(f"Expected Loss as % of Loan: {(expected_loss/loan_amount)*100:.4f}%" if loan_amount > 0 else "N/A")
    
    return {
        "pd": pd,
        "lgd": lgd,
        "ead": ead,
        "expected_loss": expected_loss,
        "expected_loss_percentage": (expected_loss/loan_amount)*100 if loan_amount > 0 else None
    }

def calculate_loan_portfolio_risk(loans):
    """
    Calculate risk metrics for a loan portfolio.
    
    Args:
        loans (list of dict): List of loan dictionaries, each containing 'amount', 'pd', 'lgd', and 'ead'.
        
    Returns:
        dict: Dictionary containing portfolio risk metrics.
    """
    if not loans:
        print("Error: No loans provided.")
        return None
    
    # Calculate total exposure and expected loss
    total_exposure = sum(loan['ead'] for loan in loans)
    total_expected_loss = sum(loan['pd'] * loan['lgd'] * loan['ead'] for loan in loans)
    
    # Calculate weighted average PD and LGD
    weighted_pd = sum(loan['pd'] * loan['ead'] for loan in loans) / total_exposure if total_exposure > 0 else 0
    weighted_lgd = sum(loan['lgd'] * loan['ead'] for loan in loans) / total_exposure if total_exposure > 0 else 0
    
    # Calculate expected loss ratio
    expected_loss_ratio = (total_expected_loss / total_exposure) * 100 if total_exposure > 0 else 0
    
    # Print results
    print("\n--- Loan Portfolio Risk Analysis ---")
    print(f"Total Portfolio Exposure: ${total_exposure:,.2f}")
    print(f"Total Expected Loss: ${total_expected_loss:,.2f}")
    print(f"Expected Loss Ratio: {expected_loss_ratio:.4f}%")
    print(f"Weighted Average PD: {weighted_pd:.2%}")
    print(f"Weighted Average LGD: {weighted_lgd:.2%}")
    
    return {
        "total_exposure": total_exposure,
        "total_expected_loss": total_expected_loss,
        "expected_loss_ratio": expected_loss_ratio,
        "weighted_pd": weighted_pd,
        "weighted_lgd": weighted_lgd
    } 