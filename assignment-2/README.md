# Introduction
The problem of discovering association rules between itemsets in a sales transaction database (a set of baskets) includes the following two sub-problems

1. Finding frequent itemsets with support at least $s$.
2. Generating association rules with confidence at least $c$ from the itemsets found in the first step.

Reminder that an association rule is an implication $X \implies Y$, where $X$ and $Y$ are itemsets such that $X \cap Y = ∅$. Support of rule $X \implies Y$ is the number of transactions that contain $X \cup Y$. Confidence of rule $X \implies Y$ is the fraction of transactions containing $X \cup Y$ in all transactions that contain $X$.

# Task
You are to solve the first sub-problem: to implement the A-Priori algorithm for finding frequent itemsets with support at least $s$ in a dataset of sales transactions. Remind that support of an itemset is the number of transactions containing the itemset. To test and evaluate your implementation, write a program that uses your A-Priori algorithm implementation to discover frequent itemsets with support at least $s$ in a given dataset of sales transactions.

## Optional Task
Solve the second sub-problem, i.e., develop and implement an algorithm for generating association rules between frequent itemsets discovered using the A-Priori algorithm in a dataset of sales transactions. The rules must have the support of at least $s$ and confidence of at least $c$, where $s$ and $c$ are given as input parameters.

# Report
Write a report (in PDF) with a short description of your solution, instructions on how to build and run, command-line parameters, if any (including default values), and results, e.g., plots or screenshots. For results, your report should include results from running with the specific inputs of the assignment (if specified in the instructions; otherwise, results from running sample inputs should be included). The report should also include info on how long it took your implementation to compute each set of the results.
