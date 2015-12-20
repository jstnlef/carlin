# Problem 2

This tiny webserver is designed to return rendered HTML when POST requests are made with request bodies similar to the 
JSON object found in `sample.json`. This exercise took me about 2 hours and is missing key parts I would consider necessary
if this were to run in a production setting. For example, I would probably end up using a production WSGI server such as
gunicorn instead of Flask's development server but it gets the job done. I also would have spent a bit more time fleshing
out the unit test suite.

## Installation Instructions

### Prerequisites
* Python 3 (though I imagine Python 2 should probably work as well)
* pip (should come with your installation of python 2/3 but may not) Instructions here: https://pip.pypa.io/en/stable/installing/
* virtualenv (also should be included in your python install) Instructions here: http://virtualenv.readthedocs.org/en/latest/installation.html

### Install
Run the following commands in a terminal to prepare the environment
```
virtualenv .venv
source .venv/bin/activate
pip install -r problem_2/requirements.txt
```
Now, all you have to do is start the server.
```
python problem_2/server.py
```
You should see something similar to
```
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```
## Running
The endpoint to POST to is `http://127.0.0.1:5000/samples` and you should expect a response with an HTML body.

I was testing with [httpie](https://github.com/jkbrzt/httpie) with the following command:
```
http POST http://localhost:5000/samples < problem_2/sample.json
```
and you should see something like

```
HTTP/1.0 200 OK
Content-Length: 600
Content-Type: text/html; charset=utf-8
Date: Sun, 20 Dec 2015 03:56:36 GMT
Server: Werkzeug/0.11.2 Python/3.5.1

<!DOCTYPE html>
<html>
<head>
    <title>Problem 2 Sample Rendering</title>
</head>
<body>
    <div>
        <p>id: 123</p>
        <p>name: Sample Name</p>
        <p>active: True</p>
        <p>count: 1000</p>
        <p>address_ids: [1, 30, 100, 50]</p>
        <p>accounts:
            <ul>
                <li>
                    <p>id: 1</p>
                    <p>name: Test Account 1</p>
                </li>
                <li>
                    <p>id: 2</p>
                    <p>name: Test Account 2</p>
                </li>
            </ul>
        </p>
    </div>
</body>
</html>
```


## Testing
You can run the unit tests with the following command
```
py.test
```
At this moment, there is some minimal testing around the schema validation to ensure that I was using the library correctly
but if this were a production system I would expand the testing to include a few more edge cases and in general be a bit more
thorough.
