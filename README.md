# discordbot
Bot for the gamers

## Guide

1. Create and activate a virtual environment:
```
python3.9 -m venv py39env
./py39env/bin/activate
```
2. Install the required modules
```
pip install -r requirements.txt
```

2. Run the tests:
```
pytest
```  

## File descriptions

`requirements.txt` lists the python modules that need to be `pip`-installed to run the bot/tests

#### Heroku files
`app.json` is used by Heroku to describe the process (May no longer be needed)

`Procfile` is used by Heroku to run the bot

`runtime.txt` is used by Heroku to specify the python version to run
