# High-score Tracker Game

while True:
  #Ask the player for High-score
  score_input = input("Enter your game score (or type 'stop to exit'): ")
  
  #Check if player wants to stop
  if score_input.strip().lower() == "stop":
    print("Game session ended")
    break
  
  #Convert score to integer
  score = int(score_input)
  
  #Check high score
  if score > 100:
    print("Wow! That's a new high score!")
  else:
    print("Good try, keep playing!")