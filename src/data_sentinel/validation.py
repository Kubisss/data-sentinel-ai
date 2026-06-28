def validate_required_columns(df, required_columns):
    missing_columns = [col for col in required_columns if col not in df.columns]
    
    return {
        "check_name": "required_columns",
        "passed": len(missing_columns) == 0,
        "missing_columns": missing_columns
    }