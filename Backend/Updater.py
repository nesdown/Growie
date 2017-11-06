import Scraper as scraper
import time, datetime

#this will update tasks amount each 5 days
launchDate = datetime.datetime.now().day
print('The date is: ' + str(launchDate))

#get tasksAmount
allTasks = scraper.findTasksNumber()
print('An amount of tasks is: ' + allTasks)

#get current task on launch
previousTask = scraper.updateTask()

while(True):
    currentTask = scraper.updateTask()
    if not(currentTask == previousTask):
        print('The task has changed from ' + previousTask + ' to ' + currentTask)
        previousTask = currentTask

    #and here we update the task
    currentDate = datetime.datetime.now().day
    launchDelta = int(currentDate) - int(launchDate)
    print('Delta between dates is: ' + str(launchDelta))

    if launchDelta / 10 == 0:
        allTasks = scraper.findTasksNumber()

    time.sleep(2)
