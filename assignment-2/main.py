import time
from functions import *

def load_data(filename):
	# Each line in the file represents a transaction.
	# Each transaction consists of a list of space separated items (represented by an integer).
	with open (filename, "r") as f:
		transactions = [list(map(int, line.strip().split(" "))) for line in f]
	return transactions

def print_results(apriori_time, generation_time, verbose, s, c, frequent_itemsets, association_rules):
	# Get only the frequent item sets for the results, don't include the support values
	frequent_itemsets = list(map(lambda x: list(x.keys()), frequent_itemsets))
	itemsets_total = 0

	print(f"Results with a support of {s} and a confidence of {c}:")
	print()

	print("Frequent itemsets:")
	print(f"Found frequent itemsets in: {apriori_time} seconds")
	print()
	for i in range(len(frequent_itemsets)):
		num_frequent = len(frequent_itemsets[i])
		itemsets_total += num_frequent
		print(f"Found {num_frequent} frequent itemsets of length {i+1}")
		if verbose:
			print(frequent_itemsets[i])
			print()
	print(f"Total number of frequent itemsets found: {itemsets_total}")
	print()

	print("Association rules:")
	print(f"Generated association rules in: {generation_time} seconds")
	print()
	for rule in association_rules:
		antecedent, consequent, confidence = rule[0], rule[1], rule[2]
		print(f"{antecedent} → {consequent} (confidence: {confidence})")
	print()
	print(f"Total number of association rules found: {len(association_rules)}")


# Combine the functions and run the program on a dataset of sales transactions.
if __name__ == "__main__":
	# Parameters
	transactions = load_data("data/transactions.dat")
	verbose = True
	# A typical s is 1% of the baskets, i.e. an item is frequent if it appears in > 1% of the baskets
	s = round(0.01 * len(transactions))
	c = 0.5

	# A priori algorithm to find frequent itemsets
	start = time.time()
	frequent_itemsets = a_priori_algorithm(s, transactions)
	end = time.time()
	apriori_time = round(end-start, 2)

	# Generate association rules from frequent itemsets
	start = time.time()
	association_rules = generate_association_rules(c, frequent_itemsets)
	end = time.time()
	generation_time = round(end-start, 5)

	# Print the results
	print_results(apriori_time, generation_time, verbose, s, c, frequent_itemsets, association_rules)
