##create a program that will allow you to enter events organizable by hour. There must be menu options of some form, and you must be able to easily
##edit, add, and delete events without directly changing the source code.
##(note that by menu i dont necessarily mean gui. as long as you can easily access the different options and receive prompts and instructions telling you
##how to use the program, it will probably be fine)

class EventMenu(object):
    def __init__(self):
        self.events = []
    def addEvent(self, details, time):
        if time not in range(0,23):
            print("Invalid time. Time must be an integer, and an hour in a 24 hour clock.")
        else:
            self.events.append([details, time])
            print(details + " at " + str(time) + " has been created.")
            self.sortEvents()
    def deleteEvent(self, index):
        self.events.pop(index - 1)
        print("Event has been deleted.")
    def editEventDetails(self, index, details):
        self.events[index - 1][0] = details
        print("Event details have been edited to " + details)
    def editEventTime(self, index, time):
        if time not in range(1,23):
            print("Invalid time. Time must be an integer, and an hour in a 24 hour clock.")
        else:
            self.events[index - 1][1] = time
            print("Event time has been edited to " + str(time))
    def sortEvents(self):
        for times in range(len(self.events)):
            for event in range(len(self.events) - 1):
                if self.events[event][1] > self.events[event + 1][1]:
                    hold = self.events[event]
                    self.events[event] = self.events[event + 1]
                    self.events[event + 1] = hold
    def __str__(self):
        for event in range(len(self.events)):
            print(str(event + 1) + ": " + self.events[event][0] + " at " + str(self.events[event][1]))
    def getEvents(self):
        for event in range(len(self.events)):
            print(str(event + 1) + ": " + self.events[event][0] + " at " + str(self.events[event][1]))

menu = EventMenu()
menu.addEvent("Wake up", 6)
menu.addEvent("Sleep", 21)
menu.addEvent("Breakfast", 6)
menu.addEvent("Lunch", 12)
menu.addEvent("Dinner", 18)
menu.addEvent("Work", 7)
menu.addEvent("Stop work", 17)
menu.getEvents()
menu.deleteEvent(3)
menu.deleteEvent(4)
menu.editEventTime(2, 5)
menu.editEventTime(4, 19)
menu.getEvents()

user = EventMenu()
print("A new blank menu has been created.")
while True:
    action = input("What to do?\nOptions:\n1) Quit\n2) Get Events\n3) Add Event\n4) Edit Event Details\n5) Edit Event Time\n6) Delete Event\nAction: ")
    if action == "1":
        break
    elif action == "2":
        user.getEvents()
    elif action == "3":
        details = input("Enter details. ")
        time = int(input("Enter time. "))
        user.addEvent(details, time)
    elif action == "4":
        index = int(input("Enter index. "))
        details = input("Enter details. ")
        user.EditEventDetails(index, details)
    elif action == "5":
        index = int(input("Enter index. "))
        time = int(input("Enter time. "))
        user.EditEventDetails(index, time)
    elif action == "6":
        index = int(input("Enter index. "))
        user.deleteEvent(index)
