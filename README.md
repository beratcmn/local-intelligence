# Local Intelligence

Local Intelligence is a versatile desktop application designed to perform various text processing tasks using a sophisticated language model. It provides an intuitive GUI with buttons for summarizing text, composing emails, fixing grammar, extracting keywords, and explaining text. The application leverages advanced machine learning models to generate accurate and contextually appropriate outputs.


https://github.com/beratcmn/local-intelligence/assets/47108366/cc223c7e-cae0-465e-9663-b6dad4bf5820


## Table of Contents

- [Local Intelligence](#local-intelligence)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Todo](#todo)
  - [Installation](#installation)
    - [Prerequisites](#prerequisites)
    - [Steps](#steps)
  - [Usage](#usage)
  - [Contributing](#contributing)
  - [License](#license)
  - [Contact](#contact)

## Features

- **Summarize Text:** Get concise summaries of lengthy text.
- **Compose Emails:** Automatically draft emails based on input text.
- **Fix Grammar:** Correct grammatical errors in your text.
- **Extract Keywords:** Identify key terms and phrases.
- **Explain Text:** Generate explanations for complex text.
- **Rephrase Generated Text:** Rephrase the generated text based on the desired tone. Tones are categorized as `Casual`, `Formal`, `Professional`, `Technical`, `Simple`.

## Todo

- [ ] Add CPU only LLM inference
- [x] Add more features such as rephrasing based on the desired tone
- [x] Ensure the application is running smoothly on Mac
- [ ] Ensure the application is running smoothly on Linux
- [ ] Build the project to a standalone executable for Windows, macOS, and Linux
- [ ] Create a user-friendly installer for the application
- [ ] Learn how to be a open source maintainer

## Installation

### Prerequisites

- Python 3.8 or higher

### Steps

1. **Clone the repository:**

   ```sh
   git clone https://github.com/beratcmn/local-intelligence.git
   cd local-intelligence
   ```

2. **Create a virtual environment:**

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate.ps1 or venv\Scripts\activate.bat`
   ```

3. **Install the dependencies:**

   ```sh
   pip install -r requirements.txt
   ```

4. **Download the pre-trained language model:**
   - Don't worry, llama.cpp got you covered. It will automatically download the model for you to the `./models` directory.

## Usage

1. **Run the application:**

   ```sh
   python src/app.py
   ```

2. **Use the GUI:**
   - Press `CTRL + SPACE` to toggle the application window.
   - Copy the text you want to process to the clipboard. (For now, the application only supports clipboard input.)
   - Select the desired task by clicking the appropriate button.
   - The result will be displayed in a new window and copied to the clipboard.

## Contributing

I welcome contributions from the community! Here's how you can help:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a Pull Request.

## License

This project is licensed under the Apache 2.0 License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or issues, please open an issue in this repository or contact the project maintainers.

- [Berat Çimen](https://github.com/beratcmn)
