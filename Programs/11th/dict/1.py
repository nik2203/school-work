import json
items={'cherry tomatoes':60, 'avocados':120, 'bread':30, 'olive oil':250}
price=0
for i in items.values():
    price+=i
print(json.dumps(items,indent=1))
print('The total price is',price,'rupees')
