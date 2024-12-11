country = input("Enter country name: ")
product_price = int(input("Enter the cost of the products: "))

if country == "US":
    if product_price <= 50:
        print("Shipping cost is $50")
    elif product_price <= 100:
        print("Shiping cost is $ 25")
    elif product_price <= 150:
        print("Shiping cost $5")
    else:
        print("Shipping cost Free")
elif country == "UK":
    if product_price <= 100:
        print("Shiping cost is $ 25")
    else:
        print("Shipping is Free")
else:
    print("Soory! We deliver our product only us and uk")
