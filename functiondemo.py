
def sum(start, end):
    '''Calculate sum of list [start, end].'''
    total = 0

    for i in range(start, end + 1):
        total += i

    return total


print('Tong cac so tu 1 den 10:', sum(1, 10))
