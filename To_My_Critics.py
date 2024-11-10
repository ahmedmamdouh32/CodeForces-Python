#Task Name : To My Critics
#Link : https://codeforces.com/contest/1850/problem/A

t = int(input())
while t > 0:
    a, b, c = map(int, input().split())
    l = [a,b,c]
    l.sort(reverse = True)
    if l[0] + l[1] >= 10:
        print("YES")
    else:
        print("NO")
    t-=1