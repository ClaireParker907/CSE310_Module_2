import sqlite3
import pandas as pd

# 1. Connect to the database file your script created
conn = sqlite3.connect("inventory_mgmt.db")

# 2. Use Pandas to read the actual SQL table
df = pd.read_sql_query("SELECT * FROM products;", conn)

# 3. Print the table to your terminal screen
print(df.to_string(index=False))

# 4. Close it out
conn.close()