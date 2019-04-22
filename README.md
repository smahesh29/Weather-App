# Weather-App
This is a weather app in Django, it shows current weathers in multiple cities. You can add cities of your choice and can delete existing cities.I used Python Requests to call the Open Weather Map API.

To run this project, you should first Sign Up to Open Weather Map.

Open Weather Map - https://openweathermap.org/

How to run the project:

    1.Clone or Download the project.
    2.If you download the ZIP file then unzip it first.
    3.Now go to Open Weather Map --> sign in through your account --> go to API keys and copy the key.
    4.Open the Weather-App-master folder--> Open WeatherApp folder.
    5.Open weather folder and then open views.py file in any text editor.
    6.In views.py the line number 20 is -->   url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=EnterYourAPIKey' in place of EnterYourAPIKey paste your API key.
    7.Save the views.py file.
    8.Go to WeatherApp folder and copy the location of it.
    9.Open Command Prompt if you are working on Windows or Terminal if you are working on Linux or Mac
    10.Change working directory to WeatherApp using cd command as --> cd CTRL+V
    11.Now type python manage.py runserver, this will start the local web server.
    12.In your web browser enter the address : http://localhost:8000 or http://127.0.0.1:8000/ 
    13.The project is run successfully, now you can add city of which you wants to check weather and also can remove existing cities. 

