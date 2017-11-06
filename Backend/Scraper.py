#Here is a short variables list
# - inCompletance - current task that is worked on.
# - taskAmount - amount of tasks

from bs4 import BeautifulSoup
import requests

def updatePage():
    #here we scrape all code of frontend page
    url = ("growie.com.ua/id0001/")
    r = requests.get("http://" + url)
    data = r.text
    soup = BeautifulSoup(data, "html5lib")
    return soup

def updateTask():
    newSoup = updatePage()
    #check the number of current milestone
    link = newSoup.find_all('div', {'id': 'content'})
    inCompletance = str(link[0].contents)
    inCompletance = inCompletance[38:-22]
    print('The task is: ' + inCompletance)
    return inCompletance


def findTasksNumber():
    newSoup = updatePage()
    #find the amount of milestones
    link = newSoup.find_all('div', {'id': 'tasks'})
    taskAmount = str(link[0].contents)
    taskAmount = taskAmount[38:-22]
    print("Tasks amount: " + taskAmount)
    return taskAmount
