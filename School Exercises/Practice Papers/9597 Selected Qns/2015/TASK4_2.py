# Task 4.2
def validate_user_id(user_id: str) -> int:
    """
    Validates user ID and returns an error code if it is invalid

    Args:
        user_id: string representing the user ID.
    Returns:
        Error code (0-4)
    """
    if len(user_id) != 9:
        return 1  # Invalid length
    elif user_id[:5] != "2015_":
        return 2  # Invalid format
    elif not user_id[5:].isdigit():
        return 3  # NNNN not numbers
    else:
        return 0  # Valid
