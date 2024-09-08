import sys

from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton


class TemperatureConverter(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()

        self.temp_label = QLabel("Enter Temperature in Celsius(C): ")
        self.input = QLineEdit()
        self.convert_button = QPushButton("Convert to Fahrenheit")
        self.result_label = QLabel('')

        self.layout.addWidget(self.temp_label)
        self.layout.addWidget(self.input)
        self.layout.addWidget(self.convert_button)
        self.layout.addWidget(self.result_label)

        self.setLayout(self.layout)

        self.convert_button.clicked.connect(self.calculate_fahrenheit)

    def calculate_fahrenheit(self):
        celsius = float(self.input.text())
        fahrenheit = (celsius * 9/5) + 32
        self.result_label.setText(f"{celsius} in fahrenheit is {str(fahrenheit)}")


app = QApplication(sys.argv)
window = TemperatureConverter()
window.show()

sys.exit(app.exec())
