import random, sys

print('ROCK, PAPER, SHOTGUN')

# These variables keep track of the number of wins, losses and ties.
wins = 0
losses = 0
ties = 0

while True:  # The main game loop
    print ('{} Wins, {} Losses, {} Ties'.format(wins, losses, ties))
    while True:  # The player input loop
        print('Enter your move : (r)ock, (p)aper, (s)hotgun or (q)uit')
        playerMove = input()
        if playerMove == 'q':
            sys.exit()  # Quit the program
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break  # Breaks out of the player loop
        print('Type one of r, p, s or q.')

    # Displays player move
    if playerMove == 'r':
        print('ROCK versus ...')
    elif playerMove == 'p':
        print('PAPER versus ...')
    elif playerMove == 's':
        print('SHOTGUN versus ...')

    # Displays what the CPU chose
    randomNumber = random.randint(1,3)
    if randomNumber == 1:
        computerMove = 'r'
        print('ROCK')
    elif randomNumber == 2:
        computerMove = 'p'
        print('PAPER')
    elif randomNumber == 3:
        computerMove = 's'
        print('SHOTGUN')

    # Display and record the win, loss, tie rate
    if playerMove == computerMove:
        print('It is a tie')
        ties = ties + 1
    elif playerMove == 'r' and computerMove == 's' or playerMove == 'p' and computerMove == 'r' or playerMove == 's' and computerMove == 'p':
        print('It is a WIN')
        wins = wins + 1
    elif playerMove == 'r' and computerMove == 'p' or playerMove == 'p' and computerMove == 's' or playerMove == 's' and computerMove == 'r':
        print('You LOSE')
        losses = losses + 1