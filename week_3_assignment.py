def calculate_discount(price, discount_percent) :
    discount = price * discount_percent / 100
    if discount_percent > 20 :
        print(f"Congrats! you've got a discount of {discount_percent}% Please pay {price - discount}")
    else :
        print(f"Sorry! There is no discount. please pay {price}") 
    
price = float(input("Enter the price: "))
discount_percent = float(input("Enter the discount percent: "))
calculate_discount(price, discount_percent)
