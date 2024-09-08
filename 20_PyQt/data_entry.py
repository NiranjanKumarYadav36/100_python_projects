from PyQt6.QtWidgets import QWidget, QVBoxLayout, QApplication, QLineEdit, QLabel, QMessageBox, QPushButton
import sys, os


class DataEntryTool(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Data Entry")
        self.setGeometry(500, 300, 300, 100)

        self.layout = QVBoxLayout()

        self.first_name = QLineEdit()
        self.first_name.setPlaceholderText("Enter the first name")

        self.last_name = QLineEdit()
        self.last_name.setPlaceholderText("Enter the last name")

        self.submit_button = QPushButton("Submit")
        self.submit_button.clicked.connect(self.data_entry)

        self.layout.addWidget(self.first_name)
        self.layout.addWidget(self.last_name)
        self.layout.addWidget(self.submit_button)

        self.setLayout(self.layout)

    def data_entry(self):
        first = self.first_name.text().capitalize()
        last = self.last_name.text().capitalize()

        # Check if both fields are filled
        if not first or not last:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Icon.Warning)
            msg_box.setText("Please fill both fields!")
            msg_box.setWindowTitle("Warning")
            msg_box.exec()
            return

        # Write to CSV file
        if os.path.isfile("data.csv"):
            with open("data.csv", "a") as file:
                file.write(f"{first}, {last}\n")
        else:
            with open("data.csv", 'w') as file:
                file.write("First Name, Last Name\n")
                file.write(f"{first}, {last}\n")

        # Show success message
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Icon.Information)
        msg_box.setText("Data successfully added!")
        msg_box.setWindowTitle("Information")
        msg_box.exec()

        # Clear the input fields
        self.first_name.clear()
        self.last_name.clear()


app = QApplication(sys.argv)
window = DataEntryTool()
window.show()

sys.exit(app.exec())
