![](https://img.shields.io/badge/python-3.8%20%7C%203.9-blue) 
![](https://img.shields.io/badge/coverage-76%25-brightgreen)

The k-mxt-w3 library contains an implementation of the k-mxt and k-mxt-w algorithms.
Using clustering algorithms can identify clusters on a dataset.

## Installation
```bash
pip install k-mxt-w3
```

## Parameters
 * The larger the parameter k, the more vertices will be in each cluster, and the number of clusters will be less.
 * The eps parameter indicates the maximum distance between the vertices at which these vertices are connected.
 
 ## Usage
1. Clustering 2d data using k-mxt and k-mxt-w algorithms with Euclidean metric
 ```python
import k_mxt_w3
import sklearn.datasets

# Get dataset from sklearn.datasets.
# coord contains coordinates of points along x-axis, y-axis
coord, labels = sklearn.datasets.make_moons(n_samples=50, noise=0.05, random_state=0)

# To create class instance of data class
# which contains data of points along x-axis, y-axis and
# Euclidean metric will be used to calculate distance between points
clusters = k_mxt_w3.clusters_data.ClustersDataSpace2d(
    x_init=coord[:, 0],
    y_init=coord[:, 1],
    metrics='euclidean')

# To create the class of k-mxt clustering algorithm
alg = k_mxt_w3.clustering_algorithms.K_MXT(
    k=9,
    eps=0.4,
    clusters_data=clusters,
)

# To calculate clusters
alg()
# To print clustering result
print(alg.clusters_data.cluster_numbers)

# To create the class of k-mxt-w clustering algorithm
alg = k_mxt_w3.clustering_algorithms.K_MXT_gauss(
    k=9,
    eps=0.4,
    clusters_data=clusters,
)

# To calculate clusters
alg()

# To print clustering result
print(alg.clusters_data.cluster_numbers)
```

2. Clustering 2d data using k-mxt and k-mxt-w algorithms with Manhattan metric
```python
import k_mxt_w3
import sklearn.datasets

# Get dataset from sklearn.datasets.
# coord contains coordinates of points along x-axis, y-axis
coord, labels = sklearn.datasets.make_moons(n_samples=50, noise=0.05, random_state=0)

# To create class instance of data class which contains data of points along x-axis, y-axis and
# Manhattan metric will be used to calculate distance between points
clusters = k_mxt_w3.clusters_data.ClustersDataSpace2d(x_init=coord[:, 0], y_init=coord[:, 1], metrics='manhattan')

# To create the class of k-mxt clustering algorithm
alg = k_mxt_w3.clustering_algorithms.K_MXT(
    k=9,
    eps=0.4,
    clusters_data=clusters,
)

# To calculate clusters
alg()
# To print clustering result
print(alg.clusters_data.cluster_numbers)

# To create the class of k-mxt-w clustering algorithm
alg = k_mxt_w3.clustering_algorithms.K_MXT_gauss(
    k=9,
    eps=0.4,
    clusters_data=clusters,
)

# To calculate clusters
alg()

# To print clustering result
print(alg.clusters_data.cluster_numbers)
```
3. Loading data from csv-file and clustering 2d data using k-mxt and k-mxt-w 
```python
import k_mxt_w3
import pandas as pd


# To load dataframe using pandas
df = pd.read_csv('dataset.csv', sep=',')

# Get numpy-arrays which contain latitudes and longitudes of points
latitude, longitude = k_mxt_w3.data.DataPropertyImportSpace.get_data(
    df,
    name_latitude_cols='latitude',  # name of column containing latitude
    name_longitude_cols='longitude',  # name of column containing longitude
    features_list=None,  # list of column names which contain other features or None
)

# To create class instance of data class
# which contains data of points along x-axis, y-axis and
# Euclidean metric will be used
# to calculate distance between points
clusters = k_mxt_w3.clusters_data.ClustersDataSpace2d(
    x_init=latitude,
    y_init=longitude,
    metrics='euclidean'
)

# To create the class of k-mxt clustering algorithm
alg = k_mxt_w3.clustering_algorithms.K_MXT(
    k=3,
    eps=0.01,
    clusters_data=clusters,
)

# To calculate clusters
alg()
# To print clustering result
print(alg.clusters_data.cluster_numbers)

# To create class instance of data class
# which contains data of points along x-axis, y-axis and
# Euclidean metric will be used
# to calculate distance between points
clusters = k_mxt_w3.clusters_data.ClustersDataSpace2d(
    x_init=latitude,
    y_init=longitude,
    metrics='euclidean'
)

# To create the class of k-mxt-w clustering algorithm
alg = k_mxt_w3.clustering_algorithms.K_MXT_gauss(
    k=3,
    eps=0.01,
    clusters_data=clusters,
)

# To calculate clusters
alg()

# To print clustering result
print(alg.clusters_data.cluster_numbers)
```
4. Loading data from csv-file and clustering multidimensional data using k-mxt and k-mxt-w 
```python
import k_mxt_w3
import pandas as pd


# To load dataframe using pandas
df = pd.read_csv('dataset.csv', sep=',')

# Get numpy-arrays which contain latitudes and longitudes and values of other features of points
latitude, longitude, features = k_mxt_w3.data.DataPropertyImportSpace.get_data(
    df,
    name_latitude_cols='latitude',  # name of column containing latitude
    name_longitude_cols='longitude',  # name of column containing longitude
    features_list=['price', 'living_space'],  # list of column names which contain other features or None
)

# To create class instance of data class
# which contains data of points along x-axis, y-axis and
# Euclidean metric will be used
# to calculate distance between points
clusters = k_mxt_w3.clusters_data.ClustersDataSpaceFeatures(
    x_init=latitude,
    y_init=longitude,
    features_init=features,
    metrics='euclidean'
)

# To create the class of k-mxt clustering algorithm
alg = k_mxt_w3.clustering_algorithms.K_MXT(
    k=3,
    eps=0.01,
    clusters_data=clusters,
)

# To calculate clusters
alg()
# To print clustering result
print(alg.clusters_data.cluster_numbers)

# To create class instance of data class
# which contains data of points along x-axis, y-axis and
# Euclidean metric will be used
# to calculate distance between points
clusters = k_mxt_w3.clusters_data.ClustersDataSpaceFeatures(
    x_init=latitude,
    y_init=longitude,
    features_init=features,
    metrics='euclidean'
)

# To create the class of k-mxt-w clustering algorithm
alg = k_mxt_w3.clustering_algorithms.K_MXT_gauss(
    k=3,
    eps=0.01,
    clusters_data=clusters,
)

# To calculate clusters
alg()

# To print clustering result
print(alg.clusters_data.cluster_numbers)
```