
import streamlit as st
import os
import re

# Load the LaTeX file
TEX_FILE = "main.tex"

st.set_page_config(page_title="OverLifter v1", layout="wide")
st.title("📄 OverLifter – Tailor Your LaTeX Resume Easily")

with open(TEX_FILE, "r") as f:
    latex = f.read()

sections = {
    "Education": "",
    "Experience": "",
    "Projects": "",
    "Technical Skills": ""
}

# Extract existing sections
for section in sections:
    pattern = rf"\\section{{{section}}}(.*?)(?=\\section{{|\\end{{document}})"
    match = re.search(pattern, latex, re.DOTALL)
    if match:
        sections[section] = match.group(1).strip()

edited = {}

st.sidebar.header("✏️ Edit Sections")
for sec, content in sections.items():
    with st.expander(f"Section: {sec}", expanded=True):
        edited[sec] = st.text_area(f"{sec} content", content, height=300)

# Add custom section
st.sidebar.markdown("---")
custom_sec = st.sidebar.text_input("➕ Add Custom Section")
custom_content = ""
if custom_sec:
    custom_content = st.sidebar.text_area("Custom Section Content", height=150)

if st.sidebar.button("💾 Save & Download .tex"):
    updated_tex = latex
    for sec, content in edited.items():
        updated_tex = re.sub(
            rf"(\\section{{{sec}}})(.*?)(?=\\section{{|\\end{{document}})",
            rf"\1\n{content}\n",
            updated_tex,
            flags=re.DOTALL
        )
    if custom_sec and custom_content:
        custom_block = f"\\section{{{custom_sec}}}\n{custom_content}\n"
        updated_tex = updated_tex.replace("\end{document}", custom_block + "\end{document}")
    with open("updated_resume.tex", "w") as f:
        f.write(updated_tex)
    st.success("✅ Updated LaTeX saved as updated_resume.tex")
    with open("updated_resume.tex", "rb") as f:
        st.download_button("📥 Download .tex File", f, file_name="updated_resume.tex", mime="text/plain")
