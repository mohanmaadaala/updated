num_items = int(input("how many items you are going to buy:"))
total_price = 0
for i in range(num_items):
    item_price = float(input(f"enter the price of item{i + 1}:"))
    total_price += item_price
if total_price > 100:
  discount = total_price * 0.10
  total_price -= discount
print(f"Your Total price after discount is:${total_price:.2f}")
  