# HCI-ColorBlind
Mini project 1 for HCI
Author: Ryan Bell, Sam Woodworth

How To Run:
Step 1: Download and install Python (preferably python 3.7.7 or greater)

Step 2: Install PyGame by using Pip. Open a command prompt and input the below command:
Command: python3 -m pip install -U pygame --user
More info on how to install PyGame here: https://www.pygame.org/wiki/GettingStarted

Step 3: Download 'ColorBlind.py' from this GitHub and place in a location you'll remember (preferably in a new folder on your Desktop)
Link to GitHub here: https://github.com/rrrryyyaan/HCI-ColorBlind

Step 4: Open up your Windows Search bar (pressing 'Windows key' or click the Windows/Search Icon on the bottom right of your screen) and search for 'IDLE', open this Python IDE application. Alternatively, you may be able to find this application where you installed python. This application should have been downloaded when you installed PyGame. If not, you'll have to search the web for a download of IDLE

Step 5: Once you have opened 'IDLE', it will open a Python shell. Simply click 'File' on the top right, then 'Open'

Step 6: Once a file explorer pops up, find where you placed 'ColorBlind.py' and open that file. This will open the python file with the IDLE IDE

Step 7: On your new window, where you opened 'ColorBlind.py' (it'll show the name in the top bar of the application), simply select 'Run', then 'Run Module'. Alternatively, you can just press 'F5' to run the module.

Step 8: The application will load up and the first current bus stop will show up in about 7 seconds. You'll get a message 'You are arriving shortly' when a new current bus stop is about to show up.

Dependencies:
There shouldn't be any other dependencies that you need to download besides the ones that come with Python and PyGame. You should be able to run the application with ease if you have followed the above steps.

How to Use:
As stated in step 8 of the tutorial,, on first startup, the first current bus stop will take about 7 seconds to show up.
When a new current bus stop shows up, simply select the color above that is the same as the 'Current Stop'. If you get it right, your 'Actual Arrival' and 'Delay' will be updated to show you how you did for each bus stop. A new bus stop will show up every 7 seconds! This will run for about 30 bus stops to get a decent amount of data for us to analyze. After you get the complete message, you can simply exit the game.

How to Send Us Your Data:
After completing all 30 stops and exiting the game, you'll notice a 'testResults.csv' file within the same directory that you put 'ColorBlind.py' in. Please send us this file as this is the file we used to collect the data! Again, the data output file should be located within the same directory as 'ColorBlind.py' You can send us the data through Slack
