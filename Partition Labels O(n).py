def partitionLabels(self, s: str) -> List[int]:
    end, offset, res, idx = 0, -1, [], {s[i]: i for i in range(len(s))}

    for i in range(len(s)):
        end = max(end, idx[s[i]])

        if i == end:
            res.append(i - offset)
            offset = i

    return res
