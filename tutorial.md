# Hands on github tutorial

Each team makes their own edits and by pushing it all to the local repository we will see how it all comes together

## New Tutorial

Create a new repository on your personal github page. Follow guide here: https://help.github.com/articles/create-a-repo/

Clone the repository: https://help.github.com/articles/cloning-a-repository/
```
git clone <url-to-repo-on-github>
```

Add in a new file by downloading the following python game https://www.dropbox.com/s/o128wr5aggybrj8/dice_game.py?dl=0
. Run `git status` and notice that there is an untracked file. Add it with 
```
git add dice_game.py
```

In this game you are trying to beat the computer in a simple dice rolling game. You guess the number of eyes and the computer does the same. Every time you guess wrong you loose money. The first to loose all their money loses the game. Try running the game (and beat the computer) by typing
```
python dice_game.py
```

Now your task is to make this game a little bit more interesting. Start of by making a new branch that we will call: `game-improvement`.
```
git checkout -b game-improvement
```

Run `git branch` to see that you are on the right branch
```
> git branch
* game-improvement
master
```

Now we want to push this branch to Github. We do this using
```
git push origin game-improvement
```
This tells git that we want to push this branch to github. After this we do not need to specify `origin game-improvement`

The code have 6 different edits commented out of the code. Your job is now to go through the code and uncomment the edits one by one. After each edit you comment out make a commit. So the workflow will be the following

1. Uncomment one edit
2. Stage the edit
```
git add dice_game.py
```
3. Commit the edit
```
git commit -m '<Descriptive message>'
```
4. Push your edit to github
```
git push
```
As further explanation to this push command, we need to specify that we want to push the edits on the `game-improvement` branch to github (origin).

When all the edits are done it is time to make a pull request. In this step we put all our edits into the master version of the game. 
1. Go online to github and navigate to your repository containing the game
2. Switch to the game-improvements branch.
3. Click `New pull request` next to the branch name.
4. Make a brief comment like: "Major improvements to the game". Notice how you can see all the edits below and the edits each individual commit contributed with. This can be very usefull in the future to make sure the correct edits are made.
5. Press `Create pull request`
6. Hopefully you will see a green checkmark saying that there are no conflicts and that you can go ahead and merge the two branches. **Note!** This step of actually merging the edits to the master branch will only be made by the repository admin for the projects we work on in the lab. This serves as a good demostration of the workflow though.
7. After you create a pull request a discussion thread is opened where users can discuss the changes and potentially make additionally changes to the branch before merging.  
8. In this simple case, just click `Merge pull request` and then `Confirm merge`.
9. At this stage we can delete the `game-improvement` branch.
10. Congratulations!


## Description of the edits
### Edit 1
- We want a nice welcome screen to the game. Add at the top of the script after `import`
```
def welcome_banner():
    print '-------------------------------------'
    print '- - - Man vs. Machine Dice Game - - -'
    print '-------------------------------------'
```
- Then add `welcome_banner()` at the begining of `main()`

### Edit 2
- Ask the user how many rounds to play by adding the following to the `main()` function.
```
nrounds = int(raw_input('How many rounds shall we play: '))
play(nrounds)
```

### Edit 3
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
- Don't forget to remove the old function above (since we use version control we can safely delete it instead of comment it out since we can go back and retrieve it if we want to.)

### Edit 4
- In the current implementation you will win if you both end up with the same score. Add the possibility for it all ending up in a tie. We also want to give the user a chance for a rematch in case he/she loses the game
- Change the last part of `play()` to:
```
if computer_capital < player_capital:
    print 'You Win!'
    
elif computer_capital > player_capital:
    print 'Machine Wins!'

else:
    print 'Tie!'

ans = raw_input('Do you want a rematch (y/n): ')
if ans == 'y':
    print "\n - Let's go again! - \n"
    main()
```
- Again, don't forget to remove the code above that we don't want anymore.

