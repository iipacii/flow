import streamlit as st
import streamlit.components.v1 as components
from test import tester
from github.fileImportance import get_repository_files_contents
from github.fileTree import *
from streamlit_lottie import st_lottie
import json
from typing_live import live_typing_effect






def load_lottiefile(filepath: str):
    """ Load a Lottie animation from a JSON file located at filepath """
    with open(filepath, 'r') as file:
        return json.load(file)


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



# render_mermaid(tester(source_code))


if __name__ == '__main__':
    # Initialize the session state for page navigation if not already set
    if 'page' not in st.session_state:
        st.session_state['page'] = 'home'





    # Display content based on the current page stored in session state
    if st.session_state['page'] == 'github_repo':
        st.title("GitHub Repo Flow Chart")

        # Placeholder for your content rendering function
        # Example: render_mermaid(tester(get_repository_files_contents("your-repo/your-project")))

    elif st.session_state['page'] == 'code':
        # st.title("Code Flow Chart")
        st.title("Code Flow Chart")
        # Text area for user to input code
        user_code = st.text_area("Paste your code here:", height=300)
        # Radio buttons for diagram type selection
        diagram_type = st.radio("Select Diagram Type:",
                                ("Sequence Diagram", "Class Diagram",
                                 "Entity Relationship Diagram", "State Diagram",
                                 "User Journey Diagram"))
        if st.button("Generate Diagram"):
            # Call to the tester function with user's code and selected diagram type
            diagram_code = tester(user_code, diagram_type)
            render_mermaid(diagram_code)


        # Placeholder for your content rendering function
        # Example: render_mermaid(tester(your_code))

    # Load and display Lottie animation on the homepage
    if st.session_state['page'] == 'home':
        st.title("Welcome! Let's generate Flow Charts from your GitHub repo")
        lottie_animation_path = "assets/Animation - 1715030681143.json"
        lottie_animation = load_lottiefile(lottie_animation_path)
        st_lottie(lottie_animation, height=200, width=550, key="example")
        live_typing_effect("hello, I am GitHub hero", speed=100)
        col1, col2 = st.columns(2)

        with col1:
            if st.button('Generate from GitHub Repo'):
                st.session_state['page'] = 'github_repo'
                st.experimental_rerun()

        with col2:
            if st.button('Generate from Code'):
                st.session_state['page'] = 'code'
                st.experimental_rerun()


