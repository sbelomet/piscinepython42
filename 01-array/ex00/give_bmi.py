
def give_bmi(
    height: list[int | float],
    weight: list[int | float],
) -> list[int | float]:
    """Calculate BMI for height and weight lists.

    Args:
        height: list of heights in meters (int or float).
        weight: list of weights in the same order (int or float).

    Returns:
        List of BMI values (float) computed as weight / height**2.

    Raises:
        TypeError: if inputs are not lists or contain non-numeric elements.
        ValueError: if lists differ in length or any height is zero.
    """
    if not isinstance(height, list) or not isinstance(weight, list):
        raise TypeError("height and weight must be lists")
    if len(height) != len(weight):
        raise ValueError("height and weight must be the same length")
    result: list[float] = []
    for h, w in zip(height, weight):
        if not isinstance(h, (int, float)) or not isinstance(w, (int, float)):
            raise TypeError("height and weight elements must be int or float")
        if h == 0:
            raise ValueError("height elements must be non-zero")
        bmi = w / (h ** 2)
        result.append(bmi)
    return result


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Return booleans indicating which BMI values exceed `limit`.

    Args:
        bmi: list of BMI values (int or float).
        limit: integer threshold to compare against.

    Returns:
        List of booleans where each element is True if bmi > limit.

    Raises:
        TypeError: if `bmi` is not a list or contains non-numeric elements.
        TypeError: if `limit` is not int.
    """
    if not isinstance(bmi, list):
        raise TypeError("bmi must be a list")
    if not isinstance(limit, int):
        raise TypeError("limit must be an int")
    result: list[bool] = []
    for v in bmi:
        if not isinstance(v, (int, float)):
            raise TypeError("bmi elements must be int or float")
        result.append(v > limit)
    return result
