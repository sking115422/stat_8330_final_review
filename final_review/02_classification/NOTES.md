# Classification / Categorical Prediction Notes

Use this bucket when the response variable is categorical and the goal is predicting class labels, comparing classifiers, tuning decision boundaries, or summarizing classification error.

## Exam Decision Flow

```text
categorical response -> choose classifier -> choose metric
-> train/test or stratified CV -> tune parameters
-> report accuracy/confusion matrix -> interpret error types
```

## Core Metrics

| Metric | Meaning | Use when |
|---|---|---|
| Accuracy | proportion correctly classified | classes are balanced and mistakes have similar cost |
| Error rate | proportion incorrectly classified | same information as 1 - accuracy |
| Confusion matrix | counts of true/predicted labels | you need false positives and false negatives |
| Sensitivity / recall | TP / actual positives | missing positives is costly |
| Specificity | TN / actual negatives | false positives are costly |
| Precision | TP / predicted positives | positive predictions must be reliable |
| F1 score | harmonic mean of precision and recall | class imbalance and both FP/FN matter |

Exam warning: accuracy can hide class-specific failures when classes are imbalanced.

## Train/Test And Stratified CV

Classification evaluation should usually preserve class proportions.

Use:

- `train_test_split(..., stratify=y)` for train/test splitting;
- `StratifiedKFold` for cross-validation;
- `accuracy_score`, `confusion_matrix`, and `classification_report` for metrics.

Do not evaluate only on training accuracy unless the prompt specifically asks for apparent error. Training accuracy is often optimistic, especially for flexible classifiers.

## LDA

Linear Discriminant Analysis models each class as Gaussian with a shared covariance matrix.

What it does:

- estimates class means;
- estimates one common covariance matrix;
- predicts using Bayes-rule-style discriminant scores;
- produces linear decision boundaries.

Use LDA when:

- classes are roughly Gaussian;
- boundaries look approximately linear;
- sample size is not huge;
- you want a lower-variance classifier.

Assumptions:

- observations independent;
- predictors approximately multivariate normal within each class;
- class covariance matrices are similar.

Relative to logistic regression:

- both can produce linear boundaries;
- LDA models predictor distribution within classes;
- logistic regression models class probability directly.

## QDA

Quadratic Discriminant Analysis allows each class to have its own covariance matrix.

What it does:

- estimates class-specific means and covariances;
- produces quadratic or curved boundaries;
- is more flexible than LDA.

Use QDA when:

- classes appear to have different covariance shapes;
- curved boundaries are plausible;
- you have enough data to estimate more parameters.

Relative to LDA:

| Method | Boundary | Parameters | Risk |
|---|---|---|---|
| LDA | linear | fewer | underfit if covariances differ |
| QDA | quadratic | more | overfit if sample size is small |

Exam phrase: “QDA is more flexible than LDA because it allows different covariance matrices by class.”

## KNN Classification

KNN predicts a class by majority vote among the `k` nearest training observations.

What it does:

- stores the training data;
- computes distances from a new point to training points;
- predicts using nearby labels.

Main tuning parameter:

- **k**, the number of neighbors.

k intuition:

- small k: flexible, low bias, high variance;
- large k: smoother, high bias, low variance.

Use KNN when:

- decision boundary may be nonlinear;
- interpretability of coefficients is not required;
- you can scale predictors first if units differ.

Exam warning: KNN is distance-based. Standardize predictors when variables have different scales.

## Decision Trees

Decision trees classify by recursively splitting the predictor space.

What they do:

- choose split variables and split points;
- create rectangular decision regions;
- produce interpretable rules.

Strengths:

- easy to explain;
- handles nonlinear relationships and interactions;
- no need for linearity assumptions.

Weaknesses:

- high variance;
- can overfit badly;
- small data changes can produce different trees.

Pruning:

- reduces tree complexity;
- improves generalization;
- controlled in sklearn by `ccp_alpha`.

Exam phrase: “I tune the pruning parameter by cross-validation and evaluate the selected tree on held-out data.”

## Random Forest

Random forest averages many decision trees.

What it does:

