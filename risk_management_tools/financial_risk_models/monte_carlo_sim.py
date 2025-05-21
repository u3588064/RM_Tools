import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def simulate_asset_price_monte_carlo(initial_price, mu, sigma, days, simulations=1000, percentile=5, plot=False):
    """
    Simulate future asset prices using Monte Carlo simulation with Geometric Brownian Motion.
    
    Args:
        initial_price (float): Initial price of the asset.
        mu (float): Expected annual return (drift).
        sigma (float): Annual volatility.
        days (int): Number of days to simulate.
        simulations (int): Number of simulation paths.
        percentile (int): Percentile for risk calculation (e.g., 5 for 5% worst case).
        plot (bool): Whether to plot the simulations.
        
    Returns:
        dict: Dictionary containing simulation results and risk metrics.
    """
    # Convert annual parameters to daily
    daily_returns = mu / 252  # Assuming 252 trading days in a year
    daily_volatility = sigma / np.sqrt(252)
    
    # Generate random normal returns
    np.random.seed(42)  # For reproducibility
    random_returns = np.random.normal(loc=daily_returns, scale=daily_volatility, size=(days, simulations))
    
    # Create price paths
    price_paths = np.zeros((days + 1, simulations))
    price_paths[0] = initial_price
    
    for t in range(1, days + 1):
        price_paths[t] = price_paths[t-1] * np.exp(random_returns[t-1])
    
    # Calculate final prices and statistics
    final_prices = price_paths[-1]
    mean_final_price = np.mean(final_prices)
    median_final_price = np.median(final_prices)
    min_price = np.min(final_prices)
    max_price = np.max(final_prices)
    percentile_price = np.percentile(final_prices, percentile)
    
    # Calculate potential loss at the specified percentile
    potential_loss = initial_price - percentile_price
    potential_loss_percentage = (potential_loss / initial_price) * 100
    
    # Print results
    print("\n--- Monte Carlo Simulation Results ---")
    print(f"Initial Price: ${initial_price:.2f}")
    print(f"Simulations: {simulations}")
    print(f"Time Horizon: {days} days")
    print(f"Mean Final Price: ${mean_final_price:.2f}")
    print(f"Median Final Price: ${median_final_price:.2f}")
    print(f"Range: ${min_price:.2f} to ${max_price:.2f}")
    print(f"{percentile}th Percentile Price: ${percentile_price:.2f}")
    print(f"Potential Loss at {percentile}th percentile: ${potential_loss:.2f} ({potential_loss_percentage:.2f}%)")
    
    # Plot if requested
    if plot:
        plt.figure(figsize=(10, 6))
        plt.plot(price_paths[:, :100])  # Plot first 100 simulations for clarity
        plt.axhline(y=initial_price, color='r', linestyle='-', label='Initial Price')
        plt.axhline(y=percentile_price, color='g', linestyle='--', 
                   label=f'{percentile}th Percentile: ${percentile_price:.2f}')
        plt.title(f'Monte Carlo Simulation: {simulations} Paths over {days} Days')
        plt.xlabel('Days')
        plt.ylabel('Price ($)')
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()
    
    return {
        "initial_price": initial_price,
        "price_paths": price_paths,
        "final_prices": final_prices,
        "mean_final_price": mean_final_price,
        "median_final_price": median_final_price,
        "min_price": min_price,
        "max_price": max_price,
        "percentile_price": percentile_price,
        "potential_loss": potential_loss,
        "potential_loss_percentage": potential_loss_percentage
    }

def simulate_portfolio_monte_carlo(initial_values, expected_returns, volatilities, correlations, days, simulations=1000, percentile=5):
    """
    Simulate portfolio performance using Monte Carlo simulation with correlated assets.
    
    Args:
        initial_values (dict): Dictionary with asset names as keys and their initial values as values.
        expected_returns (dict): Dictionary with asset names as keys and their expected annual returns as values.
        volatilities (dict): Dictionary with asset names as keys and their annual volatilities as values.
        correlations (dict): Dictionary with tuples of asset pairs as keys and their correlations as values.
        days (int): Number of days to simulate.
        simulations (int): Number of simulation paths.
        percentile (int): Percentile for risk calculation.
        
    Returns:
        dict: Dictionary containing simulation results and risk metrics.
    """
    assets = list(initial_values.keys())
    n_assets = len(assets)
    
    # Create correlation matrix
    corr_matrix = np.identity(n_assets)
    for i in range(n_assets):
        for j in range(i+1, n_assets):
            asset_pair = (assets[i], assets[j])
            reverse_pair = (assets[j], assets[i])
            if asset_pair in correlations:
                corr_matrix[i, j] = corr_matrix[j, i] = correlations[asset_pair]
            elif reverse_pair in correlations:
                corr_matrix[i, j] = corr_matrix[j, i] = correlations[reverse_pair]
    
    # Convert annual parameters to daily
    daily_returns = np.array([expected_returns[asset] / 252 for asset in assets])
    daily_volatilities = np.array([volatilities[asset] / np.sqrt(252) for asset in assets])
    
    # Create covariance matrix
    cov_matrix = np.outer(daily_volatilities, daily_volatilities) * corr_matrix
    
    # Generate correlated random returns
    np.random.seed(42)
    random_returns = np.random.multivariate_normal(mean=daily_returns, cov=cov_matrix, size=(days, simulations))
    
    # Create price paths for each asset
    price_paths = {asset: np.zeros((days + 1, simulations)) for asset in assets}
    for i, asset in enumerate(assets):
        price_paths[asset][0] = initial_values[asset]
        for t in range(1, days + 1):
            price_paths[asset][t] = price_paths[asset][t-1] * np.exp(random_returns[t-1, :, i])
    
    # Calculate portfolio value paths
    portfolio_paths = np.zeros((days + 1, simulations))
    for asset in assets:
        portfolio_paths += price_paths[asset]
    
    # Calculate final portfolio values and statistics
    initial_portfolio_value = sum(initial_values.values())
    final_portfolio_values = portfolio_paths[-1]
    mean_final_value = np.mean(final_portfolio_values)
    median_final_value = np.median(final_portfolio_values)
    min_value = np.min(final_portfolio_values)
    max_value = np.max(final_portfolio_values)
    percentile_value = np.percentile(final_portfolio_values, percentile)
    
    # Calculate potential loss at the specified percentile
    potential_loss = initial_portfolio_value - percentile_value
    potential_loss_percentage = (potential_loss / initial_portfolio_value) * 100
    
    # Print results
    print("\n--- Portfolio Monte Carlo Simulation Results ---")
    print(f"Initial Portfolio Value: ${initial_portfolio_value:.2f}")
    print(f"Simulations: {simulations}")
    print(f"Time Horizon: {days} days")
    print(f"Mean Final Value: ${mean_final_value:.2f}")
    print(f"Median Final Value: ${median_final_value:.2f}")
    print(f"Range: ${min_value:.2f} to ${max_value:.2f}")
    print(f"{percentile}th Percentile Value: ${percentile_value:.2f}")
    print(f"Potential Loss at {percentile}th percentile: ${potential_loss:.2f} ({potential_loss_percentage:.2f}%)")
    
    return {
        "initial_portfolio_value": initial_portfolio_value,
        "portfolio_paths": portfolio_paths,
        "final_portfolio_values": final_portfolio_values,
        "mean_final_value": mean_final_value,
        "median_final_value": median_final_value,
        "min_value": min_value,
        "max_value": max_value,
        "percentile_value": percentile_value,
        "potential_loss": potential_loss,
        "potential_loss_percentage": potential_loss_percentage
    } 