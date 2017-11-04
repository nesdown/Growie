#Here is a short variables list
# - inCompletance - current task that is worked on.

from bs4 import BeautifulSoup
import time
import lightBlinks
import requests

ledColors = "purple"
milPreviousState = "Current Milestone Number: 1"
maxMilestones = 20

#here we scrap all code of frontend page
url = ("localhost/growie/id0001/")
r = requests.get("http://" + url)
data = r.text
soup = BeautifulSoup(data, "html5lib")


#check the number of current milestone
link = soup.find_all('div', {'id': 'content'})
inCompletance = str(link[0].contents)
print(inCompletance)
inCompletance = inCompletance[38:-22]
print('The task is: ' + inCompletance)

#find the amount of milestones
yeah = soup.find_all('div', {'class': 'fw-wizard-step'})
print(yeah[len(yeah) - 1])
#milAmount = str(link[0])
#milAmount = milAmount[25:-10]
#print('\n' + 'The amount is: ' + milAmount)

#if (task == "Project#1"):
#   ledColors = "purple"
#elif (task == "Project#2"):
#    ledColors = "green"
#else:
#    ledColors = "red"
#    lightBlinks.errorCode()

#Checkout of updates
#milState = soup.findAll('div')
#milState = str(milState[2])
#milState = milState[39:44]
#print("Current milsetone: " + milState)

#if not(milState == milPreviousState):
#    curProgress = int(milState[:1])
#    #check if the task is completed
#    if (curProgress == maxMilestones):
#        lightBlinks.endProject()
#    else:
#        lightBlinks.newMilestone(curProgress)