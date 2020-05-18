n,m = map(int,input().split())
long = (n%12+m/60)*30
short = m*6
print(min([abs(long-short),abs(360-abs(long-short))]))
