# Website-with-chatbot-widget

Run following commands in virtual environment containing rasa chatbot dependencies: 

  1. rasa run -m models --enable-api --cors "*" -p 5021 
  2. rasa run actions
  
 Images load fine when just directly running the html file but not when running it via something else such as VSCode's Live Server plugin or Flask.
