# Rock Paper Scissors
import random

def computerChoice():
  choice = random.randint(0, 2)

  if choice == 0:
    print('I played rock')
  elif choice == 1:
    print('I played paper')
  elif choice == 2:
    print('I played scissors')

  return choice

def playerChoice():
  choice = int(input('Enter Choice: '))

  if choice < 0 or choice > 2:
    print('This is not a valid choice!')
    return playerChoice()
  else:
    if choice == 0:
      print('\nYou played rock')
    elif choice == 1:
      print('\nYou played paper')
    elif choice == 2:
      print('\nYou played scissors')

    return choice

# When 0 is returned, it is a draw.
# When 1 is returned, player wins
# When 2 is returned, computer wins.
def playRound(p, c):
  if c == 0:
    if p == 0:
      print('Ah, a draw!!')
      return 0
    elif p == 1:
      print('You win this round!')
      return 1
    elif p == 2:
      print('You lost this round!')
      return 2
  elif c == 1:
    if p == 0:
      print('You lost this round!')
      return 2
    elif p == 1:
      print('Ah, a draw!!')
      return 0
    elif p == 2:
      print('You win this round!')
      return 1
  elif c == 2:
    if p == 0:
      print('You win this round!')
      return 1
    elif p == 1:
      print('You lost this round!')
      return 2
    elif p == 2:
      print('Ah, a draw!!')
      return 0

def multipleRounds():
  wins = 0
  losses = 0

  rounds = int(input('Best of how many rounds? '))

  if rounds % 2 == 0:
    print('There has to be an odd number of rounds!')
    multipleRounds()

  for index in range(rounds):
    print('\n0 - rock\n1 - paper\n2 - scissors')
    round = playRound(playerChoice(), computerChoice())

    if round == 0:
      pass
    elif round == 1:
      wins += 1
    elif round == 2:
      losses += 1

  print('\n--------------------------------------')
  print('Final Result:\n')
  print('Your score: ' + str(wins))
  print('My score: ' + str(losses))

  if wins > losses:
    print('\nYou are the ultimate winner!')
    print('You now have bragging rights!')
  elif losses > wins:
    print('\nYou are the ulimate loser!')
    print('Take the walk of shame!')
  else:
    print('\nIt is the ultimate draw!')
    print('It was a pleasure playing with you!')

#playRound(playerChoice(), computerChoice())
  
# PROGRAM START
print('Welcome to Rock Paper Scissors!')

multipleRounds()

# PROGRAM END