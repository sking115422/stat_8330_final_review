# Unsupervised Learning Notes

Use this bucket when there is no response variable and the goal is finding structure, reducing dimension, visualizing data, or grouping observations.

## Exam Decision Flow

```text
no response variable -> choose PCA or clustering
-> standardize if variables have different scales
-> fit unsupervised method
-> summarize variance, clusters, or dendrogram
-> interpret cautiously
```

## Supervised vs Unsupervised

| Type | Has response y? | Goal | Examples |
|---|---:|---|---|
| Supervised learning | yes | predict y | regression, classification |
| Unsupervised learning | no | discover structure in X | PCA, k-means, hierarchical clustering |

Exam warning: do not report prediction accuracy for a real unsupervised problem unless labels are available separately for validation or simulation recovery.

## Standardization

Standardization is often essential before unsupervised learning.

Why:

- PCA is variance-based, so large-scale variables dominate;
- k-means is distance-based, so large-scale variables dominate;
- hierarchical clustering is distance-based, so large-scale variables dominate.

Use:

```python
StandardScaler().fit_transform(X)
```

Exam phrase: “I standardize because variables measured in larger units would otherwise drive the distances or variances.”

## PCA

Principal Component Analysis finds orthogonal directions of maximum variance.

What it does:

- transforms correlated variables into uncorrelated principal components;
- orders components by explained variance;
- provides low-dimensional scores for visualization;
- can reduce dimension before modeling or clustering.

Important objects:

- **loadings**: weights defining each principal component as a linear combination of variables;
- **scores**: transformed coordinates of observations in PC space;
- **explained variance ratio**: fraction of total variance explained by each component;
- **scree plot**: plot of explained variance by component.

Use PCA when:

- many numeric variables are correlated;
- you need a low-dimensional visualization;
- the prompt asks for explained variance;
- you want to reduce dimension before another method.

What PCA does not do:

- it does not use class labels;
- it does not maximize class separation;
- it does not produce clusters by itself.

Relative to clustering:

- PCA finds continuous low-dimensional axes;
- clustering assigns discrete group labels;
- PCA can help visualize clustering but is not a clustering method.

## K-Means Clustering

K-means partitions observations into `k` clusters by minimizing within-cluster squared distances.

What it does:

```text
choose k centers -> assign each point to nearest center
-> update centers -> repeat until stable
```

Main tuning parameter:

- **k**, the number of clusters.

Diagnostics:

- **inertia / within-cluster sum of squares**: decreases as k increases;
- **elbow plot**: look for diminishing returns as k grows;
- **silhouette score**: measures separation and cohesion for k >= 2;
- **Adjusted Rand Index**: compares recovered clusters to known labels in simulation only.

Use k-means when:

- clusters are roughly spherical;
- clusters have similar size and spread;
- variables are numeric;
- you can choose or justify k.

Weaknesses:

- must specify k;
- sensitive to scaling;
- sensitive to random initialization;
- poor for non-spherical or different-density clusters;
- cluster labels are arbitrary names.

Exam phrase: “The elbow plot suggests the number of clusters where adding another cluster gives only a small reduction in inertia.”

## Hierarchical Clustering

Hierarchical clustering builds a tree of nested clusters.

Agglomerative version:

```text
start with each point as its own cluster
-> repeatedly merge closest clusters
-> visualize merge history with dendrogram
```

Important terms:

- **dendrogram**: tree showing cluster merges;
- **linkage**: rule for measuring distance between clusters;
- **cut height**: level where the dendrogram is cut to choose clusters.

Common linkage methods:

| Linkage | Meaning | Typical behavior |
|---|---|---|
| Single | closest pair between clusters | can chain clusters |
| Complete | farthest pair between clusters | compact clusters |
| Average | average pairwise distance | compromise |
| Ward | increase in within-cluster variance | spherical, k-means-like clusters |

Use hierarchical clustering when:

- you want a dendrogram;
- the number of clusters is unknown;
- nested cluster structure is useful;
- sample size is not too large for dendrogram visualization.

Relative to k-means:

| Method | Need k upfront? | Output | Strength | Weakness |
|---|---:|---|---|---|
| K-means | yes | one partition | simple and scalable | assumes spherical clusters |
| Hierarchical | no for tree, yes for final cut | dendrogram plus partition | visual hierarchy | can be sensitive to linkage/outliers |

## Unsupervised Simulation

Simulation helps answer: “When does this unsupervised method recover known structure?”

Simulation workflow:

```text
simulate clusters with known labels
-> hide labels during clustering
-> run clustering
-> use labels only afterward to evaluate recovery
```

Use simulation to study:

- cluster overlap;
- number of clusters;
- non-spherical clusters;
- noise variables;
- scaling effects;
- sample size effects.

Important distinction:

- In simulation, true labels are known and can be used after fitting.
- In real unsupervised learning, labels are not available, so interpretation is exploratory.

## High-Probability Exam Prompts

- Standardize a data matrix and run PCA.
- Report explained variance and choose how many PCs to keep.
- Make and interpret a scree plot.
- Run k-means for multiple k values and make an elbow plot.
- Interpret k-means cluster assignments cautiously.
- Draw or interpret a hierarchical clustering dendrogram.
- Compare k-means and hierarchical clustering.
- Simulate easy and hard clustering scenarios and discuss recovery/failure.

## Python Function Map

| Task | Common Python tool |
|---|---|
| Standardize | `StandardScaler` |
| PCA | `PCA` |
| PCA scores | `pca.fit_transform(X_scaled)` |
| Explained variance | `pca.explained_variance_ratio_` |
| K-means | `KMeans` |
| K-means labels | `fit_predict` |
| K-means inertia | `model.inertia_` |
| Silhouette | `silhouette_score` |
| Hierarchical clustering | `AgglomerativeClustering` |
| Dendrogram | `scipy.cluster.hierarchy.dendrogram` |
| Linkage matrix | `scipy.cluster.hierarchy.linkage` |
| Simulation clusters | `make_blobs` |
| Recovery score | `adjusted_rand_score` |

## What To Say In Interpretations

- “Because there is no response variable, this is exploratory structure discovery.”
- “I standardized variables before PCA/clustering because scale affects variance and distance.”
- “The first principal component explains the largest possible share of variance among linear combinations.”
- “The elbow plot suggests a reasonable k, but it is not a formal proof.”
- “Cluster labels are arbitrary and require subject-matter interpretation.”
- “Simulation labels are used only after clustering to assess recovery.”

