
import streamlit as st
import re

st.set_page_config(page_title="OverLifter v2.3.1", layout="wide")
st.title("🧠 OverLifter v2.3.1 — Projects Section Editor")

uploaded_file = st.file_uploader("📤 Upload your LaTeX (.tex) resume", type=["tex"])

if uploaded_file:
    raw_tex = uploaded_file.read().decode("utf-8")

    # Parse Projects section
    pattern = r"\\section\{Projects\}(.*?)(?=\\section\{|\\end\{document\})"
    match = re.search(pattern, raw_tex, re.DOTALL)

    if match:
        project_section = match.group(1)
        entries = re.findall(
            r"\\resumeProjectHeading\{\\textbf\{(.+?)\} \| \emph\{(.+?)\}\}\{(.+?)\}(.*?)\\resumeItemListEnd",
            project_section,
            re.DOTALL
        )

        edited_projects = []

        col1, col2 = st.columns([1, 1])
        with col1:
            st.header("🛠️ Edit Projects")
            for i, (title, tech, date, bullets_block) in enumerate(entries):
                with st.expander(f"{title} — {date}", expanded=False):
                    new_title = st.text_input(f"Project Title {i+1}", title)
                    new_tech = st.text_input(f"Tech Stack {i+1}", tech)
                    new_date = st.text_input(f"Date {i+1}", date)
                    bullets = re.findall(r"\\resumeItem\{(.*?)\}", bullets_block or "", re.DOTALL)
                    new_bullets = []
                    for j, bullet in enumerate(bullets):
                        new_bullets.append(st.text_area(f"Bullet {j+1}", bullet.strip(), key=f"{i}_{j}"))
                    edited_projects.append({
                        "title": new_title,
                        "tech": new_tech,
                        "date": new_date,
                        "bullets": new_bullets
                    })

        with col2:
            st.header("📄 Live .tex Preview")
            if st.button("🔁 Generate Updated .tex"):
                rebuilt = "\\section{Projects}\n  \\resumeSubHeadingListStart"
                for proj in edited_projects:
                    rebuilt += (
                        f"\n    \\resumeProjectHeading"
                        f"{{\\textbf{{{proj['title']}}} $|$ \\emph{{{proj['tech']}}}}}"
                        f"{{{proj['date']}}}"
                        f"\n    \\resumeItemListStart"
                    )
                    for bullet in proj['bullets']:
                        rebuilt += f"\n      \\resumeItem{{{bullet.strip()}}}"
                    rebuilt += "\n    \\resumeItemListEnd"
                rebuilt += "\n  \\resumeSubHeadingListEnd"

                new_tex = re.sub(pattern, rebuilt, raw_tex, count=1, flags=re.DOTALL)
                st.code(new_tex, language="latex")
                st.download_button("📥 Download Updated .tex", new_tex, file_name="updated_resume.tex", mime="text/plain")
    else:
        st.warning("⚠️ Could not locate Projects section in the uploaded .tex file.")
