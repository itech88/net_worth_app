import numpy as np

def gather_debt_accounts():
    sources = []
    complete = False
    more_sources = ''
    while not complete:
        source = input(f'Please name the debt ccount: ')
        sources.append(source)
        
        more_sources = input(f'Do you have more debt accounts to add? \n y/n: ') 
        if more_sources.lower() != 'y':
            complete = True      
    return sources


