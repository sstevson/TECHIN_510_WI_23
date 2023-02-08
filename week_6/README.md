# Flask
Flask is a lightweight framework for creating websites with just a few lines 
of Python code.

Flask is highly extensible which means that you can install plugins for 
things like HTML templates, CSS styles, and JavaScript, as well as database 
connectors.

## The Application Instance
Flask applications must create an *Application Instance*. The web server 
passes requests to the Application Instance object for handling.

## Today's Lab
You will create a basic Flask application and run it locally before 
deploying it to the Azure App Service which we explored last week.

## Requirements
To complete this lab, you will need to following:
- An IDE installed on your machine (most of you have Visual Studio Code)
- Flask
- Flask-Bootstrap
- The Azure CLI
- An Azure student account
- Templates which you can find in the `templates` directory

## Steps
- First, create a new project in your IDE
- Ensure you have a virtual environment installed (`python -m venv venv`)
- Use `pip` to install the packages in the `requirements.txt` file
- Create a new Python file (`.py`) called `app.py`