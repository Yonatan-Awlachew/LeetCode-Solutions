counter = {}
        for x in strs:
            a=''.join(sorted(x))
            if a in counter:counter[a].append(x)
            else: counter[a]=[x]
        result = list(counter.values())
        return result
