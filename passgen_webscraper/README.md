# Password generator

This is a simple webscraping project that focuses on generating a password that is both readable and strong.

## API routes

### /animal/webscrape - POST
- Route that scrapes the data from (1) to collect animal names and save it on db/data/animal.csv

### /yokai/webscrape - POST
- Route that scrapes the data from (2) to collect yokai names and save it on db/data/yokai.csv

### /password/generate - POST

It generates a password based on this pattern:
- (parts_of_speech)(separator)(noun_type)(special_character)(number)

- Parameters:
    - noun_type: The noun that the password will contain
        - supported types:
            - ANIMAL
            - YOKAI
            - PERSON
            - NOUN
            - RANDOM
        - parameter type: string

    - parts_of_speech: Parts of speech based on RandomWord.word

    - separator: Character or string that separes noun_type from parts_of_speech

    - special_character: Character that separes noun_type from number

    - min_num_rand: The minimum number that can be randomly generated

    - max_num_rand: The maximum number that can be randomly generated


## How to run

1. Install dependencies
- Make sure you have Python 3.9+ installed, then install the required packages:

```pip install -r requirements.txt```

2. Run the FastAPI server

```uvicorn main:app --reload```

3. Access the API docs
Once the server is running, open your browser and navigate to:

    Swagger UI: http://127.0.0.1:8000/docs

    ReDoc: http://127.0.0.1:8000/redoc

4. Test the routes

    - Use a tool like Postman, curl, or the interactive Swagger UI to POST to the following endpoints:

        /animal/webscrape

        /yokai/webscrape

        /password/generate

## Sources for Web Scraping

The following links were used to scrape data for this project:

- (1)[List of animal names](https://en.wikipedia.org/wiki/List_of_animal_names) - Used for collecting the names of different existing animals.
- (2)[Yokai Finder](https://yokai.com/finder/) - Used for collecting the names of different Yokai entities.

- The collected data is solely used for educational and non-commercial purposes.