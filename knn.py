import numpy as np
import operator

''' 
	The tile function creates a new n dimensional array using the 2 input
	parameters. For example tile(inp, (2, 1)) uses the inp array and makes 2
	rows by 1 column of the original array, so if original is [1, 2] the tile 
	function above would output [[1, 2], [1, 2]]

	The sum function sums all items in a specified direction such as all values
  in a row or all values in a column. Axis=1 sums rows, Axis=0 sums columns.

	The dictionary.get() function provides the key and a defualt if not present.

	The argsort() function places the index of the value in its place so this
  allows for looking up the correct position in the label vector.
'''

def classifyKnn(inp, dataSet, labels, k):
	dataSetRows = dataSet.shape[0]
	diffMat = np.tile(inp, (dataSetRows, 1)) - dataSet
	sqDiffMat = diffMat ** 2
	sqDistances = sqDiffMat.sum(axis=1)
	distances = sqDistances**0.5
	sortedDistIndicies = distances.argsort()
	classCount = {}
	for i in range(k):
		voteIlabel = labels[sortedDistIndicies[i]]
		classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
	sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
	return sortedClassCount[0][0]

def file2matrix(filename, numFeatures):
	fr = open(filename)
	numberOfLines = len(fr.readlines())
	returnMat = np.zeros((numberOfLines, numFeatures))
	classLabelVector = []

	index = 0
	fr = open(filename)
	for line in fr.readlines():
		line = line.strip()
		listFromLine = line.split('\t')
		returnMat[index, :] = listFromLine[0:numFeatures]
		classLabelVector.append(int(listFromLine[-1]))
		index = index + 1
	fr.close()
	return returnMat, classLabelVector

def autoNorm(data):
	min_vals  = data.min(0)
	max_vals  = data.max(0)
	ranges 	  = max_vals - min_vals
	norm_data = np.zeros(np.shape(data))
	m = data.shape[0]
	norm_data = data - np.tile(min_vals, (m, 1))
	norm_data = norm_data / np.tile(ranges, (m, 1))
	return norm_data, ranges, min_vals

mat, labels = file2matrix('./playerstats.txt', 3)
test_input = np.array([[24.0, 9.0, 12.0]])

mat = np.append(mat, test_input, axis=0)
mat, ranges, min_vals = autoNorm(mat)

test_input_norm = mat[-1, :]
mat = mat[:-1, :]


print(classifyKnn(test_input_norm, mat, labels, 5))
