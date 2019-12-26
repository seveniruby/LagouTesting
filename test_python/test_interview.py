def test_interview_1():
    data = [1, 2, 3, 11, 2, 5, 3, 2, 5, 3]
    result = list(set(data))
    print(result)


def test_interview_2():
    data = [1, 2, 3, 4, 5]
    result = data[10:]
    print(result)
    print(len(result))


def test_interview_3():
    data = [1, 2, 3, 5, 6]
    result = ''.join([str(d) for d in data])
    print(result)
