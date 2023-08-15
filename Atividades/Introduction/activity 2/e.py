price = float(input("Price: "))
discount = float(input("Discount percentual: "))
value = price - (price * (discount/100))
print("\nPrice : {} \nDiscount percentual: {}% \nFinal value: {}".format(price, discount, value))