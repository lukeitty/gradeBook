grades = [[76, 78, 82, 67, 88, 83],
		  [88, 92, 95, 73, 91, 77],
		  [85, 77, 93, 99, 95, 91],
		  [99, 99, 98, 97, 99, 98],
		  [67, 77, 30, 18, 73, 75]]
		  


def average_student(grades):
	
	averageList = []
	
	for row in grades:
		totalAverages = 0
		
		for item in row:
			totalAverages = totalAverages + item
		
		totalAverages = totalAverages / 6
		averageList.append(totalAverages)
	
	return averageList


def total_averages(grades):
	
	averageList = []
	totalAverages = 0
	
	for row in grades:
		for item in row:
			totalAverages = totalAverages + item
		
	totalAverages = totalAverages / 30
	averageList.append(totalAverages)

	return averageList


############################# ----- MAIN PROGRAM ----- #############################


print("The averages of each student is: {}".format(average_student(grades)))
print("The total average of every student is: {}".format(total_averages(grades)))
