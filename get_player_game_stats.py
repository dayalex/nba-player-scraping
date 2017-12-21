import player
import team
from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
import os

def readFromCSV(teamName):
    #Reads from organized CSV file and saves data to variables and objects
    with open(os.path.dirname(os.path.realpath(__file__))+'/'+'player_stats.csv', 'r') as fp:
        counter = 0
        statCounter = 0
        reader = csv.reader(fp, delimiter=',')
        rowCount = 0
        for row in reader:
            if(rowCount>15):
                if all(x.isalpha()==False for x in row[0]):
                    stats.append(row[0])
                else:
                    if(row[0] == "Totals"):
                        break
                    playerNames.append(row[0])
            rowCount+=1
    fp.close()


def writeToCSV(teamName):
    #Scrapes web data to a csv file
    with open(os.path.dirname(os.path.realpath(__file__))+'/'+'player_stats.csv', 'wt') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=' ', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
        for stats in all_td:
            if stats.string is None:
                player = stats.find("a")
                # html padding to find player names
                filewriter.writerow(player.text.split())
                #append column here
            if stats.string is not None:
                filewriter.writerow(stats.string.split())

    csvfile.close()


def getFullTeamName(teamName):
    #Uses given team location name and finds its full team name
    for count in range(len(teamLocations)):
        if(teamName == teamLocations[count]):
            return teamFullNames[count]
            

#Load given file with team names to choose from
locations = open(os.path.dirname(os.path.realpath(__file__))+"/"+"team_names.txt",'r')
locTxt = locations.read()
print(locTxt)
locations.close()

#Team locations are its abbreviated name in url
teamLocations = []
#Full team name useful for user reading information
teamFullNames = []
CONST_STATSIZE = 14
teams = []
teamNames = []

with open(os.path.dirname(os.path.realpath(__file__))+'/'+'team_names.txt', 'r') as fp:
    reader = csv.reader(fp, delimiter=' ')
    for row in reader:
        teamLocations.append(row[0])
with open(os.path.dirname(os.path.realpath(__file__))+'/'+'team_list.txt', 'r') as fp:
    reader = csv.reader(fp, delimiter=' ')
    for row in reader:
        teamFullNames.append(row[0])
        # print("teamfullnames: ",teamFullNames)


#Choose as many teams as the user wants
loc = input("Choose a team location from above:")
teamNames.append(loc)
while(loc!=""):
    loc = input("Choose another team or hit enter to stop choosing teams:")
    if(loc!=""):
        teamNames.append(loc)
#Iterates through each team name chosen
for i in range(len(teamNames)):
    playerNames = []
    players = []
    stats = []
    #Store multiple team objects in a dynamic array
    teams.append(team.team(teamNames[i]))
    site = "http://www.espn.com/nba/team/stats/_/name/"+teamNames[i]+"/"+""     #Last part of url isn't necessary
    #Scrape player data from espn with current team chosen
    page = urlopen(site)
    soup = BeautifulSoup(page, "html.parser")

    all_tr = soup.find_all("tr")
    sub_td = 0
    all_td = soup.find_all("td")
    #write to csv file
    writeToCSV(teamNames[i])
    # read off of newly built csv file with all necessary data
    readFromCSV(teamNames[i])

    #Build an array of player objects
    for a in range(len(playerNames)):
        x = player.player(playerNames[a])
        players.append(x)

    #Set each players stats
    playerCount = 0
    for statCount in range(0,len(stats),CONST_STATSIZE):
        players[playerCount].setStats(stats[statCount+0], stats[statCount+1],stats[statCount+2],stats[statCount+3],stats[statCount+4],stats[statCount+5],stats[statCount+6],stats[statCount+7],stats[statCount+8],stats[statCount+9],stats[statCount+10],stats[statCount+11],stats[statCount+12],stats[statCount+13])
        if(statCount%CONST_STATSIZE==0):
            playerCount+=1
    #Set the current team object to hold an array of player objects. Each team object holds an array of player objects, respectively.
    teams[i].setPlayers(players)

#variables for storing highest stats
highestStat = [0]*CONST_STATSIZE
highestTeam = [""]*CONST_STATSIZE
highestPlayer = [""]*CONST_STATSIZE
#Finds which player/team holds the best statistic in each common player statistic with available data from espn
for a in range(len(teams)):
    for b in range(len(teams[a].players)):
        for i in range(CONST_STATSIZE):
            if(float(teams[a].players[b].stats[i])) > highestStat[i]:
                highestStat[i] = float(teams[a].players[b].stats[i])
                highestPlayer[i] = teams[a].players[b].name
                highestTeam[i] = getFullTeamName(teams[a].name)

statNames = ["GP", "GS", "MIN", "PPG", "OFFR", "DEFR", "RPG", "APG", "SPG", "BPG", "TPG", "FPG", "A/TO", "PER"]
for x in range(len(highestStat)):
    #Output best players by statistics of given teams to compare between.
    print(statNames[x],":",highestTeam[x],"-",highestPlayer[x],"-",highestStat[x])