num_of_classes = int(input("Enter the total number of classs:"))
att_classes = int(input("Enter the number of classes attended by student:"))
per = (att_classes/num_of_classes)*100
if per>=75:
    print("The student can attend the exam")
else:
    print("The student cannot attend the exam")
print("The attendance percentage is",per,"%")

