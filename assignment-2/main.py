from collections import defaultdict
from itertools import combinations
import time

# A-Priori algorithm for finding frequent itemsets with support at least s in a dataset of sales transactions.
# The support of an itemset is the number of transactions containing the itemset.
def a_priori_algorithm(s, transactions):
	res = []
	# First pass
	# item_counts stores all unique items in the data along with their counts
	candidate_singletons = defaultdict(int)
	for transaction in transactions:
		for item in transaction:
			candidate_singletons[item] += 1

	# Determine which items are frequent as singletons
	frequent_items = filter_candidates(candidate_singletons, s)
	# frequent_items now contains all frequent singletons along with their counts
	frequent_singletons = [item for item in frequent_items.keys()]
	res.append(frequent_singletons)

	# k pass
	k = 1
	while True:
		k += 1
		frequent_ks = apriori_pass(transactions, frequent_items, k, s)
		if len(frequent_ks) == 0:
			break
		else:
			frequent_ks = [item for item in frequent_ks.keys()]
			res.append(frequent_ks)

	return res

# Find frequent itemsets of length k from existing frequent itemsets
def apriori_pass(transactions, frequent_items, k, s):
	candidate_ks = defaultdict(int)
	for basket in transactions:
		basket_freqs = []
		for item in basket:
			if item in frequent_items:
				basket_freqs.append(item)
		# Generate all unique combinations of length k from the basket
		k_items = list(combinations(basket_freqs, k))
		for item in k_items:
			candidate_ks[item] += 1
	frequent_ks = filter_candidates(candidate_ks, s)
	return frequent_ks

# Filter out all candidate items that are not frequent according to the support threshold
def filter_candidates(candidates, s):
	to_delete = []
	for item, count in candidates.items():
		if count < s:
			to_delete.append(item)
	for item in to_delete:
		del candidates[item]
	return candidates


# Algorithm for generating association rules between frequent itemsets discovered using
# the A-Priori algorithm in a dataset of sales transactions.
# The rules must have the support of at least s and confidence of at least c.
def generate_association_rules(s, c, itemsets):
	pass


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
	# print("Association rules:")
	# for rule in association_rules:
		# print(rule)
	# print()

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
	frequent_itemsets = a_priori_algorithm(s, transactions)
	end = time.time()
	print(f"A priori algorithm finished in: {round(end-start, 2)} seconds")

	# Generate association rules from frequent itemsets
	association_rules = generate_association_rules(s, c, frequent_itemsets)

	# Print the results
	print_results(verbose, s, c, frequent_itemsets)
