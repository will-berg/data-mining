import numpy as np
import sympy
import string
from collections import defaultdict

corpus = "text_files/"

# Functions for the different stages
# Constructs and returns a set of hashed k-shingles for a given document
def shingling(document, k):
	res = set()
	with open(corpus + document, "r") as f:
		doc = preprocess(f.read())
		for i in range(len(doc) - k):
			shingle = doc[i:i+k]
			res.add(hash(shingle))
	return res

# Prepare a document (text string) for shingling
def preprocess(text):
	return text.translate(str.maketrans("", "", string.punctuation)).lower().replace("\n", " ")


# Computes the Jaccard similarity of two sets of integers - two sets of hashed shingles "S" and "T"
def compare_sets(S, T):
	return round(len(S.intersection(T)) / len(S.union(T)), 2)


# Builds a minHash signature (integer vector) of length "n" from a set of hashed shingles "S"
def minhashing(S, n=100):
	hash_funcs = generate_hash_functions(n)

	signature = np.full(n, np.inf)
	# Represents set "S" by the n values of h_min(S) for the n hash functions
	for shingle in S:
		for i in range(n):
			# Hash function from slides
			hash_value = hash_funcs[i](shingle)
			signature[i] = np.minimum(signature[i], hash_value)

	return signature

# Generate n different hash functions for minhashing
def generate_hash_functions(n=100):
	c = sympy.nextprime(2**32-1)
	a, b = np.linspace(1, c, n), np.linspace(1, c, n)
	return [lambda x, a=a[i], b=b[i], c=c: (a * x + b) % c for i in range(n)]


# Estimates the similarity of two integer vectors (minhash signatures) "v" and "w"
def compare_signatures(v, w):
	assert len(v) == len(w)
	return np.sum(v == w) / len(v)


# Implements the LSH technique: given a collection of minhash signatures and a similarity threshold "t",
# lsh finds candidate pairs of signatures and calculates their signature similarity
def lsh(signatures, t):
	candidates = defaultdict(set)
	# Split the signatures into bands, represent each band as a tuple for hashing
	for document, signature in signatures.items():
		bands = [tuple(band) for band in np.array_split(signature, 50)]
		# Hash each band and add the document to the corresponding bucket
		for band in bands:
			candidates[hash(band)].add(document)
	# Find candidate pairs among documents that have at least one band hashed to the same bucket
	candidate_pairs = set()
	for documents in candidates.values():
		bucket_size = len(documents)
		if bucket_size >= 2:
			documents = list(documents)
			for i in range(bucket_size):
				for j in range(i+1, bucket_size):
					if (documents[j], documents[i]) not in candidate_pairs:
						candidate_pairs.add((documents[i], documents[j]))

	# Calculate the signature similarity of the candidate pairs
	res = []
	for pair in candidate_pairs:
		if compare_signatures(signatures[pair[0]], signatures[pair[1]]) >= t:
			res.append(pair)
	return res

if __name__ == "__main__":
	# Test shingling and minhash
	S = shingling("aliceinwonderland.txt", 10)
	T = shingling("dracula.txt", 10)

	print("Jaccard similarity of aliceinwonderland and dracula:", compare_sets(S, T))
	print("Minhash similarity of aliceinwonderland and dracula:", compare_signatures(minhashing(S), minhashing(T)))
