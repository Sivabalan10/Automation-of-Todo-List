def user():
    print("press enter to submit your task")
    global routine
    routine = [0]
    while True:
        user = input(">>")
        if user == "":
            break
        else:
            routine.append(user)
    routine.remove(0)
    print(routine)
    global sx
    sx = len(routine)
    print(sx)
    var = open("user_task.txt", "w")
    var.write(routine[0])
    var.write(",")
    var.close()
    i = 1
    while (i < sx):
        var = open("user_task.txt", "a")
        var.write(routine[i])
        var.write(",")
        var.close()
        i = i + 1
    print("Data is successfully stored..")
    print("Restart the program")
