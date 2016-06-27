# Getting started with Github

## Setup

### SSH keys
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

### Configure Git
Let's set up your git installation:
```
git config --global user.name <name>
```
Put in your full name. It will be attached to each commit you make so other users know who made them.

```
git config --global user.email <email>
```
Similarly, tell git your email address.

```
git config --global core.editor emacs
```
And, if you want, your favorite text editor.



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

### Add files and commit
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




## Using branches

Branches allow you to work on different aspects of a project separately, get different features working separately and merge the branches back together.

The default branch for each project is called "master", but you can make your own. We'll make a new branch to add some python code to our project.

```
> git checkout -b myfeature
```

"Checkout" is the command that allows you to switch between branches. The -b flag tells git to create a new branch called "myfeature". You can see which branch you're currently on by typing
```
> git branch
```
and switch between branches with ```git checkout {branch}```
Switching between branches changes the files in the project directory so be careful! Git will warn you if you have uncommited changes before switching branches, you should listen to it!

Let's make a change in our script in the new branch by adding an argument:
```
#!/bin/bash
name=$1
echo "Hello ${name}!"
```

Once you test that your new feature is working, commit your changes to the new branch:
```
git add helloworld.sh
git commit -m "add custom name feature"
```

To include the changes back into the master branch.

```
> git checkout master
```

You're now back on the master branch (double check by typing ```git branch``` and by looking at the content of your script). To combine the changes from the feature branch into the master branch, type
```
> git merge myfeature
```

You've now merged your feature into the master branch! If you wanted to you could delete your feature branch (we'll keep it for now). This merge was trivial since it just added the more recent changes. This is called a "fast forward merge". More complicated merges occur when concurrent changes have been made to the master and feature branches.

If your merge cannot be resolved by git trivially, it will tell you so when you try to run git merge. Your file(s) that have conflicts between the feature and master branches will be marked up by git pointing out where the conflicts are. You can go in and fix the conflicts by hand or use a graphical tool ("mergetool") to help


## Updating your local repository

We've already shown how to push your local commits to the central repo. But sometimes, changes will occur on the origin repo and your local repo become out of date. This could happen because
* You pushed some changes from your laptop, and now want to make sure those changes are included on your desktop
* A collaborator added a feature and pushed to origin since the last time you updated your local version.

There are two main tools that will update your local repo, "fetch" and "pull".

### Fetch

To download all the branches from the central repo, run
```
git fetch origin
```
Or, if you just want the latest version of a specific branch,
```
git fetch origin <branch>
```
The branches from origin are now accessible to you, but they behave slightly different than local branches. To see them, type
```
git branch -r
```
You can checkout these branches like normal using the "checkout" command, but it's not a good idea to commit changes to them. If you want to update changes from origin master branch to your local master branch,
```
git checkout master
git merge origin/master
```
The benefit of using "fetch" is that it allows you to download the remote branches and examine them on your own computer before merging.

### Pull

If you're confident that you want to include the remote changes, you can combine the "fetch" and "merge" commands with "pull":
```
git pull origin master
```

Instead of merging, you also have the option to "rebase". Rebasing essentially means tacking on your recent commits on top of whatever remote branch you want to synchronize with. This is handy because it saves the trouble of a merge and keeps the project history more straightforward. The important thing to remember is that since rebasing changes the history of a branch, it should never be used on public branches. To rebase, use the pull command as above but with the rebase option:
```
git pull --rebase origin master
```

Try both of these in your test repository and check ```git log``` to see the project history and how it differs in either case. For example, try editing the README.md file directly on the github interface, then update your local project to show the changes.
