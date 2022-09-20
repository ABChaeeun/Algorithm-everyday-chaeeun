num = int(input())

for _ in range(num):
    year_month_day = int(input())
  
    year = int(year_month_day / 10000)
    month = int(year_month_day / 100 % 100)
    day = int(year_month_day % 100)
  
    if month >= 1 and month <= 12:
        if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
            if day >= 1 and day <= 31:
                print("%04d/%02d/%02d" %(year, month, day))
            else:
                print("-1")
    
        elif month == 2:
            if day >= 1 and day <= 28:
                print("%04d/%02d/%02d" %(year, month, day))
            else:
                print("-1")
    
        elif month == 4 or month == 6 or month == 9 or month == 11:
            if day >= 1 and day <= 30:
                print("%04d/%02d/%02d" %(year, month, day))
            else:
                print("-1")
            
        else:
            print("-1")
  
    else:
        print("-1")