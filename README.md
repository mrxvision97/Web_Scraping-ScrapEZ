# ScrapEZ

ScrapEZ is a web application that allows you to extract data from any website in CSV or JSON format. It utilizes Python's web scraping libraries like BeautifulSoup and Requests, and is built with the modern FastAPI framework for the backend and Vue.js for the frontend.

## Features

- **User-Friendly Interface**: Intuitive and easy-to-use interface for entering the target URL and selecting the desired output format.
- **Dynamic Web Scraping**: Scrape data from any website with customizable scraping logic.
- **Multiple Output Formats**: Download scraped data in CSV or JSON format for easy integration with other tools or analysis.
- **Modern Tech Stack**: Leverages the power of FastAPI for the backend API and Vue.js for the reactive frontend.
- **Responsive Design**: Seamless experience across different devices and screen sizes.

## Getting Started

### Prerequisites

- Python 3.7 or later
- Node.js (for Vue.js development server)

### Installation

1. Clone the repository:

```bash
git clone https://github.com/mrxvision97/Web_Scraping-ScrapEZ.git

```
2. Navigate to the project directory:
```bash
cd web-scraper
```
3. Create and activate a virtual environment (optional but recommended):
```bash
python -m venv env
source env/bin/activate  # On Windows, use `env\Scripts\activate`
```
4. Install the Python dependencies:
```bash
pip install -r requirements.txt
```
5. Install the Node.js dependencies for the frontend:
```bash
cd frontend
npm install
```
### Running the Application
1. Start the FastAPI backend server:
```bash
uvicorn app.main:app --reload
```
2. In a separate terminal, navigate to the frontend directory and start the Vue.js development server:
```bash 
cd frontend
npm run serve   
```
3. Open your web browser and go to `http://localhost:8080` to access the Web Scraper application.

### Usage
1. Enter the target URL and select the output format (CSV or JSON) to scrape the website data.
2. Click the "Scrape" button to initiate the scraping process.
3. Once the scraping is complete, you can download the scraped data in the selected format.
4. For more advanced scraping, you can customize the scraping logic in the Python code under `app/scraper.py`.
5. To stop the FastAPI server, press `Ctrl + C` in the terminal where it is running.
6. To stop the Vue.js development server, press `Ctrl + C` in the terminal where it is running.
7. To deactivate the virtual environment (if used), run `deactivate` in the terminal.
8. To run the application in production mode, refer to the FastAPI and Vue.js documentation for deployment instructions.
9. For more information on how to use FastAPI and Vue.js, check out their official documentation and tutorials.
10. Happy scraping!

### Contributing
Contributions are welcome! If you find any issues or want to add new features, please open an issue or submit a pull request.

