from icecream import ic, install
install() 
from PySide6.QtWidgets import QApplication
import pandas as pd
import numpy as np
from get_month_year import get_month_year
from gather_income_accounts import gather_income_accounts
from gather_income_account_values import gather_income_account_values
from gather_income_assets import gather_income_assets
from gather_income_asset_values import gather_income_asset_values
from gather_debt_accounts import gather_debt_accounts

'''
0. Ask user the month and year

1. Gather income sources from user
a. Ask User for account type
b. Ask User for account's value

2. Gather assets from user
a. Ask user for type of asset
b. Ask user for asset value

3. Gather debt sources from user
a. Ask user for debt type
b. Ask user for debt value

4. Add the income and assets together as revenue
5. Subtract the debts from revenue

6. Export to CSV
'''

app = QApplication([])  # Create the QApplication instance here


# Welcom message
print(
'''
Welcome to the Net Income Calculator. There are multiple accounts, assets and debts
to gather. 

Accounts, for example:
-Checking/savings accounts
-Retirement Accounts (401k, Roth)
-Stock Brokerage Accounts
-Crypto accounts (Coinbase, Cold Wallets)


Assets, for example:
-House Value:
-Car Value:

Debts, for example:
-Cred card debt
-Student loans
-Personal loans
-Mortgage

''')
month, year = get_month_year()
ic(month,year)

# 1a
user_account_list = gather_income_accounts(app)
ic(user_account_list)

# 1b (Updated to use the new function)
account_list, account_value_dict = gather_income_account_values(app, user_account_list)
ic(account_list, account_value_dict)

# 2a
user_asset_list = gather_income_assets()
ic(user_asset_list)

# 2b
asset_list, asset_values_dict = gather_income_asset_values(user_asset_list)
ic(asset_list, asset_values_dict)

# 3a
debt_list = gather_debt_accounts()
ic(debt_list)

