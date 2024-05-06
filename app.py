import streamlit as st
import streamlit.components.v1 as components


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
    components.html(mermaid_html, height=400)


# Use a text area in Streamlit for user to enter or modify Mermaid code
user_input_mermaid_code = st.text_area("Enter your Mermaid diagram code:", height=300,
                                       value="graph TD;\n    A-->B;\n    A-->C;\n    B-->D;\n    C-->D;")

# Call the render_mermaid function with the user provided Mermaid code
if user_input_mermaid_code:
    render_mermaid(user_input_mermaid_code)
else:
    st.write("Please enter a Mermaid diagram script.")
