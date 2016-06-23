import random

# Let's play dice against the computer!
# In this simple implementation both you and computer throw the 
# dice and guess how many eyes that will show up.
# If you loose, you loose one point, if you win you gain 
# the as many coins as the number of eyes you guess. 
# Let's beat the machine!


# Team 3
# def welcome_banner():
#     print '-------------------------------------'
#     print '- - - Man vs. Machine Dice Game - - -'
#     print '-------------------------------------\n'

def roll_dice_and_compute_sum(ndice):
	return sum([random.randint(1, 6) \
		for i in range(ndice)])

def computer_guess(ndice):
	return random.randint(ndice, 6*ndice)

def player_guess(ndice):
	return input('Guess the sum of the no of eyes' \
		'in the next throw: ')

# Team 4
# def player_guess(ndice):
# 	while True:
# 		guess = input('Guess the sum of the no of eyes' \
# 			'in the next throw: ')
# 		if guess < ndice:
# 			print 'You guessed %d but there are %d dice.' \
# 				' Guess higher!' % (guess, ndice)
# 		elif guess > 6*ndice:
# 			print 'You guessed %d but with %d dice the greatest' \
# 				'sum is %d. Guess lower!' %(guess, ndice, 6*ndice)
# 		else:
# 			break

# 	return guess


def play_one_round(ndice, capital, guess_function):
	guess = guess_function(ndice)
	throw = roll_dice_and_compute_sum(ndice)
	if guess == throw:
		capital += guess
	else:
		capital -= 1
	return capital, throw, guess

def play(nrounds, ndice=2):
	player_capital = computer_capital = nrounds # start capital

	for i in range(nrounds):
		player_capital, throw, guess = \
			play_one_round(ndice, player_capital, player_guess)
		print 'You guessed %d, got %d' % (guess, throw)

		computer_capital, throw, guess = \
			play_one_round(ndice, computer_capital, computer_guess)
		print 'Machine guessed %d, got %d' % (guess, throw)

		print 'Status: you have %d CAD, machine has %d CAD' % \
			(player_capital, computer_capital)

		if player_capital == 0 or computer_capital == 0:
			break

	if computer_capital > player_capital:
		winner = 'Machine'
	else:
		winner = 'You'
	print winner, 'won!'

	# Team 6
	# if computer_capital > player_capital:
	# 	ans = raw_input('Do you want a rematch (y/n): ')
	# 	if ans == 'y':
	# 		print "\n"
	# 		main()

	# Team 5
	# if computer_capital > player_capital:
	# 	print 'Machine Wins!'
	# elif computer_capital < player_capital:
	# 	print 'You win!'
	# else:
	# 	print 'Tie!'


def main():
	# Team 3
	# welcome_banner()

	# Team 2
	# nrounds = int(raw_input('How many rounds shall we play: '))
	# play(nrounds)

	play(2) 

# Run the game!
main()