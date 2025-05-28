# SmartSectorScout

SmartSectorScout is a Python-based news aggregator and ranking system that fetches news articles from various sources, processes them using advanced NLP models, and ranks them by relevance in different industry sectors.

## Features

- Fetches news using RSS feeds and APIs
- Uses embedding models (like Cohere) for semantic ranking
- Supports multiple industry sectors such as Technology, Finance, Healthcare, Renewable Energy, etc.
- Modular code structure for easy extension and maintenance

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/SmartSectorScout.git
   cd SmartSectorScout

2. (Optional) Create and activate a virtual environment:

bash
Copy
Edit
python -m venv venv
source venv/bin/activate    # Linux/macOS
venv\Scripts\activate       # Windows

3. Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt

## Usage
Run the main script to fetch and rank news:

bash
Copy
Edit
python news_ranker.py
Make sure you have your API keys and configurations set up in utils/config/.

## Project Structure
bash
Copy
Edit
SmartSectorScout/
├── fetcher/           # Modules to fetch news articles (RSS, APIs)
├── ranker/            # Modules to rank and process news articles
├── utils/             # Configuration and utility scripts
├── news_ranker.py     # Main entry point script
├── requirements.txt   # Python dependencies
├── README.md          # This file

## Dependencies
Key packages used include:

newspaper3k

cohere

feedparser

lxml

requests

Check the requirements.txt for full list.

## Contributing
Contributions are welcome! Please fork the repository and create a pull request.

## License
This project is licensed under the MIT License.

## Created by Sahil Moharil