import time
from functions import *


# Helper functions
def load_data(filename):
	# Each line in the file represents a transaction.
	# Each transaction consists of a list of space separated items (represented by an integer).
	with open (filename, "r") as f:
		transactions = [list(map(int, line.strip().split(" "))) for line in f]
	return transactions

def print_results(verbose, s, c, frequent_itemsets, association_rules=None):
	total = 0
	print(f"Results with a support of {s} and a confidence of {c}:")
	print()
	print("Frequent itemsets:")
	for i in range(len(frequent_itemsets)):
		num_frequent = len(frequent_itemsets[i])
		total += num_frequent
		print(f"Found {num_frequent} frequent itemsets of length {i+1}")
		if verbose:
			print(frequent_itemsets[i])
			print()
	print()
	print("Association rules:")
	for rule in association_rules:
		print(rule)
	print()

	print(f"Total number of frequent itemsets found: {total}")
	# print(f"Number of association rules found: {}")


# Combine the functions and run the program on a dataset of sales transactions.
if __name__ == "__main__":
	# Parameters
	transactions = load_data("data/transactions.dat")
	verbose = False
	# A typical s is 1% of the baskets
	s = round(0.01 * len(transactions))
	c = 0.5

	# A priori algorithm to find frequent itemsets
	start = time.time()
	frequent_itemsets, frequent_items_support = a_priori_algorithm(s, transactions)
	end = time.time()
	print(f"Found frequent itemsets in: {round(end-start, 2)} seconds")

	# Generate association rules from frequent itemsets
	# start = time.time()
	# association_rules = generate_association_rules(s, c, frequent_items_support)
	# end = time.time()
	# print(f"Generated association rules in: {round(end-start, 2)} seconds")
	# print()

	# Print the results
	print_results(verbose, s, c, frequent_itemsets)
