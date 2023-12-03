import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import networkx as nx

# Extract the edges from the file and get the number of nodes
def handle_file(filename):
    with open(filename) as f:
        edge_list = f.readlines()

    # Get a list of edges
    edges = [tuple(map(int, edge.split(","))) for edge in edge_list]
    # Get the number of nodes, by max node number
    n = max([max(edge) for edge in edges])

    return edges, n

# Get the adjacency matrix
# Step 1: Same A as in matlab instructions
def get_matrix(edges, n, weighted):
    A = np.zeros((n, n))
    if weighted:
        for edge in edges:
            i, j, w = edge
            i, j = i - 1, j - 1
            A[i][j] = w
        return A
    else:
        for edge in edges:
            i, j = edge
            i, j = i - 1, j - 1
            A[i][j] = 1
        return A

# Corresponds to step 2
def laplacian(A):
    D_sqrt = np.diag(np.sum(A, 1)**(-0.5))
    return D_sqrt @ A @ D_sqrt

# Eigengap heuristic: number of clusters k is given by the value of k that maximizes the eigengap
def optimal_k(eigenvalues):
    # Get the eigengaps and find the index of the max gap
    eigengaps = np.diff(eigenvalues)
    max_gap_index = np.argmax(eigengaps)
    # Ascending order and 0 indexing
    optimal_k = len(eigenvalues) - (max_gap_index + 1)
    return optimal_k

# Corresponds to step 3
def eigen_X(L):
    eigenvalues, eigenvectors = np.linalg.eigh(L)
    k = optimal_k(eigenvalues)
    # Get the k largest eigenvectors, at the end because of ascending order
    X = eigenvectors[:, -k:]
    return eigenvalues, eigenvectors, X, k

# Plot results
def plots(A, eigenvalues, predictions, fiedler):
    # Plot the eigenvalues
    plt.figure()
    plt.title("Eigenvalues")
    plt.plot(eigenvalues)
    plt.show()

    # Plot the sorted fiedler vector
    plt.figure()
    plt.title("Sorted Fiedler Vector")
    plt.plot(fiedler)
    plt.show()

    # Plot the sparsity pattern
    plt.figure()
    plt.title("Sparsity Pattern")
    plt.spy(A)
    plt.show()

    # Plot the clusters
    G = nx.from_numpy_array(A)
    plt.figure()
    plt.title("Clusters")
    nx.draw(G, node_color=predictions)
    plt.show()


# The algorithm
def spectral_clustering(edges, n, weighted):
    # Steps 1-3
    A = get_matrix(edges, n, weighted)
    L = laplacian(A)
    eigenvalues, eigenvectors, X, k = eigen_X(L)

    # Get the second smallest eigenvector, the fiedler vector
    fiedler = eigenvectors[:, 1]

    # Step 4, normalize the rows of X
    Y = np.array([row / np.linalg.norm(row) for row in X])

    # Step 5, cluster the rows of Y using k-means
    kmeans = KMeans(k, n_init="auto")
    predictions = kmeans.fit(Y).labels_

    plots(A, eigenvalues, predictions, np.sort(fiedler))


# Run the algorithm, choose the graph to run it on
if __name__ == "__main__":
    graph = "example2"

    if graph == "example1":
        edges, n = handle_file("data/example1.dat")
        spectral_clustering(edges, n, weighted=False)

    if graph == "example2":
        edges, n = handle_file("data/example2.dat")
        spectral_clustering(edges, n, weighted=True)
