def intro ():
  print ("Welcome to to text based interactive game")
  print("you found yourself in a dark forest") 
  choice=input("Do you want to gi left or right : ").lower()
  if choice == "left":
    path_left()
  elif choice == "right":
    path_right()
  else:
    print(" Invalid choice choose 'left' or 'right' : ")
    intro()

def path_right ():
  print("wooh You encounter a Wolf! ")
  choice = input(" Do you want to figt or run (fight/run) : ").lower()
  if choice == " fight":
    fight_wolf ()
  elif choice == "run":
    run_wolf()
  else:
    print(" Invalid choice chokse between (fight/run) : ")
    path_right()

def path_left():
  print(" wow you find a hidden treasure chest ")
  choice=input(" Do you want to open it or leave it (open/leave) ").lower()
  if choice=="open":
    open_chest() 
  elif choice=="leave":
    leave_chest()
  else:
    print(" Invalid choice. Choose between (open/leave) : ")
    path_left

def fight_wolf():
  print(" You fought bravely but unfortunately you lose")
  end_game()

def run_wolf():
  print("You ran with your own strength and cone out of the forest")
  end_game()

def open_chest():
  print ("You found a map and a sword")
  end_game()

def leave_chest():
  print("You left the chest and continued your journey")
  end_game()

def end_game():
  print ("You are a brave man and you have completed the game")
  







  
  

  
  
    
