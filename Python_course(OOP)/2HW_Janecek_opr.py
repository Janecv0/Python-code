# Parsing function
# Made by Vojtěch Janeček
# 05.10.2022


data = {
    "students": ["Adam Levine", "Monica Muller", "John Deere", "John Deere", "John Deere", "Thomas Garrigue Masaryk","John Deere"],
    "active": [True, False, True, True, True, True, True]
}
def unique_usernames(data:dict):
    # grabs list of student from data dict
    all_studenst = data["students"]
    # grabs list of activity from data dict
    activity = data["active"]

    # number of letters used in nicks
    num_sur = 5
    num_name = 3

    # prepartation od lists
    active_students = []
    active_real = []
    active_student_num = []
    username = []


    # function makes usernames based on name, surname and order, works "only" for 100 users with same name, else return error
    def username_maker(name, surname, num):
        username = ""

        if num == 0:
            for n in range(num_sur):
                username += surname[n]

            for n in range(num_name):
                username += name[n]

        elif num in range(10):

            for n in range(num_sur):
                username += surname[n]

            for n in range(num_name - 1):
                username += name[n]

            username += str(num)

        elif num in range(100):

            for n in range(num_sur - 1):
                username += surname[n]

            for n in range(num_name - 1):
                username += name[n]

            username += str(num)

        else:
            raise NotImplementedError("Error: Too many users with same name")

        return username.lower()


    # check if all students have activity status
    if len(all_studenst) != len(activity):
        print("Students and their activity isn\'t same lenght.")

    else:
        # picks active students and adds them to new active student list
        for i in range(len(all_studenst)):
            if activity[i] == True:
                active_students.append(all_studenst[i])
                active_real.append(activity[i])
                active_student_num.append(0)

        for i in range(len(active_students)):
            # finds position of duplicates
            pos_dupl = [n for n, x in enumerate(active_students) if x == active_students[i]]

            # based on found duplicates changes value on duplicant list
            if len(pos_dupl) != 1:
                for n in range(len(pos_dupl)):
                    active_student_num[pos_dupl[n]] = n

        #splits name (can be longer than two words) and takes first and last word, calls function
        for i in range(len(active_students)):
            student_full_name = active_students[i].split(" ")

            username.append(username_maker(student_full_name[0], student_full_name[-1], active_student_num[i]))

    result = {"students": active_students,
              "active": active_real,
              "usernames": username
              }
    return result


print(unique_usernames(data))
