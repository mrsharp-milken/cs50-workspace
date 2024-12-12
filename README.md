# CS50 Workspace!

Use this repository to work on your CS50 projects!

1. First, download and install these four programs:
    * [VSCode](https://code.visualstudio.com/download) - This is the code editor!
    * [Python](https://www.python.org/downloads/macos/) - The python "interpreter" that lets us run python programs.
    * [git](https://sourceforge.net/projects/git-osx-installer/) - git is the program that saves and your work, it's a lot like google drive but for programmers. If you get an "unknown developer" warning when you try to open the installer package, try going to Finder, right clicking the installer package, then clicking Open from that menu. This should give you the option to open and complete the install.
    * [Github CLI](https://github.com/cli/cli/releases/download/v2.62.0/gh_2.62.0_macOS_universal.pkg) - Github  CLI is what lets you save, submit, and check your code using the command line, you need it to use submit50 and check50. You might also get an "unknown developer" warning here, follow the same steps as above.
2. Download the CS50 VSCode Profile [with this link](https://drive.google.com/uc?export=download&id=19O9L1eGiU19j441sVVzeuvSFwhzLx5Po) - this will help us install and setup all of the important extensions and settings for you after we import it.
3. Open VSCode, then click the gear icon at the bottom of the left sidebar. Click "Profiles" >> "Import Profile" >> "Select File" and choose the file you just downloaded, with the name `cs50.code-profile`. If it worked, you should see a small loading indicator on the bottom of your VSCode window.
4. While the profile installs, come back here to Github and create your own copy of this repository. using the green "Use as Template" button in the upper right.
    * Click the green "Use as Template" button in the upper right of this page
    * Use `cs50-workspace` as the repository name
    * **Make sure the repository is Private**
    * When finished, copy the link to your new repo
6. Now you'll finish setting up the profile. Go back to VSCode, and choose the CS50 profile by clicking on the gear icon in the bottom left. Click "Profiles" >> "cs50 student". If you don't see it, you might have to wait a bit longer for the profile to finish installing. You'll know you're correctly using the profile when the icon at the bottom of the left sidebar changes from a gear to a little robot head.
7. Now find the file explorer icon on the top of the left sidebar and click it. Then click the blue "Clone Repository" button
8. Paste the link to you github repository you copied earlier here. (The link should look like `https://github.com/YOUR_USERNAME/cs50-workspace` but with your username instead of `YOUR_USERNAME`). Choose a reasonable location, like your user folder, Documents, or Desktop. This step will download the files in the github repository, and put them in a folder called "cs50-workspace".
9. Use the menu at the top to open terminal by clicking Terminal >> New Terminal
10. Test if you can run your code!
    * Use `cd python-test` to move into the python-test folder
    * Then `python hello-world.py` (or possibly `python3 hello-world.py`) to run the python file

### It should look like this when you're done:

<img width="1440" alt="Screenshot 2024-12-12 at 12 56 02 PM" src="https://github.com/user-attachments/assets/ea6f7b53-4f53-4160-be76-051c4e35b00e" />

> [!NOTE]  
> Using the terminal "locally" is slightly different than using it on cs50.dev! You'll need to use `cd ..` instead of `cd` to "back out" of a folder. If you type `cd` without other arguments, instead of going to the "project home" folder, you'll go to the "user" folder of your computer, which might make you feel lost. If your terminal gets lost in the wrong folder, you can always close and reopen the VSCode terminal, and it'll put you back in your project home.

## Autosaving Code to GitHub

To make sure you don't lose your code, let's connect your GitHub account so your code autosaves to Github!

1. Double check that you've downloaded and installed Github CLI. We'll check this by trying a command to check the version of Github CLI. This command will only work if we have it installed. Open Terminal and type `gh --version`

_You're good if you see a version number, like `gh version 2.43.1 (2024-01-31)` (your numbers can be different). If you get `zsh: command not found: gh`, first try quitting Terminal and reopening, and try again. If that still doesn't work, then you need to try installing Github CLI again (see link at the top)._

2. Now we want to login and connect GitHub CLI with GitHub. Type this command: `gh auth login`. Then (using your keyboard) select the following options:
    * What account do you want to log into? **Github.com**
    * What is your preferred protocol for Git operations on this host? **HTTPS**
    * Authenticate Git with your GitHub credentials? **Y**
    * How would you like to authenticate GitHub CLI? **Login with a web browser**

3. Copy the 8-letter code shown in the terminal, then hit enter. Terminal will open your web browser to GitHub.com and you can paste the 8-letter code there.

4. Once you've finished those steps successfully, quit Terminal.

5. Now, let's check that everything is working with a command that tests our ability to save code to Github. Go to VSCode and make sure we have the cs50-workspace folder open, and the robot icon in bottom left shows our profile is enable. Then open VSCode's terminal and run this command: `git push --dry-run`

_You're good if you see `Everything up-to-date`. If you see a different error message, screenshot it to show to Mr. Sharp._

## Python Graphics

1. Test graphics with a basic command: `python3 -m tkinter`. It should give you a little window like this:
<img width="178" alt="image" src="https://github.com/user-attachments/assets/2e95bb2b-aacb-41fd-8dd1-2a8b07bf1518" />

2. Next, try a more substantial graphics program. Run this command to download the program:
```bash
curl -O https://raw.githubusercontent.com/mrsharp-milken/python-samples/refs/heads/main/simple-text-graphics.py
```

3. Run the program. What does it do? Look around!

4. This program uses python's default graphics library, called **tkinter**. We'll be using it for the next project. Look it up, then add some code to draw a different shape, like a rectangle or circle.

## Notes

Check out this link to [Mr. Sharp's code reference document](https://github.com/mrsharp-milken/AP-CS-Principles/blob/main/README.md), with terminal commands, code samples, and debugging strategies.

Write your own notes / things you want to remember here!

