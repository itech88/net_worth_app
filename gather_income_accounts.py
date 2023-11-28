import numpy as np
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
'''
Allow users to enter various sources of income, including salary, investments, and any other revenue streams. 
Consider providing options for both one-time and recurring income.'''


class IncomeAccountWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.is_done = False  # Add a flag to indicate completion
        self.sources = []  # List to store account names
        self.init_ui()

    def done(self):
        self.is_done = True  # Set flag to True when done
        self.close()

    def add_account(self):
        account_name = self.account_input.text()
        if account_name:
            self.sources.append(account_name)  # Add to the sources list
            self.account_input.clear()
            print(f'Account "{account_name}" added.')
        else:
            print('Please enter a valid account name.')
        
    def init_ui(self):
        self.sources = []
        self.layout = QVBoxLayout()
        self.account_label = QLabel("Account Name:")
        self.account_input = QLineEdit()
        self.add_button = QPushButton("Add Account")
        self.add_button.clicked.connect(self.add_account)
        self.done_button = QPushButton("Done")
        self.done_button.clicked.connect(self.done)  # Connect to the new 'done' method
        
        self.layout.addWidget(self.account_label)
        self.layout.addWidget(self.account_input)
        self.layout.addWidget(self.add_button)
        self.layout.addWidget(self.done_button)
        
        self.setLayout(self.layout)
        
    def add_account(self):
        account_name = self.account_input.text()
        if account_name:
            self.sources.append(account_name)
            self.account_input.clear()
            print(f'Account "{account_name}" added.')
        else:
            print('Please enter a valid account name.')

def gather_income_accounts(app):
    source_list = []

    source_widget = IncomeAccountWidget()
    source_widget.show()

    while not source_widget.is_done:
        app.processEvents()  # Process GUI events
        if source_widget.sources:  # Check if new sources have been added
            source_list.extend(source_widget.sources)  # Add them to the list
            source_widget.sources = []  # Reset the sources in the widget

    return source_list



