# CS50 Workspace! (macOS)

Use this repository to work on your projects locally! Developing locally lets us use cool stuff like graphics libraries for data visualization.

> [!TIP]
> These steps involve a lot of switching between windows and things popping up. Fullscreening windows makes managing multiple windows much harder and hides these popups. I strongly recommend not fullscreening anything as you go through this process.

## 1. Install Your Tools

### A - Install Python 3.13

* Download the installer directly: **[Python 3.13.15 macOS installer](https://www.python.org/ftp/python/3.13.15/python-3.13.15-macos11.pkg)**
* **NOTE:** If you get an "unknown developer" warning when you try to open the installer, go to Finder, right-click the installer, then click Open from that menu. This should give you the option to open and complete the install.
* **NOTE:** If you get "macOS can't ensure the security of this program," go to System Settings/Preferences → Security and Privacy → (scroll down) → Open Anyway, then follow the prompts.
* Verify it worked by opening **Terminal** (Cmd+Space, type "Terminal", Enter) and running:
  ```
  python3 --version
  ```
  ```
  python3 -m tkinter
  ```
  The first command should print something starting with `Python 3.13.`. The second should pop open a small test window with buttons — if that appears, `tkinter` is working. Close it when done.

### B - Install Homebrew

Homebrew is a "package manager" — instead of hunting down installer files on the web, it lets you install everything else with one-line commands.

* In Terminal, paste this and press Enter:
  ```
  /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
  ```
* Follow the prompts — it may ask for your Mac password (typing won't show characters, that's normal) and may ask you to press Enter to confirm.

> [!IMPORTANT]
> At the end, the installer prints 1–2 "Next steps" commands to add Homebrew to your PATH (something like `echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile` followed by `eval "$(/opt/homebrew/bin/brew shellenv)"`). Copy and run exactly what it shows — skipping this means the `brew` command won't work in new terminal windows.
>
> <!-- TODO: screenshot of the installer's "Next steps" output -->

* Verify it worked (in Terminal):
  ```
  brew --version
  ```

### C - Install the Rest with Homebrew

* `vscodium` — the code editor.
  ```
  brew install --cask vscodium
  ```
* `git` — saves your work, like Google Drive but for programmers.
  ```
  brew install git
  ```
* `gh` — the GitHub CLI, needed for `submit50` and `check50`.
  ```
  brew install gh
  ```

<br/>

<br/>

## 2. Set Up GitHub

### A - Sign Up for GitHub

[Sign up for a GitHub Account](https://github.com/signup) using your personal email! (you'll want access to it after you graduate)

### B - Check GitHub CLI Is Installed

Double check that you've downloaded and installed GitHub CLI. We'll check this by trying a command to check the version of GitHub CLI. This command will only work if we have it installed. Open Terminal and type: 

```terminal
gh --version
```

_You're good if you see a version number, like `gh version 2.43.1 (2024-01-31)` (your numbers can be different). If you get `zsh: command not found: gh`, first try quitting Terminal and reopening, and try again. If that still doesn't work, then you need to try installing GitHub CLI again (see link at the top)._

### C - Log In with GitHub CLI

Now we want to login and connect GitHub CLI with GitHub. Type this command: 
```terminal
gh auth login
```

Then (using your keyboard) select the following options:
* Where do you use GitHub? **GitHub.com**
* What is your preferred protocol for Git operations on this host? **HTTPS**
* Authenticate Git with your GitHub credentials? **Y**
* How would you like to authenticate GitHub CLI? **Login with a web browser**

### D - Confirm in Your Browser

Copy the 8-letter code shown in the terminal, then hit enter. Terminal will open your web browser to GitHub.com and you can paste the 8-letter code there.

Once you've finished those steps successfully, quit Terminal.

<br/>

<br/>

## 3. Set Up Your Project in VSCodium

### A - Copy the Profile URL

Copy this URL - you'll paste it into VSCodium in the next step:

```
https://raw.githubusercontent.com/mrsharp-milken/cs50-workspace/main/mrsharp-student.code-profile
```

### B - Import the Profile

Import the profile and its settings! Open VSCodium (this is an app you just downloaded), then:
* Click the gear icon at the bottom of the left sidebar.
* Click "Profiles" >> Blue Arrow dropdown next to "New Profile" >> "Import Profile".
<img width="668" height="179" alt="image" src="https://github.com/user-attachments/assets/da9b7e36-fcf6-4b5c-aec4-0f511d0798b2" />
* A text box will appear at the top of the window - paste the URL you just copied and press Enter.
* You should see a small loading indicator on the bottom of your VSCodium window, followed by a preview of what's being imported.
* Click "Import" to confirm.

### C - Select the Profile

Now switch to the profile you just imported.
* Click on the gear icon in the bottom left, then "Profiles" >> "mrsharp-student" >> "✔️".
* You'll know you're correctly using the profile when the icon at the bottom of the left sidebar changes from a gear to a little robot head.

### D - Create Your Own Copy of the Repo

Come back here to GitHub and create your own copy of this repository. Click the green "Use as Template" button in the upper right of [this page](https://github.com/mrsharp-milken/cs50-workspace/tree/main).
* Use `cs50-workspace` as the repository name
* **Make sure the repository is Private**
* (the other settings don't matter)

### E - Clone Your Repo

Now you'll download the starter files from your GitHub repo using the terminal.
* Open a terminal in VSCodium: Terminal >> New Terminal (top menu bar).
* Clone your repo:
  ```
  gh repo clone $(gh api user --jq .login)/cs50-workspace
  ```
  This downloads the files into a new folder called `cs50-workspace`.
* Open that folder in VSCodium: File >> Open Folder... and select the `cs50-workspace` folder you just cloned.
* You'll know this worked when you can see some files show up on the left like `python-test` and `README.md`

<br/>

<br/>

## 4. Test & Save Your Work

### A - Run Your First Program

Test if you can run your code!
* Open terminal by clicking (on the menu bar on top of your screen) Terminal >> New Terminal
* Use `cd python-test` to move into the python-test folder
* Then `python3 hello-world.py` to run the python file.

**It should look like this when you're done:**
<img width="1440" alt="Screenshot 2024-12-12 at 12 56 02 PM" src="https://github.com/user-attachments/assets/ea6f7b53-4f53-4160-be76-051c4e35b00e" />

> [!NOTE]  
> The `cd` command is the terminal command to enter a folder! You can use `cd ..` to "back out" of a folder. If you type `cd` without other options, instead of going to the "project home" folder, you'll go to the "user" folder of your computer, which might make you feel lost. If your terminal gets lost in the wrong folder, you can always close and reopen the VSCodium terminal, and it'll put you back in your project home.

### B - Configure Git and Push Your First Commit

Now, let's connect your GitHub account so your code autosaves to GitHub. Go to VSCodium and make sure we have the cs50-workspace folder open, and the robot icon in bottom left shows our profile is enabled. Then open VSCodium's terminal and run these commands:

```terminal
git config --global user.name "$(gh api user --jq '.login')"
```

```terminal
git config --global user.email "$(gh api user --jq '"\(.id)+\(.login)@users.noreply.github.com"')"
```

```terminal
python3 .setup/setup-hooks.py
```

```terminal
git add .
```

```terminal
git commit -m "first commit"
```

```terminal
git push
```

_If you see an error message, screenshot it to show to Mr. Sharp._

<br/>

<br/>

## 5. Verify Your Setup

Want to double check everything above actually worked? Open VSCodium's terminal in the `cs50-workspace` folder and run:

```terminal
python3 .setup/check-setup.py
```

This checks Python/tkinter, git, GitHub CLI login, your git remote, recent commits, and installed extensions, and tells you exactly what to fix if something's missing.

<br/>

<br/>

## Done!

Whew!
