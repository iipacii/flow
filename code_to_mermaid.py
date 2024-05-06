import openai
import re




def code_to_mermaid(code_text):
    # Use OpenAI language model to analyze the code
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a code analysis assistant."},
            {"role": "user", "content": f"Analyze the following code:\n\n{code_text}\n\nIdentify and describe the code structure, including classes, functions, control flow statements, data structures, and their relationships. Provide your response in a structured format suitable for generating a Mermaid diagram."}
        ],
        max_tokens=1000,
        n=1, 
        stop=None,
        temperature=0.5,
    )

    # Extract code constructs from the OpenAI response
    code_analysis = response.choices[0].message.content

    # Map code constructs to Mermaid syntax
    mermaid_code = "mermaid\n" + "flowchart TD\n" + code_analysis + "\n"

    return mermaid_code

# Example usage
input_code = """
class MyClass:
    def _init_(self):
        self.data = []

    def my_method(self):
        if self.data:
            for item in self.data:
                print(item)

numbers = [1, 2, 3, 4, 5]
sum = 0
for num in numbers:
    sum += num
"""

mermaid_equivalent = code_to_mermaid(input_code)
print(mermaid_equivalent)