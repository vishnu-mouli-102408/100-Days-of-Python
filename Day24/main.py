from pathlib import Path
x = str(Path.cwd()) + "/Day24/text.txt"

# with open(x) as file:
#     content = file.read()
#     print(content)

# with open(x,mode="w") as file:
#     content = file.write("Mouli ML")

with open(x,mode="a") as file:
    content = file.write("Mouli ML HHHHH")

# When there is no txt file while on write "w" mode. Python will automatically create new Txt file. 

