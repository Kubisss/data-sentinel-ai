def summarize_validation_results(validation_results):
    failed_checks = [
        check for check in validation_results
        if check["passed"] is False
    ]

    total_checks = len(validation_results)
    failed_checks_count = len(failed_checks)
    passed_checks = total_checks - failed_checks_count

    quality_score = round((passed_checks / total_checks) * 100, 2)

    return {
        "overall_status": "passed" if len(failed_checks) == 0 else "failed",
        "total_checks": total_checks,
        "passed_checks": passed_checks,
        "failed_checks": failed_checks_count,
        "failed_check_names": [
            check["check_name"] for check in failed_checks
        ],
        "quality_score": quality_score,
    }