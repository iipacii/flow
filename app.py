import streamlit as st
import streamlit.components.v1 as components

def render_mermaid(mermaid_code):
    """Function to render Mermaid diagram from the given Mermaid code."""
    mermaid_html = f"""
    <html>
    <head>
    <script src="https://cdn.jsdelivr.net/npm/mermaid@10.5.0/dist/mermaid.min.js"></script>
    </head>
    <body>
    <div class="mermaid"> {mermaid_code} </div>
    <script> mermaid.initialize({{startOnLoad:true}}); </script>
    </body>
    </html>
    """
    components.html(mermaid_html, height=400)

# Set page config
st.set_page_config(page_title="Bro's Mermaid Mania")

# Add custom CSS
st.markdown(
    """
    <style>
    .stTextArea > label {
        font-size: 20px;
        font-weight: bold;
        color: #FF4136;
    }
    .stTextArea textarea {
        font-size: 16px;
        background-color: #2B2D42;
        color: #EDF2F4;
    }
    body {
        background-color: #1E1E24;
        color: #EDF2F4;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title
st.title("Bro's Mermaid Mania 🌊🔥")

# User input for Mermaid code
user_input_mermaid_code = st.text_area("Yo bro, drop your Mermaid code here! 💻📝", height=300, value="graph TD;\\n A-->B;\\n A-->C;\\n B-->D;\\n C-->D;")

# Export options
export_format = st.selectbox("Bro, how do you want to export your diagram? 📤", ["PNG", "SVG", "PDF"])
export_button = st.button("Export Diagram 💾")

# Example code
example_code = """graph TD
    A[Start] --> B{Condition}
    B -->|Yes| C[Do something]
    B -->|No| D[Do something else]
    C --> E[Finish]
    D --> E
"""
st.expander("Need some inspo, bro? 💡").code(example_code)

# Render Mermaid diagram
if user_input_mermaid_code:
    render_mermaid(user_input_mermaid_code)
else:
    st.write("Bro, you gotta enter some Mermaid code first! 🤷‍♂️")