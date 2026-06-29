# PhilGEPS Bid Monitoring Web App

This project converts the existing Excel-based Bid Monitoring sheet into a Flask web application with a SQLite database backend.

## Goals
- Build a simple Flask application for `Bid Monitoring`
- Use `Flask`, `SQLAlchemy`, `openpyxl`, `Bootstrap`, and basic JavaScript
- Make the app available on the office server so other PCs can access it

## Setup
1. Open PowerShell in this project folder.
2. Create a Python virtual environment:
   ```powershell
   python -m venv .venv
   ```
3. Activate the virtual environment:
   - Windows PowerShell:
     ```powershell
     .\.venv\Scripts\Activate.ps1
     ```
   - Windows CMD:
     ```cmd
     .\.venv\Scripts\activate.bat
     ```
4. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```
5. Import the Excel data into SQLite (if needed):
   ```powershell
   python import_data.py
   ```
6. Start the Flask app:
   ```powershell
   python app.py
   ```
7. Open a browser and visit:
   ```text
   http://localhost:5000
   ```

## Portable setup for another PC
To move this system to another PC, copy the entire project folder and follow these steps:
1. Copy the whole project folder, including:
   - `app.py`
   - `models.py`
   - `requirements.txt`
   - `README.md`
   - `templates/`
   - `static/`
   - `uploads/` (if you need existing uploaded files)
   - `app.db` (important: contains your database data)
2. Open PowerShell in the copied folder on the other PC.
3. Create a virtual environment:
   ```powershell
   python -m venv .venv
   ```
4. Activate the virtual environment:
   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```
5. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```
6. If you copied `app.db`, you are ready to run the app. If you did not copy `app.db`, import the data now:
   ```powershell
   python import_data.py
   ```
7. Start the app:
   ```powershell
   python app.py
   ```
8. Open a browser and go to:
   ```text
   http://localhost:5000
   ```

## Notes
- The app stores bid monitoring records in `app.db`.
- Use `--host=0.0.0.0` if you start Flask manually to make it available on the local network.
- For production, consider running behind a WSGI server such as `waitress` or `gunicorn`.
