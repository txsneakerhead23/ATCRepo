                                                Overview for v2
This python based “bot” is a free openatc and auto checkout bot for supremenewyork.com. This bot release(v2) is a major upgrade from the last on in that this one solves the checkout CAPTCHA. NOte, YOU MUST MAKE AN ACCOUNT at captchasolutions.com and buy tokens if you want this program to work correctly
New File
This release features a new file, the config.py file. To run this program correctly, you must edit this file.
                                                Editing the Config File
To edit the config file, you have to know three things:
The path to your default chrome profile, your captchasolutions key and your captchasolutions secret. 

To get the path to your default chrome profile, type chrome://version into the url bar and copy the path next to Profile Path: Past this in between the single quotes in the config file. 

You can copy and past your captchasolutions key and secret by logging in to your account, going to the dashboard and copying them from the right hand side panel.
                                                        Setting Up
                                                    Ubuntu/Debian OS’s
Go to Terminal and type mkdir supremebot
Download chromedriver and extract the file to the supremebot folder.
Press enter
Download the folder supreme from the github(in ZIP format)
OPen the folder
Press the Extract button at the upper left hand corner
Select the supremebot directory you just made
Click OK
Open terminal and run these commands in the order they appear:
 sudo apt-get install python --fix-missing
cd supremebot
sudo apt-get install python-pip python-dev build-essential
pip install selenium
pip install pause
pip install datetime
pip install pickle
pip install requests
pip install threading
chmod u+x supremebotv2.py
To run the bot, type supremebotv2.py into the Terminal window. T run it in the future. OPen up a fresh Terminal window, type and press enter cd supremebot and then type and press enter supremebotv2.py

                                                        Windows
If you do not have Python, follow this tutorial: https://www.howtogeek.com/197947/how-to-install-python-on-windows/ to learn how to install it(NOTE: INSTALL PYTHON 2.7 NOT Python 3)
Refer to this link to learn how to install pip: https://github.com/BurntSushi/nfldb/wiki/Python-&-pip-Windows-installation#pip-install
Open PowerShell and type mkdir supremebot
Press enter
Download chromedriver and extract the file to the supremebot folder.
Go to the github page and download the whole supreme folder as a zip file.
Click on the little down arrow on the download bar

Click Show in Folder
Extract the files(should be a button at the top) to the supremebot folder you just made
Right click on the supremebot folder where all the files you just downloaded should be
CLick on “Open command window here”
IN the command window type the pip commands from steps 12-17 in the Ubuntu tutorial above.
Type chmod u+x supremebotv2.py into the command window.
To run the bot, type supremebotv2.py in the same command window. 

                                                        Mac OSX
OPen up Terminal
Run this command: /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
Follow the instructions for the Ubuntu tutorial but whenever apt-get is used, use the word breq instead. I.e. sudo apt-get update becomes 
sudo brew update 


Note: If you ever get the error “chromedriver” executable needs to be in PATH, make a copy of chromedriver and move it to the directory /usr/bin
