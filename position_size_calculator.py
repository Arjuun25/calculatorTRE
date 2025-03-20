# Position Size Calculator

# Get user inputs
account_balance = float(input("Enter your total account balance: "))
risk_percentage = float(input("Enter the percentage of risk per trade (e.g., 2 for 2%): "))
stop_loss = float(input("Enter the stop-loss amount: "))

# Calculate risk amount
risk_amount = (risk_percentage / 100) * account_balance

# Calculate position size
position_size = risk_amount / stop_loss

# Display result
print(f"Your position size should be: {position_size} units")
