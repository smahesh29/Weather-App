# Weather-App  <img alt="GitHub" src="https://img.shields.io/github/license/smahesh29/Weather-App">

This is a weather app in Django, it shows current weathers in multiple cities. You can add cities of your choice and can delete existing cities.I used Python Requests to call the Open Weather Map API.

To run this project, you should first Sign Up to <a href = https://openweathermap.org/>Open Weather Map</a>

<h2>How to run the project:</h2>
<ol>
    <li>Clone or Download the project.</li>
    <li>If you download the ZIP file then unzip it first.</li>
    <li>Now go to Open Weather Map --> sign in through your account --> go to API keys and copy the key.</li>
    <li>Open the Weather-App-master folder--> Open WeatherApp folder.</li>
    <li>Open weather folder and then open <i><b>views.py</b></i> file in any text editor.</li>
    <li>In views.py the line number 20 is -->   url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=EnterYourAPIKey' in place of EnterYourAPIKey paste your API key.</li>
    <li>Save the <i><b>views.py</b></i> file.</li>
    <li>Go to WeatherApp folder and copy the location of it.</li>
    <li>Open Command Prompt if you are working on Windows or Terminal if you are working on Linux or Mac</li>
    <li>Change working directory to WeatherApp using cd command as --> <i><b>cd CTRL+V</b></i></li>
    <li>Now type <i><b>python manage.py runserver</b></i>, this will start the local web server.</li>
    <li>In your web browser enter the address : <i><b>http://localhost:8000</b></i> or <i><b>http://127.0.0.1:8000/</b></i></li>
    <li>The project is run successfully, now you can add city of which you wants to check weather and also can remove existing cities.</li>
</ol>

<h2>Note :</h2>

<b>The Secret_Key required for the execution and debugging of project is not removed from the project code. So you can use the project as your college mini-project or by using the project code you can build your own project.</b>

# Screenshot :

<img src="Screenshots/Weather App - Google Chrome 03-12-2019 19_55_54.png" height = 400 width = 800>

# Support :
If you found this project helpful or you learned something from the source code and want to thank me, consider me to pay my internet bills. This would encourage me to create many such projects 👨🏻‍💻
<ul>
    <li><a href="https://www.paypal.me/smahesh29"><b>PayPal</b></a></li>
    <li><b>G Pay :</b> +919545123305</li>
    <li><b>PhonePe :</b> +919545123305</li>
    <li><b>UPI ID :</b> maheshusa29@oksbi</li>
</ul>
