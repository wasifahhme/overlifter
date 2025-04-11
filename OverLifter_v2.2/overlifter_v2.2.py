
import streamlit as st

st.set_page_config(page_title="OverLifter v2.2 — Regex-Free", layout="wide")
st.title("📄 OverLifter v2.2 — Regex-Free LaTeX Resume Editor")

uploaded_file = st.file_uploader("📤 Upload your LaTeX (.tex) resume", type=["tex"])

if uploaded_file:
    latex_text = uploaded_file.read().decode("utf-8")

    # Detect section blocks via simple string logic
    section_titles = []
    section_map = {}

    parts = latex_text.split("\section{")
    for i in range(1, len(parts)):
        header = parts[i].split("}")[0]
        body = parts[i].split("}", 1)[1]
        section_titles.append(header)
        section_map[header] = body

    edits = {}
    col1, col2 = st.columns([1, 1])

    with col1:
        st.header("🖊️ Edit Sections")
        for title in section_titles:
            content = section_map[title]
            items = []
            lines = content.split("\n")
            for line in lines:
                if "\resumeItem{" in line:
                    items.append(line.strip().replace("\resumeItem{", "").rstrip("}"))
            plain_text = "\n".join(items) if items else content.strip()
            with st.expander(f"{title}", expanded=False):
                edits[title] = st.text_area(f"{title} Bullets", plain_text, height=200)

    with col2:
        st.header("📄 Live .tex Preview")
        if st.button("🔁 Update Preview"):
            rebuilt_latex = latex_text.split("\section{")[0]
            for title in section_titles:
                bullet_lines = edits.get(title, "").split("\n")
                rebuilt_items = "\n".join([f"\resumeItem{{{line.strip()}}}" for line in bullet_lines if line.strip()])
                new_section = f"\section{{{title}}}\n\resumeItemListStart\n{rebuilt_items}\n\resumeItemListEnd"
                rebuilt_latex += new_section
            rebuilt_latex += "\end{document}"
            st.code(rebuilt_latex, language="latex")
            st.download_button("📥 Download Updated .tex", rebuilt_latex, file_name="updated_resume.tex", mime="text/plain")
