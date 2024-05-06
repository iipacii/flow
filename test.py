import openai
import re


def extract_and_print(content):
    # Regex pattern to match content between ```mermaid and ```
    pattern = r"```mermaid\s*(.*?)\s*```"
    result = re.search(pattern, content, re.DOTALL)
    if result:
        # Print the extracted content
        return (result.group(1).strip())


# Replace 'your_api_key' with your actual OpenAI API key
openai.api_key = ''


def tester(source_code, diagram_type):

    # Constructing the prompt for GPT-3.5 Turbo to generate a Mermaid flowchart
    prompt = f"Translate the following code into a Mermaid {diagram_type} diagram to visually represent the flow of the program. Just return the mermaid code. Do not embed it within ``` mermaid ```:\n{source_code}\n"

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "Generate a Mermaid diagram from Python code."},
                  {"role": "user", "content": prompt}]
    )

    # Print the Mermaid diagram
    return extract_and_print(response['choices'][0]['message']['content'])
    # return response['choices'][0]['message']['content']

# tester(source_code)
