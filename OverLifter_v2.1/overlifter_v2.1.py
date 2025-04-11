
import streamlit as st
import re

st.set_page_config(page_title="OverLifter v2.1", layout="wide")
st.title("📄 OverLifter v2.1 — Stable LaTeX Resume Editor")

uploaded_file = st.file_uploader("📤 Upload your LaTeX (.tex) resume", type=["tex"])

if uploaded_file:
    latex_text = uploaded_file.read().decode("utf-8")

    # Match all section blocks
    pattern = r"\\section\{(.+?)\}(.*?)(?=(\\section\{|\\end\{document\}))"
    sections = re.findall(pattern, latex_text, re.DOTALL)

    edits = {}
    col1, col2 = st.columns([1, 1])

    with col1:
        st.header("🖊️ Edit Sections")
        for title, content, _ in sections:
            items = re.findall(r"\\resumeItem\{(.*?)\}", content, re.DOTALL)
            plain_text = "\n".join(items) if items else content.strip()
            with st.expander(f"{title}", expanded=False):
                edits[title] = st.text_area(f"Edit bullets for {title}", plain_text, height=250)

    with col2:
        st.header("📄 Live .tex Preview")
        if st.button("🔁 Update Preview"):
            updated_latex = latex_text
            for title, content, _ in sections:
                if title in edits:
                    lines = edits[title].split("\n")
                    rebuilt = "\n".join([f"\\resumeItem{{{line.strip()}}}" for line in lines if line.strip()])
                    new_block = f"\\section{{{title}}}\n\\resumeItemListStart\n{rebuilt}\n\\resumeItemListEnd"
                    escaped_title = re.escape(title)
                    section_regex = re.compile(r"(\\section\{" + re.escape(title) + r"\})(.*?)(?=(\\section\{|\\end\{document\}))", re.DOTALL)
                    updated_latex = section_regex.sub(new_block, updated_latex)


            st.code(updated_latex, language="latex")
            st.download_button("📥 Download Updated .tex", updated_latex, file_name="updated_resume.tex", mime="text/plain")
