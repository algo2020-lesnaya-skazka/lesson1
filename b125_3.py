table = 7
for i in range(1, 13):
    print('What\'s', i, 'x', table, '?')
    quess = input()
    if quess == 'stop':
        break
    if quess == 'skip':
        print('Skipping')
        continue
    ans = i * table
    if int(quess) == ans:
        print('Correct!')
    else:
            print('No, it\'s', ans)
print('Finished')
    
