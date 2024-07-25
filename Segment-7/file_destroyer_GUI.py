from pathlib import Path
from PyQt6.QtWidgets import QApplication,QWidget,QVBoxLayout,QLabel,QPushButton,QFileDialog
from PyQt6.QtCore import Qt



# function to open files
def open_files():
    global filenames
    filenames, _ = QFileDialog.getOpenFileNames(window,'Select files')
    message.setText('\n'.join(filenames))



# function to destroy file
def destroy_files():
    for filename in filenames:
        path = Path(filename)
        with open(path,'wb') as file:
            file.write(b'')
        path.unlink()
    message.setText('Destruction Successful!')


# GUI code

app = QApplication([])
window = QWidget()
window.setWindowTitle("File Destroyer")

layout = QVBoxLayout()
description = QLabel('Select the files you want to destroy.The files will be <font color="red">permanently</font> deleted')
layout.addWidget(description)

#adding file open button

open_btn = QPushButton('Open Files')
open_btn.setFixedWidth(100)
layout.addWidget(open_btn,alignment=Qt.AlignmentFlag.AlignCenter)
open_btn.clicked.connect(open_files)

# adding file destroy button
destroy_btn = QPushButton('Destroy Files')
destroy_btn.setFixedWidth(100)
layout.addWidget(destroy_btn,alignment=Qt.AlignmentFlag.AlignCenter)
destroy_btn.clicked.connect(destroy_files)


# adding a label to see the files which are going to be deleted

message = QLabel('')
layout.addWidget(message,alignment=Qt.AlignmentFlag.AlignCenter)
# executing
window.setLayout(layout)
window.show()
app.exec()


