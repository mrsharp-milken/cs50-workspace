# CS50 Workspace!

Use this repository to work on your projects locally! Developing locally lets us use cool stuff like graphics libraries for data visualization.

1. **Tip:** These steps involves a lot of switching between different windows and things popping up. Fullscreening windows makes managing multiple windows much harder and hides these popups. I strongly recommend not fullscreening anything as you go through this process. 
2. With that, download and install these four programs:
    * [VSCode](https://code.visualstudio.com/download) - This is the code editor!
    * [Python for Mac](https://www.python.org/downloads/macos/) or [Python for Windows](https://www.python.org/downloads/windows/) - The python "interpreter" that lets us run python programs. Choose the "latest Python 3 Release" link at the top of the page.
    * [git for Mac](https://sourceforge.net/projects/git-osx-installer/) or [git for Windows](https://git-scm.com/downloads/win) - git is the program that saves and your work, it's a lot like google drive but for programmers. 
        * **NOTE:** If you get an "unknown developer" warning when you try to open the installer package, try going to Finder, right clicking the installer package, then clicking Open from that menu. This should give you the option to open and complete the install.
        * **NOTE:** If you get "macOS can't ensure the security of this program" you have to to go to your system settings / system preferences >> Security and Privacy >> (Scroll down) ... Open Anyway. Then follow the prompts to finish opening and installing.
    * [Github CLI for Mac](https://github.com/cli/cli/releases/download/v2.62.0/gh_2.62.0_macOS_universal.pkg) or [Github CLI for Windows](https://github.com/cli/cli/releases/tag/v2.78.0#Contributors:~:text=ankddev-,Assets,-24) - Github  CLI is what lets you save, submit, and check your code using the command line, you need it to use submit50 and check50. You might also get an "unknown developer" warning here on Mac, follow the same steps as above.

<br/>

<br/>

3. **Before moving on, make sure you've installed everything, not just downloaded it!** Every file you just downloaded is an installer, and many of the steps below won't work until you run the installers.

<br/>

<br/>

4. Download the CS50 VSCode Profile [clicking the download button at this link](https://github.com/mrsharp-milken/cs50-workspace/blob/main/cs50student.code-profile) - this will help us install and setup all of the important extensions and settings for you after we import it.
<img width="1190" height="344" alt="Screenshot 2025-09-07 at 8 03 34 PM" src="https://github.com/user-attachments/assets/1029b7dd-05bd-4ea1-b280-e61c74c7fcc3" />

5. Open VSCode, then click the gear icon at the bottom of the left sidebar. Click "Profiles" >> Blue Arrow dropdown next to "New Profile" >> "Import Profile" >> "Select File" and choose the file you just downloaded, with the name `cs50.code-profile`. If it worked, you should see a small loading indicator on the bottom of your VSCode window.
<img width="668" height="179" alt="image" src="https://github.com/user-attachments/assets/da9b7e36-fcf6-4b5c-aec4-0f511d0798b2" />

<br/>

<br/>

6. While things are installing, you can come back here to Github and create your own copy of this repository. Click the green "Use as Template" button in the upper right of this page.
    * Click the green "Use as Template" button in the upper right of this page
    * Use `cs50-workspace` as the repository name
    * **Make sure the repository is Private**
    * (the other settings don't matter)
    * When finished, copy the link to your new repo

<br/>

<br/>

7. Now you'll finish setting up the profile. 
    * Go back to VSCode, and choose the CS50 profile by clicking on the gear icon in the bottom left. 
    * Click "Profiles" >> "cs50 student". If you don't see it, you might have to wait a bit longer for the profile to finish installing. 
    * You'll know you're correctly using the profile when the icon at the bottom of the left sidebar changes from a gear to a little robot head.

<br/>

<br/>

8. Next, you'll download the starter files from your github repo.
    * Find the file explorer icon on the top of the left sidebar and click it. 
    * Click the blue "Clone Repository" button. 
    * Paste the link to you github repository you copied earlier here. (The link should look like `https://github.com/YOUR_USERNAME/cs50-workspace` but with your username instead of `YOUR_USERNAME`). 
    * Choose a location you'll remember, like your user folder, Documents, or Desktop. 
    * This step will download the files in the github repository, and put them in a folder called "cs50-workspace".
    * You'll know this worked when you can see some files show up on the left like `python-test` and `README.md`

<br/>

<br/>

9. Test if you can run your code!
    * Open terminal by clicking (on the menu bar on top of your screen) Terminal >> New Terminal
    * Use `cd python-test` to move into the python-test folder
    * Then `python3 hello-world.py` to run the python file. 

### It should look like this when you're done:

<img width="1440" alt="Screenshot 2024-12-12 at 12 56 02 PM" src="https://github.com/user-attachments/assets/ea6f7b53-4f53-4160-be76-051c4e35b00e" />

> [!NOTE]  
> The `cd` command is the terminal command to enter a folder! You can use `cd ..` to "back out" of a folder. If you type `cd` without other options, instead of going to the "project home" folder, you'll go to the "user" folder of your computer, which might make you feel lost. If your terminal gets lost in the wrong folder, you can always close and reopen the VSCode terminal, and it'll put you back in your project home.

<br/>

<br/>

## Autosaving Code to GitHub

To make sure you don't lose your code, let's connect your GitHub account so your code autosaves to Github!

1. Double check that you've downloaded and installed Github CLI. We'll check this by trying a command to check the version of Github CLI. This command will only work if we have it installed. Open Terminal and type `gh --version`

_You're good if you see a version number, like `gh version 2.43.1 (2024-01-31)` (your numbers can be different). If you get `zsh: command not found: gh`, first try quitting Terminal and reopening, and try again. If that still doesn't work, then you need to try installing Github CLI again (see link at the top)._

2. Now we want to login and connect GitHub CLI with GitHub. Type this command: `gh auth login`. Then (using your keyboard) select the following options:
    * Where do you use Github? **Github.com**
    * What is your preferred protocol for Git operations on this host? **HTTPS**
    * Authenticate Git with your GitHub credentials? **Y**
    * How would you like to authenticate GitHub CLI? **Login with a web browser**

3. Copy the 8-letter code shown in the terminal, then hit enter. Terminal will open your web browser to GitHub.com and you can paste the 8-letter code there.

4. Once you've finished those steps successfully, quit Terminal.

5. Now, let's check that everything is working with a command that tests our ability to save code to Github. Go to VSCode and make sure we have the cs50-workspace folder open, and the robot icon in bottom left shows our profile is enabled. Then open VSCode's terminal and run these commands: 

```terminal
git commit -am “first commit!”
```

```terminal
git push
```


_If you see an error message, screenshot it to show to Mr. Sharp._

## Python Graphics

1. Test graphics with a basic command: `python3 -m tkinter`. It should give you a little window like this:
<img width="178" alt="image" src="https://github.com/user-attachments/assets/2e95bb2b-aacb-41fd-8dd1-2a8b07bf1518" />

2. Next, try a more substantial graphics program. Run this command to download the program:
```bash
curl -O https://raw.githubusercontent.com/mrsharp-milken/python-samples/refs/heads/main/simple-text-graphics.py
```

3. Run the program. What does it do? Look around!

4. This program uses python's default graphics library, called **tkinter**. We'll be using it for the next project. For now, use google to help you add code to draw a rectangle or circle using the **tkinter** library.

## Submitting

Once you've completed Step 4 above, **take a screenshot that shows the graphics and the code you added, then submit it on MyMilken.**

For some assignments, we'll submit using the `submit50` tool via the command line. It's worth installing `submit50` and `check50` now so you don't have to do it last minute later:

```bash
pip3 install submit50 check50
```

## Notes

Check out this link to [Mr. Sharp's code reference document](https://github.com/mrsharp-milken/AP-CS-Principles/blob/main/README.md), with terminal commands, code samples, and debugging strategies.

Write your own notes / things you want to remember here!

