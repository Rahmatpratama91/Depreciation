# Depreciation Methods Calculator
- Depreciation is the process of allocating the cost of a tangible fixed asset over its useful life. It reflects how much of the asset’s value has been used up over time.
- Why depreciation matters: shows asset’s decreasing value on financial statements.Helps in tax deduction (as expense). Aids in budgeting for replacement of assets.
- Examples of depreciable assets: machines,vehicles,buildings,computers.

---

## 📌 Project Overview
- A Python project to compute and visualize annual depreciation and book value of an asset using three different depreciation methods:
1. Straight Line Method
2. Sinking Fund Method
3. Double Declining Balance Method
   
- This project simulates the depreciation of a machine with the following conditions:
<img width="950" height="275" alt="image" src="https://github.com/user-attachments/assets/13d5848d-a00e-41bc-9a39-d64eb885329e" />

- **Initial Cost:** Rp 15,000
- **Salvage Value:** 10% of purchase price (Rp 1,500)
- **Useful Life:** 5 years
- **Interest Rate:** 18%

The results are visualized using matplotlib to compare the depreciation effect over time.

---

## 🧩 Problem
Understanding how different depreciation methods affect the value of assets is crucial in industrial engineering and accounting. This project helps to:

- Calculate depreciation for fixed assets
- Compare methods with different financial assumptions
- Visualize financial performance over asset lifespan

---

## ✨ Features

- Calculates annual depreciation and book value for 5 years
- Generates comparative line plot for straight line, sinking fund and double declining balance methods

## 🛠 Tools Used

- Python(numpy, matplotlib)

---

## 📈 Result 

The final output shows a comparative plot of book values:
<img width="1425" height="849" alt="image" src="https://github.com/user-attachments/assets/99b2bf21-44a7-4b12-bd53-37215073ca9c" />

- Straight Line = Linear drop
- Sinking Fund = Slow start, fast end
- DDB = Fast start, slow end

Each method provides different financial implications for asset management.

---

## 🚀 Run the script

python depreciation_methods.py
