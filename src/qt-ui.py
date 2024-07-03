import sys
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QGridLayout,
    QWidget,
    QLabel,
)
from PySide6.QtGui import QPixmap
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

        # Colors for borders
        colors = ["#ED7D3A", "#1E90FF", "#0CCE6B", "#DCED31", "#EF2D56"]

        # Load the image and set up the QLabel
        pixmap = QPixmap("./assets/sparkles_72x72.png").scaled(
            64, 64, Qt.KeepAspectRatio, Qt.SmoothTransformation
        )
        image_label = QLabel()
        image_label.setPixmap(pixmap)
        image_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(image_label, 2, 0)  # Place in first column

        # Emoji and button text
        buttons = [
            "Summarize",
            "Compose Mail",
            "Fix Grammar",
            "Extract Keywords",
            "Explain",
        ]

        # Add buttons to the grid
        for i, text in enumerate(buttons):
            button = QPushButton(text)
            # Set button styles with dynamic color assignment and transition effects
            button.setStyleSheet(f"""
                QPushButton {{
                    background-color: white;
                    color: black;
                    border: 2px solid {colors[i]};
                    border-radius: 15px;
                    padding: 10px;
                    font-size: 16px;
                    margin: 5px;
                    transition: transform 0.3s ease, background-color 0.3s ease;
                }}
                QPushButton:hover {{
                    background-color: {colors[i]};
                    color: white;
                    transform: scale(1.1);
                }}
            """)
            layout.addWidget(button, i, 1)  # Place in second column

        layout.setAlignment(Qt.AlignCenter)  # Center the layout


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
