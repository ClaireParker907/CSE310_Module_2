import sqlite3
import pandas as pd

# 1. SETUP: Read Excel using your preferred function and Initialize SQL Database
excel_file = "InvData.xlsx"
db_name = "inventory_mgmt.db"

print("--- Step 1: Loading Excel Data into SQL Database ---")
try:
    df_excel = pd.read_excel(excel_file)
    print(f"Successfully loaded '{excel_file}' into Pandas.")
except Exception as e:
    print(f"Error reading Excel file: {e}")
    print("Falling back to mock shirt data for demonstration...")
    mock_data = {
        "product_id": [101, 102, 103, 104, 105, 106, 107, 108, 109],
        "product_name": ["Red Shirt", "Orange Shirt", "Yellow Shirt", "Green Shirt", "Blue Shirt", "Purple Shirt", "Black Shirt", "Brown Shirt", "White Shirt"],
        "quantity": [7, 15, 20, 6, 20, 35, 6, 25, 10],
        "price": [24.99, 20.55, 15.99, 15.99, 24.99, 20.55, 24.99, 15.99, 20.55]
    }
    df_excel = pd.DataFrame(mock_data)

# Connect to SQLite Database (creates the file automatically)
conn = sqlite3.connect(db_name)
cursor = conn.cursor()

# Use Pandas to write the DataFrame into a SQL table named 'products'
df_excel.to_sql("products", conn, if_exists="replace", index=False)
print("Database initialized and 'products' table created successfully.\n")


# 2. CREATE (Insert Data)
print("--- Step 2: Inserting a New Product (CREATE) ---")
# Adding a new clothing item: Pink Shirt
new_product = (110, "Pink Shirt", 12, 18.99)
insert_query = "INSERT INTO products (product_id, product_name, quantity, price) VALUES (?, ?, ?, ?);"

cursor.execute(insert_query, new_product)
conn.commit()
print(f"Inserted: {new_product[1]}\n")


# 3. UPDATE (Modify Data)
print("--- Step 3: Restocking a Product (UPDATE) ---")
# Restock the Green Shirt (ID 104) from 6 items up to 30 items
update_query = "UPDATE products SET quantity = ? WHERE product_id = ?;"
cursor.execute(update_query, (30, 104))
conn.commit()
print("Updated Product ID 104 (Green Shirt) quantity to 30.\n")


# 4. DELETE (Remove Data)
print("--- Step 4: Simulating a Discontinued Product (DELETE) ---")
# Delete the Brown Shirt (ID 108) from inventory
delete_query = "DELETE FROM products WHERE product_id = ?;"
cursor.execute(delete_query, (108,))
conn.commit()
print("Deleted Product ID 108 (Brown Shirt) from inventory.\n")


# 5. RETRIEVE & USE DATA (Query via Pandas)
print("--- Step 5: Retrieving Current Clothing Inventory (READ) ---")
# Pull the updated data back out of SQL using Pandas
select_query = "SELECT * FROM products;"
df_current_inventory = pd.read_sql_query(select_query, conn)

print("Current Clothing Inventory Status:")
print(df_current_inventory.to_string(index=False))
print("\n")


# 6. STRETCH CHALLENGE: Aggregate Functions
print("--- Step 6: Stretch Challenge (Aggregate Functions) ---")
# SUM calculates total items in stock, AVG calculates the average shirt price
aggregate_query = """
SELECT 
    SUM(quantity) AS total_items, 
    AVG(price) AS average_price 
FROM products;
"""
cursor.execute(aggregate_query)
totals = cursor.fetchone()

print(f"Total Apparel Items in Stock (SUM): {totals[0]}")
print(f"Average Shirt Price (AVG): ${totals[1]:.2f}")

# Clean up connection
conn.close()
print("\nDatabase connection closed. Process complete.")
