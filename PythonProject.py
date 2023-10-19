import datetime

def ageCalculate(year, month, date):                            #ye age ke-liye function
    today = datetime.datetime.now().date()
    dob = datetime.date(year, month, date)
    years= ((today-dob).total_seconds()/ (365.242*24*3600))
    yearsInt=int(years)
    months=(years-yearsInt)*12
    monthsInt=int(months)
    days=(months-monthsInt)*(365.242/12)
    daysInt=int(days)
    print('You Are {0} Years, {1} Months And {2} Days Old. \n'.format(yearsInt,monthsInt,daysInt))

def remainingdays(yearinp, monthsinp, dateinp):  #ye days remaining ke liye -function
    today = datetime.date.today()
    dob = datetime.date(yearinp, monthsinp, dateinp)
    if(
        today.month == monthsinp
        and today.day >= dateinp
        or today.month > monthsinp                                          
    ):
        nextBirthdayYear = today.year+1
    else:
        nextBirthdayYear = today.year
        nextBirthday = datetime.date(
        nextBirthdayYear, monthsinp, dateinp
)

    print("Next birthday: ", nextBirthday)

    diff = nextBirthday - today
    print("Days left for next birthday: ", diff.days)                      
while True:                                                             #loops for retry
    yearinp = int(input("Enter Year Of Birth in YYYY :\t"))  
    if yearinp <1000 or yearinp>9999:
        print("Invalid year") 
        break              #user entry
    monthsinp = int(input("Enter Month of Birth MM:\t"))
    if monthsinp<1 or monthsinp>12:
        print("invalid month")
        break
    dateinp = int(input("Enter Date DD :\t"))
    if dateinp<1 or dateinp>31:
             print("invalid date")
             break

    ageCalculate(yearinp, monthsinp, dateinp)                                       #call functions
    remainingdays(yearinp, monthsinp, dateinp)
    a = input('Type y to Continue \n n To Exit \n') 
    if a == 'y':
        continue
    else:
        break
