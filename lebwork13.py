a=input("press 1 for Gujrati,2 for Hindi,3 for English ")
match a:
    case '1':
        print("you selected Gujarati")
    case '2':
        print("you selected Hindi")
    case '3':
        print("you selected English")
    case _:
        print("Invalid choice.")
'''
output:
1=> press 1 for Gujrati,2 for Hindi,3 for English 1
    you selected Gujarati
2=> press 1 for Gujrati,2 for Hindi,3 for English 2
    you selected Hindi
3=> press 1 for Gujrati,2 for Hindi,3 for English 3
    you selected English
4=> press 1 for Gujrati,2 for Hindi,3 for English 4
    Invalid choice.
5=> press 1 for Gujrati,2 for Hindi,3 for English a
    Invalid choice.
'''