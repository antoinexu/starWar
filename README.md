# Star Wars Character Information Web Application

## Description
This is a web application that allows users to get information about Star Wars characters. Users can enter the name of a character, and the application will display relevant information about the character, including home planet details, species information, and starships they are associated with.

## Getting Started
### Prerequisites
- Python (version 3.9.7)
- Flask (version 2.3.2)

### Installation
1. Clone this repository:

```bash
git clone git@github.com:antoinexu/starWar.git
```

2. Install the required dependencies:
```bash
pip install flask
```

### Usage
Run the Flask application:
```bash
python app.py
```
1. Access the application in your web browser by visiting http://127.0.0.1:5000.
2. Enter the name of a Star Wars character in the provided form and click the "Get Information" button.
3. If there's only one character with the given name, detailed information about that character will be displayed.
4. If multiple characters are found with the same name, a list of characters will be shown, and the user can choose the desired character to view detailed information.
5. If no character is found for the entered name, a message will be displayed indicating that no character was found.

