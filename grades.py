"""import courses
classesList = []
for i in range(0,courses.List_Of_Courses.numPeriods):
    classesList.append(courses.List_Of_Courses.listOfClasses[i])
print(classesList)
#important
#to access the class name, use c["class"], and so on and so forth

#THIS PIECE OF CODE PRINTS EVERY CLASS, TYPE, and GRADE!!!
#for c in classesList:
    #print(str.format("Class: {} Type: {} Grade: {}",c["class"],c["type"],c["numberGrade"]))

def convertNumberGrades():
    for c in classesList:
        #Checks if the type of class is level I, II, or III
        if (c["type"] == "Honors GT") or (c["type"] == "Honors") or (c["type"] == "Level III"):
            #maxing
            #each if statement checks the grade value
            if c["numberGrade"] >= 96.5:
                c["letterGrade"] = "A+"
                c["gpaGrade"] = 5.5 
                print(c["class"] + ": " + str(c["gpaGrade"]))

            elif c["numberGrade"] >= 93.5 and c["numberGrade"] < 96.5:
                c["letterGrade"] = "A"
                c["gpaGrade"] = 5.3 
                print(c["class"] + ": " + str(c["gpaGrade"]))

            elif c["numberGrade"] >= 89.5 and c["numberGrade"] < 93.5:
                c["letterGrade"] = "A-"
                c["gpaGrade"] = 5.1
                print(c["class"] + ": " + str(c["gpaGrade"]))

            elif c["numberGrade"] >= 86.5 and c["numberGrade"] < 89.5:
                c["letterGrade"] = "B+"
                c["gpaGrade"] = 4.9
                print(c["class"] + ": " + str(c["gpaGrade"]))

            elif c["numberGrade"] >= 83.5 and c["numberGrade"] < 86.5:
                c["letterGrade"] = "B"
                c["gpaGrade"] = 4.7 
                print(c["class"] + ": " + str(c["gpaGrade"]))

            elif c["numberGrade"] >= 79.5 and c["numberGrade"] < 83.5:
                c["letterGrade"] = "B-"
                c["gpaGrade"] = 4.5 
                print(c["class"] + ": " + str(c["gpaGrade"]))

            elif c["numberGrade"] >= 76.5 and c["numberGrade"] < 79.5:
                c["letterGrade"] = "C+"
                c["gpaGrade"] = 4.3 
                print(c["class"] + ": " + str(c["gpaGrade"]))

            elif c["numberGrade"] >= 73.5 and c["numberGrade"] < 76.5:
                c["letterGrade"] = "C"
                c["gpaGrade"] = 4.1 
                print(c["class"] + ": " + str(c["gpaGrade"]))

            elif c["numberGrade"] >= 70.5 and c["numberGrade"] < 73.5:
                c["letterGrade"] = "C-"
                c["gpaGrade"] = 3.9 
                print(c["class"] + ": " + str(c["gpaGrade"]))
            
            elif c["numberGrade"] >= 70 and c["numberGrade"] < 70.5:
                c["letterGrade"] = "D"
                c["gpaGrade"] = 3.7 
                print(c["class"] + ": " + str(c["gpaGrade"]))

            elif c["numberGrade"] < 70:
                c["letterGrade"] = "F"
                c["gpaGrade"] = 0.0
                print(c["class"] + ": " + str(c["gpaGrade"]))
                
        if (c["type"] == "Normal") or (c["type"] == "Regular") or (c["type"] == "Level II"):
            #maxing
            if c["numberGrade"] >= 96.5:
                c["letterGrade"] = "A+"
                c["gpaGrade"] = 5.0 
                print(c["class"] + ": " + str(c["gpaGrade"]))

            elif c["numberGrade"] >= 93.5 and c["numberGrade"] < 96.5:
                c["letterGrade"] = "A"
                c["gpaGrade"] = 4.8 
                print(c["class"] + ": " + str(c["gpaGrade"]))

            elif c["numberGrade"] >= 89.5 and c["numberGrade"] < 93.5:
                c["letterGrade"] = "A-"
                c["gpaGrade"] = 4.6
                print(c["class"] + ": " + str(c["gpaGrade"]))

            elif c["numberGrade"] >= 86.5 and c["numberGrade"] < 89.5:
                c["letterGrade"] = "B+"
                c["gpaGrade"] = 4.4
                print(c["class"] + ": " + str(c["gpaGrade"]))

            elif c["numberGrade"] >= 83.5 and c["numberGrade"] < 86.5:
                c["letterGrade"] = "B"
                c["gpaGrade"] = 4.2 
                print(c["class"] + ": " + str(c["gpaGrade"]))

            elif c["numberGrade"] >= 79.5 and c["numberGrade"] < 83.5:
                c["letterGrade"] = "B-"
                c["gpaGrade"] = 4.0 
                print(c["class"] + ": " + str(c["gpaGrade"]))

            elif c["numberGrade"] >= 76.5 and c["numberGrade"] < 79.5:
                c["letterGrade"] = "C+"
                c["gpaGrade"] = 3.8
                print(c["class"] + ": " + str(c["gpaGrade"]))

            elif c["numberGrade"] >= 73.5 and c["numberGrade"] < 76.5:
                c["letterGrade"] = "C"
                c["gpaGrade"] = 3.6 
                print(c["class"] + ": " + str(c["gpaGrade"]))

            elif c["numberGrade"] >= 70.5 and c["numberGrade"] < 73.5:
                c["letterGrade"] = "C-"
                c["gpaGrade"] = 3.4 
                print(c["class"] + ": " + str(c["gpaGrade"]))
            
            elif c["numberGrade"] >= 70 and c["numberGrade"] < 70.5:
                c["letterGrade"] = "D"
                c["gpaGrade"] = 3.2 
                print(c["class"] + ": " + str(c["gpaGrade"]))

            elif c["numberGrade"] < 70:
                c["letterGrade"] = "F"
                c["gpaGrade"] = 0.0
                print(c["class"] + ": " + str(c["gpaGrade"]))
        
        if (c["type"] == "AP") or (c["type"] == "IB") or (c["type"] == "Level IV"):
            #maxing
            if c["numberGrade"] >= 96.5:
                c["letterGrade"] = "A+"
                c["gpaGrade"] = 6.0 
                print(c["class"] + ": " + str(c["gpaGrade"]))

            elif c["numberGrade"] >= 93.5 and c["numberGrade"] < 96.5:
                c["letterGrade"] = "A"
                c["gpaGrade"] = 5.8
                print(c["class"] + ": " + str(c["gpaGrade"]))

            elif c["numberGrade"] >= 89.5 and c["numberGrade"] < 93.5:
                c["letterGrade"] = "A-"
                c["gpaGrade"] = 5.6
                print(c["class"] + ": " + str(c["gpaGrade"]))

            elif c["numberGrade"] >= 86.5 and c["numberGrade"] < 89.5:
                c["letterGrade"] = "B+"
                c["gpaGrade"] = 5.4
                print(c["class"] + ": " + str(c["gpaGrade"]))

            elif c["numberGrade"] >= 83.5 and c["numberGrade"] < 86.5:
                c["letterGrade"] = "B"
                c["gpaGrade"] = 5.2
                print(c["class"] + ": " + str(c["gpaGrade"]))

            elif c["numberGrade"] >= 79.5 and c["numberGrade"] < 83.5:
                c["letterGrade"] = "B-"
                c["gpaGrade"] = 5.0
                print(c["class"] + ": " + str(c["gpaGrade"]))

            elif c["numberGrade"] >= 76.5 and c["numberGrade"] < 79.5:
                c["letterGrade"] = "C+"
                c["gpaGrade"] = 4.8 
                print(c["class"] + ": " + str(c["gpaGrade"]))

            elif c["numberGrade"] >= 73.5 and c["numberGrade"] < 76.5:
                c["letterGrade"] = "C"
                c["gpaGrade"] = 4.6 
                print(c["class"] + ": " + str(c["gpaGrade"]))

            elif c["numberGrade"] >= 70.5 and c["numberGrade"] < 73.5:
                c["letterGrade"] = "C-"
                c["gpaGrade"] = 4.4 
                print(c["class"] + ": " + str(c["gpaGrade"]))
            
            elif c["numberGrade"] >= 70 and c["numberGrade"] < 70.5:
                c["letterGrade"] = "D"
                c["gpaGrade"] = 4.2 
                print(c["class"] + ": " + str(c["gpaGrade"]))

            elif c["numberGrade"] < 70:
                c["letterGrade"] = "F"
                c["gpaGrade"] = 0.0
                print(c["class"] + ": " + str(c["gpaGrade"]))
convertNumberGrades()
#def periodDisplayer(period):
    #print(classesList[period-1])
#periodDisplayer(1)


def get_grade_and_gpa(number_grade, scale):
    Given a number grade and scale, return the letter grade and GPA.
    # Define grade ranges for each class type scale
    grade_ranges = [
        (96.5, 'A+', scale[0]),
        (93.5, 'A', scale[1]),
        (89.5, 'A-', scale[2]),
        (86.5, 'B+', scale[3]),
        (83.5, 'B', scale[4]),
        (79.5, 'B-', scale[5]),
        (76.5, 'C+', scale[6]),
        (73.5, 'C', scale[7]),
        (70.5, 'C-', scale[8]),
        (70, 'D', scale[9]),
        (0, 'F', 0.0)
    ]
    
    for lower, letter_grade, gpa in grade_ranges:
        if number_grade >= lower:
            return letter_grade, gpa

def convertNumberGrades():
    # Define GPA scales for different class types
    scales = {
        "Honors GT": [5.5, 5.3, 5.1, 4.9, 4.7, 4.5, 4.3, 4.1, 3.9, 3.7],
        "Honors": [5.5, 5.3, 5.1, 4.9, 4.7, 4.5, 4.3, 4.1, 3.9, 3.7],
        "Level III": [5.5, 5.3, 5.1, 4.9, 4.7, 4.5, 4.3, 4.1, 3.9, 3.7],
        "Normal": [5.0, 4.8, 4.6, 4.4, 4.2, 4.0, 3.8, 3.6, 3.4, 3.2],
        "Regular": [5.0, 4.8, 4.6, 4.4, 4.2, 4.0, 3.8, 3.6, 3.4, 3.2],
        "Level II": [5.0, 4.8, 4.6, 4.4, 4.2, 4.0, 3.8, 3.6, 3.4, 3.2],
        "AP": [6.0, 5.8, 5.6, 5.4, 5.2, 5.0, 4.8, 4.6, 4.4, 4.2],
        "IB": [6.0, 5.8, 5.6, 5.4, 5.2, 5.0, 4.8, 4.6, 4.4, 4.2],
        "Level IV": [6.0, 5.8, 5.6, 5.4, 5.2, 5.0, 4.8, 4.6, 4.4, 4.2]
    }
    
    for c in classesList:
        class_type = c["type"]
        
        if class_type in scales:
            # Get the appropriate GPA scale based on class type
            scale = scales[class_type]
            
            # Get letter grade and GPA for the number grade
            letter_grade, gpa_grade = get_grade_and_gpa(c["numberGrade"], scale)
            
            # Assign grade and GPA to the class
            c["letterGrade"] = letter_grade
            c["gpaGrade"] = gpa_grade
            
            # Print the result
            print(f"{c['class']}: {gpa_grade}")

# Example classesList for testing
classesList = [
    {"class": "Math", "type": "Honors GT", "numberGrade": 95},
    {"class": "History", "type": "Normal", "numberGrade": 88},
    {"class": "Science", "type": "AP", "numberGrade": 91}
]

convertNumberGrades()




grades = []
def averageMaintainer(goal=70):
    goal = float(input("What is your goal grade? "))
    while True:
        try:
            grade = input("Enter your grades (Type 'Q' if you're done or 'R' if you would like to reenter the previous grade): ")
            if grade != 'Q' and grade != 'R':
                grades.append(float(grade))
                print(grades)
            elif grade == 'R':
                grades.pop()
                #removes the last entered grade and goes to start of loop
            elif grade == 'Q':
                sumGrades = sum(grades)
                numGrades = len(grades)
                average = sumGrades / numGrades
                print("Your average is:", average)
                neededGrade = (((goal*numGrades) + goal) - sumGrades) 
                neededGrade = round(neededGrade,3) 
                # this sets the equation of: goal = sumGrades + neededGrade / numGrades + 1
                # and puts it in terms of neededGrade!
                if neededGrade > 100:
                    print(f"To average a {goal} in the class, you need at least a {neededGrade} on the next assignment.\n Unfortunately, you can't hit your goal, but make sure to try your best!")
                    break
                else:
                    print(f"To average a {goal} in the class, you need at least a {neededGrade} on the next assignment.\
                        You can do this!")
                    break
        except:
            #if the user doesn't enter anything at all, this will print
            #if the user enters an invalid type (e.g. string) this will print
            #if the user does anything that they're not supposed to, this will print!!
            print("Please enter a valid grade!")

averageMaintainer()

def update_html_element(element_id, content):
       from js import document
       element = document.getElementById(element_id)
       element.textContent = content"""
