# Weather Chatbot Assistant

Klima tells the current weather forecast for a certain city.
Currently it has been defined mostly brazilian counties.

For the weather forecasting API we used https://hgbrasil.com/status/weather
Simply create an account and an API key for the weather forecasting API.

In order to run the actions (actions server) properly, we need to first specify the API key created by passing the API key to the API_KEY variable in the actions.py file.

To run the project with Rasa
- install de dependencies required in the pipeline if needed (config.yml)
- execute `rasa x` or `rasa shell` to run it in the terminal

For more information on the Rasa Framework, please check their documentation under https://rasa.com/docs/.