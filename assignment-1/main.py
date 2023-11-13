import os
import sys
import time
from functions import *

# Command line arguments, lsh, verbose, and support threshold
def handle_cli_args():
	try:
		if len(sys.argv) < 2 or len(sys.argv) > 4:
			raise Exception

		if sys.argv[1] == "lsh":
			mode = "lsh"
		elif sys.argv[1] == "jaccard":
			mode = "jaccard"
		elif sys.argv[1] == "minhash":
			mode = "minhash"
		else:
			raise Exception

		if len(sys.argv) > 2 and sys.argv[2] == "verbose":
			verbose = True
		elif len(sys.argv) > 2 and sys.argv[2] == "no-verbose":
			verbose = False
		else:
			raise Exception

		if len(sys.argv) > 3 and float(sys.argv[3]) >= 0 and float(sys.argv[3]) <= 1:
			s = float(sys.argv[3])
		else:
			raise Exception

		return mode, verbose, s
	except:
		print("ERROR! Usage: python main.py [lsh|jaccard|minhash] [verbose|no-verbose] [THRESHOLD]")
		exit()

# Run the program
if __name__ == "__main__":
	mode, verbose, s = handle_cli_args()
	n = 100
	k = 10
	# Documents to compare
	documents = os.listdir(corpus)

	# If the minhash signatures and the shingle sets have already been computed, load them
	if os.path.exists("signatures.npy") and os.path.exists("shingle_sets.npy"):
		signatures = np.load("signatures.npy", allow_pickle=True)
		shingle_sets = np.load("shingle_sets.npy", allow_pickle=True)
	# Else, compute them
	else:
		# Shingling the documents
		shingle_sets = []
		for document in documents:
			shingle_sets.append(shingling(document, k))

		# Minhashing the sets of hashed shingles
		signatures = []
		for shingle_set in shingle_sets:
			signatures.append(minhashing(shingle_set))

		# Save the minhash signatures and the shingle sets so I don't have to recompute them
		np.save("signatures.npy", signatures)
		np.save("shingle_sets.npy", shingle_sets)

	# LSH
	if mode == "lsh":
		start = time.time()
		signatures = dict(zip(documents, signatures))
		candidate_similarity = lsh(signatures, s)
		if verbose:
			for pair in candidate_similarity:
				print("Signature similarity of", pair[0], "and", pair[1], ":", compare_signatures(signatures[pair[0]], signatures[pair[1]]))
			print()
		print("Similar documents (LSH signature similarity):")
		for pair in candidate_similarity:
			print(pair[0], "and", pair[1])

		lsh_time = round(time.time() - start, 5)
		print()
		print("LSH time:", lsh_time, "seconds")
	# Jaccard
	elif mode == "jaccard":
		# Jaccard similarity of the sets of hashed shingles
		start = time.time()
		jaccard_similar_documents = []
		for i in range(len(documents)):
			for j in range(i+1, len(documents)):
				jaccard_sim = compare_sets(shingle_sets[i], shingle_sets[j])
				if verbose:
					print("Jaccard similarity of", documents[i], "and", documents[j], ":", jaccard_sim)
				if jaccard_sim >= s:
					jaccard_similar_documents.append((documents[i], documents[j]))

		if verbose: print()

		print("Similar documents (Jaccard similarity):")
		for pair in jaccard_similar_documents:
			print(pair[0], "and", pair[1])

		jaccard_time = round(time.time() - start, 5)
		print()
		print("Jaccard time:", jaccard_time, "seconds")
	# Minhash
	else:
		# Similarity of the minhash signatures, estimate of the Jaccard similarity
		start = time.time()
		signature_similar_documents = []
		for i in range(len(documents)):
			for j in range(i+1, len(documents)):
				signature_sim = compare_signatures(signatures[i], signatures[j])
				if verbose:
					print("Signature similarity of", documents[i], "and", documents[j], ":", signature_sim)
				if signature_sim >= s:
					signature_similar_documents.append((documents[i], documents[j]))

		if verbose: print()

		# Print the similar documents
		print("Similar documents (signature similarity):")
		for pair in signature_similar_documents:
			print(pair[0], "and", pair[1])

		minhash_time = round(time.time() - start, 5)
		print()
		print("Minhash time:", minhash_time, "seconds")
