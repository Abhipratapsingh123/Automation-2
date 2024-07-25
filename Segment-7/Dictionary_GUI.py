from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout
from PyQt6.QtWidgets import QLabel, QPushButton, QLineEdit
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
import json

data = json.load(open("data.json"))

def translate():
    w = text.text()
    w = w.lower()
    if w in data:
        results = data[w]
        output_label.setText("\n".join(results))
    else:
        output_label.setText("The word doesn't exist. Please double check it.")

app = QApplication([])
window = QWidget()
window.setWindowTitle('Word Definition')

# Main layout
layout = QVBoxLayout()
layout.setSpacing(20)
layout.setContentsMargins(10, 10, 10, 10)

# Input layout
layout1 = QHBoxLayout()
layout.addLayout(layout1)

text_label = QLabel('Enter Word:')
text_label.setFont(QFont('American typewriter', 12))
layout1.addWidget(text_label)

text = QLineEdit()
text.setFont(QFont('American typewriter', 12))
layout1.addWidget(text)

btn = QPushButton('Convert')
btn.setFont(QFont('American typewriter', 12))
layout1.addWidget(btn, alignment=Qt.AlignmentFlag.AlignBottom)
btn.clicked.connect(translate)

# Output layout
layout2 = QVBoxLayout()
layout.addLayout(layout2)

output_label = QLabel('')
output_label.setFont(QFont('American typewriter', 12))
output_label.setWordWrap(True)
output_label.setAlignment(Qt.AlignmentFlag.AlignTop)
output_label.setStyleSheet("border: 1px solid gray; padding: 10px;")
layout2.addWidget(output_label)

window.setLayout(layout)
window.setMinimumSize(400, 200)
window.show()
app.exec()
