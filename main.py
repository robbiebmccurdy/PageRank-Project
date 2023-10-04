import sys
import numpy as np
import pandas as pd
import csv

# FUNCTIONS

def dampMatrix(nNodes, matrixA, dampValue):
	# Creating Matrix S
	
	matrixS = np.ones((nNodes, nNodes)) / nNodes

	print("\nMatrix S:\n")
	print(matrixS)

	# Calculating Matrix M

	matrixM = (dampValue[0] * matrixA) + ((1 - dampValue[0]) * matrixS)

	with open('modlinkmatrix.csv', 'w', newline='') as file:
	    # Write the number of nodes at the beginning of the file
	    file.write(f"{nNodes}, {dampValue[0]}\n")

	    # Use np.savetxt to append the matrix below the number of nodes, formatted to two decimal places
	    np.savetxt(file, matrixM, delimiter=",", fmt="%.2f")

	return matrixM

def simplePageRank(nodesFile, edgesArray, d, max_iterations):
	# Grabbing amount of nodes
	nodes = len(nodesFile)

	# Creating Page Rank Vector
	rankVector = np.ones(nodes) / nodes

	# Creating graph matrix
	graphMatrix = np.zeros((nodes, nodes))

	# Making edge connection values equal 1 in our matrix

	for k, l in edgesArray:
		if l == 0:
			graphMatrix[l, k] = 1
		else:
			graphMatrix[l - 1, k - 1] = 1

	outgoingSum = np.sum(graphMatrix, axis=0)

	for i in range(max_iterations):
		newRankVector = (1 - d[0]) / nodes * np.ones(nodes)

		for j in range(nodes):
			incomingSum = np.sum(rankVector * graphMatrix[j, :] / outgoingSum)

			newRankVector[j] += d[0] * incomingSum

		rankVector = newRankVector

	return rankVector

def computeEigen(matrix):
	# Compute the eigenvalues and eigenvectors
	eigenValues, eigenVectors = np.linalg.eig(matrix)

	# Find index of eigenvalue closest to 1
	idx = np.abs(eigenValues - 1).argmin()

	# Return the corresponding eigenvector
	return eigenVectors[:, idx]

# Checking to see if the command line arguements to call the program are correct, if not we will break the program and give an error message

if len(sys.argv) > 4 or len(sys.argv) < 3:
	print("ERROR: Incorrect amount of arguments. Please only input the program name, the node.csv, and edge.csv file in the command line argument when calling this program.")
	sys.exit()
elif ".csv" not in sys.argv[1] or ".csv" not in sys.argv[2]:
	print("ERROR: Please enter the correct file format (.csv) ")
	sys.exit()
elif "node" not in sys.argv[1]:
	print("ERROR: Incorrect file! Please put the node.csv file first.")
	sys.exit()
elif "edge" not in sys.argv[2]:
	print("ERROR: Incorrect file! Please put the edge.csv file second.")
	sys.exit()
elif "d.csv" not in sys.argv[3]:
	print("ERROR: Incorrect file! Please put the d.csv file third.")
	sys.exit()
else:
	print("File checks passed. Starting program...")

# PART 1

# SECTION A

print("\nPart 1, Section A starting...\n")

# Grabs the file names from the arguements and reads the csv files, stores them in their own variables

nodeFile = pd.read_csv(sys.argv[1], header=None).values.flatten()
nodeFile = np.delete(nodeFile, 0)
edgeFile = pd.read_csv(sys.argv[2], skiprows=1, header=None) # Skips the first row to avoid having Strings in the array
edgeArray = edgeFile.values
dFile = pd.read_csv(sys.argv[3], header=None).values.flatten() # Grabbing this for later use in 1b

# Grabs the length of our nodes file (n) and then creates a blank matrix that is size (n x n)

nodes = len(nodeFile)
linkMatrix = np.zeros((nodes, nodes)) 

# Iterates through the array grabbed from the edges csv file then inserts them into a link matrix

for i, j in edgeArray:
	if j == 0:
		linkMatrix[j,i] += 1
	else:
		linkMatrix[j-1,i-1] += 1

# Sums the columns and divides the values in the columns by the sum of the columns 
# (basically if we have 0,1 and 0,3 in the edges .csv we fill both of those spots with a 1, then later we divide them by 2 giving us 0.50)

col_sums = linkMatrix.sum(axis=0, keepdims=True)
col_sums[col_sums == 0] = 1
linkMatrix = linkMatrix / col_sums

# Writing to linkmatrix.csv

# Save to CSV with requested formatting
with open('linkmatrix.csv', 'w', newline='') as file:
    # Write the number of nodes at the beginning of the file
    file.write(f"{nodes}\n")

    # Use np.savetxt to append the matrix below the number of nodes, formatted to two decimal places
    np.savetxt(file, linkMatrix, delimiter=",", fmt="%.2f")

print("\nPart 1, Section A finished...")

# SECTION B

print("\nPart 1, Section B starting...\n")

mMatrix = dampMatrix(nodes, linkMatrix, dFile)

print("\nPart 1, Section B finished...\n")

# PART 2

# SECTION A

iterations_list = [0, 1, 2, 4, 8, 16, 32, 50]

with open("pagerankiterations.csv", "w") as f:
    for iters in iterations_list:
        rankVector = simplePageRank(nodeFile, edgeArray, dFile, iters)
        
        # Write the result to the file
        f.write(f"Iteration {iters}\n")
        f.write(str([round(rank, 3) for rank in rankVector]))
        f.write("\n\n")  # Adding extra newlines for separation

print("\nPart 2, Section A finished...\n")

# PART 3

# SECTION A

eigenA = computeEigen(linkMatrix)

eigenM = computeEigen(mMatrix)

with open('eigenvectors.csv', 'w') as file:
	pass

# Write eigenvector for A
with open('eigenvectors.csv', 'a') as file:
    file.write("Eigenvector for A corresponding to eigenvalue 1:\n")
    formatted_vector_A = ", ".join(["{:.6f}".format(val) for val in eigenA])
    file.write(formatted_vector_A + "\n\n")

# Write eigenvector for M
with open('eigenvectors.csv', 'a') as file:
    file.write("Eigenvector for M corresponding to eigenvalue 1:\n")
    formatted_vector_M = ", ".join(["{:.6f}".format(val) for val in eigenM])
    file.write(formatted_vector_M + "\n\n")

print("\nSuccessfully read files.")
print("\nQuitting program...")