# from turtle import Turtle, Screen

# mouli = Turtle();

# print(mouli)
# mouli.shape("turtle")
# mouli.color("blue")
# mouli.forward(100)

# my_screen = Screen()

# print(my_screen.canvheight)

# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()


table.add_column("Mouli",["Apple", "Ball", "Cat", "Dog"])
table.add_column("Dinesh",["Eagle", "Fox", "Ginger", "Hyna"])

table.align = "l"

print(table)