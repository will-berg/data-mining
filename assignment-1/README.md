# Task
You are to implement the stages of finding textually similar documents based on Jaccard similarity using the shingling, minhashing, and locality-sensitive hashing (LSH) techniques and corresponding algorithms. The implementation can be done using any big data processing framework, such as Apache Spark, Apache Flink, or no framework, e.g., in Java, Python, etc. To test and evaluate your implementation, write a program that uses your implementation to find similar documents in a corpus of 5-10 or more documents, such as web pages or emails.

The stages should be implemented as a collection of classes, modules, functions, or procedures depending on the framework and the language of your choice. Below, we describe sample classes implementing different stages of finding textually similar documents. You do not have to develop the exact same classes and data types described below. Feel free to use data structures that suit you best.

1. A class *Shingling* that constructs k–shingles of a given length k (e.g., 10) from a given document, computes a hash value for each unique shingle and represents the document in the form of an ordered set of its hashed k-shingles.
2. A class *CompareSets* computes the Jaccard similarity of two sets of integers – two sets of hashed shingles.
3. A class *MinHashing* that builds a minHash signature (in the form of a vector or a set) of a given length n from a given set of integers (a set of hashed shingles).
4. A class *CompareSignatures* estimates the similarity of two integer vectors – minhash signatures – as a fraction of components in which they agree.
5. (Optional task for extra 2 bonus points) A class *LSH* that implements the LSH technique: given a collection of minhash signatures (integer vectors) and a similarity threshold t, the LSH class (using banding and hashing) finds candidate pairs of signatures agreeing on at least a fraction t of their components.

To test and evaluate your implementation's scalability (the execution time versus the size of the input dataset), write a program that uses your classes to find similar documents in a corpus of 5-10 documents. Choose a similarity threshold s (e.g., 0,8) that states that two documents are similar if the Jaccard similarity of their shingle sets is at least s.

## Implementation


## Running the Program
The requested functionality outlined in the assignment is implemented as functions in the `functions.py` file.
To test the implementation, run the `main.py` file, adhering to the following usage:
```
$ python main.py [lsh|jaccard|minhash] [verbose|no-verbose] [THRESHOLD]
```
You specify what mode you would like to use (lsh, jaccard, or minhash; i.e. how you would like to compute the similarities) in the second command line argument. In the third argument you specify whether or not you want a more verbose print out when running the program. In the fourth argument you specify the support threshold to use. NB: the support threshold must be between 0 and 1. There are no default values for the command line arguments, so you need to explicitly specify values for all arguments when running the program. A valid example run could thus look like this:
```shell
$ python main.py lsh no-verbose 0.2
```
