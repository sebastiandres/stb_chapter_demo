import streamlit as st
import streamlit_book as stb
from pathlib import Path

def main():
    # Set wide display
    st.set_page_config(layout="wide")

    # Set multipage
    save_answers = True
    current_path = Path(__file__).parent.absolute()
    path = current_path / "pages" 
    stb.set_chapter_config(path=path, save_answers=save_answers)


if __name__ == "__main__":
    main()