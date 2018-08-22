urls = [
    "http://www.google.com/a.txt",
    "http://www.google.com.tw/a.txt",
    "http://www.google.com/download/c.jpg",
    "http://www.google.co.jp/a.txt",
    "http://www.google.com/b.txt",
    "https://facebook.com/movie/b.txt",
    "http://yahoo.com/123/000/c.jpg",
    "http://gliacloud.com/haha.png",
]

dic=[]
count=[]


for i in range(0, len(urls)):
    s = "";
    for j in range(len(urls[i])-1, -1, -1):
        if urls[i][j] == '/':
            break
        else :
            s = s+urls[i][j]

    j = 0
    while j < len(dic):
        if dic[j] == s:
            count[j] += 1
            break
        j += 1

    #print(j)
    if j == len(dic):
        dic.append(s)
        count.append(1)

    #print(s)

first = -1
second = -1
third = -1
index_1 = -1
index_2 = -1
index_3 = -1

for i in range(0, len(dic)):
    if count[i] > first:
        index_3 = index_2
        index_2 = index_1
        index_1 = i
        third = second
        second = first
        first = count[i]
    elif count[i] > second:
        index_3 = index_2
        index_2 = i
        third = second
        second = count[i]
    elif count[i] > third:
        index_3 = i
        third = count[i]
    #print(dic[i] , count[i])

print(dic[index_1], first)
print(dic[index_2], second)
print(dic[index_3], third)
