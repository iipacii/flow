import os
import requests
import openai
from dotenv import load_dotenv
from github.fileTree import get_repo_contents

openai.api_key = 'OPENAI_API_KEY'


# def load_api_key():
#     # Load the OpenAI API key from the .env file
#     load_dotenv()
#     openai.api_key = os.getenv("OPENAI_API_KEY")
#     print(openai.api_key)


def get_important_files(repo_url, messages):

    negative_files = 'package-lock.json'+', ' + 'node_modules'
    content = f"What are the most important files in this repository to understand the flow of the program? Please list them. Don't number them. Don't add any bullets of any kind. Just seperate them by a comma. Don't include {negative_files} . Give importance to files that might help us undertand the program logic. Don't include any other message in the response. "
    # Ask the AI to list the important files
    messages.append({"role": "user", "content": content})

    # Generate the response
    chat = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    reply = chat.choices[0].message.content
    # print(f"ChatGPT: {reply}")

    # Update the conversation history
    messages.append({"role": "assistant", "content": reply})

    # Get the list of important files
    important_files = reply.split(', ')
    return important_files


def retrieve_file_contents(repo_url, important_files):
    # Retrieve the contents of the important files
    file_contents = []
    for file_path in important_files:
        # Construct the API URL for the file content
        file_url = f"https://raw.githubusercontent.com/{repo_url}/master/{file_path}"
        response = requests.get(file_url)

        if response.status_code == 200:
            content = response.text
            file_contents.append(f"File: {file_path}\n\n```\n{content}\n```\n")
        else:
            file_contents.append(
                f"Error retrieving {file_path}: {response.status_code} - {response.text}")

    # Combine the file contents into a single string
    file_contents_str = "\n".join(file_contents)
    return file_contents_str


def get_repository_files_contents(repo_url):
    # load_api_key()

    # Get the repository contents
    repo_info = get_repo_contents(repo_url)

    # Initialize the conversation
    messages = [
        {"role": "system", "content": "You are an intelligent assistant."}]

    # Attach the repo_info as context to the messages
    messages.append(
        {"role": "user", "content": f"Here is the information about the files and directories in the repository:\n\n{repo_info}"})

    # Get the list of important files
    important_files = get_important_files(repo_url, messages)

    # Print the list of important files
    # print(f"\n\nImportant files in the repository:\n\n{important_files}")

    # Retrieve the contents of the important files
    file_contents_str = retrieve_file_contents(repo_url, important_files)

    # Print the contents of the important files
    # print(f"\n\nContents of the important files:\n\n{file_contents_str}")

    return file_contents_str


def main():
    repo_url = "amith-2001/RealEstateApplication"
    file_contents_str = get_repository_files_contents(repo_url)
    print(f"\n\nContents of the important files:\n\n{file_contents_str}")


if __name__ == "__main__":
    main()
