import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def chat_with_openai(user_input):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input},
            ]
        )
        # Retourne uniquement le contenu de la réponse
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"Une erreur s'est produite : {e}"

def start_chatbot():
    print("👋 Bienvenue ! Tape 'exit' pour quitter le chat.\n")

    while True:
        user_input = input("Toi : ")

        if user_input.lower() == 'exit':
            print("Au revoir ! 👋")
            break

        response = chat_with_openai(user_input)
        print(f"Bot : {response}\n")

if __name__ == "__main__":
    # Vérifie si la clé API est disponible
    if openai.api_key is None:
        print("Erreur : La clé API OpenAI n'est pas configurée.")
        print("Veuillez définir la variable d'environnement 'OPENAI_API_KEY'.")
    else:
        start_chatbot()
