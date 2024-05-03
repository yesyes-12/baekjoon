#2941 크로아티아 알파벳
s = input()
cAlphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for ca in cAlphabet:
    s = s.replace(ca, ' ')
print(len(s))