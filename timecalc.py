print(' ')
time_ammount = int(input(f'How many durations would you like to add? '))
print('')
hour = []
min = []

for i in range(time_ammount):
    print('----- DURATION ' + str(i+1) + ' -----')
    h = int(input(f'Hour(s): '))
    m = int(input(f'Minute(s): '))
    print('')
    hour.append(h)
    min.append(m)

hours = sum(hour)
minutes = sum(min)

while minutes >= 60:
    minutes = minutes - 60
    hours = hours + 1

print('\nTotal Duration = ' + str(hours) + 'hr ' + str(minutes) + 'min\n')
