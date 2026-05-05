# Hello World Python GUI

A simple "Hello World" Python project with a graphical user interface (GUI).

## Project Structure
- `main.py`: Main application file.
- `requirements.txt`: Python dependencies.
- `.gitignore`: Files and directories to ignore.
- `.gitattributes`: Line ending and encoding normalization.

## Git Flow
This project follows the Git Flow branching model:
- `main`: Production-ready code.
- `develop`: Integration branch for features.
- `feature/*`: New features in development.
- `release/*`: Preparation for a new production release.
- `hotfix/*`: Critical bug fixes for production.

## Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/timteam/hello-world-python-gui.git
   cd hello-world-python-gui
   ```
2. Initialize Git Flow (if not already done):
   ```bash
   git flow init -d
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   python main.py
   ```