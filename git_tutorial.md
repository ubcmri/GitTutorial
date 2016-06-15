# Getting started with Github

## Setup
To make everything as easy as possible we need to follow a few simple steps. Start by generating a ssh key for the computer you work on. This is unique to every computer you work on.
```
ssh-keygen -t rsa -b 4096 -C "your_name@youremail.com"
```
(If there already is a ssh key stored you can either overwrite it by pressing *y*. If you know you need the other ssh key for something else please look at the more advanced github tutorial).
It will now ask you where to save the file. Chose default by pressing `enter`. It will then ask you for a passphrase, we will leave this blank. To set this press `enter` twice. Now we add this ssh key to the ssh-agent by
```
ssh-add ~/.ssh/id_rsa
```
Now we need to do some stuff on your github account.
- Go online and login to your account.
- Press the small icon with your avatar in the top right corner and chose settings.
- Now go to *SSH and GPG keys*.
- Click *New SSH key*
- In the *Title* box type in the name of the computer you are adding in (Ex: Amadeus, Icenine, My_macbook)
- Keep the browser window open in the background and get back to the terminal.

We want to copy the content of the ssh key to Github.
```
cat ~/.ssh/id_rsa.pub
```
This will type out the content of the ssh key in the terminal, a really long key with weird characters. Copy the content, including `ssh-rsa` all the way to your email adress at the end. Now past this into the `Key` box on your github account in the browser that is in the background. Finish by pressing `Add SSH key`.

What we have done here allows you to pull and push data from private Github repos without typing in your password every time.


## Create your first repo

### Initialize a local repos

Create a working directory where repositories you create or clone will live. This can be named anything. In the working directory, make a direcory called "myfirstrepo"
```
> mkdir working_dir
> cd working_dir
> mkdir myfirstrepo
> cd myfirstrepo
```

Initialize a git repository in this directory. This will tell git to create some hidden files that will allow you to keep track of changes to this directory. Each directory you initialize with git is a separate project
```
> git init
```
By typing "ls -a" you should now see a hidden folder called "./.git". Your local version history will be kept in this folder. If you ever want to check whether git has been initialized for some project, check whether this folder exists. Deleting it will remove the local version history. Mostly, though, you can ignore it completely.

Here we're initializing a git repo in an empty directory to start a new project, but you can do the same thing in a directory that already has lots of scripts in it!

### Add files to your repo
You should have a README in your project to tell other users (and yourself) what this project is about. Using your favorite text editor, open a file called README.md and enter a description of this project such as
```
# myfirstrepo

This is an example project to learn the basic git commands
```
and save the file.

Now, we'll tell git that we want this file included in our next commit
```
> git add README.md
```
and now we can make our first commit:
```
> git commit -m "Adds a readme file to the project"
```

The is now a record of the state of this project at this point in time. If we ever screw something up, we can revert the project directory to this state. To see the history of commits, type
```
> git log
```
and you'll see something like
```
commit a54b0265456f976a570839dc20ed0c7c28e1c071
Author: Mike Jarrett <msjarrett@gmail.com>
Date:   Tue Jun 14 14:55:00 2016 -0700

    Adds a readme file to the project
  ```

Each commit is uniquely identified by the hex number at the top. Use short but descriptive commit notes to easily identify what the commit does.

Add a helloworld.sh script
```
#!/bin/bash

echo "hello world!"
```
and update the readme

```
# myfirstrepo

This is an example project to learn the basic git commands. It includes a basic hello world script.
```

To make your next commit, add both these files and commit
```
> add README.md helloworld.sh
> commit -m "updates README.md and adds helloworld.sh"
```
As before, ```> git log``` will show the new commit history.

### Connect your repository to github

Currently, your project is saved locally and the version history is only available to you. If you want access to this project from other computers, want a safe backup, or want to share it with other people, you can connect it to a remote repository such as GitHub.

Log in to GitHub. You should see a green button that says "New Repository". Click it! Keep yourself as the owner, and name the repo the same thing you named the project directory on your computer (in our case "myfirstrepo") and click "Create repository". We've already started the repo on our local machine but if we hadn't we'd select the "initialize project with a README" box.

You'll now see a screen with instruction on how to connect your local repo to the remote repo. Copy the ssh address of the GitHub repo then go back to the command line and type:
```
> git remote add origin git@github.com:{username}/myfirstrepo.git
```
This permanently connects your local repo to GitHub. (Note that the remote origin doesn't have to be GitHub; there are other services like GitLab and BitBucket, or you can host your own.)

Finally, we'll push the changes we've made in our local directory to the remote repo:
```
> git push origin master
```
In this command, "push" means copy your commit history to the remote host ("origin") on the branch "master". "Master" is the name of the default branch. We'll talk more about branches shortly.

## Branches

Branches allow you to work on different aspects of a project separately, get different features working separately and merge the branches back together.

The default branch for each project is called "master", but you can make your own. We'll make a new branch to add some python code to our project.

```
git checkout -b python_test
```

"Checkout" is the command that allows you to switch between branches. The -b flag tells git to create a new branch called "python_test". You can see which branch you're currently on by typing
```
git branch
```
and switch between branches with ```git checkout {branch}```
Switching between branches changes the files in the project directory so be careful! Git will warn you if you have uncommited changes before switching branches, you should listen to it!

Add a new file called helloworld2.py
```
#!/usr/bin/python

print "Hello again, world!"
```





## Clone your first repo
Open the terminal and navigate to where you want to keep your scripts. To get started and download a repo you use the `clone` command. Example with T2 analysis
```
> git clone -b develop git@github.com/ubcmri/T2_MWI.git
```
This have created a new folder in your current directory. Navigate to it
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
