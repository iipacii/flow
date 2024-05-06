import streamlit as st
import streamlit.components.v1 as components
from test import tester
from github.fileImportance import get_repository_files_contents
from github.fileTree import *
def render_mermaid(mermaid_code):
    """Function to render Mermaid diagram from the given Mermaid code."""
    # Create a template for the HTML container with the provided Mermaid code
    mermaid_html = f"""
    <html>
    <head>
    <script src="https://cdn.jsdelivr.net/npm/mermaid@10.5.0/dist/mermaid.min.js"></script>
    </head>
    <body>
    <div class="mermaid">
    {mermaid_code}
    </div>
    <script>
    mermaid.initialize({{startOnLoad:true}});
    </script>
    </body>
    </html>
    """

    # Render the HTML with the Mermaid diagram
    components.html(mermaid_html, width= 600,height=500)


# Use a text area in Streamlit for user to enter or modify Mermaid code
# user_input_mermaid_code = st.text_area("Enter your github link to create diagram code:", height=300)

# source_code = """
# def calculate_area(length, width):
#     return length * width
#
# area = calculate_area(10, 20)
# print(f"The area is {area}")
# """




# Call the render_mermaid function with the user provided Mermaid code
# if user_input_mermaid_code:
#     render_mermaid(tester())
# else:
#     st.write("Please enter a Mermaid diagram script.")
print(tester(get_repository_files_contents("Meskine-Yasser/AI_Expert_System")))

# render_mermaid(tester(source_code))

if __name__ == '__main__':
    render_mermaid(tester(get_repository_files_contents("Meskine-Yasser/AI_Expert_System")))
    print("render complete")