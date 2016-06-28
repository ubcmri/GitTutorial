# Hands on Github tutorial

## Introduction
By this time we hope you have somewhat of an idea of how git works but most importantly why we want to use it. To get this more into context you will do a small exercise that will teach you some of the most important aspects of the Github workflow. To facilitate this you will work on your own small project that will give you an idea of how the workflow works.

For clarification, most of the work in the exercise is done in the terminal. To reduce confusion, everything that you are suppose to run in the terminal is shown in code blocks like below:

```
> example of command you run in the terminal
```

Things that you do in Github will be marked with :octocat:.

In this tutorial you will use a workflow very similar to the [feature branch workflow](feature_branch_workflow.md). The workflow won't be explicitly specified in this tutorial but please refer to the document linked above.

### Learning goals
- Setting up a new local git repository and sync it with Github
- Understand the difference between git on your computer and Github
- Know how to use git commands including: `clone`, `pull`, `push`, `add`, `commit`, `branch`, `merge`
- Use Github online for viewing files and issue control
- Understanding of the *feature branch workflow*

## Exercise

### Setting up a new Github repository
(:octocat:) First, open your web browser and go to http://www.github.com. At this point Mike should already have shown you how to create a repository on your Github profile. If you have done that alread, skip to the next paragraph, if not, continue reading. Now you want to create a new repository, i.e. a new project. Go to your profile on github and set up a new repository. If you can't find it, follow guide here: https://help.github.com/articles/create-a-repo/

Managed to create a new repository (git slang *repo*)? Great! Then you want to get this project onto your computer, this is called cloning.

Open up your terminal and navigate to the folder where you want to put your repo. Clone the repository by typing in the following command and substitute `<url-to-repo-on-github>` with the address to the repository that can be found on the repository page on Github (:octocat:)
```
> git clone <url-to-repo-on-github>
```
If you are having issues with this, have a look at the online help: https://help.github.com/articles/cloning-a-repository/.

Great job setting up the repo on your computer! Now we want to put our project files into the folder. In this small exercise you will be working with a dice game written in python and your task will be to improve the functionality of the game.

Copy the [`dice_game.py`](dice_game.py) into the git repository on your computer. The python file can be found in the GitTutorial repository. Either using the terminal or the windows on your desktop. Now run `git status` in your terminal and notice that there is an untracked file. We will fix this later when we make edits to the file.

In this very simple game you are trying to beat the computer in guessing the sum of two dice that you roll. You guess the sum of the two dice and the computer does the same. Every time you guess wrong you lose money. The first to lose all their money loses the game. Try running the game (and beat the computer) by typing

```
> python dice_game.py
```

### Time to branch out - Creating your first branch
Your task is to make this game a little bit more interesting. Start off by making a new branch that we will call: `game-improvement`. The idea of creating a new branch is similar to making a copy of the file when you want to make some new adjustments to it in case you want to revert back to the previous version. With git we don't need to create a second copy of the file, with branches we can do the exact same thing!
```
> git checkout -b game-improvement
```

Run `git branch` to see that you are on the right branch
```
> git branch
* game-improvement
master
```

At this stage, this branch is only on your computer. No one else in the group know that you are working on this awesome new feature. To let people know what you are working on you can push this branch to Github. To do this, we need to tell git on your computer which branch to push and where. `origin` is the word we use for the shared repository on Github.
```
git push origin game-improvement
```

This tells git that we want to push this branch to github. After this we do not need to specify `origin game-improvement` again for future commits.

### Add and commit changes in the code
Now that everything is set up it is time to make some edits in the code! This is the point where you would start development on your new feature on the script but in the interest of saving time I have prepared this for you already (yeah, cooking show style!).

Open up the terminal and open the `dice_game.py` in your favorite text editor (sublime, atom, gedit, textedit, vim, vi (if you are hardcore coder), nano, just don't use word!). Scroll through the code and try to get an idea of what it does.

The prepared edits are commented out of the code so your job will be to comment these out one by one. To simulate the real development process you will `commit` all changes you make.

**NOTE!** Code in Python needs to be properly indented. After an `if` statement the code needs to be indented with one tab. Make sure there are no additional spaces as this will make the code to crash.

So this is the process you will iterate through 4 times
1. Find the edit and uncomment it. Note! Some edits require you to delete lines above the new code as well. So please have a look at the end of this document for further description of each edit.
2. Stage the edit
```
> git add dice_game.py
```
3. Commit the edit
```
> git commit -m '<Descriptive message>'
```
4. Push your edit to github
```
> git push
```


(:octocat:) When all the edits are done it is time to make what is called a pull request. In this step we put all our edits into the master version of the game.

1. Go online to github and navigate to your repository containing the game
2. Switch to the game-improvements branch.
3. Click `New pull request` next to the branch name.
4. Make a brief comment like: "Major improvements to the game". Notice how you can see all the edits below and the edits each individual commit contributed with. This can be very usefull in the future to make sure the correct edits are made.
5. Press `Create pull request`
6. Hopefully you will see a green checkmark saying that there are no conflicts and that you can go ahead and merge the two branches. **Note!** This step of actually merging the edits to the master branch will only be made by the repository admin for the projects we work on in the lab. This serves as a good demostration of the workflow though.
7. After you create a pull request a discussion thread is opened where users can discuss the changes and potentially make additionally changes to the branch before merging.  
8. In this simple case, just click `Merge pull request` and then `Confirm merge`.
9. At this stage we can delete the `game-improvement` branch.
10. Congratulations! You did it!


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
