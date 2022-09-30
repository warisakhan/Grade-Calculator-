# I received no asistance on this assignment that violates the ethical guidelines set forth by the professor and the class syllabus 
#function to remove lowest grades 
def drop_one(grades):
    finaldrop = []
    found = 0
    for i in range(len(grades)):
        if grades[i] == min(grades) and found == 0:
            found = 1
            continue
        else:
            finaldrop.append(grades[i])
    return finaldrop
    

#function two - finding overall reading score - done
def wreadings(grades, drop = 0):
    weight = 10
    count = 0
    #removing the lowest items using drop_one function
    for i in range(drop):
        grades = drop_one(grades)
        #adding rest of the numbers togtehter to find average and weighted score 
    for i in range(len(grades)):
        count += grades[i]
    finalgrade = count / ((len(grades)))
    finalgrade /= weight
    finalgrade *= .05
    finalgrade *= 100
    finalgrade = round(finalgrade, 2)
    return finalgrade
#print(wreadings([10,9,8,9]))
#print(wreadings([7,6,9,9,2,3,6,7,0,9,8,1], 2))

# function three - finding overall labs score -done
def wlabs (grades, drop = 0):
	weight = 10
	count = 0
	#using drop_one function to find lowest grades 
	for i in range(drop):
		grades = drop_one(grades)
	for i in range(len(grades)):
		count += grades[i]
	final_labs = count / ((len(grades)))
	final_labs /= weight
	final_labs *= .10
	final_labs *= 100
	final_labs = round(final_labs, 2)
	return final_labs
#print(wlabs([5,8,0], 2))
#print(wlabs([6,7,0,0,0,10,9]))

# function four - finding overall programming assingment scores - done
def wPAs(grades, drop = 0):
	weight = 50
	count = 0 
	# using drop_one function to remove the lowest grades 
	for i in range(drop):
		grades = drop_one(grades)
	for i in range(len(grades)):
		count += grades[i]
	final_PAs = count / ((len(grades)))
	final_PAs /= weight
	final_PAs *= .40
	final_PAs *= 100
	final_PAs = round(final_PAs, 2)
	return final_PAs
#print(wPAs([40, 10, 35, 5], 1))
#print(wPAs([30, 20, 50]))

# function five - finding overall exams score - done
def wexams(mt1 = 100, mt2 = 100, fe = 250):
	mt_weight = 100
	fe_weight = 250
	# creating a new list to add all values for exams 
	final_exams = []
	# finding weighted score for midterm 1 
	mt1 /= mt_weight
	mt1 *= .10
	mt1 *= 100
	mt1 = round(mt1, 2)
	#adding to list
	final_exams.append(mt1)
	# finding weighted score for midterm 2
	mt2 /= mt_weight
	mt2 *= .10
	mt2 *= 100
	mt2 = round(mt2, 2)
	# adding to list 
	final_exams.append(mt2)
	#finding weighted score for final exam 
	fe /= fe_weight
	fe *= .25
	fe *= 100
	fe = round(fe, 2)
	# adding to list 
	final_exams.append(fe)
	return final_exams
#print(wexams(mt2 = 70))
#print(wexams(45, fe = 100))
#print(wexams())



# function one - final overall grade
def finalGrade(readings, labs, PAs, mt1 = 100, mt2 = 100, fe = 250):
	# calling the readings function 
	readingscore = 0
	#reading function has two parameters, need to include to call properly 
	if len(readings) == 2:
		readingscore = wreadings(readings[0], readings[1])
	else:
		readingscore = wreadings(readings[0], drop = 0)

	# calling the labs function
	labscore = 0
	# reading function has two parameters, need to include to call properly 
	if len(labs) == 2:
		labscore = wlabs(labs[0], labs[1])
	else:
		labscore = wlabs(labs[0], drop = 0)

	#calling the programming function 
	pa_score = 0
	# programming function has two parameters, need to include to call properly 
	if len(PAs) == 2:
		pa_score = wPAs(PAs[0], PAs[1])
	else:
		pa_score = wPAs(PAs[0], drop = 0)

        #adding all of the items from the exams list to the final grade by retreving them individually
	examscore = 0 
	examslist = wexams(mt1, mt2, fe)
	for i in range(len(examslist)):
		examscore += examslist[i]
		#adding together all of the scores to get final grade 
	finalgrade = readingscore + labscore + pa_score + examscore

        #rounded score that will be used for the final grade 
	totalscore = round(finalgrade)
	#finding the letter grade 
	letter_grade = ""
	if finalgrade >= 98.0:
		letter_grade = 'A+'
	elif finalgrade >= 92.0 and finalgrade < 98.0:
		letter_grade = 'A'
	elif finalgrade >= 90.0 and finalgrade < 92.0:
		letter_grade = 'A-'
	elif finalgrade >= 88.0 and finalgrade < 90.0:
		letter_grade = 'B+'
	elif finalgrade >= 82.0 and finalgrade < 88.0:
		letter_grade = 'B'
	elif finalgrade >= 80.0 and finalgrade < 82.0:
		letter_grade = 'B-'
	elif finalgrade >= 78.0 and finalgrade < 80.0:
		letter_grade = 'C+'
	elif finalgrade >= 72.0 and finalgrade < 78.0:
		letter_grade = 'C'
	elif finalgrade >= 70.0 and finalgrade < 72.0:
		letter_grade = 'C-'
	elif finalgrade >= 60.0 and finalgrade < 70.0:
		letter_grade = 'D'
	elif finalgrade < 60.0:
		letter_grade = 'F'
	final = (totalscore, letter_grade)
	return final 
#print(finalGrade([[10,9,8,9]], [[5,8,0], 2], [[40, 10, 35, 5], 1], mt2 = 70))


