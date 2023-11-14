import numpy as np


def gather_income_accounts():
    sources = []
    complete = False
    more_sources = ''
    while not complete:
        source = input(f'Please name the account: ')
        sources.append(source)
        
        more_sources = input(f'Do you have more accounts to add? \n y/n: ') 
        if more_sources.lower() != 'y':
            complete = True      
    return sources


