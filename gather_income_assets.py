
def gather_income_assets():
    sources = []
    complete = False
    more_sources = ''
    while not complete:
        source = input(f'Please name the asset: ')
        sources.append(source)
        
        more_sources = input(f'Do you have more assets to add? \n y/n: ') 
        if more_sources.lower() != 'y':
            complete = True      
    return sources


