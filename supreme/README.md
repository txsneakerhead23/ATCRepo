General Notes:
- You mustn't have any other instances of Chrome open when running the bot
- If you encounter any errors relating to "Permission denied", simply append the word "sudo" without the quotes as a prefix to the command that throws that error

To use the windows bot, follow these steps:
1. Download the zip file by clicking "View Raw" after clicking on the zip file above
2. Extract the zip file to any folder you please
3. Click on the folder and, inside that folder, there are two key files:config and supremebotv2

The config files contains all the necessary info that is needed to successfully run the bot. This info includes: your personal "key" and "secret" and the path to your chrome profile.

To successfully run this bot, you will need to obtain a "key" and "secret" by either emailing grandstreetsupreme@gmail.com; or messaging /u/grandstreetsupreme on Reddit. The current rate for a "key" and "secret" is $14. 
Furthermore, this bot uses your default chrome profile(the path to which can be obtained by typing chrome://version into the url bar of google chrome and copying the Profile Path) and, as such, it is expected that you have all of your checkout information autofilled on the checkout page of Supreme's website. 

Once you have your key, path and secret, you can simply paste them into the appropriate places in the config file.

To run the bot, simply double click on "suprembotv2" in the windows bot folder. 

----------------------------------------------------------------------------------------------------------------------------
If you would like to use our software and you do not use Windows but instead use an os such as Mac or Linux, please  email or message grandstreetsupreme for a key and secret, as well as getting the path to your default chrome profile and copying the key/secret into the config file. To install the bot on Mac, follow these instructions:
1. Open terminal
2. Run: /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)" in the terminal window
3. When that finishes, run: brew install subversion
4. When that finishes run: mkdir supremebot
5. When that finishes run: cd supremebot
7. when that finishes run: svn checkout https://github.com/GrandStreetSupreme/ATCRepo/trunk/supreme
8. when that finishes run: cd supreme
9. When that finishes run: cd
10. When that finishes run: brew install python --fix-missing
11. When that finishes run: easy_install pip
12. When that finishes run: wget https://chromedriver.storage.googleapis.com/2.28/chromedriver_mac64.zip
13. When that finishes run: brew install unzip
14. When that finishes run: unzip chromedriver_mac64.zip
15. When that finishes run: mv chromedriver /usr/bin
16. When that finishes run: cd supremebot
17. When that finishes run: cd supreme
18. When that finishes run: chmod u+x setup.py
19. When that finishes run: sudo python setup.py
20. When that finishes edit the config.py file to include your path, key and secret
20. After you do that, to run the bot run: python supremebotv2.py

To install it on Linux, follow the same instructions fro the mac tutorial except:
- Do not do step two
- Everytime the word "brew" is used, use "apt-get" instead e.g 'brew install python' becomes 'apt-get install python'
- instead of running what ist says to in step 12, run this: 


wget https://chromedriver.storage.googleapis.com/2.28/chromedriver_linux64.zip
