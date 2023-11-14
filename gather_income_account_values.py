import icecream as ic 

def gather_income_account_values(user_list):
    source_value_dict = {}
    source_list = set(user_list)
    
    for source in source_list:
        while True:
            user_input = input(f'Please enter the value for {source}: ')
            try:
                source_value = float(user_input)
                if source_value < 0:
                    print('Cannot be negative value...')
                else:
                    source_value_dict[source]=source_value
                break
            except ValueError:
                print('Not numeric, please re-enter...')
                    

    return source_list, source_value_dict
