def isListOfInts(l):
    if type(l) is not list:
        raise ValueError(l + ' - arg not of <list> type')

    else:
        if len(l) == 0:
            return True
        else:
            qty = 0
            for x in l:
                if type(x) is not int:
                    qty += 1
                    break
            if qty == 0:
                return True
            else:
                return False


print(isListOfInts([]))
print(isListOfInts([1]))
print(isListOfInts([1, 2]))
print(isListOfInts([0]))
print(isListOfInts(['1']))
print(isListOfInts([1, 'a']))
print(isListOfInts(['a', 1]))
print(isListOfInts([1, 1.0]))
print(isListOfInts([1.0, 1.0]))
print(isListOfInts('a'))
