
UI tests are created following [Page Object Model](https://www.lambdatest.com/blog/page-object-model-in-selenium-python/) design pattern.
The Page Object Pattern (a.k.a the Page Object “Model”) is a design pattern that abstracts web page interactions for enhanced readability and reusability. Pages are represented as classes with locator attributes and interaction methods. Instead of making raw WebDriver calls, tests call page object methods instead. Page Object Pattern is arguably the most common pattern used for web UI test automation. There are many ways to implement the pattern, but most of them are fairly similar.
Chosen to group all files (each with a class for a page) in pages folder. Added an empty `__init__.py` file to make it a package. Test related modules are outside this package.

# Setup

1. Download and install [Python 3.x](https://www.python.org/downloads/windows/)
- If it is already installed, check in terminal:

```
python --version
```

2. Make sure to have the [latest pip version](https://pip.pypa.io/en/stable/installation/) installed

```
python.exe -m pip install --upgrade pip
```

3. Create a [virtual environment](https://mothergeo-py.readthedocs.io/en/latest/development/how-to/venv-win.html):

```
python.exe -m venv .venv
.venv\Scripts\activate
```

4. Install all dependencies:

```
pip install -r requirements.txt
```


## Selenium

5. Install driver (used chrome) : have the most recent version of browser and download the matching version of [ChromeDriver here](https://sites.google.com/chromium.org/driver/)
6. Add chromedriver to system environment variable Path [e.g. how to set it](https://www.computerhope.com/issues/ch000549.htm)

## Playwright


# Run tests

```
pytest
```

See the list of tests:
```
pytest --collect-only
```

# Tools

- [Pytest framework](https://docs.pytest.org/en/6.2.x/#)
- [Selenium](https://selenium-python.readthedocs.io/index.html)
- [Playwright](https://playwright.dev/python/docs/intro)

