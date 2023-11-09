import numpy as np

# Documents location
corpus = "documents/"

# Functions for the different stages
"""
Constructs and returns a set of hashed k-shingles for a given document
1. shingling constructs k-shingles of a given length k from a given document.
2. Computes a hash value for each unique shingle.
3. Represents the document in the form of an ordered set of its hashed k-shingles.
"""
def shingling(document, k=10):
	res = set()
	with open(corpus + document, "r") as f:
		doc = f.read()
		for i in range(len(doc) - k):
			shingle = doc[i:i+k]
			res.add(hash(shingle))
	return res

"""
compare_sets computes the Jaccard similarity of two sets of integers - two sets of hashed shingles S and T.
"""
def compare_sets(S, T):
	return len(S.intersection(T)) / len(S.union(T))

"""
minhashing builds a minHash signature (in the form of a vector or a set) of a given length n
from a given set of integers (a set of hashed shingles S). Should ideally return numpy array.
"""
def minhashing(S, n=100):
	pass

"""
compare_signatures estimates the similarity of two integer vectors - minhash signatures -
as a fraction of components in which they agree.
"""
def compare_signatures(v, w):
	return np.sum(v == w) / len(v)


# Run the program
if __name__ == "__main__":
	# Go through the stages
	S = shingling("israel-1.txt")
	T = shingling("israel-2.txt")

	# Jaccard similarity of the sets of hashed shingles
	jaccard_sim = compare_sets(S, T)

	# Minhashing the sets of hashed shingles
	signature_S = minhashing(S, n)
	signature_T = minhashing(T, n)

	# Similarity of the minhash signatures, estimate of the Jaccard similarity
	signature_sim = compare_signatures(signature_S, signature_T)

	# Support threshold
	s = 0.8

	if jaccard_sim >= s:
		print("The documents are similar.")

