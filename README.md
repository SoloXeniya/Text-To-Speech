This Django project is a web application integrated with the Django admin panel and also linked to a chatbot. The project is designed to convert text information into speech

Main functions
A convenient administrative panel for managing the contents of the application and database with information about the number of free attempts to convert users.
The ability to add, edit and delete texts for subsequent conversion to speech.
Integration with a chatbot to interact with end users.
Users can send text requests to convert to speech.
Using libraries to generate speech based on the provided text.

Using
Launch the administrative panel.
Launch the telegram bot.
In the telegram bot, add the texts that you want to convert to speech.
Interact with the chatbot by sending text requests.
Receive generated speech in response to your requests.
The project has the ability to send 10 free text-to-speech conversion attempts.


<section class="installation">
    <h2>Getting Started</h2>
    <pre>
<code>
# Install dependencies
pip install -r requirements.txt

# Apply migrations
python3 manage.py makemigrations
python3 manage.py migrate

# Run the Django admin site
python3 manage.py runserver

# Start the Telegram bot
python3 manage.py runbot
</code>
    </pre>
</section>
