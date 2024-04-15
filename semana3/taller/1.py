def gym_price():
    while True:
        try:
            hours = int(input("How many hours do you train per month? "))
        except ValueError:
            print("Please enter a valid number of hours.")
            continue
        
        if hours < 0:
            print("Please enter a positive number of hours.")
            continue
        
        if hours < 14:
            price_per_hour = 5000
        elif hours < 30:
            price_per_hour = 3500
        else:
            price_per_hour = 2000
        
        total_price = hours * price_per_hour
        print(f"The total price is {total_price}")
        break

gym_price()
