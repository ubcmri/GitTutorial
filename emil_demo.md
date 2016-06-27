# Emil Keynote Demo

In this demo I will go through how to

- clone a repository from Github
- create a new branch
- push a branch to Github
- checkout a remote branch
- adding and commit new edits
- push edits to github
- pull request on Github

First I clone the repository from Github
```
> git clone https://github.com/ubcmri/T2_MWI.git
> cd T2_MWI
```
If I look at the branches available I only see the current one
```
> git branch
* master
```
But there are branches on Github that I can't see right now. I can see them using
```
> git branch -r
  origin/HEAD -> origin/master
  origin/develop
  origin/master
```
If I want to start working on either of these branches I can check them out using
```
git checkout -b develop origin/develop
```
The first `develop` is the name of the local branch, and `origin/develop` tells git that you want to connect it to the `develop` branch on github.
Now you will see that there is another branch
```
> git branch
* develop
  master
```
You can now continue to work on this branch. But I want to create my own branch here. I start from the master branch
```
> git checkout master
```
Then I create a new branch from the `master` branch
```
> git checkout -b emil-fix
```
This is a local branch, it does not exist online on Github yet. Now I make some edits to the README.md file. Once I am done I add and commit my edits
```
> git add README.md
> git commit -m 'More help'
```
Then it is time to push this to Github. But Github doesn't know about my personal `emil-fix` branch. So I have to tell git this by adding in the `-u` option like this
```
git push -u origin emil-fix
```
Now when I go online on Github I can see that there is another branch available! Perfect! Now someone else can access this branch.

I am not 100% happy with the edits so I do some more edits
```
# more edits
> git add README.md
> git commit -m 'Changed my mind'
> git push
```
Not that this time I don't have to specify `-u origin emil-fix`, that was a one-time thing. Now that all the edits are done and things are on Github I go online to put these edits into the master branch where we have the working version.

I navigate to the repository and choose my `emil-fix` branch. I create a pull request and follow the steps that comes after this. The repository admin will be the one to do the final OK in this before the merge is completed.

Now that everything is on the master branch I don't need the local branch anymore! When you are sure the branch isn't needed delete it on github by navigating to the branch tab and click delete. To remove the branch locally I navigate to my terminal and type
```
> git checkout master
# To make sure we are not on the branch we delete
> git branch -d emil-fix
```
