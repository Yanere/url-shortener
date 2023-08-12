
#  URL Shortener
The Flask URL Shortener is a web application that allows users to create shortened versions of long URLs. This is achieved using the Flask framework, SQLite database for data storage, and Python for backend logic. Additionally, the application includes a static folder for CSS styles to enhance the user interface.

## Getting Started
### Prerequisites
Before you begin, ensure you have the following installed:

- [Python](https://www.python.org/downloads/) 
- [Flask](https://flask.palletsprojects.com/) 

### Installation
1. Clone the Repository: Clone this repository to your local machine using the following command:
```bash
git clone https://github.com/Yanere/url-shortener.git
``` 

2. Navigate to the Project Directory: Move to the project directory using the command:
```bash
cd flask-url-shortener
```

3. Run the Application: Start the Flask web server and run the application by executing:
```bash
python3 shortener.py

```

4. Access the Application: Open your web browser and visit [http://127.0.0.1:5000/](http://127.0.0.1:5000/)  access the homepage of the URL shortener.

## Usage

1. Shorten a URL:

- Enter a long URL in the input field on the homepage.
- Click "Shorten" to generate a shortened URL.
- You'll be redirected to a page displaying a randomly generated 6-character string.

2. Access Shortened URLs:

- To access a shortened URL, append the 6-character string to your IP address, e.g., http://127.0.0.1:5000/abcdef.

## File Structure

The project structure is as follows:

- shortener.py: The main Flask application script containing URL routing and database setup.
- templates/: Contains HTML templates used by the Flask application.
- static/: Contains CSS styles for the user interface.

## Database Setup

The SQLite database is automatically created when you run the application. The shortener.py script defines the necessary database schema and handles table creation.

## Custom Styles (CSS)

Customize the user interface using the CSS styles located in the static/ directory.

## Contributing

Contributions are welcome! If you encounter issues or have suggestions for improvements:

- Open an issue to discuss changes.
- Fork the repository and create a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE)  for details.
