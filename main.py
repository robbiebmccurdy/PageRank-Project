import sys
import numpy as np
import pandas as pd

# Checking to see if the command line arguements to call the program are correct, if not we will break the program and give an error message

if len(sys.argv) != 3:
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
else:
	print("File checks passed. Starting program...")

# PART 1

# SECTION A

# Grabs the file names from the arguements and reads the csv files, stores them in their own variables

nodeFile = pd.read_csv(sys.argv[1], header=None).values.flatten()
nodeFile = np.delete(nodeFile, 0)
edgeFile = pd.read_csv(sys.argv[2], skiprows=1, header=None) # Skips the first row to avoid having Strings in the array
edgeArray = edgeFile.values
print(edgeArray)

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

# Printing Link Matrix with the formatting requested

print("\nLink Matrix: \n")
for row in linkMatrix:
    formatted_row = ", ".join(["{:.2f}".format(val) for val in row])
    print(formatted_row)



print("\nSuccessfully read files.")
print("\nQuitting program...")