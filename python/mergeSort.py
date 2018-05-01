def mergeSortCombine(sortedListOfNumbersA, sortedListOfNumbersB):
	if len(sortedListOfNumbersA) == 0:
		return sortedListOfNumbersB

	if len(sortedListOfNumbersB) == 0:
		return sortedListOfNumbersA

	indexA = 0
	indexB = 0
	mergedListOfNumbers = []

	while indexA < len(sortedListOfNumbersA) and indexB < len(sortedListOfNumbersB):
		if sortedListOfNumbersA[indexA] <= sortedListOfNumbersB[indexB]:
			mergedListOfNumbers.append(sortedListOfNumbersA[indexA])
			indexA += 1
		else:
			mergedListOfNumbers.append(sortedListOfNumbersB[indexB])
			indexB += 1

	if indexA < len(sortedListOfNumbersA):
		remainingNumbers = sortedListOfNumbersA[indexA:]
		mergedListOfNumbers.extend(remainingNumbers)
	else:
		remainingNumbers = sortedListOfNumbersB[indexB:]
		mergedListOfNumbers.extend(remainingNumbers)

	return mergedListOfNumbers

def mergeSort(listOfNumbers):
	if len(listOfNumbers) <= 1:
		return listOfNumbers

	middleIndex = len(listOfNumbers) // 2

	leftHalf = listOfNumbers[:middleIndex]
	rightHalf = listOfNumbers[middleIndex:]

	sortedLeftHalf = mergeSort(leftHalf)
	sortedRightHalf = mergeSort(rightHalf)

	return mergeSortCombine(sortedLeftHalf, sortedRightHalf)
