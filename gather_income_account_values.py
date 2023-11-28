import icecream as ic
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton

# Check if a QApplication already exists, create one if it doesn't

class IncomeAccountValueWidget(QWidget):
    def __init__(self, source_name):
        super().__init__()
        self.source_name = source_name
        self.init_ui()
        
    def init_ui(self):
        self.value_label = QLabel(f"Enter the value for {self.source_name}:")
        self.value_input = QLineEdit()
        self.add_button = QPushButton("Add Value")
        self.add_button.clicked.connect(self.add_value)
        
        layout = QVBoxLayout()
        layout.addWidget(self.value_label)
        layout.addWidget(self.value_input)
        layout.addWidget(self.add_button)
        
        self.setLayout(layout)
        
    def add_value(self):
        user_input = self.value_input.text()
        try:
            source_value = float(user_input)
            if source_value < 0:
                print('Cannot be a negative value...')
            else:
                self.close()  # Close the widget after adding the value
                print(f'Value for {self.source_name}: {source_value}')
        except ValueError:
            print('Not numeric, please re-enter the value.')

def gather_income_account_values(app, user_list):
    source_value_dict = {}
    
    for source in user_list:
        value_widget = IncomeAccountValueWidget(source)
        value_widget.show()
        app.exec_()
        
        source_value = float(value_widget.value_input.text())
        source_value_dict[source] = source_value

    return user_list, source_value_dict

if __name__ == '__main__':
    user_list = ['Account 1', 'Account 2']  # Example list of income accounts
    account_list, account_value_dict = gather_income_account_values(user_list)
    ic(account_list, account_value_dict)