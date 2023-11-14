import datetime as datetime
import numpy as np

def get_month_year():
    # initialize variables
    months = np.array(['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec'])
    month = ''
    year = ''
    now_time = datetime.datetime.now()
    print(f'The current datetime is {now_time}')
    confirm = input(f'Please confirm you are entering net worth for \n {now_time.month} {now_time.year} \n Y or N: ')
    ic(confirm)
    if confirm.lower() != 'y':
        while month not in months:
            print('Invalid month, try again')
            month = input(f'Please enter the desired month: \n {months} \n')
            
        year = input(f'Please enter the year: ')        
        while not year.isdigit() or int(year) <2020 or int(year) > now_time.year:
            print('Invalid year, try again')
            year = input(f'Please enter the year: ')    
            
    else:
        month = months[now_time.month - 1] # string representation
        year = now_time.year
            

     # Convert month back to number if needed
    month_number = np.where(months == month)[0][0] + 1
    ic(month_number, year)
    
    # Now you can return or process the month and year as needed
    return month_number, year
