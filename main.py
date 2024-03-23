# import sys
# import os
import subprocess

if __name__ == "__main__":
    print("Welcome to Chef CLI made by TEAM_26!\n")
    print("Generate: recipes, dishes from ingredients, critique ingredients with seasoned chefs:")
    print(
        "#1: Kenyan pastry chef who loves baking sweet and savory pastries that appeal to young taste buds\n"
    )
    print("2: Turkish chef, famous for your mouthwatering shawarmas known for flavorful dishes marked for Turkish cuisine marked by tradition.\n")

    chef = int(input("Input 1 for the Kenyan pastry chef, input 2 for the Turkish chef: "))

    # files = os.listdir('./')
    # choices = {}
    # chefs = ["tCTGAz", "fJcu5j"]

    # for file_name in files:
    #     file_path = os.path.join('./', file_name)
    #     for chef in chefs:
    #         if chef in file_path:
    #             choices[]

    if chef == 1:
        subprocess.call(["python3", "chef-gpt-fJcu5j.py"])
    elif chef == 2:
        subprocess.call(["python3", "chef-gpt-tCTGAz.py"])
    else:
        print('Wrong input, please try again')
        # chef = input("Input 1 for the Kenyan pastry chef, input 2 for the Turkish chef: ")
        # function call

