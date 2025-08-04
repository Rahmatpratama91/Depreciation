import matplotlib.pyplot as plt 
import numpy as np

# Given data / Diketahui dari soal
initial_cost = 15000
salvage_value = 0.10 * initial_cost  # 10% of initial cost
n_years = 5
interest_rate = 0.18

# Year range
years = np.arange(1, n_years + 1)

# Straight line depreciation method
straight_annual_depreciation = (initial_cost - salvage_value) / n_years
straight_book_value = [initial_cost - straight_annual_depreciation * i for i in range(n_years + 1)]

# Sinking fund depreciation method
A = (initial_cost - salvage_value) * (interest_rate / ((1 + interest_rate) ** n_years - 1))
sinking_book_value = [initial_cost]
for i in range(1, n_years + 1):
    prev = sinking_book_value[-1]
    new = prev * (1 + interest_rate) - A
    sinking_book_value.append(new)

# Double declining balance depreciation method
ddb_book_value = [initial_cost]
ddb_rate = 2 / n_years
for i in range(n_years):
    depreciation = ddb_book_value[-1] * ddb_rate
    new_value = ddb_book_value[-1] - depreciation
    if new_value < salvage_value:
        new_value = salvage_value
    ddb_book_value.append(new_value)

# Plotting
plt.figure(figsize=(10, 7))
plt.plot(range(n_years + 1), straight_book_value, marker='o', label='Straight Line')
plt.plot(range(n_years + 1), sinking_book_value, marker='s', label='Sinking Fund')
plt.plot(range(n_years + 1), ddb_book_value, marker='^', label='Double Declining Balance')

plt.title("Book value over time by each depreciation method")
plt.xlabel("Year")
plt.ylabel("Book Value (Rp)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
