# Name: Monica Constantino
# Date: 10/27/2020
# Description: Monica's Restaurant
# TO DO:
# 1. create a function that displays menu items
# 2. create a function that determines meal cost
# 3. create a function that determine whether the customer wants to continue purchasing
# 4. in main(), call menu() and ask user what meal they want to buy
# 5.            once they order, ask user again if they want to continue ordering
# 6.            if they want to continue ordering, show menu again and calculate cost
# 7.            if user does not want to continue ordering, show total cost
# 8. make sure to not forget error-checking
# functions

# show menu
def menu():
    meals = ["1.Burger", "2.Pasta", "3.Salad"]
    for meal_type in meals:
        print(meal_type, end = " ")

    order = int(input("\nPlease type in the number that corresponds with the meal you want (1-3): "))

    while order < 0 or order > 4:
        order = int(input("Invalid input. Please type a number between 1-3: "))

    return order

# meal cost
def get_order(food):
    if food == 1:
        amount = 5.00
    elif food == 2:
        amount = 8.00
    elif food == 3:
        amount = 4.00

    return amount

# does customer still want to order food
def continue_purchase():
    ask_customer = input("Do you want to continue ordering? Please type Y for yes or N for no: ")

    while ask_customer != "Y" and ask_customer != "y" and ask_customer != "n" and ask_customer != "N":
        ask_customer = input("Invalid input. Please type Y for yes or N for no: ")

    if ask_customer == 'Y' or ask_customer == 'y':
        return True
    else:
        return False

#main
def main():
    choice = menu()    
    meal_cost = get_order(choice)
    subtotal_meal_cost = "Subtotal: ${:4.2f}".format(meal_cost)
    print(subtotal_meal_cost)
    add_menu = continue_purchase()
    while add_menu == True:
        choice = menu()
        if choice == 1:
            burger = get_order(choice)
            meal_cost = meal_cost + burger
        elif choice == 2:
            pasta = get_order(choice)
            meal_cost = meal_cost + pasta
        elif choice == 3:
            salad = get_order(choice)
            meal_cost = meal_cost + salad
        subtotal_meal_cost = "Subtotal: ${:4.2f}".format(meal_cost)
        print(subtotal_meal_cost)
        add_menu = continue_purchase()
    else:
        total_meal_cost = "Total cost: ${:4.2f}".format(meal_cost)
        print(total_meal_cost)

#call main
main()
        
        
        
