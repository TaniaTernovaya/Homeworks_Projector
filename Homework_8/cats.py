def cats(number_cats: list, number_round) -> list:
    cats = [1 for i in range(number_cats)]
    result = []
    for i in range(2, number_round + 1):
        for number, cat in enumerate(cats):
            if ((number + 1) % i == 0) and (cat == 0):
                cats[number] = 1
            if ((number + 1) % i == 0) and (cat == 1):
                cats[number] = 0
    for number, hat in enumerate(cats, start=1):
        if hat == 1:
            result.append(number)
    return result


print(cats(100, 100))
