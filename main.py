import sys

# Checking to see if the program was called correctly with the correct arguments
=======
import pandas as pd
>>>>>>> main
>>>>>>> Stashed changes

if len(sys.argv) != 3:
	print("Incorrect amount of arguments. Please only input the program name, the node.csv, and edge.csv file in the command line argument when calling this program.")
	sys.exit()
elif ".csv" not in sys.argv[1] or ".csv" not in sys.argv[2]:
	print("Please enter the correct file format (.csv) ")
	sys.exit()
elif "node" not in sys.argv[1]:
	print("Incorrect file! Please put the node.csv file first.")
	sys.exit()
elif "edge" not in sys.argv[2]:
	print("Incorrect file! Please put the edge.csv file second.")
	sys.exit()
else:
	print("File checks passed. Starting program...")

print("\nFirst File: ")
print(sys.argv[1])
print("\nSecond File: ")
print(sys.argv[2])

nodes = len(nodeFile)

print("Node file: \n")
print(nodeFile.read())
print("\nEdge file: \n")
print(edgeFile.read())

print("\nSuccessfully read files.")
print("\nQuitting program...")