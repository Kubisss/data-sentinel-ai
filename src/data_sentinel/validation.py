def validate_required_columns(df, required_columns):
    missing_columns = [col for col in required_columns if col not in df.columns]
    
    return {
        "check_name": "required_columns",
        "passed": len(missing_columns) == 0,
        "missing_columns": missing_columns
    }

def validate_not_null_columns(df, columns):
    null_counts = df[columns].isnull().sum().to_dict()
    columns_with_nulls = [col for col, count in null_counts.items() if count > 0]

    return {
        "check_name": "not_null_columns",
        "passed": len(columns_with_nulls) == 0,
        "null_columns": columns_with_nulls
    }