
amount = 20.00
weeks = 2

days = weeks * 7
hours = days * 24

value = amount
current = amount

for i in range(0, hours, 1):
    current = current / 2
    value += current
print(value)
