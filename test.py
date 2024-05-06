import openai
import re


# Function to add Diagram name to the beginning of the result if the diagram type is not mentioned
def add_diagram_name(result, diagram_type):
    if diagram_type == "Class Diagram" and not result.startswith("classDiagram"):
        return f"classDiagram\n{result}"
    elif diagram_type == "Sequence Diagram" and not result.startswith("sequenceDiagram"):
        return f"sequenceDiagram\n{result}"
    elif diagram_type == "Entity Relationship Diagram" and not result.startswith("erDiagram"):
        return f"erDiagram\n{result}"
    elif diagram_type == "State Diagram" and not result.startswith("stateDiagram"):
        return f"stateDiagram\n{result}"
    elif diagram_type == "User Journey Diagram" and not result.startswith("journey"):
        return f"journey\n{result}"
    return result


def extract_and_print(content, diagram_type):
    # Regex pattern to match content between ```mermaid and ```
    pattern = r"```mermaid\s*(.*?)\s*```"
    result = re.search(pattern, content, re.DOTALL)
    if result:
        # Print the extracted content
        res = (result.group(1).strip())

        # Replace ', @, / with nothing
        res = res.replace("'", "")
        res = res.replace("@", "")
        res = res.replace("/", "")

        return res
# Replace 'your_api_key' with your actual OpenAI API key
# openai.api_key = ''


openai.api_key = ''


def tester(source_code, diagram_type):

    # Constructing the prompt for GPT-3.5 Turbo to generate a Mermaid flowchart
    prompt = f"Translate the following code into a Mermaid diagram which is a {diagram_type}to visually represent the flow of the program. Be sure to give the syntax of {diagram_type} . Just return the mermaid code. Do not add any other comments or text. Do not embed it within ``` mermaid ```:\n{source_code}\n"

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "Generate a Mermaid diagram from Python code."},
                  {"role": "user", "content": prompt}]
    )

    result = response['choices'][0]['message']['content']

    # if the result starts with ``` send the result to extract_and_print
    if result.startswith('```'):

        final = add_diagram_name(extract_and_print(
            result, diagram_type), diagram_type)
        print("\nFinal with the regex\n", final)
        return final
    else:

        final = add_diagram_name(result, diagram_type)
        print("\nFinal without the regex\n", final)
        return final

# tester(source_code)
