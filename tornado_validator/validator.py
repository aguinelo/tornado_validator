"""Validator for Python Tornado Framework"""

VALIDATIONS_ERRORS = []

def valid(data, rules, fillable=None):
    """Return True if all conditions are met, else return False"""
    global VALIDATIONS_ERRORS
    VALIDATIONS_ERRORS = []
    fillable_data = []

    if fillable:
        for field in fillable:
            if field in data:
                fillable_data[field] = data[field]
    else:
        fillable_data = data

    for rule in rules:
        if rule["field"] in fillable_data:
            if "type" in rule:
                if isinstance(fillable_data[rule["field"]], rule["type"]):
                    print()
                else:
                    VALIDATIONS_ERRORS.append({rule["field"]: rule["message"]})
        else:
            VALIDATIONS_ERRORS.append({rule["field"]: rule["message"]})

    if VALIDATIONS_ERRORS:
        return False
    return True

def errors():
    """Return list of errors"""
    return VALIDATIONS_ERRORS
