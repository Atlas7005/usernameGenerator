# usernameGenerator
A Python3 username generator that follows Twitch's username restrictions.  
This is just a tiny script/program/whatever I made because I am passively learning Python, and I made a Node.js version of this.  
Tested and made on Windows 10 - Python 3.8.2 and Python 3.9.2.

## Features
  - Saves generated usernames to `names.txt` in same directory.
  - Command Line Interface - Specify the amount of usernames you wanna generate, as well as the length of those usernames. Ex: `python usernameGen.py 50 10`: This generates 50, 10 character long usernames.
  - Created by a complete newbie.
  - May or may not give you a free cake.

## Installation & Usage
First, clone the repo.  
`git clone https://github.com/Atlas7005/usernameGenerator`  

Then, install the requirements.  
Windows: `py -m pip install -r requirements.txt`  
Linux/macOS: `python -m pip install -r requirements.txt`  

When that is done, all you need to do is run the thing.  
Windows: `py usernameGen.py <amount> <length>`  
Linux/macOS: `python usernameGen.py <amount> <length>`

## License
[GNU GPLv3](https://choosealicense.com/licenses/gpl-3.0/)