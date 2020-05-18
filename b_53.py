s = input()

a_index = s.index('A')
z_index = s.rfind('Z')
print(z_index-a_index+1)