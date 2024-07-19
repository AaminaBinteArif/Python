# Input customer details and bill amount
name = input("Enter the customers name : ")
cashier = input("Enter the cashiers name : ")
amount = float(input("Enter the bill amount : "))

# Calculating tip (10% of the bill amount) and GST (20% of the bill amount)
tip = amount * (10 / 100)
gst = amount * (20 / 100)

# Calculating Total Bill including tip and GST
total = amount + tip + gst

# Displaying Total Amount Due
print(f"The total is {total}")

# Inputting the amount of cash given by customer
cash = float(input("Enter the amount of cash given by user : "))

# Calculating the change to be returned
change = cash - total

# Printing the reciept
print("\n\n\t\t\t RECIEPT")
print("\n______________________________________________________________")
print(f"\n\nCustomer Name : {name}\nCashier Name : {cashier}")
print("\n______________________________________________________________")
print(
    f"\n\n\t\t Billing Amount : \t\t{amount}\n\t\t\t Tip    : \t\t {tip}\n\t\t\t GST    : \t\t {gst}"
)
print("\n______________________________________________________________")
print(f"\n\n\t\t Sub Total     : \t\t{total} ")
print(f"\n\t\t Cash Recieved : \t\t{cash}\n\t\t Change        : \t\t{change}")
print("\n______________________________________________________________")
