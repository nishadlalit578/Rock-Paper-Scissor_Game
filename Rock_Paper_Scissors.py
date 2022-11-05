import random
heading = '''

     | |                                                                                                                               | |
 ____| |_______________________________________________________________________________________________________________________________| |____
(____   _______________________________________________________________________________________________________________________________   ____)
     | |                                                                                                                               | |   
     | |      ____   ___     __  __  _      ____   ____  ____   ___  ____        _____   __  ____ _____ _____  ___   ____    _____     | |   
     | |     |    \ /   \   /  ]|  |/ ]    |    \ /    ||    \ /  _]|    \      / ___/  /  ]|    / ___// ___/ /   \ |    \  / ___/     | |
     | |     |  D  )     | /  / |  ' /     |  o  )  o  ||  o  )  [_ |  D  )    (   \_  /  /  |  (   \_(   \_ |     ||  D  )(   \_      | |
     | |     |    /|  O  |/  /  |    \     |   _/|     ||   _/    _]|    /      \__  |/  /   |  |\__  |\__  ||  O  ||    /  \__  |     | |
     | |     |    \|     /   \_ |     |    |  |  |  _  ||  | |   [_ |    \      /  \ /   \_  |  |/  \ |/  \ ||     ||    \  /  \ |     | |   
     | |     |  .  \     \     ||  .  |    |  |  |  |  ||  | |     ||  .  \     \    \     | |  |\    |\    ||     ||  .  \ \    |     | |   
     | |     |__|\_|\___/ \____||__|\_|    |__|  |__|__||__| |_____||__|\_|      \___|\____||____|\___| \___| \___/ |__|\_|  \___|     | |   
     | |                                                                                                                               | |
 ____| |_______________________________________________________________________________________________________________________________| |____
(____   _______________________________________________________________________________________________________________________________   ____)
     | |                                                                                                                               | |
     |_|                                                                                                                               |_|     

'''
print(heading)

rock = '''
    _______
---'   ____)_     
      (______)
      (_____)
      (____)
---.__(___)

'''

paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)

'''

scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''

game_images = [rock, paper, scissor]

play_again = "y"

while True :

    user_choice = int(input("\nWhat do you choose? \n0 for Rock.\n1 for Paper.\n2 for Scissor.\n\n"))

    computer_choice = random.randint(0,2)


    if user_choice < 0 or user_choice > 2 :
        print("You chose invalid number, you lose !!")

    else :

        print(f"You chose : {game_images[user_choice]}")
        print(f"Computer Chose : {game_images[computer_choice]}")

        if user_choice == 0 and computer_choice == 2 :
            print("You Win !!")

        elif user_choice == 2 and computer_choice == 0 :
            print("You Lose !!")

        elif user_choice == computer_choice :
            print("It's a Draw !!")

        elif computer_choice > user_choice :
            print("You Lose !!")

        elif user_choice > computer_choice :
            print("You Win !!")

    play_again = input("\nDo you want to play again ? (y / n) ").lower()   
    if not play_again == "y" : 
        break


