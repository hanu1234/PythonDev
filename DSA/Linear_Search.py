def locate_card(card: list, query: int) -> int:
    """Locate the position of the query number in the given list of cards.
    :type card: object
    :type query: object
    """
    print(f"Given list of cards: {card}")
    print(f"Given query number: {query}")

    for index in range(len(card)):
        if card[index] == query:
            print(f"given number:{query} present at position {index}")
            return index
    print(f"Given number {query} not present in the given list of cards")
    return -1


cards = [13, 12, 10, 7, 6, 5]
query = 15
locate_card(cards, query)
