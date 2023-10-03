import sys
import pandas as pd

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

nodeFile = pd.read_csv(sys.argv[1])
edgeFile = pd.read_csv(sys.argv[2])

nodes = len(nodeFile)

print("\nNodes: ", nodes)

print("\nSuccessfully read files.")
print("\nQuitting program...")