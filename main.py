# import sys
# import os
import subprocess

if __name__ == "__main__":
    print("Welcome to Chef CLI made by TEAM_26!\n")
    print("Generate: recipes, dishes from ingredients, critique ingredients with seasoned chefs.\n")
    print(
        "#1: Kenyan pastry chef who loves baking sweet and savory pastries that appeal to young taste buds.\n"
    )
    print(
        "#2: Turkish chef, famous for your mouthwatering shawarmas known for flavorful dishes marked for Turkish cuisine marked by tradition.\n"
    )
    print(
        "#3: Chinese chef, famous for your noodles or stir-fried specialties known for flavorful dishes marked for Chinese cuisine marked by precision and creativity.\n"
    )

    chef = int(input("Which chef do you want? (1/2/3?): "))

    def choose_chef(chef):
        if chef == 1:
            subprocess.call(["python3", "chef-gpt-fJcu5j.py"])
        elif chef == 2:
            subprocess.call(["python3", "chef-gpt-tCTGAz.py"])   
        elif chef == 3:
            subprocess.call(["python3", "chef-gpt-Ea56g7.py"])
        else:
            print('Wrong input, please try again.\n')
            chef = int(input("Which chef do you want? (1/2/3?): "))
            choose_chef(chef)

    choose_chef(chef)
