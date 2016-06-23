# Hands on github tutorial

Each team makes their own edits and by pushing it all to the local repository we will see how it all comes together

## New Tutorial
1. Create a new repository on your personal github page. Follow guide here: https://help.github.com/articles/create-a-repo/
2. Clone the repository: https://help.github.com/articles/cloning-a-repository/
3. Add in a new file by downloading the following python game (download link)
4. Try running the game (and beat the computer) by typing
```
python dice_game.py
```
5. Now your task is to make this game a little bit more interesting. Start of by making a new branch that we will call: `develop`.
6. The code have 6 edits commented out of the code. Go through the code and uncomment the edits one by one. Make a commit after each edit that you comment out and write in the commit message.
7. When you are all done, push your changes to Github and go online. 
8. Notice now how there are two branches in your repository and that the repo content change if you switch branch!
9. Next, make a pull request!


## How to:
- Navigate using the terminal to the place where you want to put the git repo
- Clone the local Github repo
```
git clone some_github_repo -b develop
```
- Make sure you are on the develop branch by running
```
> git branch
develop
```
    + If you don't see `develop` as return type `git checkout develop`
- Create a local branch, and checkout the branch, for your edits
```
git checkout -b my_new_branch_name
```
- Add an issue on Github describing the issue/improvement you are fixing and assign yourself to that issue. (It could also be that there already is an issue that you are fixing.)
Make the edit listed below for your team
    + Edit the file
    + `add` the file
    + `commit` your changes
- Merge your edits to the `develop` branch
```
git merge <add in commands here>
```
- Push your commit to the remote (to github)
```
git push ...
```


## Team Edits

### Team 1
- Add issue: `Wrong currency`
- Change the currency in the game from Euros to to Canadian dollars.

### Team 2
- Add issue: `Ask user for rounds`
- Ask the user how many rounds to play by changing the following:
```
nrounds = int(raw_input('How many rounds shall we play: '))
play(nrounds)
```


### Team 3
- Add issue: `Welcome screen to the game`
- We want a nice welcome screen to the game. Add at the top of the script after `import`
```
def welcome_banner():
    print '-------------------------------------'
    print '- - - Man vs. Machine Dice Game - - -'
    print '-------------------------------------'
```
- Then add `welcome_banner()` before calling `play()`

### Team 4
- Add issue: `Check the guess`
- It doesn't seem fair if the user guess a number that is outside the reasonable limits based on the number of dices.
- Add a check for the guess by updating the `player_guess` function
```
def player_guess(ndice):
    while True:
        guess = input('Guess the sum of the no of eyes' \
            'in the next throw: ')
        if guess < ndice:
            print 'You guessed %d but there are %d dice.' \
                ' Guess higher!' % (guess, ndice)
        elif guess > 6*ndice:
            print 'You guessed %d but with %d dice the greatest' \
                'sum is %d. Guess lower!' %(guess, ndice, 6*ndice)
        else:
            break

    return guess
```

### Team 5
- Add issue: `Possibility for a tie`
- In the current implementation you will win if you both end up with the same score. Add the possibility for it all ending up in a tie.
- Change the last part of `play()` to:
```
if computer_capital > player_capital:
    print 'Machine Wins!'
elif computer_capital < player_captital:
    print 'You win!'
else:
    print 'Tie!'
```

### Team 6
- Add issue: `Ask for rematch`
- It only seems fair that we ask for a rematch if we loose the game!
- Add the following at the end of the of the `play` function
```
if computer_capital > player_capital:
    ans = raw_input('Do you want a rematch (y/n): ')
    if ans == 'y':
        print "\n"
        main()
```

### Team 7
???

### Team 8
???

### Team 9
???

