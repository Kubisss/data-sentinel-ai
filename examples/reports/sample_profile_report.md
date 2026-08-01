# Data Quality Report

Input file: `data/sample/customers.csv`

## Summary

- Overall status: **failed**
- Quality score: **50.0%**
- Total checks: 2
- Passed checks: 1
- Failed checks: 1

## Dataset profile

- Rows: 5
- Columns: 5

## Null counts

| Column | Null count |
|---|---:|

## Insights

- Dataset contains 5 rows and 5 columns.
- Overall quality score is 50.0%.
- 1 validation check(s) failed.
- Check 'not_null_columns' failed.
- Column 'age' contains 1 null value(s).


## AI Summary

### Dataset quality summary

The dataset failed 1 validation check(s). Failed checks: not_null_columns. These issues should be reviewed before using the dataset in production analytics.

### Recommendations

- Review failed validation checks.
- Investigate affected columns in the source data.
- Consider adding stricter checks to the ingestion pipeline.

| id | 0 |
| name | 0 |
| age | 1 |
| city | 0 |
| email | 0 |

## Null counts chart

![Null counts](charts/null_counts.png)

## Validation results

| Check | Status | Details |
|---|---|---|
| required_columns | passed ✅ |  |
| not_null_columns | failed ❌ | age (1 nulls) |