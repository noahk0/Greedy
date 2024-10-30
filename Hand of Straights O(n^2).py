def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
    if len(hand) % groupSize:
        return False

    hand = Counter(hand)

    for i in sorted(hand):
        if hand[i]:
            for j in range(1, groupSize):
                if hand[i + j] < hand[i]:
                    return False

                hand[i + j] -= hand[i]

    return True