- builds many trees on bootstrap-like samples;
- uses random subsets of features at splits;
- averages predictions or votes across trees.

Why it works:

- individual trees have high variance;
- averaging many decorrelated trees reduces variance.

Use random forest when:

- prediction accuracy matters;
- nonlinearities and interactions are expected;
- interpretability is less important than performance.

Relative to a single tree:

- usually more accurate and stable;
- less interpretable;
- has tuning parameters such as number of trees and max features.

## AdaBoost

AdaBoost builds an ensemble sequentially, focusing more on observations misclassified by earlier weak learners.

What it does:

- fits weak classifiers in sequence;
- reweights difficult observations;
- combines learners into a stronger classifier.

Use AdaBoost when:

- a single weak learner underfits;
- boosting may reduce bias;
- data are not too noisy.

Relative to random forest:

| Method | Main mechanism | Main benefit | Main risk |
|---|---|---|---|
| Random forest | parallel averaging | variance reduction | less interpretable |
| AdaBoost | sequential reweighting | bias reduction | sensitivity to noisy labels |

## SVM

Support Vector Machines find decision boundaries with large margins.

Core idea:

- separate classes with a boundary;
- maximize margin around boundary;
- allow violations through penalty parameter `C`;
- use kernels for nonlinear boundaries.

Important parameters:

- **C**: penalty for margin violations.
- **gamma** for RBF kernel: locality/flexibility of the kernel.

Parameter intuition:

- large C: tries harder to classify training data correctly, can overfit;
- small C: allows more violations, smoother boundary;
- large gamma: very local/wiggly RBF boundary;
- small gamma: smoother RBF boundary.

Exam warning: standardize predictors before SVM because the method depends on distances and dot products.

## Max-Margin Classifier

The maximal-margin classifier is the hard-margin SVM idea for separable data.

What it does:

- considers boundaries that perfectly separate classes;
- chooses the one with largest minimum distance to the data;
- closest points determine the margin and are support vectors.

Use it when:

- data are linearly separable;
- the exam asks for margin geometry;
- a randomized implementation is requested.

Relative to SVM:

- hard-margin max-margin requires perfect separation;
- soft-margin SVM allows violations through `C`;
- kernel SVM allows nonlinear separation.

## Classification Simulation Studies

Simulation studies answer: “Which classifier works better under this data-generating scenario?”

Good simulation structure:

```text
choose scenario -> repeat many times
-> simulate data -> split train/test
-> fit all methods on same training set
-> compute test accuracy on same test set
-> summarize table/boxplot
```

Use simulation when:

- the exam asks for method comparison;
- you need to vary class separation, noise, or boundary shape;
- you want to show performance variability.

## High-Probability Exam Prompts

- Compute and interpret a confusion matrix.
- Compare LDA and QDA assumptions.
- Tune KNN `k` by cross-validation.
- Prune a decision tree using CV.
- Compare a tree, random forest, and AdaBoost.
- Tune SVM `C` and `gamma`.
- Implement or explain a max-margin classifier.
- Run a classification simulation study and summarize accuracy.

## Python Function Map

| Task | Common Python tool |
|---|---|
| Stratified split | `train_test_split(..., stratify=y)` |
| Stratified CV | `StratifiedKFold` |
| Accuracy | `accuracy_score` |
| Confusion matrix | `confusion_matrix` |
| Classification report | `classification_report` |
| LDA | `LinearDiscriminantAnalysis` |
| QDA | `QuadraticDiscriminantAnalysis` |
| KNN | `KNeighborsClassifier` |
| Tree | `DecisionTreeClassifier` |
| Random forest | `RandomForestClassifier` |
| AdaBoost | `AdaBoostClassifier` |
| SVM | `SVC`, `LinearSVC` |
| Scaling | `StandardScaler` |

## What To Say In Interpretations

- “I used stratified splitting/CV to preserve class proportions.”
- “The classifier with the highest CV accuracy is preferred for prediction.”
- “The confusion matrix shows which class-specific errors dominate.”
- “Flexible classifiers can improve nonlinear boundaries but may overfit.”
- “Scaling is important for distance-based methods such as KNN and SVM.”

