
import streamlit as st
import re

st.set_page_config(page_title="OverLifter v1.5", layout="wide")
st.title("📄 OverLifter v1.5 – Edit Your LaTeX Resume, No Code Needed")

uploaded_file = st.file_uploader("📤 Upload your LaTeX (.tex) resume", type=["tex"])

if uploaded_file is not None:
    latex_text = uploaded_file.read().decode("utf-8")

    # Extract sections using \section{} headings
    section_pattern = r"\\section\{(.+?)\}(.*?)(?=\\section\{|\\end\{document\})"
    matches = re.findall(section_pattern, latex_text, re.DOTALL)

    st.markdown("---")
    st.subheader("✏️ Edit Sections")
    section_edits = {}

    for section_title, content in matches:
        with st.expander(f"Section: {section_title}", expanded=True):
            edited_content = st.text_area(f"{section_title} Content", content.strip(), height=300)
            section_edits[section_title] = edited_content

    st.markdown("---")
    st.subheader("➕ Add a New Section")

    new_section_name = st.text_input("Section Title (e.g., Certifications)")
    new_section_content = st.text_area("Section Content", height=150)
    add_section = False
    if new_section_name and new_section_content:
        add_section = True

    if st.button("💾 Download Updated .tex"):
        updated_text = latex_text
        for title, new_content in section_edits.items():
            updated_text = re.sub(
                rf"(\\section\{{{re.escape(title)}\}})(.*?)(?=\\section\{{|\\end\{{document\}})",
                rf"\1\n{content}\n",
                updated_text,
                flags=re.DOTALL
            )
        if add_section:
            insert_text = f"\\section{{{new_section_name}}}\n{new_section_content}\n"
            updated_text = updated_text.replace("\end{document}", insert_text + "\end{document}")

        st.success("✅ Resume updated!")
        st.download_button("📥 Download .tex", updated_text, file_name="updated_resume.tex", mime="text/plain")
