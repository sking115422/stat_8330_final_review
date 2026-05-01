# Regression / Numeric Prediction Notes

Use this bucket when the response variable is numeric and the goal is predicting a value, estimating a smooth mean curve, comparing prediction errors, or quantifying uncertainty for a regression quantity.

## Exam Decision Flow

```text
numeric response -> choose candidate regression method -> choose MSE/RMSE
-> use train/test or CV -> tune complexity -> plot error curve or fitted curve
-> interpret bias, variance, overfitting, and prediction performance
```

## Core Metrics

- **MSE**: average squared prediction error. Use when the problem asks for prediction error.
- **RMSE**: square root of MSE. Same units as the response, often easier to interpret.
- **Training MSE**: error on the data used to fit the model. Usually optimistic.
- **Test MSE**: error on held-out data. Better estimate of future prediction performance.
- **CV MSE**: average validation error across folds. Use to tune model complexity.

## Train/Test Evaluation

Train/test splitting answers: “How well will this model predict new observations?”

Use it when:

- the prompt asks for prediction error;
- you compare two or more models;
- you need a quick honest estimate of performance;
- you want to show overfitting by comparing train MSE and test MSE.

Key exam warning: never tune or choose a model using the test set repeatedly unless you clearly describe it as a simulation exercise. In a real analysis, repeated model selection should be done with cross-validation or a validation set.

## K-Fold CV And LOOCV

**K-fold CV** splits the data into `k` folds, fits on `k - 1` folds, validates on the remaining fold, and averages the validation error.

**LOOCV** is k-fold CV with `k = n`. Each model leaves out exactly one observation.

Use k-fold CV when:

- tuning polynomial degree;
- tuning spline knots;
- tuning lasso alpha;
- tuning kernel bandwidth or LOESS span;
- test-set estimates are too unstable.

Relative comparison:

| Method | Main use | Strength | Weakness |
|---|---|---|---|
| Train/test split | Fast performance estimate | Simple and honest | Can depend heavily on one split |
| K-fold CV | Tuning and model comparison | More stable than one split | Fits many models |
| LOOCV | Small data, leave-one-out prompts | Uses almost all data per fit | Can be slow and variable |

In sklearn, `cross_val_score(..., scoring="neg_mean_squared_error")` returns negative values because sklearn treats larger scores as better. Multiply by `-1` before interpreting as MSE.

## Linear Regression

Linear regression models:

```text
E(Y | X) = beta0 + beta1 X1 + ... + betap Xp
```

Use it when:

- the response is numeric;
- the relationship is approximately linear;
- interpretability matters;
- you need a baseline model.

Assumptions for classical inference:

- linear mean structure;
- independent observations;
- constant error variance;
- errors roughly normal for small-sample t intervals;
- no severe multicollinearity if interpreting coefficients.

For prediction-focused exam questions, the most important issue is usually test/CV MSE, not perfect normality.

## Polynomial Regression

Polynomial regression adds powers of a predictor:

```text
1, x, x^2, x^3, ...
```

What it does:

- fits curved relationships using ordinary linear regression on transformed features;
- degree controls flexibility;
- higher degree lowers training error but may increase test error.

Use it when:

- there is one main numeric predictor;
- the scatterplot shows curvature;
- the exam asks about overfitting or bias-variance tradeoff.

Relative to splines and kernel methods:

- polynomial regression is global, so changing one region can affect the whole curve;
- splines are piecewise and usually more stable;
- kernel/LOESS methods are local and more nonparametric.

Exam phrase: “The polynomial degree is a tuning parameter controlling model complexity. I would choose it by test MSE or CV MSE.”

## Splines

Splines fit piecewise polynomial curves joined at knots.

What they do:

- create flexible curves without using one high-degree global polynomial;
- allow local flexibility;
- usually behave better than high-degree polynomials at the edges.

Important terms:

- **knot**: location where polynomial pieces meet;
- **degree**: degree of each polynomial piece, often cubic;
- **degrees of freedom / number of knots**: flexibility control.

Use splines when:

- the relationship is smooth but nonlinear;
- you need a flexible regression curve;
- you want a more stable alternative to high-degree polynomials.

Relative comparison:

