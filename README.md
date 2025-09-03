# Flask Todo Application

A simple, clean todo application built with Flask and Bootstrap.

## Features

- Add new todos with title and description
- Mark todos as complete/incomplete
- Delete todos
- Clean, responsive UI
- SQLite database for data persistence
- Flash messages for user feedback

## Project Structure

```
todo-app/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── templates/          # HTML templates
│   ├── base.html      # Base template
│   └── index.html     # Main page template
├── static/            # Static files
│   └── css/
│       └── style.css  # Custom styles
└── README.md          # This file
```

## Installation

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python app.py
```

4. Open your browser and navigate to `http://localhost:5000`

## Usage

- **Add Todo**: Fill in the title (required) and optional description, then click "Add Todo"
- **Complete Todo**: Click the green checkmark button to mark as complete
- **Uncomplete Todo**: Click the yellow undo button to mark as incomplete
- **Delete Todo**: Click the red trash button to delete (with confirmation)

## Technologies Used

- **Backend**: Flask, SQLAlchemy
- **Frontend**: Bootstrap 5, Font Awesome
- **Database**: SQLite
- **Styling**: Custom CSS with Bootstrap components

## Security Notes

- Change the `SECRET_KEY` in production
- Consider using environment variables for configuration
- Add proper input validation for production use