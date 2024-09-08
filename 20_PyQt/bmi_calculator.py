from PyQt6.QtWidgets import QApplication, QVBoxLayout, QWidget, QLineEdit, QLabel, QPushButton
import sys


class BmiCalculator(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("BMI Calculator")

        self.layout = QVBoxLayout()

        self.weight_label = QLabel("Enter weight in Kg")
        self.weight_input = QLineEdit()

        self.height_label = QLabel("Enter Height in cm")
        self.height_input = QLineEdit()

        self.calculate_button = QPushButton("Calculate BMI")

        self.result_label = QLabel("")

        self.layout.addWidget(self.weight_label)
        self.layout.addWidget(self.weight_input)
        self.layout.addWidget(self.height_label)
        self.layout.addWidget(self.height_input)
        self.layout.addWidget(self.calculate_button)
        self.layout.addWidget(self.result_label)


        self.setLayout(self.layout)

        self.calculate_button.clicked.connect(self.calculate_bmi)

    def calculate_bmi(self):
        try:
            weight = float(self.weight_input.text())
            height = float(self.height_input.text()) / 100

            bmi = weight / (height ** 2)
            self.result_label.setText(f"Your BMI is {bmi}")
        except ValueError:
            self.result_label.setText("Please enter valid numbers")


app = QApplication(sys.argv)
window = BmiCalculator()
window.show()

sys.exit(app.exec())
