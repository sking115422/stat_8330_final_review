# Bootstrap And Permutation Methods Notes

Use this notebook when the question asks for uncertainty by resampling, a simulation-based confidence interval, or a p-value from a null distribution created by shuffling labels.

Associated notebook: `bootstrap_permutation_methods.ipynb`.

## Exam Decision Flow

```text
need uncertainty for a statistic? -> bootstrap
need p-value under exchangeable labels? -> permutation test
need prediction error? -> train/test or CV, not bootstrap by default
```

## Bootstrap: What It Is

Bootstrap resampling approximates the sampling distribution of a statistic by repeatedly sampling from the observed data with replacement.

Basic idea:

```text
observed data -> resample rows with replacement
-> compute statistic on each resample
-> use bootstrap statistic distribution for SE or CI
```

Use bootstrap when:

- the prompt asks for a confidence interval by simulation;
- the statistic is complicated;
- a formula-based standard error is unavailable or not requested;
- you want uncertainty for a mean, median, slope, prediction, or model performance statistic.

Do not use bootstrap as the first tool when the question is clearly about prediction error tuning. For that, use train/test or CV.

## Bootstrap Percentile Confidence Interval

Workflow:

```text
for b in 1...B:
    sample n rows with replacement
    compute statistic
take alpha/2 and 1-alpha/2 quantiles
```

For a 95% percentile CI:

```text
lower = 2.5th percentile of bootstrap statistics
upper = 97.5th percentile of bootstrap statistics
```

Interpretation:

“Using bootstrap resampling, a 95% confidence interval for the statistic is approximately [lower, upper].”

Exam warning: say what the statistic is. A bootstrap CI for the mean, median, slope, and difference in means are different analyses.

## Bootstrap Standard Error

The bootstrap standard error is the standard deviation of the bootstrap statistics.

Use it when:

- the prompt asks for standard error;
- you want to quantify variability but not necessarily form an interval;
- you want to compare uncertainty across methods.

Formula:

```text
SE_boot = sd(statistic_bootstrap_1, ..., statistic_bootstrap_B)
```

## Row Bootstrap For Regression

For regression, resample complete rows:

```text
(x_i, y_i) pairs -> sample rows with replacement -> refit model -> store slope or prediction
```

Use row bootstrap when:

- observations are independent;
- you want uncertainty for a coefficient, prediction, or fitted statistic;
- the problem does not specify residual bootstrap.

Exam warning: do not independently resample x and y. That destroys the predictor-response relationship.

## Residual Bootstrap For Regression

Residual bootstrap keeps predictors fixed and resamples fitted residuals.

Workflow:

```text
fit model -> get fitted values and residuals
-> resample residuals
-> create y* = fitted + resampled residual
-> refit model -> store statistic
```

Use residual bootstrap when:

- the linear model is considered structurally correct;
- predictors are fixed by design;
- errors are roughly identically distributed.

For most timed exam prompts, row bootstrap is simpler and safer unless residual bootstrap is explicitly requested.

## Permutation Tests: What They Are

Permutation tests simulate a null distribution by shuffling labels or group assignments.

Basic idea:

```text
compute observed statistic
-> shuffle labels under null hypothesis
-> recompute statistic many times
-> p-value = fraction of null statistics at least as extreme as observed
```

Use permutation tests when:

- the null hypothesis says labels are exchangeable;
- comparing two groups;
- testing whether group labels matter;
- the prompt asks for a p-value by simulation/randomization.

Common statistics:

- difference in means;
- difference in medians;
- difference in proportions;
- classification accuracy under shuffled labels;
- correlation after shuffling one variable.

## Exchangeability

Exchangeability is the key assumption for a permutation test.

It means that under the null hypothesis, the labels could have been assigned differently without changing the joint distribution of outcomes.

Good examples:

- randomized treatment/control labels;
- two groups assumed to come from the same distribution under the null;
- labels in a simulation where the null is true.

Bad examples:

- time series with strong temporal dependence;
- paired data treated as independent;
- groups with different sampling mechanisms unrelated to the tested effect.

Exam phrase: “Under the null hypothesis, group labels are exchangeable, so shuffling labels creates the reference distribution.”

## One-Sided vs Two-Sided P-Values

Let the statistic be:

```text
observed = mean(group A) - mean(group B)
```

Two-sided:

```text
mean(abs(null_stats) >= abs(observed))
```

Greater:

```text
mean(null_stats >= observed)
```

Less:

```text
mean(null_stats <= observed)
```

Exam warning: choose the alternative before looking at the result. If no direction is specified, use two-sided.

## Bootstrap vs Permutation

| Method | Main question | Resampling mechanism | Output |
|---|---|---|---|
| Bootstrap | How uncertain is my statistic? | sample observations with replacement | SE or confidence interval |
| Permutation | How surprising is my statistic under the null? | shuffle labels without changing outcomes | p-value |

Short version:

- bootstrap estimates sampling variability;
- permutation tests a null hypothesis.

## Relationship To Train/Test And CV

Bootstrap and permutation are not replacements for model assessment.

Use:

- train/test or CV for prediction error;
- bootstrap for confidence intervals or standard errors;
- permutation for simulation-based p-values.

There are bootstrap estimates of prediction error, but in this course context, train/test and CV are usually the expected tools for prediction performance.

## High-Probability Exam Prompts

- Bootstrap a confidence interval for a mean.
- Bootstrap a confidence interval for a regression slope.
- Use permutation to test a difference in two group means.
- Plot a bootstrap distribution and mark interval endpoints.
- Plot a permutation null distribution and mark the observed statistic.
- Explain the difference between resampling with replacement and shuffling labels.
- Explain exchangeability.

## Python Function Map

| Task | Common Python tool |
|---|---|
| Random generator | `np.random.default_rng` |
| Bootstrap row indices | `rng.integers(0, n, size=n)` |
| Permute labels/outcomes | `rng.permutation` |
| Percentile CI | `np.quantile` |
| Mean difference | `np.mean(a) - np.mean(b)` |
| Histogram | `plt.hist` |
| Reference line | `plt.axvline` |

## Exam Code Skeleton: Bootstrap CI

```python
stats_boot = []
for b in range(n_boot):
    sample = data[rng.integers(0, n, size=n)]
    stats_boot.append(statistic(sample))
lower, upper = np.quantile(stats_boot, [0.025, 0.975])
```

## Exam Code Skeleton: Permutation Test

```python
observed = np.mean(group_a) - np.mean(group_b)
combined = np.concatenate([group_a, group_b])
null_stats = []
for i in range(n_perm):
    shuffled = rng.permutation(combined)
    stat = np.mean(shuffled[:n_a]) - np.mean(shuffled[n_a:])
    null_stats.append(stat)
p_value = np.mean(np.abs(null_stats) >= abs(observed))
```

## What To Say In Interpretations

- “The bootstrap interval estimates uncertainty in the statistic.”
- “The permutation p-value estimates how often the null would produce a result this extreme.”
- “The permutation test is valid when labels are exchangeable under the null.”
- “The bootstrap resamples observations with replacement; the permutation test shuffles labels or assignments.”
- “A small p-value means the observed statistic is unusual under the shuffled-label null distribution.”

