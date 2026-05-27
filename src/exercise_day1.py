transactions = [
    {"date": "2024-01-01", "amount": 1200, "type": "food", "merchant": "Swiggy"},
    {"date": "2024-01-02", "amount": 450, "type": "transport", "merchant": "Ola"},
    {"date": "2024-01-03", "amount": 3200, "type": "rent", "merchant": "NoBroker"},
    {"date": "2024-01-04", "amount": 800, "type": "food", "merchant": "Zomato"},
    {"date": "2024-01-05", "amount": 1500, "type": "food", "merchant": "Swiggy"},
    {"date": "2024-01-06", "amount": 200, "type": "transport", "merchant": "Rapido"},
    {"date": "2024-01-07", "amount": 5000, "type": "shopping", "merchant": "Amazon"},
    {"date": "2024-01-08", "amount": 300, "type": "food", "merchant": "Swiggy"},
    {"date": "2024-01-09", "amount": 900, "type": "transport", "merchant": "Ola"},
    {"date": "2024-01-10", "amount": 2500, "type": "shopping", "merchant": "Flipkart"},
]

# Count transactions per category
counter = {}
for t in transactions:
    key = t['type']
    value = t['amount']
    if key not in counter:
        counter[key] = 0
    counter[key]+=1
print(counter)
# Which merchant did you spend the most at total
merchantbill = {}
for t in transactions:
    key = t['merchant']
    value = t['amount']
    if key not in merchantbill:
        merchantbill[key] = 0
    merchantbill[key] += value
g = max(merchantbill, key=merchantbill.get)
print(f"Highest spent: Rs {merchantbill[g]} at {g}")
# What percentage of total spend is each category
categorybill = {}
for t in transactions:
    key = t["type"]
    value = t['amount']
    if key not in categorybill:
        categorybill[key] = 0
    categorybill[key] += value

total = sum(categorybill.values())
print(categorybill)
for c in categorybill:
    dec = (categorybill[c]/total)*100
    print(f"{c}: {dec:.2f}")
# Find the single most frequent merchant
freqcounter = {}
for t in transactions:
    key = t["merchant"]
    value = t["amount"]
    if key not in freqcounter:
        freqcounter[key] = 0
    freqcounter[key] += 1
maxkey = max(freqcounter, key=freqcounter.get)
print(f"Most ordered is {freqcounter[maxkey]} times from {maxkey}.")
# Group transactions by merchant, list all amounts
merccounter = {}
for t in transactions:
    key = t["merchant"]
    value = t["amount"]
    if key not in merccounter:
        merccounter[key] = []
    merccounter[key].append(value)
for m in merccounter:
    print(f"{m}: {', '.join(map(str, merccounter[m]))}")
# Average spend per merchant
avgmercbill = {}
for m in merccounter:
    curravg = sum(merccounter[m])/len(merccounter[m])
    key = m
    value = 0
    if key not in avgmercbill:
        avgmercbill[key]=0
    avgmercbill[key] += curravg
    print(f"Average spent at {m}: {curravg}")
# Find merchants where average spend is above 1000
for a in avgmercbill:
    if avgmercbill[a] > 1000:
        print(a)
# Sort categories by total spend, highest first
sortedcategorybill = dict(sorted(categorybill.items(), key= lambda i:i[1], reverse=True))
print(sortedcategorybill)
# Flag any transaction above 2x the average as "unusual"
avg = (sum(categorybill.values()))/len(transactions)

def fraud():
    f=[]
    for t in transactions:
        if t['amount']>avg*2:
            f.append(t)
    return f    
# Build a complete summary dict and print it cleanly — total transactions, total spent, average transaction, highest category, most visited merchant, unusual transaction count

summary = {
    "total_transactions": len(transactions),
    "total_spent": sum(categorybill.values()),
    "average_transaction": avg,
    "highest_category": max(sortedcategorybill, key = sortedcategorybill.get),
    "most_visited_merchant": maxkey,
    "unusual_transactions": len(fraud())
}
print(summary)