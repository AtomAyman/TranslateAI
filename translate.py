import openai
import os

# Set your OpenAI API key
openai.api_key = 'your-API-KEY'

def translate_text(text, source_language='ur', target_language='en'):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": (
                    f"You are a translator who translates Islamic texts from {source_language} to {target_language}. "
                    "Maintain key Islamic terminology such as 'Allah', 'Rasulallah', 'Salah', 'Zakat', etc., in their English forms. "
                    "The translation should be a word to word translation of the input text."
                )},
                {"role": "user", "content": text}
            ]
        )
        translation = response['choices'][0]['message']['content'].strip()
        return translation
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def main():
    input_file = input("Enter the input file name (with extension): ")

    if not os.path.exists(input_file):
        print(f"File {input_file} does not exist.")
        return

    # Generate the output file name
    base_name, ext = os.path.splitext(input_file)
    output_file = f"{base_name}_English{ext}"

    # Read the file with UTF-8 encoding
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            text = file.read()
    except UnicodeDecodeError as e:
        print(f"Failed to read {input_file}: {e}")
        return

    translation = translate_text(text)

    if translation:
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(translation)
        print(f"Translation saved to {output_file}")
    else:
        print("Translation failed.")

if __name__ == "__main__":
    main()
