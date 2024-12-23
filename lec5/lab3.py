def make_change(amount, coins):
    """Return a list of coins that sum to amount, preferring the smallest coins
    available and placing the smallest coins first in the returned list.

    The coins argument is a dictionary with keys that are positive integer
    denominations and values that are positive integer coin counts.

    >>> make_change(2, {2: 1})
    [2]
    >>> make_change(2, {1: 2, 2: 1})
    [1, 1]
    >>> make_change(4, {1: 2, 2: 1})
    [1, 1, 2]
    >>> make_change(4, {2: 1}) == None
    True

    >>> coins = {2: 2, 3: 2, 4: 3, 5: 1}
    >>> make_change(4, coins)
    [2, 2]
    >>> make_change(8, coins)
    [2, 2, 4]
    >>> make_change(25, coins)
    [2, 3, 3, 4, 4, 4, 5]
    >>> coins[8] = 1
    >>> make_change(25, coins)
    [2, 2, 4, 4, 5, 8]
    """
    if not coins:
        return None
    smallest = min(coins)
    rest = remove_one(coins, smallest)
    if amount < smallest:
        return None
    amount=amount-smallest
    

def remove_one(coins, coin):
    """Remove one coin from a dictionary of coins. Return a new dictionary,
    leaving the original dictionary coins unchanged.

    >>> coins = {2: 5, 3: 2, 6: 1}
    >>> remove_one(coins, 2) == {2: 4, 3: 2, 6: 1}
    True
    >>> remove_one(coins, 6) == {2: 5, 3: 2}
    True
    >>> coins == {2: 5, 3: 2, 6: 1} # Unchanged
    True
    """
    copy = dict(coins)
    count = copy.pop(coin) - 1  # The coin denomination is removed
    if count:
        copy[coin] = count      # The coin denomination is added back
    return copy