def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
    possible = [False] * 3

    for triplet in triplets:
        if not possible[0] and triplet[0] == target[0] and triplet[1] <= target[1] and triplet[2] <= target[2]:
            possible[0] = True

        if not possible[1] and triplet[1] == target[1] and triplet[0] <= target[0] and triplet[2] <= target[2]:
            possible[1] = True

        if not possible[2] and triplet[2] == target[2] and triplet[0] <= target[0] and triplet[1] <= target[1]:
            possible[2] = True

        if possible[0] and possible[1] and possible[2]:
            return True
