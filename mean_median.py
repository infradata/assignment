students = []
fees = []


def enrollment_status(universities):
    for u in universities:
        students.append(u[1])
        fees.append(u[2])

    return students,fees


def mean(total_list):
    mean_value = 0
    length_list = len(total_list)
    for t in total_list:
        mean_value = mean_value + t
    return mean_value/length_list


def median(total_list):
    length_list = len(total_list)
    total_list.sort()
    if length_list % 2 == 0:
        return total_list[length_list / 2]
    else:
        undivided = total_list[int(length_list / 2)] + total_list[int((length_list / 2)-1)]
        return undivided / 2 

universities = [
        ['California Institute of Technology', 2175, 37704],
        ['Harvard', 19627, 39849],
        ['Massachusetts Institute of Technology', 10566, 40732],
        ['Princeton', 7802, 37000],
        ['Rice', 5879, 35551],
        ['Stanford', 19535, 40569],
        ['Yale', 11701, 40500],
    ]
stats = enrollment_status(universities)

print("Total students:   {}".format(sum(stats[0])))
print("Total tuition:  $ {}".format(sum(stats[1])))
print("Student mean:     {}".format(int(mean(stats[0]))))
print("Student median:   {}".format(int(median(stats[0]))))
print("Tuition mean:   $ {}".format(int(mean(stats[1]))))
print("Tuition median: $ {}".format(int(median(stats[1]))))
