# STAT 8330 Final Review Python Notebook Library

This folder is a Python-only, self-contained notebook library for STAT 8330 final review. The previous shared utilities folder has been removed intentionally: each notebook now includes its own simulation helpers, evaluation code, assumptions, Python documentation links, plots/tables, and exam-style adaptation pattern.

The design goal is timed-exam reuse: open the notebook for the method you need and copy the complete local workflow without flipping between files.

## Course Bucket Map

1. Regression / numeric prediction
2. Classification / categorical prediction
3. Unsupervised learning
4. Bootstrap, permutation, and computational evaluation workflows

## Revised Structure

```text
STAT8330_Final_Review/
├── 00_quick_start_exam_workflows.ipynb
├── 01_regression_prediction/
├── 02_classification/
├── 03_unsupervised_learning/
├── 04_bootstrap_permutation_methods.ipynb
├── README.md
└── requirements.txt
```

There is no local utility module to import. Every notebook is standalone.

## Suggested Study Order

1. `00_quick_start_exam_workflows.ipynb`
2. Regression train/test, CV, polynomial regression, splines, kernel smoothers, LOESS, lasso, and bootstrap CI notebooks
3. Classification metrics, LDA/QDA, KNN, trees/pruning, ensembles, SVM, simulation comparisons, and randomized max-margin notebook
4. `04_bootstrap_permutation_methods.ipynb`
5. PCA, k-means, hierarchical clustering, and unsupervised simulation notebooks

## Exam Workflow Checklist

```text
identify response type -> choose method -> choose metric -> choose evaluation strategy
-> write local helper functions -> run simulation/data analysis -> summarize table/plot
-> interpret briefly
```

## Reusable Patterns Embedded In Notebooks

```text
simulate -> split/CV -> fit -> predict -> evaluate -> summarize
CV over tuning values -> choose best error/accuracy
bootstrap statistic -> percentile CI
permutation null distribution -> p-value
classification simulation -> accuracy table/boxplot
regression simulation -> MSE curve
unsupervised simulation -> recovery/failure explanation
```

## How to Run

From this directory, install dependencies if needed:

```bash
pip install -r requirements.txt
```

Then start Jupyter:

```bash
jupyter notebook
```

You can also execute all notebooks from this directory with `jupyter nbconvert --execute`.

## Academic Integrity Reminder

This library is intended for studying and preparation. Before using it during the actual final, confirm the course rules about notes, code, and AI-created resources.
