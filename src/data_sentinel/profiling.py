def profile_dataframe(df):
    results = {
        "num_rows": len(df),
        "num_columns": len(df.columns),
        "column_names": df.columns.tolist(),
        "null_counts_per_column": df.isnull().sum().to_dict(),
        "duplicate_rows": int(df.duplicated().sum()),
        "data_types": df.dtypes.astype(str).to_dict(),
    }
    return results