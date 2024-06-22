
def class_of_students(arrival_times,threshold):
    return class_of_students
arrival_times=input("Enter the integers representing arrival times(non-positive integer indicates on-time arrival): ")
threshold=input("Enter the minimum no of students that should be present in the class: ")

for i in arrival_times:
    if (i<threshold):
        print("Class Cancelled: YES")
        break

    else:
        print("Class Cancelled: NO")
        break
