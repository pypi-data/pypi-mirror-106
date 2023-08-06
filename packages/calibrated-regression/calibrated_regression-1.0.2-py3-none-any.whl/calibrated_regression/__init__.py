def calibrated_new_cases(new_cases, calibrated_regression_number):
    if new_cases > 333:
        new_cases = new_cases - calibrated_regression_number
    return new_cases
