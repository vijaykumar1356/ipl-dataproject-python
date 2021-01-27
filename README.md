# _dataproject-python_
## **IPL Data Analytics**
The data for this exercise is sourced from [Kaggle](https://www.kaggle.com/manasgarg/ipl/version/5). you can follow this link and find 1. deliveries.csv 2. matches.csv files and can download them individually.
* click this link for two csv files in a zip format [csv files zip](https://www.kaggle.com/manasgarg/ipl/download) 

### 1. Settip up the Environment for the project
* make sure that you have Python 3.x in your machine and pip(Python Package Manager) is installed. If not follow this command
  * `sudo apt install python3-pip` 
* Create a folder named  "dataproject-python"
* Open Command Line your Machine and go to that Directory using command 'cd' (ex: `cd Desktop/python/dataproject-python`)
* Clone the repository using the command
  * `git clone git@gitlab.com:mountblue/cohort-14-python/vijay_yarramsetty/dataproject-python.git`
* After cloning the repository, while being in the same directory where you cloned the remote repository. use the following command for setting up a virtual environment.
  * `pip install virtualenv` - it installs virtualenv package if it is not there already
  * `virtualenv env_name` here you can name anything in the place of 'env_name'
  * Now the Virtual Environment is created and we have to activate it with the help of following command
    * `source env_name/bin/activate`
  * now to install the Python Dependencies for executing the Project use the following command. 
  * `pip install -r requirements.txt` 
  * now the Environment setup is complete

### 2. Context of the Exercise
1. The 1st problem should fetch the total runs scores by each team in the course of IPL hisory from the given CSV file and plot chart of Team vs Total Runs scored on Matplotlib Module.
2. The 2nd problem should plot the top 15 Batsmen over the course of IPL History exclusively scored runs for Royal Challengers Bangalore
3. The 3rd problem is about obtaining the country of origin of foreign umpires from external sources and plot a chart of country vs number of umpires represented in IPL.
4. The 4th Problem is plotting a stacked chart of matches played by all teams participated over the course of IPL History separated by season. 
### 3. Executing the project
1. We have total 4 individual questions to solve using the data of IPL statistics from Season 1 to Season 10. 
2. Before getting into executing the problems, there is a bug in the downloaded `deliveries.csv` file where team 'Rising Pune Supergiants' is wrongly spelt in an entire season as 'Rising Pune Supergiant' so, the data is being separated into two container whenever we process it with the help of team name. so I fixed it using file `fixing_bug.py`. run this file from the virtual environment, It will generate new `deliveries_new.csv` file in the project directory that we are going to use.
3. Also, we need to source Umpire's 'country of origin' for all the Non Indian Umpires who participated in the matches. This has been web scraped using `scrape_umpires.py`. So when you run this file from command line `umpires_nation.csv` file will be generated in the same Project Directory.
4. in order to view the solution your interest of question number just execute the `main.py` file which displays the "Question Set" and asks you to enter a question number for solution, it then calls that function and displays the bar chart of particular qustion.
5. Or you can directly run a question by executing particular question from command line. It will show the result.
 

