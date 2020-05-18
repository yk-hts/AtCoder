import fractions
N = int(input())
t_lcm = int(input())
for i in range(N-1):
  t = int(input())
  t_lcm = (t_lcm*t)//fractions.gcd(t,t_lcm)
print(t_lcm)

