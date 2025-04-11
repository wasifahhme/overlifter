
import streamlit as st
import re

st.set_page_config(page_title="OverLifter v2.0", layout="wide")
st.title("📝 OverLifter v2.0 – Clean LaTeX Resume Editor")

uploaded_file = st.file_uploader("📤 Upload your LaTeX (.tex) resume", type=["tex"])

if uploaded_file is not None:
    latex = uploaded_file.read().decode("utf-8")

    section_pattern = r"\\section\{(.+?)\}(.*?)(?=\\section\{|\\end\{document\})"
    matches = re.findall(section_pattern, latex, re.DOTALL)
    edits = {}

    col1, col2 = st.columns([1, 1])
    with col1:
        st.header("🖊️ Edit Sections")
        for title, content in matches:
            clean_bullets = re.findall(r"\\resumeItem\{(.*?)\}", content, re.DOTALL)
            joined = "\n".join(clean_bullets) if clean_bullets else content.strip()
            with st.expander(title, expanded=False):
                edits[title] = st.text_area(f"{title} Bullets", joined, height=200)

    with col2:
        st.header("📄 Live .tex Preview")
        if st.button("🔁 Update Preview"):
            updated_latex = latex
            for title, edited_text in edits.items():
                # Split by lines
                lines = edited_text.strip().split("\n")

# 1. Escape section title safely
                escaped_title = re.escape(title)

                # 2. Build pattern (DO NOT use f-strings or raw strings here)
                pattern = "(\\\\section\\{" + escaped_title + "\\})(.*?)(?=\\\\section\\{|\\\\end\\{document\\})"

                # 3. Rebuild the bullet points
                lines = edited_text.strip().split("\\n")
                rebuilt = "\n".join([f"\\resumeItem{{{line.strip()}}}" for line in lines if line.strip()])

                # 4. Build replacement text
                replacement_text = "\\1\n\\resumeItemListStart\n" + rebuilt + "\n\\resumeItemListEnd\n"

                # 5. Run the substitution
                updated_latex = re.sub(pattern, replacement_text, updated_latex, flags=re.DOTALL)


            st.code(updated_latex, language="latex")
            st.download_button("📥 Download Updated .tex", updated_latex, file_name="updated_resume.tex", mime="text/plain")
