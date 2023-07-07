from googletrans import Translator

def translate_text(text, dest='en', src='auto'):
    translator = Translator()
    translation = translator.translate(text, dest=dest, src=src)
    return translation.text

# Get user input
user_input = input("Enter text to translate: ")

# Detect the language of the user input
translator = Translator()
detected_lang = translator.detect(user_input).lang

# Translate based on the detected language
if detected_lang == 'hi':
    translation = translate_text(user_input)
    print("Hindi Text: ", user_input)
    print("English Translation: ", translation)
elif detected_lang == 'en':
    translation = translate_text(user_input, dest='hi')
    print("English Text: ", user_input)
    print("Hindi Translation: ", translation)
else:
    print("Unsupported language.")
