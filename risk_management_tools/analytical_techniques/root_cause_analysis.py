def perform_5whys(problem_statement, whys=None, max_whys=5):
    """
    Perform a 5 Whys root cause analysis by asking "why" repeatedly to dig deeper into the cause.
    
    Args:
        problem_statement (str): The initial problem statement.
        whys (list, optional): List of "why" questions and answers. If None, will prompt for input.
        max_whys (int): Maximum number of "why" questions to ask (default is 5).
        
    Returns:
        dict: Dictionary containing the problem statement, whys, and root cause.
    """
    if whys is None:
        whys = []
        print("\n--- 5 Whys Root Cause Analysis ---")
        print(f"Problem Statement: {problem_statement}")
        
        for i in range(1, max_whys + 1):
            why_question = f"Why #{i}: Why {problem_statement if i == 1 else whys[-1]['answer']}?"
            print(f"\n{why_question}")
            
            answer = input("Answer: ")
            if not answer:
                break
                
            whys.append({"question": why_question, "answer": answer})
            
            continue_analysis = input(f"\nContinue to Why #{i+1}? (y/n): ").lower()
            if continue_analysis != 'y':
                break
    
    # Print results
    print("\n--- 5 Whys Analysis Results ---")
    print(f"Problem Statement: {problem_statement}")
    for i, why in enumerate(whys, 1):
        print(f"\nWhy #{i}: {why['question']}")
        print(f"Answer: {why['answer']}")
    
    root_cause = whys[-1]['answer'] if whys else "No root cause identified"
    print(f"\nRoot Cause: {root_cause}")
    
    return {
        "problem_statement": problem_statement,
        "whys": whys,
        "root_cause": root_cause
    }

def create_fishbone_diagram_data(problem_statement, categories=None):
    """
    Create data structure for a fishbone (Ishikawa) diagram to analyze root causes.
    Note: This function creates the data structure only. Visualization would require
    a graphical library or manual drawing.
    
    Args:
        problem_statement (str): The problem to analyze.
        categories (dict, optional): Dictionary of categories and their causes.
                                    If None, will use standard categories and prompt for input.
        
    Returns:
        dict: Dictionary containing the problem statement and categorized causes.
    """
    standard_categories = [
        "People", "Process", "Equipment", "Materials", 
        "Environment", "Management"
    ]
    
    if categories is None:
        categories = {}
        print("\n--- Fishbone (Ishikawa) Diagram Data Collection ---")
        print(f"Problem Statement: {problem_statement}")
        
        for category in standard_categories:
            print(f"\nCategory: {category}")
            causes = []
            while True:
                cause = input(f"Enter a cause for '{category}' (or press Enter to finish this category): ")
                if not cause:
                    break
                causes.append(cause)
            
            if causes:
                categories[category] = causes
    
    # Print results
    print("\n--- Fishbone Diagram Data ---")
    print(f"Problem Statement: {problem_statement}")
    for category, causes in categories.items():
        print(f"\n{category}:")
        for cause in causes:
            print(f"  - {cause}")
    
    return {
        "problem_statement": problem_statement,
        "categories": categories
    }

def perform_barrier_analysis(hazard, target, barriers=None):
    """
    Perform a barrier analysis to identify controls that prevent hazards from reaching targets.
    
    Args:
        hazard (str): The hazard or threat being analyzed.
        target (str): The target that could be harmed by the hazard.
        barriers (list, optional): List of dictionaries containing barrier information.
                                  If None, will prompt for input.
        
    Returns:
        dict: Dictionary containing the hazard, target, and barriers.
    """
    if barriers is None:
        barriers = []
        print("\n--- Barrier Analysis ---")
        print(f"Hazard: {hazard}")
        print(f"Target: {target}")
        
        while True:
            print("\nAdd a barrier:")
            name = input("Barrier name (or press Enter to finish): ")
            if not name:
                break
                
            effectiveness = input("Effectiveness (Low/Medium/High): ")
            status = input("Status (Intact/Breached/Missing): ")
            
            barriers.append({
                "name": name,
                "effectiveness": effectiveness,
                "status": status
            })
    
    # Print results
    print("\n--- Barrier Analysis Results ---")
    print(f"Hazard: {hazard}")
    print(f"Target: {target}")
    print("\nBarriers:")
    for i, barrier in enumerate(barriers, 1):
        print(f"\n{i}. {barrier['name']}")
        print(f"   Effectiveness: {barrier['effectiveness']}")
        print(f"   Status: {barrier['status']}")
    
    # Identify gaps
    breached_or_missing = [b for b in barriers if b['status'].lower() in ['breached', 'missing']]
    if breached_or_missing:
        print("\nGaps in Protection:")
        for barrier in breached_or_missing:
            print(f"  - {barrier['name']} ({barrier['status']})")
    
    return {
        "hazard": hazard,
        "target": target,
        "barriers": barriers,
        "gaps": breached_or_missing
    } 
 