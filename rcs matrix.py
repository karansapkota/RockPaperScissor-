import random 

win_matrix = [
              ['D', 'L', 'W'],
              ['W', 'D', 'L'],
              ['L', 'W', 'D']
]
choice_list = ['ROCK', 'PAPER', 'SCISSOR']
dict = {'R':0, 'P':1, 'S':2}
com_choice = random.choice(choice_list)

while True:
  player_1 = input("Select your option (Rock,Paper,Scissor) or type q to quit?: ").upper()
  
  if player_1 == 'Q' or player_1 == 'QUIT':
    print("Thanks for playing. Goodbye!")
    break

  if player_1 not in choice_list:
    print("Invalid choice. Please enter Rock, Paper, or Scissor.")
    continue
  
  player_2 = random.choice(choice_list)
  print(f"System selected :  {player_2} ")

  print("You : " , win_matrix[dict[player_1[0]]][dict[player_2[0]]])
