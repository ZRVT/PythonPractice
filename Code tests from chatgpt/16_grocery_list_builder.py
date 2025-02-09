#this function will add an item in the shopping list. 
def add_item():
    """     
    This function will add items to he shopping list. 

    :param numbers: Just an example so i can see how this looks. 
    :return: Shopping list object
    """
    item = input('Please add an item: ')

        #This section will validate the input of the quantity / value of the items added to the list. 
    while True: 
        try:
            value = float(input('Add value of item: '))
            quantity = float(input('Add quantity of item: '))
            break
        except ValueError: 
            print('Please provide a valid value')
        total_value = value * quantity 
    
    #this section will check if the item already exists in the list or not. 
    for existing_item in grocery_list:
        if existing_item['item'] == item.lower():
            print(f'Item: {item} already exist')
            return 
    
    #this section will add the item into the list, with its value and quantity.
    grocery_list.append({"item": item, "value": value,"quantity": quantity, "total_value": total_value})
    print(f'\nNew item added: {item} ---------- ${value} * {quantity} = ${total_value}')

#This function will remove an item in the shopping list. 
# Function to remove an item from the shopping list.
def remove_item():
    while True:
        print('\nWhat item would you like to remove?\n')
        for item in grocery_list:
            print(item["item"])
        item_name = input('\nChoose from the above list: ')
        for existing_item in grocery_list:
            if existing_item["item"].lower() == item_name.lower():
                grocery_list.remove(existing_item)
                print(f'\nItem "{item_name}" has been removed.')
                return
            print(f'\nItem "{item_name}" not found in the list.') 


#this funcion allow the choice to be defined of the user.
def user_choice():
    print('\n Please define what you would like to do')
    print('1. Add items to your list')
    print('2. Remove items from your list')
    print('3. Show my shopping list')
    print('4. Finalize my shopping list')

    while True: 
        try:
            choice = int(input('Choose from (1,2,3,4): '))
            if choice in[1,2,3,4]:
                return choice 
            else:
                print('please provide a valid choice.')
        except ValueError:
           print('please provide a valid choice.')

#printing of the entire grocery list once done with adding items.
def print_grocery_list():
    total_list_value = 0
    print("\nYour Grocery List:")
    print("______________________________________\n")

    #this for loop will print out each item of the list and print it to the user. 
    for items in grocery_list:
        print(f'{items["item"]} ---------- ${items["value"]} x {items["quantity"]} = ${items["total_value"]}')
        total_list_value +=  items["total_value"]

    print("______________________________________\n")
    print(f'Your total cost = ${total_list_value:.2f}')

grocery_list = []

while True: 
    choice = user_choice()
    #choice 1 is for adding items to the shopping list. 
    if choice == 1:
        add_item()
    
    #choice 2 is for removing items
    elif choice == 2:
        #here i am verifying if anything is actually on the list or not. 
        if len(grocery_list) == 0:
            print('\nThere are no items to remove in your list.')
        else:
            remove_item()

    #shows the groceery list 
    elif choice == 3:
        print_grocery_list()

    #shows the groccery list and finalizes the function.
    elif choice == 4:
        print_grocery_list()
        break

