#input jam@ + avelacvox jam@
Enter_hour = int(input('Enter hour: '))

am_or_pm = int(input('Enter \n am = 1 \n pm = 2 ? '))

How_many_hours_ahead = int(input('How many hours ahead ? '))

New_hour = int(Enter_hour) + int(How_many_hours_ahead)

if New_hour > 12:
    New_hour -= int(12) 
    am_or_pm += int(1)
    
if am_or_pm > int(2) :
    am_or_pm -= int(2)

if am_or_pm == int(1) :
    am_or_pm = 'am'

if am_or_pm == int(2):
    am_or_pm = 'pm'

print(New_hour,am_or_pm)