| Method | Global or local? | Tuning parameter | Best exam use |
|---|---|---|---|
| Polynomial | Global | degree | simple curve and overfitting demo |
| Splines | piecewise/local-ish | knots or df | smooth nonlinear fit |
| Kernel smoother | local | bandwidth | nonparametric smoothing |
| LOESS | local | span | intuitive local regression |

## Kernel Smoothers

Kernel smoothing predicts at a point by averaging nearby responses:

```text
prediction at x0 = weighted average of y values,
where weights are largest for x values near x0
```

Main tuning parameter:

- **bandwidth**: controls how wide the neighborhood is.

Bandwidth intuition:

- small bandwidth: very local, wiggly, low bias, high variance;
- large bandwidth: very smooth, high bias, low variance.

Use kernel smoothing when:

- one predictor is numeric;
- the relationship is nonlinear;
- the exam asks for Nadaraya-Watson or bandwidth selection;
- you need a clear LOOCV tuning example.

Exam pattern:

```text
candidate bandwidths -> for each bandwidth leave out each point
-> predict left-out y using remaining points
-> average squared errors -> choose smallest LOOCV MSE
```

## LOESS / Local Regression

LOESS fits local weighted regressions near each target point.

What it does:

- uses nearby points more heavily;
- fits a small local regression repeatedly;
- produces a smooth nonlinear curve.

Main tuning parameter:

- **span** or `frac`: fraction of the data used in each local fit.

Span intuition:

- small span: follows local detail, possibly noisy;
- large span: smoother, possibly misses curvature.

Relative to kernel smoother:

- kernel smoother often uses a weighted average;
- LOESS uses local weighted regression, often local linear fits;
- both are local smoothers tuned by bandwidth/span.

## Lasso Regression

Lasso minimizes:

```text
residual sum of squares + alpha * sum(abs(coefficients))
```

What it does:

- shrinks coefficients toward zero;
- can set some coefficients exactly to zero;
- performs prediction and variable selection.

Use it when:

- there are many predictors;
- some predictors may be irrelevant;
- variable selection is useful;
- the exam asks about penalty strength or sparse signal.

Important parameter:

- **alpha**: penalty size.

Alpha intuition:

- small alpha: close to least squares, more flexible;
- large alpha: more shrinkage, simpler model, more coefficients zero.

Exam warning: standardize predictors before lasso. Otherwise variables with larger scales are penalized differently.

## Bootstrap Regression Confidence Intervals

Bootstrap answers: “How uncertain is this regression statistic?”

Common regression bootstrap statistics:

- slope coefficient;
- intercept;
- predicted value at a point;
- test MSE;
- difference in slopes.

Basic row bootstrap:

```text
resample rows (X, y) with replacement
-> refit model
-> store statistic
-> percentile interval from bootstrap statistics
```

Use it when:

- the prompt asks for a confidence interval by simulation/resampling;
- formulas are hard or not requested;
- you need uncertainty for a fitted quantity.

Exam warning: resample whole rows, not x and y separately. The row preserves the relationship between predictors and response.

## High-Probability Exam Prompts

- Compare polynomial degrees by train/test MSE.
- Use k-fold CV or LOOCV to choose a smoothing parameter.
- Explain why training error is lower than test error.
- Plot MSE versus tuning parameter.
- Simulate data under different noise levels and compare prediction error.
- Choose lasso alpha and interpret coefficient shrinkage.
- Bootstrap a regression slope confidence interval.

## Python Function Map

| Task | Common Python tool |
|---|---|
| Split data | `train_test_split` |
| K-fold CV | `KFold`, `cross_val_score` |
| LOOCV | `LeaveOneOut` |
| MSE | `mean_squared_error` |
| Linear model | `LinearRegression` |
| Polynomial basis | `PolynomialFeatures` |
| Pipeline | `make_pipeline` |
| Spline basis | `SplineTransformer` |
| Lasso | `Lasso`, `LassoCV` |
| LOWESS | `statsmodels.nonparametric.smoothers_lowess.lowess` |

## What To Say In Interpretations

- “I selected the model with the smallest estimated test/CV MSE.”
- “The more flexible model has lower training error, but not necessarily lower test error.”
- “The tuning parameter controls the bias-variance tradeoff.”
- “The fitted curve is descriptive unless evaluated on held-out data.”
- “Bootstrap uncertainty comes from repeated resampling of the observed data.”

