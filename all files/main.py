import datetime
import pyttsx3
import random

engine  = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


hour = datetime.datetime.now().hour
minute = datetime.datetime.now().minute
h1 = str(minute)
h2 = len(h1)

f = open("user_task.txt", "r")
was = f.read()
data = was.split(",")
data.remove("")


def start():
    f = open("newupd.txt", "r")
    var = f.readline()
    f.close()
    up = int(var)
    print("Your work is", data[int(up)])
    print("can we start this work ?")
    check = input("Press [y/n]")
    check = check.lower()
    if "y" in check:
        print("Your work started.....")
        speak("Your     work     started..")
        var = open("current_task.txt", "a")
        var.write(str(data[up]))
        var.write(",")
        var.close()
        # minute check
        if h2 == 1:
            start_time = str(hour) + str(0) + str(minute)
        else:
            start_time = str(hour) + str(minute)
        var = open("timeline.txt", "w")
        var.write(start_time)
        var.write("\n")
        var.close()
        f = open("logicse.txt", "w")
        var = f.write("1")
        f.close()

    else:
        print("Okay do it as soon as possible")
        speak("do it     as   soon as possible")


def end():
    f = open("newupd.txt", "r")
    var = f.readline()
    f.close()
    up = int(var)

    print("WORK STATUS:",data[up])
    print("Have you completed your task? [y/n]")
    check1 = input(">>")
    check1 = check1.lower()
    if "y" in check1:
        print("You completed the task")
        words = ["Perfect", "Amazing", "Great", "Well done"]
        a = random.randint(0, 3)
        speak(words[a])
        speak("You   completed    the    task....")
        # update files
        f = open("newupd.txt", "r")
        var1 = f.readline()
        f.close()
        up = int(var1)
        up1 = up + 1
        f = open("newupd.txt", "w")
        var = f.write(str(up1))
        f.write("\n")
        f.close()

        # Start time - completed time
        var = open("timeline.txt", "r")
        f = var.readline()
        if h2 == 1:
            t2 = str(hour) + str(0) + str(minute)
        else:
            t2 = str(hour) + str(minute)
        # -----------------------------------------
        g = open("timeline.txt", "r")
        var = g.readline()
        t3 = (abs(int(var) - int(t2)))


        # Store time corresponding to order
        f = open("time_taken.txt", "a")
        var = f.writelines(str(t3))
        var = f.writelines(",")
        f.close()
        f = open("logicse.txt", "w")
        var = f.write("0")
        f.close()



    else:
        print("Then do it fast..")





if __name__ == '__main__':
    f = open("logicse.txt", "r")
    var = f.read()
    f.close()
    if var == "1":
        end()

    else:
        try:
            start()
        except Exception as e:
            print("You completed all the task")
            print("press enter to continue....")
            u  = input(">>")
            f = open("current_task.txt", "r")
            var = f.read()
            task = var.split(",")
            task.remove("")
            n1 = len(task)

            f = open("time_taken.txt", "r")
            var = f.readline()
            f.close()
            timings = var.split(",")
            timings.remove("")  # list of timings


            def sort(timings, task):
                for i in range(len(timings) - 1, 0, -1):
                    for j in range(i):
                        if timings[j] > timings[j + 1]:
                            temp = timings[j]
                            temp1 = task[j]
                            timings[j] = timings[j + 1]
                            task[j] = task[j + 1]
                            timings[j + 1] = temp
                            task[j + 1] = temp1


            sort(timings, task)
            # Our aim is task2
            f = open("Learned_data.txt", "w")
            for i in task:
                f.write(i)
                f.write(",")
            f.close()

            # Transfer learned data to user task
            f = open("Learned_data.txt", "r")
            var1 = f.read()
            f.close()

            f = open("user_task.txt", "w")
            f.write(var1)
            f.close()

            # makenewup to 0
            f = open("newupd.txt", "w")
            var = f.write("0")
            f.close()

            g = open("time_taken.txt", "r+")
            g.truncate(0)
            g.close()

            g = open("current_task.txt", "r+")
            g.truncate(0)
            g.close()

            f = open("logicse.txt", "w")
            d3 = f.write("0")
            f.close()
            print("Do you want to continue with [AI recommended task] or [new task] ")
            print("press (1 for AI) or (2 for New task) ")
            user_enters = int(input(">>"))
            if user_enters == 1:
                print("turtle")
            elif user_enters == 2:
                print("user input")


            exit()
