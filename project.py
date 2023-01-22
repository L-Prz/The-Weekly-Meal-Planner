from recipes import my_recipes
import random,sys
def main():
    print("Welcome to the Weekly Meal Planner!\nThis program allows you to create custom dinner menus and generates a grocery list using your own preferences.")
    length_of_menu=set_menu_length(input("How many days are you meal planning for? Please enter a number from 1-14."))
    diet_preference=set_diet_preference(input("Do you have any dietary restrictions? Choose one by entering:\n\"K\" for Keto\n\"G\" for Gluten Free\n\"V\" for Vegetarian\n\"N\" for no restrictions.  "))
    print(f"\nGreat! Here is your menu for {length_of_menu} days: ")
    menu=create_menu(length_of_menu, diet_preference)
    format_menu(menu)
    groceries=create_grocery_list(menu)
    print("\nHere is your shopping list:")
    format_grocery_list(groceries)

def set_menu_length(n):
    if (not str(n).isdigit()) or (int(n)<0 or int(n)>14):
        raise ValueError("Please enter a number from 1-14.")
    else:
        return n
def set_diet_preference(diet):
    diet=diet.upper()
    if diet in ['K', 'G', 'V', 'N']:
        if diet=="K":
           return "keto"
        elif diet=="G":
            return "gluten_free"
        elif diet=="V":
            return "vegetarian"
        elif diet=="N":
            return "none"
    else:
        raise ValueError("Sorry, that is not a valid response.")

def create_menu(length_of_menu, diet_preference):
    menu=[]
    while len(menu)<int(length_of_menu):
        random_key=random.randint(0, len(my_recipes)-1)
        if (not my_recipes[random_key]['name'] in menu) and (diet_preference in my_recipes[random_key]['diet']):
            menu.append(my_recipes[random_key]['name'])
    return menu

def format_menu(menu):
     for count, menu in enumerate(menu, start=1):
        print(count, menu)

def create_grocery_list(menu):
    grocery_list={}
    ingredients=[]
    for i in range(len(menu)-1):
        for recipe in my_recipes:
            if my_recipes[recipe]['name']==menu[i]:
                ingredients+=my_recipes[recipe]['ingredients']
                for ingredient in ingredients:
                    if ingredient not in grocery_list:
                        grocery_list[ingredient]=1
                    else:
                        grocery_list[ingredient]=((grocery_list.get(ingredient))+1)
            ingredients=[]
    return grocery_list

def format_grocery_list(g):
    #sort alphabetically
    myKeys=list(g.keys())
    myKeys.sort()
    sorted_grocery_list={i:g[i] for i in myKeys}

    #format print
    print("INGREDIENT -- QTY")
    for item in sorted_grocery_list:
        print(f"{item.capitalize()}-{sorted_grocery_list[item]}")



if __name__=="__main__":
    main()
