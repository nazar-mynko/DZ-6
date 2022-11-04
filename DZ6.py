try:
    result = []
    def divideer(a,b):
        if a < b:
            raise ValueError
            if b > 100:
                raise IndexEror
            return a/b
    date = {10: 2, 2: 5, "123": 4, 18: 0, []: 15, 8 : 4}
    for key in data:
        res = divider(key, data[kem])
        result.append(res)

    print(result)
except (TypeError, NameError, IndexError, ZeroDivisionError, SyntaxError, ValueError) as error:
    print(error)
