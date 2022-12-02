import os
def print_horizontal_line():
    print(" --- "*board_size)
def print_vertical_line():
    print("|    "*(board_size+1))
board_size=int(input("What size game board do you need?"))
number=board_size 
while number >0:
    print_horizontal_line()
    print_vertical_line()
    number=number  -1
print( " --- "*board_size)
os.system("pause")
