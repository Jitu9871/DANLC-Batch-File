
import matplotlib.pyplot as plt
import pandas as pd

# Sample sales data
data = {
    'Date': pd.date_range(start='2024-01-01', periods=10, freq='M'),
    'North': [100, 120, 130, 140, 150, 160, 170, 180, 190, 200],
    'South': [90, 110, 115, 130, 135, 145, 155, 165, 175, 185],
    'East': [80, 95, 100, 110, 120, 130, 140, 150, 160, 170],
    'West': [70, 85, 90, 100, 110, 120, 130, 140, 150, 160]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Create subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 8))  # 2x2 grid

# List of regions
regions = ['North', 'South', 'East', 'West']

# Loop through regions and create subplots
for ax, region in zip(axes.flatten(), regions):
    ax.plot(df['Date'], df[region], marker='o', label=region)
    ax.set_title(f'{region} Region Sales')
    ax.set_xlabel('Date')
    ax.set_ylabel('Sales')
    ax.legend()
    ax.grid(True)

# Adjust layout
plt.tight_layout()
plt.show()
