# The Weekly Meal Planner
##### Video Demo: https://youtu.be/Zua0vNVolrc
#### Description:
The Weekly Meal Planner is a tool to automate the menu-planning and grocery-list-writing process! The program starts by accepting two inputs: **Length of Menu** in days, and **Dietary Restrictions**.  It is important that users follow the proper formatting of their responoses, in order to avoid raising a ValueError.

__Length of Menu:__ Users can input anywhere from 1-14 days, to plan a menu for up to a total of two weeks. Any numerical input outside of that range, or non-numerical input, will raise a ValueError.

**Dietary Restrictions:** This program supports four dietary options:
    *Gluten Free: In general, all gluten free (GF) recipes are free of wheat products. For any recipes that include pasta or flour as an ingredient, the user can use their favorite GF substitutions.
    *Keto: The Ketogenic, or low-carb diet, has gained in popularity over the last few years. The keto recipes included in this program are suitable for users who are consuming ~35-45 net carbs per day.
    *Vegetarian: All vegetarian recipes are free of meat products, and many can be easily converted to vegan (by substituting dairy products), if needed.
    *None: For users without any dietary restrictions, the "none" category will generate a menu of typical dishes that do not have any restrictions.

Once the user has input their settings, the program will generate a menu based on the specified number of days by referencing a dictionary of recipes. The 'create_menu' function implments the 'random' library from python, ensuring that each execution of the program returns a unique menu. The dictionary of recipes has a numerical key, and a "recipe card" value, which has the recipe name, ingredients, cuisine and protein types, and all diet types that the recipe could accomodate. The 'create_menu" function works by randomly searching through the dictionary for a recipe; if the recipe's diet type matches the user setting, and is not already in the menu, it will be added to the menu list.

From there, the 'format_menu' function will enumerate the menu list and print out each day's meal.

The 'create_grocery_list' function then accepts the menu list as an argument, and generates a dictionary of each ingredient needed, with the ingredients being the keys, and the quantity of each item as the value. (For repeated ingredients, the quantity is updated to accurately reflect the total amount of each ingredients needed.)

Finally, the 'format_grocery_list' function is used to convert the grocery_list dictionary into a user-friendly, readable list, by iterating over the grocery_list, and printing it out line by line.

I enjoyed coding this program and have already made use of it for my family's meal planning. Future improvements will include:
    *Exporting menu and grocery list to a printable PDF
    *Adding more menu options to increase variety, or increase potential menu length
    *Adding a feature that prevents the program from repeating the same cuisine or protein types two nights in a row. (We like variety in my house! )
    *Adding additional diet types

This was The Weekly Meal Planner! Many thanks to the CS50P team for the excellent content and support during this course. I found the CS50P Discord especially useful for troubleshooting my problemsets. Finally, many thanks to my family, who will eat my cooking, no matter what's on the table. 
