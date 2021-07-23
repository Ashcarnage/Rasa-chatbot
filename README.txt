MODULES/PACKAGES REQUIRED TO RUN PROJECT:(ON WINDOWS)

I. TO RUN CHATBOT:
1. RASA-OPENSOURCE 2.x

II. TO RUN WEBSITE:
1. Flask 2. Flask-WTF 3. email_validator 4. Flask-SQLAlchemy

III. TO RUN CHATBOT AND WEBSITE TOGETHER:
1. XAMPP 


HOW TO SET-UP PROJECT:
1. Download all the required modules (prefereably in separate virtual environments, for the website and for the chatbot).
2. Search for 'XAMPP htdocs folder' in system, and create a folder named 'chatbotWidget' within this folder. Within this, place the chatbotWidget.html file.

HOW TO RUN PROJECT:
1. Open cmd in the rasa-chatbot folder, enter the venv if made, run the following command:
>>rasa run --credentials ./credentials.yml  --enable-api --auth-token XYZ123 --model ./models --endpoints ./endpoints.yml --cors "*"

2. Open XAMPP Control Panel, click on 'Start' button for Apache.

3. Open cmd in the flaskbot folder, enter the venv if made, run the following command:
>> python run.py

Now, copy the url displayed in the cmd and you can access the website.