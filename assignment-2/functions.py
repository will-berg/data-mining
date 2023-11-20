from collections import defaultdict
from itertools import combinations

# Subproblem 1

# A-Priori algorithm for finding frequent itemsets with support at least s in a dataset of sales transactions.
def a_priori_algorithm(s, transactions):
	# list of dictionaries (key for each frequent itemset of length k, value for the corresponding support)
	res = []
	# First pass, scan the transactions and count the occurrences of each item
	candidate_singletons = defaultdict(int)
	for transaction in transactions:
		for item in transaction:
			candidate_singletons[item] += 1

	# Determine which items are frequent as singletons
	frequent_items = filter_candidates(candidate_singletons, s)
	res.append(frequent_items)

	# k:th pass, start at 2 since we already did the first pass
	k = 2
	while True:
		frequent_ks = apriori_pass(transactions, frequent_items, k, s)
		# If no frequent itemsets of length k were found, monotonicity tells us we are done
		if len(frequent_ks) == 0:
			break
		else:
			res.append(frequent_ks)
			k += 1
	return res

# Find frequent itemsets of length k from existing frequent itemsets
def apriori_pass(transactions, frequent_items, k, s):
	candidate_ks = defaultdict(int)
	for basket in transactions:
		# Only consider items of the basket that are frequent
		basket_freqs = []
		for item in basket:
			if item in frequent_items:
				basket_freqs.append(item)
		# Generate all unique combinations of frequent items of length k from the basket
		k_items = list(combinations(basket_freqs, k))
		for item in k_items:
			candidate_ks[item] += 1
	frequent_ks = filter_candidates(candidate_ks, s)
	return frequent_ks

# Filter out all candidate items that are not frequent according to the support threshold
def filter_candidates(candidates, s):
	return dict(filter(lambda x: x[1] >= s, candidates.items()))

# Subproblem 2

# Algorithm for generating association rules, of support and confidence larger than s and c,
# between frequent itemsets discovered using the A-Priori algorithm.
def generate_association_rules(c, frequent_itemsets):
	association_rules = []
	for k in range(1, len(frequent_itemsets)):
		# Go through the possible rules for each frequent itemset and filter for confidence
		# E.g. possible rules for (39, 704): (39) → (704), (704) → (39), according to the book
		for itemset in frequent_itemsets[k]:
			n = len(itemset)
			itemset = list(itemset)
			for j in range(n):
				temp = itemset.copy()
				removed = temp.pop(j)
				temp = temp[0] if len(temp) == 1 else tuple(temp)
				confidence = round(frequent_itemsets[k][tuple(itemset)] / frequent_itemsets[k-1][temp], 2)
				if confidence >= c:
					rule = (temp, removed, confidence)
					association_rules.append(rule)
	return association_rules
