from collections import defaultdict
from itertools import combinations


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
	res.append(frequent_items)

	# k pass
	k = 1
	while True:
		k += 1
		frequent_ks = apriori_pass(transactions, frequent_items, k, s)
		if len(frequent_ks) == 0:
			break
		else:
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
	return dict(filter(lambda x: x[1] >= s, candidates.items()))


# Algorithm for generating association rules between frequent itemsets discovered using
# the A-Priori algorithm in a dataset of sales transactions.
# The rules must have support of at least s and confidence of at least c.
def generate_association_rules(s, c, frequent_itemsets):
	# frequent_itemsets is a list of dictionaries where each dictionary has a key for each frequent itemset of length k and a value for the support of that itemset
	pass
