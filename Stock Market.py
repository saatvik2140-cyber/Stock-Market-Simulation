import random
import matplotlib.pyplot as plt

# 1. Starting Setup
stock_price = 100
drift = 0.0004
volatility = 0.01  # Lowered slightly so your stock doesn't swing too violently
stock_crash = 25  # The dollar amount to lose during the crash

history_stock = [stock_price]

# 2. Market Loop
for day in range(250):
    # FIXED: Check for the exact crash day
    if day == random.uniform(0, 100):
        stock_price = stock_price - stock_crash

    # FIXED: Added the missing random market shock
    market_shock = random.uniform(-1, 1)

    daily_change = drift + (volatility * market_shock)
    stock_price = stock_price * (1 + daily_change)

    # FIXED: Matched variable names precisely
    history_stock.append(stock_price)


# 3. Graph Layout
plt.figure(figsize=(9, 6))
plt.plot(
    history_stock,
    label="Stock",
    color="darkgreen",
    linewidth=3,
    linestyle="--",
)

plt.title(
    "Stock simulation over 250 days",
    fontsize=12,
    fontweight="bold",
)

plt.xlabel("Timeline (Days)", fontsize=10)
plt.ylabel("Stock price", fontsize=10)
plt.legend(loc="upper left")
plt.grid(True, linestyle="--", alpha=0.5)

# display graph
plt.show()
