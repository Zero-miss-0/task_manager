from exceptions.custom_errors import (
                                        EmptyStrParametersError,
                                        InvalidPriorityError,
                                        InvalidStatusError,
                                        InvalidUrgencyLevelError,
                                        InvalidMenuChoiceError,
                                        ProjectNotFoundError,
                                        TaskNotFoundError
                                        )


def validate_str_parameters(parameter):
    if not parameter.strip():
        raise EmptyStrParametersError(f"⚠︎ Cannot be empty !!! Enter a value.")
    if not parameter.strip().isalpha():
        raise AttributeError(f"⚠︎ Invalid Input : '{parameter}' is invalid !!! Enter words.")
    return parameter

def validate_priority(priority):
    try:
        priority = int(priority)
    except (ValueError, TypeError):
            raise InvalidPriorityError(f"⚠︎ '{priority}' is invalid !!! priority must be between 1 and 5.")
    else:
        if not (1 <= priority <= 5):
            raise InvalidPriorityError(f"⚠︎ '{priority}' is invalid !!! priority must be between 1 and 5.")
    return priority

def validate_status(status):
    if status not in ("pending", "completed"):
        raise InvalidStatusError(f"⚠︎ '{status}' is invalid !!! Status must be either 'pending' or 'completed'.")
    return status

def validate_urgency_level(urgency_level):
    try:
        urgency_level = int(urgency_level)
    except (ValueError, TypeError):
        raise InvalidUrgencyLevelError(f"⚠︎ '{urgency_level}' is invalid !!! urgency level must be 4 or 5.")
    else:
        if urgency_level not in (4, 5):
            raise InvalidUrgencyLevelError(f"⚠︎ '{urgency_level}' is invalid !!! urgency level must be 4 or 5.")
    return urgency_level
