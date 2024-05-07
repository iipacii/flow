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


# def render_mermaid(mermaid_code):
#     """Function to render Mermaid diagram from the given Mermaid code."""
#     # Create a template for the HTML container with the provided Mermaid code
#     mermaid_html = f"""
#     <html>
#     <head>
#     <script src="https://cdn.jsdelivr.net/npm/mermaid@10.5.0/dist/mermaid.min.js"></script>
#     </head>
#     <body>
#     <div class="mermaid">
#     {mermaid_code}
#     </div>
#     <script>
#     mermaid.initialize({{startOnLoad:true}});
#     </script>
#     </body>
#     </html>
#     """
#
#     # Render the HTML with the Mermaid diagram
#     components.html(mermaid_html, width= 600,height=500)


# render_mermaid(tester(source_code))


def render_mermaid(mermaid_code):
    """Function to render Mermaid diagram from the given Mermaid code and allow downloading it as an SVG."""
    mermaid_html = f"""
    <html>
    <head>
    <script src="https://cdn.jsdelivr.net/npm/mermaid@10.5.0/dist/mermaid.min.js"></script>
    <script>
    function downloadSVG() {{
        var svg = document.querySelector(".mermaid svg");
        var svgData = new XMLSerializer().serializeToString(svg);
        var svgBlob = new Blob([svgData], {{type:"image/svg+xml;charset=utf-8"}});
        var svgUrl = URL.createObjectURL(svgBlob);
        var downloadLink = document.createElement("a");
        downloadLink.href = svgUrl;
        downloadLink.download = "mermaid-diagram.svg";
        document.body.appendChild(downloadLink);
        downloadLink.click();
        document.body.removeChild(downloadLink);
    }}
    </script>
    </head>
    <body>
    <!-- Button moved to the top of the diagram -->
    <button onclick="downloadSVG()">Download as SVG</button>
    <div class="mermaid">
    {mermaid_code}
    </div>
    <script>
    mermaid.initialize({{startOnLoad:true}});
    </script>
    </body>
   </html>
   """

    # Render the HTML with the Mermaid diagram and download button
    components.html(mermaid_html, width=600, height=500)


if __name__ == '__main__':
    # Initialize the session state for page navigation if not already set
    if 'page' not in st.session_state:
        st.session_state['page'] = 'home'

    # Display content based on the current page stored in session state
    if st.session_state['page'] == 'github_repo':
        st.title("GitHub Repo Flow Chart")
        # Inform the user about how to input the GitHub repository path
        st.write(
            "Enter your GitHub repository path after 'https://github.com/' (e.g., username/repository):")
        # Text input for user to specify the remainder of the URL
        github_repo = st.text_input(
            "GitHub Repository Path:", key="github_repo")

        diagram_type = st.radio("Select Diagram Type:",
                                ("Sequence Diagram", "Class Diagram",
                                 "Entity Relationship Diagram", "State Diagram",
                                 "User Journey Diagram"))
        # Check if the user input includes 'https://github.com/'
        if "https://github.com/" in github_repo:
            st.error(
                "Please enter only the repository path after 'https://github.com/'. Do not include 'https://github.com/' in the input.")
        else:
            full_github_link = f"https://github.com/{github_repo}"
            if st.button("Generate Diagram") and github_repo:
                # Logic to process the GitHub repo, e.g., fetching data
                st.write(f"Fetching data from: {full_github_link}")
                # Your code for GitHub repo processing here

                # load mermaid here
                render_mermaid(tester(get_repository_files_contents(
                    str(github_repo)), diagram_type))
                print("render complete")

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
            # print("inside buttion ")
            # Call to the tester function with user's code and selected diagram type
            diagram_code = tester(user_code,
                                  diagram_type)
            print(diagram_code)
            render_mermaid(diagram_code)

        # Placeholder for your content rendering function
        # Example: render_mermaid(tester(your_code))

    # Load and display Lottie animation on the homepage
    if st.session_state['page'] == 'home':
        st.title(
            "Welcome! Let's generate Flow Charts from your GitHub Repositories or Code! 🚀")
        lottie_animation_path = "assets/Animation - 1715030681143.json"
        lottie_animation = load_lottiefile(lottie_animation_path)
        st_lottie(lottie_animation, height=200, width=550, key="example")
        live_typing_effect("Hello, I'm your AI Flowchart Generator! 🚀 Just send over your code or GitHub repository, and I'll transform it into a sleek, easy-to-understand flow diagram. Let's streamline your work and make your projects visually engaging!", speed=25)
        col1, col2 = st.columns(2)

        with col1:
            if st.button('Generate from GitHub Repo'):
                st.session_state['page'] = 'github_repo'
                st.experimental_rerun()

        with col2:
            if st.button('Generate from Code'):
                st.session_state['page'] = 'code'
                st.experimental_rerun()
