def mergeSort(listOfNumbers):
	# If the list of numbers has 0 or 1 items we dont need to do anything
	# so just return the list back
	if len(listOfNumbers) <= 1:
		return listOfNumbers

	# We find where the middle of the list of numbers is
	# by dividing the length of the list by 2
	middleIndex = len(listOfNumbers) // 2

	# We are dividing the list of numbers into two halves which I
	# am calling leftHalf and rightHalf, respectively. 
	leftHalf = listOfNumbers[:middleIndex]
	rightHalf = listOfNumbers[middleIndex:]

	# Here we recusively call mergeSort on the left and right halves
	# of the original list of numbers
	mergeSort(leftHalf)
	mergeSort(rightHalf)