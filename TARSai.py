import openai
import pyttsx3
import speech_recognition as sr

# Klucz API
openai.api_key = 'KluczAPIGPT'

# Funkcja komunikacji z GPT oraz nadanie mu roli
def communicate_with_gpt(input_text):
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
            {"role": "system", "content": "Nazywasz się TARS. Potrafisz być bezlitosny i agresywny. Twoje odpowiedzi są bezpośrednie również posługujesz się sarkazmem. potrafisz współpracować ale jesteś w tym pragmatyczny "},  
            {"role": "user", "content": input_text},
        ]
    )
    return response['choices'][0]['message']['content']

#Funkcja TTS
def text_to_speech_ivon(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 170)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(text)
    engine.runAndWait()

# Funkcja do przechwytywania głosu z mikrofonu na tekst
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Mów teraz...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        print("Rozpoznawanie tekstu...")
        text = recognizer.recognize_google(audio, language="pl-PL")
        print("Tekst rozpoznany:", text)
        return text
    except sr.UnknownValueError:
        print("Nie rozumiem co powiedziałeś...")
        return None

# Główna pętla 
while True:
    user_input = recognize_speech()
    if user_input:
        bot_response = communicate_with_gpt(user_input)
        print("Bot:", bot_response)
        text_to_speech_ivon(bot_response)