from js import document

# Example classesList
classesList = [
    {"class": "Math", "type": "Honors GT", "numberGrade": 95},
    {"class": "History", "type": "Normal", "numberGrade": 88},
    {"class": "Science", "type": "AP", "numberGrade": 91},
    {"class": "PE", "type": "Normal", "numberGrade": 98},
]

def get_grade_and_gpa(number_grade, scale):
    """Given a number grade and scale, return the letter grade and GPA."""
    grade_ranges = [
        (96.5, 'A+', scale[0]),
        (93.5, 'A', scale[1]),
        (89.5, 'A-', scale[2]),
        (86.5, 'B+', scale[3]),
        (83.5, 'B', scale[4]),
        (79.5, 'B-', scale[5]),
        (76.5, 'C+', scale[6]),
        (73.5, 'C', scale[7]),
        (70.5, 'C-', scale[8]),
        (70, 'D', scale[9]),
        (0, 'F', 0.0)
    ]

    for lower, letter_grade, gpa in grade_ranges:
        if number_grade >= lower:
            return letter_grade, gpa

def convert_number_grades():
    scales = {
        "Honors GT": [5.5, 5.3, 5.1, 4.9, 4.7, 4.5, 4.3, 4.1, 3.9, 3.7],
        "Normal": [5.0, 4.8, 4.6, 4.4, 4.2, 4.0, 3.8, 3.6, 3.4, 3.2],
        "AP": [6.0, 5.8, 5.6, 5.4, 5.2, 5.0, 4.8, 4.6, 4.4, 4.2],
    }

    for c in classesList:
        class_type = c["type"]
        if class_type in scales:
            scale = scales[class_type]
            letter_grade, gpa_grade = get_grade_and_gpa(c["numberGrade"], scale)
            c["letterGrade"] = letter_grade
            c["gpaGrade"] = gpa_grade

def update_html():
    """Update the HTML elements with the data."""
    for i, c in enumerate(classesList, start=1):
        document.getElementById(f"class-{i}").textContent = c["class"]
        document.getElementById(f"grade-{i}").textContent = f"Grade: {c['letterGrade']}"
        document.getElementById(f"GPA-{i}").textContent = f"GPA: {c['gpaGrade']}"

# Initialize data and update HTML
convert_number_grades()
update_html()






