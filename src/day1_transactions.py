transactions = [
    {"date": "2024-01-01", "amount": 1200, "type": "food"},
    {"date": "2024-01-02", "amount": 450, "type": "transport"},
    {"date": "2024-01-03", "amount": 3200, "type": "rent"},
    {"date": "2024-01-04", "amount": 800, "type": "food"},
]

total = sum(t["amount"] for t in transactions)
print(f"Total spent: {total}")
maxval = transactions[0]
for a in transactions:
    if a["amount"] > maxval["amount"]:
        maxval = a
print(f"The most expensive transaction is {maxval["amount"]}")

# learning dict creation
bill_dict = {}
for t in transactions:
    key = t['type']
    value = t['amount']
    
    if key not in bill_dict:
        bill_dict[key] = 0
    
    bill_dict[key] += value
    
for k, v in bill_dict.items():
    print(f"{k}: {v}")

g = max(bill_dict, key=bill_dict.get)

print(f"Highest Spending Category: {g} ({bill_dict[g]})")

avg =((sum(bill_dict.values()))/len(bill_dict))
print(avg)

for t in transactions:
    if t['amount']>avg:
            print(f"{t['date']} | {t['type']} | {t['amount']}")