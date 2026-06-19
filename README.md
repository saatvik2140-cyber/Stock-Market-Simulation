# Stochastic Stock Market Stress & Random Shock Simulator

A quantitative financial risk model that simulates an individual stock asset over a 250-day trading timeline. The simulation utilizes random walk mechanics combined with unpredictable, dynamic event tracking to stress-test asset resilience.

## 📊 How the Financial Logic Works
This model simulates asset pricing by combining long-term market momentum with short-term, daily unpredictable volatility:
* **Drift (Market Momentum):** A baseline upward trend factor set at `0.0004` daily.
* **Volatility (Market Risk):** A daily price fluctuation variance factor set at `0.01`.
* **Random Walk Engine:** Every single trading day, a random shock variable (`random.uniform(-1, 1)`) is generated to simulate normal daily market news and price noise.

## 💥 Dynamic Shock Timing Mechanic
Unlike basic financial models with fixed event timelines, this simulator incorporates **unpredictable risk timing** (`random.randint(1, 100)`). A severe macroeconomic market correction drop is programmed to strike randomly within the first 100 trading days of the year, testing the asset's recovery trends and systemic stabilization.

---
*Financial simulation engine designed and maintained by Saatvik.*
