def summarize_validation_results(validation_results):
    failed_checks = [
        check for check in validation_results
        if check["passed"] is False
    ]

    return {
        "overall_status": "passed" if len(failed_checks) == 0 else "failed",
        "total_checks": len(validation_results),
        "passed_checks": len(validation_results) - len(failed_checks),
        "failed_checks": len(failed_checks),
        "failed_check_names": [
            check["check_name"] for check in failed_checks
        ],
    }