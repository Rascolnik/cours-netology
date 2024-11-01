def vote(votes):
    some_num = []
    for num in votes:
        b = votes.count(num)
        if b > 1:
            if num not in some_num:
                some_num.append(num)

    return some_num[0]

if __name__ == '__main__':
    print(vote([1,1,1,2,3]))
    print(vote([1,2,3,2,2]))