# Sample Input 1:

# 7-301-447-5820
# Sample Output 1:

# YES
# Sample Input 2:

# 301-447-5820
# Sample Output 2:

# YES
# Sample Input 3:

# 301-4477-5820

s = [i for i in input().split('-')]
if [len(i) for i in s] == [1, 3, 3, 4] and ''.join(s).isdigit() and s[0] == '7' or [len(i) for i in s] == [3, 3, 4] and ''.join(s).isdigit():
    print('YES')
else:
    print('NO')
        

    
