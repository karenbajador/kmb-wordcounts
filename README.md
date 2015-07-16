#kmb-wordcount

Built this project by following tutorial from [realpython.com][1].

Built with *Python 3.4.3, Flask, Heroku, Environment variables, Sqlalchemy, Flask-migrate, Redis, Postgresql*.

*Link:* [https://realpython.com/blog/python/flask-by-example-part-1-project-setup/][2] 

This is a Flask app that accepts a URL and calculates the word-frequency pairs based on extracted text from the given URL. It limits the results to the top 10 pairs ordered by the highest frequency to lowest.

**Tutorial Coverage:**

1. Part One: Setup a local development environment and then deploy both a staging environment and a production environment on Heroku. (current)
2. Part Two: Setup a PostgreSQL database along with SQLAlchemy and Alembic to handle migrations.
3. Part Three: Add in the back-end logic to scrape and then process the counting of words from a webpage using the requests, BeautifulSoup, and Natural Language Toolkit (NLTK) libraries.
4. Part Four: Implement a Redis task queue to handle the text processing.
5. Part Five: Setup Angular on the front-end to continuously poll the back-end to see if the request is done.
6. Part Six: Push to the staging server on Heroku – setting up Redis, detailing how to run two processes (web and worker) on a single Dyno.
7. Part Seven: Update the front-end to make it more user-friendly.
8. Part Eight: Add the D3 library into the mix to graph a frequency distribution and histogram.

[1]: http://realpython.com
[2]: https://realpython.com/blog/python/flask-by-example-part-1-project-setup/