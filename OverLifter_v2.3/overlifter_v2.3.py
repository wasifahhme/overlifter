
import streamlit as st

st.set_page_config(page_title="OverLifter v2.3", layout="wide")
st.title("📄 OverLifter v2.3 — Structure-Safe LaTeX Resume Editor")

uploaded_file = st.file_uploader("📤 Upload your LaTeX (.tex) resume", type=["tex"])

if uploaded_file:
    latex_text = uploaded_file.read().decode("utf-8")

    # Parse the document by section
    sections = latex_text.split("\\section{")
    section_titles = []
    section_map = {}

    for i in range(1, len(sections)):
        title = sections[i].split("}")[0]
        body = sections[i].split("}", 1)[1]
        section_titles.append(title)
        section_map[title] = body

    edits = {}
    col1, col2 = st.columns([1, 1])

    with col1:
        st.header("🖊️ Edit Bullet Points Only")
        for title in section_titles:
            content = section_map[title]
            lines = content.splitlines()
            editable_lines = []
            for line in lines:
                if "\\resumeItem{" in line:
                    clean = line.strip().replace("\\resumeItem{", "").rstrip("}")
                    editable_lines.append(clean)

            with st.expander(title, expanded=False):
                text = "\n".join(editable_lines)
                edits[title] = st.text_area(f"Edit \\resumeItem bullets for {title}", text, height=200)

    with col2:
        st.header("📄 Live .tex Preview")
        if st.button("🔁 Update Preview"):
            output = sections[0]  # everything before first section
            for title in section_titles:
                original = section_map[title]
                lines = original.splitlines()
                bullet_index = 0
                edited_bullets = edits[title].split("\n")
                new_lines = []
                for line in lines:
                    if "\\resumeItem{" in line:
                        if bullet_index < len(edited_bullets):
                            new_lines.append(f"\\resumeItem{{{edited_bullets[bullet_index].strip()}}}")
                            bullet_index += 1
                    else:
                        new_lines.append(line)
                rebuilt = "\n".join(new_lines)
                output += f"\\section{{{title}}}\n{rebuilt}"
            output += "\n\\end{document}"
            st.code(output, language="latex")
            st.download_button("📥 Download Updated .tex", output, file_name="updated_resume.tex", mime="text/plain")
