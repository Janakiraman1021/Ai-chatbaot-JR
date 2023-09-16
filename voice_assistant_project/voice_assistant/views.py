# views.py in voice_assistant app
from django.shortcuts import render
from .models import Conversation
import speech_recognition as sr
import nltk
from googletrans import Translator
from django.contrib.auth.decorators import login_required
from gtts import gTTS
import os
from django.http import HttpRequest
from django.http import request
from django.shortcuts import render




def voice_assistant(request):
    if request.method == 'POST':
        user_input = request.POST['user_input']
        # Process user_input, perform NLP, translation, and generate a response
        # Save the conversation to the database
        conversation = Conversation(user_input=user_input, assistant_response=response)
        conversation.save()

    conversations = Conversation.objects.all().order_by('-id')[:5]
    return render(request, 'voice_assistant.html', {'conversations': conversations})







def voice_assistant(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input')  # Use get() to safely retrieve POST data
        user_language = "en"  # Default language (e.g., English)

        # Check if the user is authenticated (logged in)
        if request.user.is_authenticated:
            user_profile = UserPreferences.objects.get(user=request.user)
            if user_profile.preferred_language:
                user_language = user_profile.preferred_language

        # Initialize the recognizer
        recognizer = sr.Recognizer()

        # Capture audio from the user's microphone
        with sr.Microphone() as source:
            print("Listening...")
            audio = recognizer.listen(source)

        try:
            # Recognize speech using the Google Web Speech API
            user_input = recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            print("Google Web Speech API could not understand audio.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Web Speech API; {e}")

        # Process user input using NLP and translation
        response = process_user_input(user_input, user_language)

        # Convert the response text to speech
        text_to_speech(response, user_language)

        # Save the conversation to the database
        conversation = Conversation(user_input=user_input, assistant_response=response)
        conversation.save()

    conversations = Conversation.objects.all().order_by('-id')[:5]
    return render(request, 'voice_assistant.html', {'conversations': conversations})



nltk.download('punkt')

def process_user_input(user_input):
    tokens = nltk.word_tokenize(user_input)
    # Perform NLP analysis and generate a response
    response = "This is your AI response."
    return response


if request.method == 'POST':
    user_input = request.POST['user_input']
    
    # Process user input using NLP
    response = process_user_input(user_input)
    
    # Save the conversation to the database
    conversation = Conversation(user_input=user_input, assistant_response=response)
    conversation.save()




translator = Translator()

def process_user_input(user_input, target_language):
    # Translate user input to the target language
    translated_input = translator.translate(user_input, dest=target_language).text
    
    # Perform NLP analysis and generate a response in the target language
    response = "This is your AI response in " + target_language + ": " + translated_input
    return response


# Assuming you've already defined the UserPreferences model


@login_required
def set_language_preference(request, preferred_language):
    user_profile = UserPreferences.objects.get(user=request.user)
    user_profile.preferred_language = preferred_language
    user_profile.save()
    return redirect('voice_assistant')


def text_to_speech(text, language):
    tts = gTTS(text, lang=language, slow=False)
    audio_file = "response.mp3"
    tts.save(audio_file)
    os.system("mpg123 " + audio_file)  # Play the audio file (you may need to install mpg123)
    os.remove(audio_file)  # Remove the temporary audio file

# ...

def voice_assistant(request):
    if request.method == 'POST':
        user_input = request.POST['user_input']
        user_language = "en"  # Default language (e.g., English)

        # Check if the user is authenticated (logged in)
        if request.user.is_authenticated==True or request.user.is_authenticated==False :
            user_profile = UserPreferences.objects.get(user=request.user)
            if user_profile.preferred_language:
                user_language = user_profile.preferred_language

        # Initialize the recognizer
        recognizer = sr.Recognizer()

        # Capture audio from the user's microphone
        with sr.Microphone() as source:
            print("Listening...")
            audio = recognizer.listen(source)

        try:
            # Recognize speech using the Google Web Speech API
            user_input = recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            print("Google Web Speech API could not understand audio.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Web Speech API; {e}")

        # Process user input using NLP and translation
        response = process_user_input(user_input, user_language)

        # Convert the response text to speech
        text_to_speech(response, user_language)

        # Save the conversation to the database
        conversation = Conversation(user_input=user_input, assistant_response=response)
        conversation.save()

    conversations = Conversation.objects.all().order_by('-id')[:5]
    return render(request, 'voice_assistant.html', {'conversations': conversations})

# ...

