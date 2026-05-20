a=input("press 1 for sandwich,2 for pizza,3 for burger: ")
b=input("press 1 for thin crust pizza,2 for cheese burst pizza,3 for fresh dough pizza: ")

match a:
    case '1':
        print("You selected a sandwich.🥪")
    case '2':
        print("You selected a pizza.🍕")
    case '3':
        print("You selected a burger.🍔")
    case _:
        print("Invalid choice.")
match b:
    case '1':
        print("You selected a thin crust pizza.🥞")
    case '2':
        print("You selected a cheese burst pizza.🧀")
    case '3':
        print("You selected a fresh dough pizza.🍞")
    case _:
        print("Invalid choice.")
'''
output: 
1=> press 1 for sandwich,2 for pizza,3 for burger: 1
    You selected a sandwich.
2=> press 1 for sandwich,2 for pizza,3 for burger: 2    
You selected a pizza.
3=> press 1 for sandwich,2 for pizza,3 for burger: 3
    You selected a burger.
4=> press 1 for sandwich,2 for pizza,3 for burger: 4
    Invalid choice.
5=> press 1 for sandwich,2 for pizza,3 for burger: a
    Invalid choice.
'''