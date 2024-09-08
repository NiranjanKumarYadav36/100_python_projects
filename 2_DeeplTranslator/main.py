import requests

url = "https://api-free.deepl.com/v2/translate"
api_key = ""

text_to_translate = input("Enter text: ")
translation_language = input(f"Enter target language (eg., IT for Italian): ")

params = {
    'auth_key': api_key,
    'text': text_to_translate,
    'target_lang': translation_language
}

response = requests.get(url, data=params)
result = response.json()

# Extract the translated text
translated_text = result['translations'][0]['text']
print("Translated text:", translated_text)

# Ask the user if they want to save the translated text to a file
save_option = input("Do you want to save the translated text to a file? (yes/no): ").strip().lower()

if save_option == "yes":
    file_name = input("Enter the file name (e.g., translation.txt): ").strip()
    with open(file_name, 'w') as file:
        file.writelines(translated_text)
    print(f"Translated text saved to {file_name}.")
else:
    print("Translated text not saved.")

