def create_risk_register():
    \"\"\"Initializes an empty risk register (a list of risk entries).\"\"\"
    return []

def add_risk_to_register(register, risk_id, name, description, category, likelihood, impact, owner, mitigation_plan, contingency_plan, status="Open"):
    \"\"\"
    Adds a new risk to the risk register.

    Args:
        register (list): The risk register (list of dicts).
        risk_id (str): Unique identifier for the risk.
        name (str): Short name or title of the risk.
        description (str): Detailed description of the risk.
        category (str): Category of the risk (e.g., Technical, Financial, Operational).
        likelihood (str): Estimated likelihood (e.g., 'High', 'Medium', 'Low').
        impact (str): Estimated impact (e.g., 'High', 'Medium', 'Low').
        owner (str): Person or team responsible for managing the risk.
        mitigation_plan (str): Actions to take to reduce likelihood/impact.
        contingency_plan (str): Actions to take if the risk occurs.
        status (str): Current status of the risk (e.g., 'Open', 'In Progress', 'Closed', 'Mitigated').

    Returns:
        list: The updated risk register.
    \"\"\"
    risk_entry = {
        "id": risk_id,
        "name": name,
        "description": description,
        "category": category,
        "likelihood": likelihood,
        "impact": impact,
        "owner": owner,
        "mitigation_plan": mitigation_plan,
        "contingency_plan": contingency_plan,
        "status": status,
        "priority": "Not set" # Could be calculated based on likelihood and impact
    }
    register.append(risk_entry)
    print(f"Risk '{name}' (ID: {risk_id}) added to the register.")
    return register

def update_risk_status(register, risk_id, new_status):
    \"\"\"Updates the status of an existing risk in the register.\"\"\"
    for risk in register:
        if risk["id"] == risk_id:
            risk["status"] = new_status
            print(f"Status of risk ID '{risk_id}' updated to '{new_status}'.")
            return register
    print(f"Risk ID '{risk_id}' not found in the register.")
    return register

def display_risk_register(register):
    \"\"\"Prints a formatted view of the risk register.\"\"\"
    if not register:
        print("Risk register is empty.")
        return

    print("\n--- Risk Register ---")
    headers = ["ID", "Name", "Category", "Likelihood", "Impact", "Owner", "Status", "Priority"]
    # Dynamically adjust column widths later if needed, for now use fixed or estimate
    print("{:<5} | {:<25} | {:<15} | {:<10} | {:<10} | {:<15} | {:<12} | {:<10}".format(*headers))
    print("-" * 120)

    for risk in register:
        print("{:<5} | {:<25} | {:<15} | {:<10} | {:<10} | {:<15} | {:<12} | {:<10}".format(
            risk.get("id", "N/A"),
            risk.get("name", "N/A"),
            risk.get("category", "N/A"),
            risk.get("likelihood", "N/A"),
            risk.get("impact", "N/A"),
            risk.get("owner", "N/A"),
            risk.get("status", "N/A"),
            risk.get("priority", "N/A")
        ))
    print("-" * 120) 