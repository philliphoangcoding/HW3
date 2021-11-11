#Name: Phillip Hoang ID: 1877593
my_list = []
the_list = input()
n = len(the_list)
for i in the_list.split():
    if int(i) >= 0:
        my_list.append(int(i))
        my_list.sort()
for x in my_list:
    print(x,end=' ')