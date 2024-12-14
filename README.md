# microblog
A blogging web application using Python and Flask.

## How to Run
1. Activate your virtual environment:
    ```bash
    source venv/bin/activate
    ```
2. Run the Flask application:
    ```bash
    flask run
    ```

## Possible Errors
- If you encounter issues accessing the application via `localhost:5000`, try running the Flask application with the following command:
    ```bash
    flask run --host=0.0.0.0
    ```