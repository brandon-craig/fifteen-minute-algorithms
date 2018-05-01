def mergeSortCombine(sortedListOfNumbersA, sortedListOfNumbersB):
	# If sortedListOfNumbersA is empty, we dont need to do anything since combining
	# an empty list with a non-empty list just yields the non-empty list back
	if len(sortedListOfNumbersA) == 0:
		return sortedListOfNumbersB

	# Same concept as above. If sortedListOfNumbersB is empty, we don't need to do
	# anything so we just return sortedListOfNumbersA
	if len(sortedListOfNumbersB) == 0:
		return sortedListOfNumbersA

	# indexA and indexB where we are within each of the two lists as we iterate over them
	indexA = 0
	indexB = 0

	# mergedListOfNumbers is our list containing the merged numbers of both lists
	mergedListOfNumbers = []

	# Here is the meat of the combine step. The idea here is simple. You have two sorted piles of
	# numbers and you want create a third pile that is also sorted that contains the numbers of
	# the original piles. You look at top, smallest, number of each pile. You pick the smallest number
	# of the two and put that number into the third pile. Now one of your piles has one less number and
	# we repeat this process until of the piles is empty. 
	while indexA < len(sortedListOfNumbersA) and indexB < len(sortedListOfNumbersB):
		if sortedListOfNumbersA[indexA] <= sortedListOfNumbersB[indexB]:
			mergedListOfNumbers.append(sortedListOfNumbersA[indexA])
			indexA += 1
		else:
			mergedListOfNumbers.append(sortedListOfNumbersB[indexB])
			indexB += 1

	# Now that one of our piles is empty, we need to take the remaining numbers from the
	# pile that is not empty and add them to the end of our third pile. Since the numbers
	# from the remaining pile are already sorted, we simple just append them to the end of
	# our third pile. We find which pile still has numbers left over by figuring out which
	# pile did not break us out of the while loop from above.
	if indexA < len(sortedListOfNumbersA):
		remainingNumbers = sortedListOfNumbersA[indexA:]
		mergedListOfNumbers.extend(remainingNumbers)
	else:
		remainingNumbers = sortedListOfNumbersB[indexB:]
		mergedListOfNumbers.extend(remainingNumbers)

	# We have completed the merge so now we just need to return
	return mergedListOfNumbers
