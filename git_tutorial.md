# Test

Open the terminal and navigate to where you want to keep your scripts. To get started and download a repo you use the `clone` command. Example with T2 analysis
```
> git clone -b develop https://github.com/ubcmri/T2_MWI.git
```
This have created a new folder in your current directory. Navigate to is
```
> cd T2_MWI
```
To see which branches currently exist write
```
> git branch
* develop
```
As you can see, you only have one branch here. This is good, we want everyone to work on the develop branch.

Now make some edits on your files. Then add and commit the changes
```
> git add myfile.txt
> git commit -m 'Swedish translation'
```
At this stage, all changes you have made are local, let's get them to the central repo as well!
```
> git push
```
Now your changes have been pushed to the main repository.

The next time we start working on this we need to make sure we have the most current updates. To do this we `pull` the latest changes.
```
> git pull
```

## Create your own feature branch
Let's say you want to get started on your own feature locally, it is good to start your own branch. To do this type
```
> git branch my_feature
> git checkout my_feature
```
Now you are on your new feautre branch. The `checkout` command moves you to the new branch. Make some edits here, add and commit. Now we want to go back to the develop branch and merge our edits
```
> git checkout develop
> git merge my_feature
```
