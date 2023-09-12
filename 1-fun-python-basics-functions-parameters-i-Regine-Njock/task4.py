# def sumAll(*lists):
#     #print(lists)
#     sum1 = 0
#     for i in lists:
#         sum1 += sum(i)
#         return sum1



# test1 = [[0, 2, 4, 5]]
# test2 = [[0, 2, 4, 5],[6],[0, 2, 4, 5, 1, 4, 3, 2]]

# print(sumAll(*test1))
# print(sumAll(*test2))
def sumAll():

    test1 = [[0, 2, 4, 5]]
    test2 = [[0, 2, 4, 5],[6],[0, 2, 4, 5, 1, 4, 3, 2]]
    sum_1 = sum (sum(test1,[]))
    sum_2 = sum (sum(test2,[]))
    print(sum_1)
    print(sum_2)
sumAll()
