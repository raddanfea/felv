
student = "Béla"
subject = "Advanced Puppy Hugging"
grades = []
num_of_grades = 3

print(student)
print(subject)


while len(grades) != num_of_grades:
    grade = eval(input(f"Enter Grade {len(grades)+1}/{num_of_grades} "))
    if type(grade) is int:
        if 0 <= grade <= 100:
            grades.append(grade)
        else:
            print("Invalid grade! 0-100")
    else:
        print("Invalid grade type! 0-100")

print("Sum:", sum(grades))
avg = float("{:.2f}".format(sum(grades)/len(grades)))
print("Average", avg)
if avg >= 70:
    print("A grade")
elif avg >= 50:
    print("B grade")
elif avg > 35:
    print("C grade")
else:
    print("Failing grade!")

