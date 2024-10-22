# A time traveler has suddenly appeared in your classroom!

# Create a variable representing the traveler's
# year of origin (e.g., year = 2000)
# and greet our strange visitor with a different message
# if he is from the distant past (before 1900),
# the present era (1900-2020) or from the far future (beyond 2020).

# year = int(input("Greetings! What is your year of origin?"))

# if year <= 1900:
#     print("Woah, that's the past!")
# elif year > 1900 and year < 2020:
#     print("That's totally the present!")
# else:
#     print("Far out, that's the future!!")




def get_year_of_origin():
    while True:
        try:
            year = int(input("Greetings! What is your year of origin? "))
            return year
        except ValueError:
            print("Invalid input. Please enter a valid number for the year.")

def greet_time_traveler(year):
    if year < 1900:
        print("Woah, that's the past!")
    elif 1900 <= year <= 2020:
        print("That's totally the present!")
    else:
        print("Far out, that's the future!!")
        
def main():
    year = get_year_of_origin()
    greet_time_traveler(year)
    
main()



#Task 2
# Create a collection of these authors and
# the year they kicked the bucket;
# print the collection in the following format:

# Charles Dickens died in 1870.

# Charles Dickens, 1870
# William Thackeray, 1863
# Anthony Trollope, 1882
# Gerard Manley Hopkins, 1889

authrs = {
    "Charles Dickens": 1870,
    "William Thackeray": 1863,
    "Anthony Trollope": 1882,
    "Gerard Manley Hopkins": 1889}
for author, date in authrs.items():
    print(author, " died in ", date)



# Calculating Grades (ok, let me think about this one)

# Write a program that will average 3 numeric exam grades, return an average test score, a corresponding letter grade, and a message stating whether the student is passing.

# Average	Grade
# 90+	A
# 80-89	B
# 70-79	C
# 60-69	D
# 0-59	F

# Exams: 89, 90, 90
# Average: 90
# Grade: A
# Student is passing.

# Exams: 50, 51, 0
# Average: 33
# Grade: F
# Student iis failing.

exam_one = int(input("Input exam grade one: "))

exam_two = int(input("Input exam grade two: "))

exam_three = int(input("Input exam grade three: "))

grades = [exam_one, exam_two, exam_three]
sum = 0
for grade in grades:
  sum += grade

avg = sum / len(grades)

if avg >= 90:
    letter_grade = "A"
elif avg >= 80 and avg < 90:
    letter_grade = "B"
elif avg >= 70 and avg < 80:
    letter_grade = "C"
elif avg >= 60 and avg < 70:
    letter_grade = "D"
else:
    letter_grade = "F"

for grade in grades:
    print("Exam: " + str(grade))

print("Average: " + str(avg))

print("Grade: " + letter_grade)

if letter_grade == "F":
    print("Student is failing.")
else:
    print("Student is passing.")



greeting = input("Hello, possible pirate! What's the password? ")
if greeting == "Arrr!":
	print("Greetings, hater of pirates!")
else:
	print("Go away, pirate.")



currentTimeStr = input("What is the current time (in hours 0-23)? ")
waitTimeStr = input("How many hours do you want to wait? ")

currentTimeInt = int(currentTimeStr)
waitTimeInt = int(waitTimeStr)

finalTimeInt = currentTimeInt + waitTimeInt
print(finalTimeInt)


str_time = input("What time is it now? ")
str_wait_time = input("What is the number of nours to wait? ")
time = int(str_time)
wait_time = int(str_wait_time)

time_when_alarm_go_off = time + wait_time
print(time_when_alarm_go_off)

