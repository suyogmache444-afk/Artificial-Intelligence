import pandas as pd
# NumPy → arrays
# pandas → tables

# pandas = Excel inside Python

# Why pandas?
# Real-world data comes in:
# CSV
# Excel
# Database tables

# Install pandas
# pip install pandas

# Two important structures #

# In pandas:
# 1.Series => Single column.
# 2.DataFrame

a = pd.Series([10,20,30])
# print(a)

data = {
    "name": ["Suyog", "Rahul"],
    "age": [25, 30]
}

df = pd.DataFrame(data)

print(df)