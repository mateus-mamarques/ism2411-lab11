# Self Assessment Questions
# 1. I would use .get() when I am not sure if a key exists and I want my program to keep running without errors. I would use bracket notation when I know the key exists and need to access its value directly. My rule of thumb is to use .get() for optional information and brackets for required information.
# 2. This pattern reminds me of using SUMIF in Excel, where you organize and add values based on specific categories. Python can be more useful for large datasets because it can automatically process thousands of transactions using loops instead of requiring me to create multiple formulas manually.
 

# Exercise 1:
customer = {
    "name": "Alice",
    "email": "alice@email.com",
    "tier": "gold",
    "ytd_spend": 1250.50
}

print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])
print(customer)

# Exercise 2:
customer["phone"] = "813-555-1234"
print(customer)

customer["tier"] = "platinum"
print(customer)

del customer["email"]
print(customer)

# Exercise 3:
print(customer.get("email", "no email on file"))

try:
    print(customer["email"])
except KeyError:
    print("KeyError: email does not exist")

# Exercise 4:
for key, value in customer.items():
    print(f"{key}: {value}")

# Without .items(), the loop only iterates through the dictionary keys.
for key in customer:
    print(key)

# Exercise 5:
tier_discounts = {
    "bronze": 0,
    "silver": 0.05,
    "gold": 0.10,
    "platinum": 0.15
}

discount = tier_discounts.get(customer["tier"], 0)
purchase_price = 200
final_price = purchase_price * (1 - discount)

print("Tier:", customer["tier"])
print("Discount rate:", discount * 100, "%")
print("Final price: $", final_price)

# Exercise 6:
dict1 = {"name": "Alice", "tier": "bronze"}
dict2 = {"name": "Bob", "tier": "silver"}
dict3 = {"name": "Charlie", "tier": "gold"}

customers = [dict1, dict2, dict3]

for customer in customers:
    discount = tier_discounts.get(customer["tier"], 0)
    discount_amount = 300 * discount

    print(f'{customer["name"]} - {customer["tier"]} - Discount: ${discount_amount:.2f}')

# Exercise 7:
catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8}
}

for product, details in catalog.items():
    if details["stock"] < 20:
        print(f"{product}: LOW STOCK")

# Exercise 8:
transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200}
]

sales_summary = {}

for transaction in transactions:
    region = transaction["region"]
    amount = transaction["amount"]

    sales_summary[region] = sales_summary.get(region, 0) + amount

for region in sorted(sales_summary):
    print(f"{region}: {sales_summary[region]}")