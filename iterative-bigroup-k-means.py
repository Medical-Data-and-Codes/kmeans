import os
from sklearn.cluster import KMeans

"""
For two groupings, runs iterative k-means (with multiple k values). 
Generates the visualizations and stores the results in CSV.
"""

# K means configuration
n_init = 10  # Number of times to retry with different seeds
minimum_k = 2  # Lowest number of clusters, will go up to n-1 number of samples
max_iter = 300  # Number of iterations for a single run
tol = 0.0001  # tolerance for Frobenius norm of the difference in the cluster centers to determine convergence
random_state = None  # Random number generator for centroid initialization
copy_x = True  # Original data is not modified during centering the data
algorithm = "auto"  # K-means algorithm to use


def check_dir(dir_path):
    """
    Simple wrapper for checking for directory existence,
    creating one if the path does not correspond with one yet.
    """
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)


# Result saving configuration
cwd = os.getcwd()
saveDir = "iterative-bigroup-k-means"
savePath = os.path.join(cwd, saveDir)
check_dir(savePath)
saveDataFile = "{k}-means-{group}.csv"
saveImageFile = "{k}-means-{group}.png"


def get_file_name(k, group, datatype="csv"):
    """
    Returns the correct file name corresponding to the data type.
    :param k: number of clusters
    :param group: group label
    :param datatype: type of file
    :return: fully qualified file path
    """
    if datatype == "csv":
        return os.path.join(saveDir, saveDataFile.format(k=k, group=group))
    else:
        return os.path.join(saveDir, saveImageFile.format(k=k, group=group))


def run_k_means(k, groupName, data):
    """
    Executes the k-means, saving the result as per specified group.
    :param k: number of clusters
    :param groupName: group label
    :param data: data for clustering
    """
    kmeans = KMeans(
        n_clusters=k,
        n_init=n_init,
        max_iter=max_iter,
        tol=tol,
        random_state=random_state,
        copy_x=copy_x,
        algorithm=algorithm).fit(data)
    labels = kmeans.labels_
    centers = kmeans.cluster_centers_

def main():
    """
    Main execute method.
    """
    print("hello")


if __name__ == "__main__":
    main()
