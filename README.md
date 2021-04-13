# HydroFarm
About 70 percent of all the world's freshwater withdrawals go towards irrigation uses. But of the water used for irrigation, only about one-half is reusable. The rest is lost by evaporation into the air, evapotranspiration from plants, or is lost in transit, by a leaking pipe. 

HydroFarm aims to improve water use efficiency without decreasing yield. We will be integrating a weather API with canopy temperature to provide real-time updated irrigation scheduling. This will help small-scale farmers on water costs while potentially using limited water resources for a larger overall yield. 

## Instructions
1. Get an [OpenWeather](https://openweathermap.org/) API key
2. Install [Django](https://www.djangoproject.com/download/)
3. Run the program
```
python3.8 manage.py runserver
```
4. To change the theme, look through [Bootswatch](https://bootswatch.com/) for themes that you like. Go to [cdnjs](https://cdnjs.com/) to get a link to the theme. [Example](https://cdnjs.com/libraries/bootswatch)
5. To make python code changes (the backend) go to the views.py file under weatherApp file. 
6. To make changes on the front-end, go to index.html file under weatherApp/templates/main.
7. If you make changes to the program, run the following:
```
python3.8 manage.py makemigrations
python3.8 manage.py migrate
```