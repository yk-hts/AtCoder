x = list(input())

choku = ['ch','o','k','u']

if x == list('chokuou'):
    print('YES')
    exit()

for i in range(len(x)):
    judge = 0
    if x[len(x)-i-1] in choku:
        judge = 1
    
    if x[len(x)-i-1] == 'h' and x[len(x)-i-2] == 'c':
        judge = 1
        i += 1
        
    
    if judge == 0:
        print('NO')
        exit()
print('YES')