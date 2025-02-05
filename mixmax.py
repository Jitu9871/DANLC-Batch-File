import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Sample sales data
data = {
    'Date': pd.date_range(start='2024-01-01', periods=12, freq='M'),
    'Region A': np.random.randint(1000, 5000, 12),
    'Region B': np.random.randint(2000, 6000, 12),
    'Region C': np.random.randint(1500, 5500, 12)
}

# Create DataFrame
df = pd.DataFrame(data)
df.set_index('Date', inplace=True)

# Create subplots
fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(10, 8), sharex=True)

# Plot sales for each region
df.plot(y='Region A', ax=axes[0], title='Sales in Region A', color='blue')
df.plot(y='Region B', ax=axes[1], title='Sales in Region B', color='red')
df.plot(y='Region C', ax=axes[2], title='Sales in Region C', color='green')

# Formatting
plt.xlabel('Date')
plt.tight_layout()
plt.show()
