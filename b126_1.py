table = 7
for i in range(1, 13):
    print('What\'s', i, 'x', table, '?')
    quess = input()
    ans = i * table
    if int (quess) == ans:
        print('Corect!')
    else:
        print('No, it\'s', ans)
print('Finished')