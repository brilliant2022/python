import os

print("Welcome to the Rock Paper Scissors Game!")
player_1=input("palyer 1:")
player_2=input("player 2:")
def compare(item_1,item_2):
    if(item_1=="石頭" and item_2=="剪刀" or item_1=='布'and item_2=='石頭' or item_1=='剪刀' and item_2=='布'):
        return (1)
    elif(item_1=='石頭' and item_2=='布' or item_1=='布' and item_2=='剪刀' or item_1=='剪刀' and item_2=='石頭'):
        return(2)
    elif(item_1==item_2=='剪刀' or item_1==item_2=='石頭' or item_1==item_2=='布'):
        return(3)
    else:
        return("This is a wrong situation.")
player_1_choice=input("%s,which one is your gesture? 石頭=石頭 剪刀=剪刀 布=布"%player_1)
os.system("cls")
player_2_choice=input("%s,which one is your gesture? 石頭=石頭 剪刀=剪刀 布=布"%player_2)
if compare(player_1_choice,player_2_choice)==1:
    print(f"{player_1} is winner!")
elif compare(player_1_choice,player_2_choice)==2:
    print(f"{player_2} is winner!")
elif compare(player_1_choice,player_2_choice)==3:
    print("It is equal!")
    
               

        
