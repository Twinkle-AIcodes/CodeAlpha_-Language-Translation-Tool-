from googletrans import Translator

translator = Translator()

# Enter text
text = input("Enter text to translate: ")

# Select source language
print("\nSource Language:")
print("1. English")
print("2. Hindi")
print("3. French")
print("4. German")
print("5. Spanish")

source_choice = input("Enter source language number: ")

# Select target language
print("\nTarget Language:")
print("1. English")
print("2. Hindi")
print("3. French")
print("4. German")
print("5. Spanish")

target_choice = input("Enter target language number: ")

languages = {
    "1": "en",
    "2": "hi",
    "3": "fr",
    "4": "de",
    "5": "es"
}

source_lang = languages.get(source_choice, "en")
target_lang = languages.get(target_choice, "hi")

# Translate text
translated = translator.translate(
    text,
    src=source_lang,
    dest=target_lang
)

print("\nTranslated Text:")
print(translated.text)