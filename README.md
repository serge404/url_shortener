# URL Shortener Web Service

Web service built in Python to 1) shorten URLs and 2) return the original longer URLs given the shortened URL

**Time Spent**: 2.5 hours on the product, then about 15 minutes on the README

**Considerations**: Would have made a UI for users to input the URLs but wanted to save time


## Setup


### Prerequisites


Users must install the python packages: **Flask** and **Flask-SQLAlchemy** using pip

```pip install Flask Flask-SQLAlchemy```



**Framework**:

Flask is chosen as the web framework because it's the simplest way to build APIs in Python

**Database**:

SQLite is chosen because it can be automatically set up without manually configuring anything

SQLAlchemy is chosen to interact with the database because of its compatibility with Flask

## Start Web Service
HTTP requests are used to interact with the service

In one Terminal tab: Run ```python app.py```

Web service will start running at http://127.0.0.1:5000/

## Using Web Service

## Shorten a URL
While app is running in another Terminal tab, run the following CURL command to get a shortened URL:

```curl http://127.0.0.1:5000/shorten -H "Content-Type: application/json" -d '{"url": "<long-url-here>"}'```

### Expected Response
```
{
  "short_url": "http://127.0.0.1:5000/<short_key>"
}
```

## Redirect to Original URL
In your browser go to the short URL in the response, you should automatically be redirected to the original URL



