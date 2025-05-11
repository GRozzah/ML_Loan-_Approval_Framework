# --- Custom Background ---
# style.py

import streamlit as st

def set_background():
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-color: #e3f2fd;  /* Light blue background */
            color: #333333;  /* Dark text for contrast */
        }}
        .block-container {{
            backdrop-filter: blur(8px);
            background-color: rgba(255, 255, 255, 0.85);  /* Slightly opaque white background */
            padding: 2rem;
            border-radius: 10px;
            border: 1px solid #dddddd;  /* Light border for a clean look */
        }}
        .stButton {{
            background-color: #007bff;  /* Blue button */
            color: Blue;
            border-radius: 10px;
            font-size: 18px;  /* Larger font size for readability */
            padding: 15px 30px;  /* Larger padding for a bigger button */
            position: fixed;
            bottom: 20px;
            left: 50%;
            transform: translateX(-50%);
            z-index: 10;  /* Ensure button is always on top */
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.2);  /* Subtle shadow to lift button */
        }}
        .stButton:hover {{
            background-color: #0056b3;  /* Darker blue on hover */
        }}
        .stSelectbox select, .stNumberInput input {{
            background-color: #ffffff;  /* White background for input fields */
            color: #333333;  /* Dark text inside input fields */
            border: 1px solid #cccccc;  /* Light gray border for inputs */
            outline: none;  /* Remove blue outline on hover or focus */
        }}
        .stSelectbox:hover, .stNumberInput:hover {{
            border: 1px solid #007bff;  /* Blue border on hover */
        }}
        .stSelectbox select:focus, .stNumberInput input:focus {{
            border: 1px solid #007bff;  /* Blue border when focused */
            box-shadow: none;  /* Remove default focus box-shadow */
        }}
        h1 {{
            font-size: 0.1rem;
            color: #1a73e8;  /* Light blue color for heading */
        }}
        .stMarkdown {{
            font-size: 1rem;
            color: #333333;
        }}
        .stSelectbox select {{
            padding: 10px;
            border-radius: 5px;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )


