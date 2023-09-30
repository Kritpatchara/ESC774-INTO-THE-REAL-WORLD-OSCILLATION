gram = float(input("Amount of flour in gram: "))
if gram < 0:
    gram = float(input("***Please input in zero or positive\nAmount of flour in gram: "))
unit = input("Unit that you want to convert: ")
cup = gram/150
tablespoon = gram/10
teaspoon = gram/3
if unit == "cup":
    print(cup)
elif unit == "tablesspoon":
    print(tablespoon)
elif unit == "teaspoon":
    print(teaspoon)