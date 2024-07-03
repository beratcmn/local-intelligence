import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set window properties
        self.setWindowTitle("App Interface")
        self.setFixedSize(370, 409)  # Adjust size to match your design
        self.setAttribute(Qt.WA_TranslucentBackground)  # Enable transparency
        self.setWindowFlags(Qt.FramelessWindowHint)  # Remove window frame

        # Create central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Define button styles
        button_style = """
            QPushButton {
                background-color: #FFD700;
                color: white;
                border-radius: 15px;
                padding: 10px;
                font-size: 16px;
                margin: 5px;
            }
            QPushButton:hover {
                background-color: #FFA500;
            }
        """

        # Create buttons
        buttons = ["Summarize", "Compose Mail", "Fix Grammar", "Extract Keywords", "Explain"]
        for text in buttons:
            button = QPushButton(text)
            button.setStyleSheet(button_style)
            layout.addWidget(button)

        layout.setAlignment(Qt.AlignCenter)  # Center the layout

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
