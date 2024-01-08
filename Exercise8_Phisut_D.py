Products = {
    "1":["Milk",15],
    "2":["Chocolate",15]
}
Username = input("Username:")
Password = input("Password:")
if Username == "You" and Password == "Correct":
    print("---Welcome to the shop---")
    print("1.Milk")
    print("2.Chocolate")
    Selected = input(">>")
    Selected = Products[Selected]
    print("Thanks for bought our", str.lower(Selected[0]), ",That will be", Selected[1])
else:
    print("Oops!, Try again")