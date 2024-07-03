import sys
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QGridLayout,
    QWidget,
    QLabel,
)
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
        layout = QGridLayout(central_widget)

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

        # Define emoji label style
        emoji_style = "font-size: 36px;"

        # Emoji and button text
        buttons = [
            "Summarize",
            "Compose Mail",
            "Fix Grammar",
            "Extract Keywords",
            "Explain",
        ]
        emoji = "✨"

        # Add emoji and buttons to the grid
        emoji_label = QLabel(emoji)
        emoji_label.setStyleSheet(emoji_style)
        emoji_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(emoji_label, 2, 0)  # Place in first column
        for i, text in enumerate(buttons):
            # Create emoji label

            # Create button
            button = QPushButton(text)
            button.setStyleSheet(button_style)
            layout.addWidget(button, i, 1)  # Place in second column

        layout.setAlignment(Qt.AlignCenter)  # Center the layout


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
