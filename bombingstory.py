start = '''
You are working in a downtown office when a bomb goes off on the 150th floor. The building is slowly crumbling, and you must find a way to escape. If you don't escape you'll fail. GOOD LUCK :))
'''
floor140 =''' You are now on the 140th floor and you have the choice to save people or leave them

'''
floor130 ='''You are now on the 130th floor. Limping or with allies, you find one of the people who set the bomb. What do you do?

'''

floor120 ='''You are now on the 120th floor. You find a clue to who set the bomb. What do you do?

'''

floor110 ='''You are now on the 110th floor, the final floor. Here you find the mastermind.

'''

print(start)


print("You have one out of three options to choose from, you can stay in your office, use the steps, or you can use the elevator. ")
user_input = input()
if user_input == "office" or user_input =="elevator":
    print("You are dead") # finished the story by writing what happens
    exit()

elif user_input == "steps":
    print("You live and you proceed to the 140th floor.") # finished the story writing what happens

print(floor140)


 print("You have two options you can save the people or you coould leave them and run.")
user_input = input()
if user_input == "save":
    print("You have gain allies and resources.")
    print ("Now you will move to steps that will lead you and your allies to safety.")
elif user_input == "leave":
    print("You have no resources and you let people die.")
    print ("Fire blocks your path and you'll have to jump down a staircase which causes you to sprang your ankle.")

print(floor130)

  print("You have the options to fight or flight.")
user_input = input()
if user_input == "fight"
    print("You have gained a resource.")
elif user_input == "flight"
    print("You lose two allies, and you are taken to the 145th floor")
    print("You have to survive smoke and fire on the 145th, which ultimately leads to your death.")
    print("You are dead")
    exit()

print(floor120)

    print("Now, you will move down to the 120th floor, and you find a clue to who set the bomb. You have two options, take or leave.)
if user_input == "take"
  print("Nice. Now you know who set the bomb.")
if user_input == "leave"
  print("Bad idea. You run into the bomber, and you and your allies perish.")
  print("You are dead")
  exit()

  print(floor110)

    print("Now, you have the choice to take on the bomber yourself or take the bomber to the police. What do you do? Police or yourself?")
if user_input == "yourself"
  print("The bomber ends up killing you and your allies and achieves his plan.")
  print("You're dead. Game over!")
 if user_input == "police"
  print("The bomber goes to jail. And, you continue to live a happy life and now have a puppy.")
  print("You win!")
