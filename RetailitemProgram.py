import RetailitemClass as rc


item1 = rc.Retailitem("Jacket", 12, 59.95)
item2 = rc.Retailitem("Designer Jeans", 10, 34.95)
item3 = rc.Retailitem("Shirt", 20, 24.95)

print(item1.get_description())
print(item1.get_units())
print(item1.get_price())
