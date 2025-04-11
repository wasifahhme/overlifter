
import streamlit as st

st.set_page_config(page_title="OverLifter v2.4", layout="wide")
st.title("📄 OverLifter v2.4 — Regex-Free Resume Editor")

uploaded_file = st.file_uploader("📤 Upload your LaTeX (.tex) resume", type=["tex"])

if uploaded_file:
    lines = uploaded_file.read().decode("utf-8").splitlines()
    projects_section = []
    inside_projects = False
    current_project = {}
    projects = []

    def flush_project():
        if current_project:
            projects.append(current_project.copy())

    for line in lines:
        if "\section{Projects}" in line:
            inside_projects = True
            projects_section.append(line)
            continue
        if inside_projects and line.strip().startswith("\section{") and not "\section{Projects}" in line:
            inside_projects = False
            flush_project()
            projects_section.append(line)
            continue
        if inside_projects:
            projects_section.append(line)
            if "\resumeProjectHeading" in line:
                flush_project()
                parts = line.split("{")
                try:
                    title = parts[2].split("}")[0]
                    tech = parts[3].split("}")[0]
                    date = parts[4].split("}")[0]
                    current_project = {
                        "title": title.strip(),
                        "tech": tech.strip(),
                        "date": date.strip(),
                        "bullets": []
                    }
                except:
                    pass
            elif "\resumeItem{" in line and current_project:
                bullet = line.split("{", 1)[1].rstrip("}")
                current_project["bullets"].append(bullet.strip())

    flush_project()

    st.header("🛠️ Edit Projects")
    edited_projects = []

    for idx, proj in enumerate(projects):
        with st.expander(f"{proj['title']} — {proj['date']}", expanded=False):
            title = st.text_input(f"Project Title {idx}", value=proj['title'], key=f"title_{idx}")
            tech = st.text_input(f"Tech Stack {idx}", value=proj['tech'], key=f"tech_{idx}")
            date = st.text_input(f"Date {idx}", value=proj['date'], key=f"date_{idx}")
            bullets = []
            for bidx, bullet in enumerate(proj['bullets']):
                bullets.append(st.text_area(f"Bullet {bidx+1}", value=bullet, key=f"b_{idx}_{bidx}"))
            new_bullet = st.text_input(f"Add new bullet to {title}", key=f"new_b_{idx}")
            if new_bullet.strip():
                bullets.append(new_bullet.strip())
            edited_projects.append({
                "title": title,
                "tech": tech,
                "date": date,
                "bullets": bullets
            })

    if st.button("🔁 Generate Updated .tex"):
        output_lines = []
        inside_projects = False
        for line in lines:
            if "\section{Projects}" in line:
                inside_projects = True
                output_lines.append(line)
                output_lines.append("  \resumeSubHeadingListStart")
                for proj in edited_projects:
                    output_lines.append(f"    \resumeProjectHeading{{\textbf{{{proj['title']}}} $|$ \emph{{{proj['tech']}}}}}{{{proj['date']}}}")
                    output_lines.append("    \resumeItemListStart")
                    for bullet in proj['bullets']:
                        output_lines.append(f"      \resumeItem{{{bullet}}}")
                    output_lines.append("    \resumeItemListEnd")
                output_lines.append("  \resumeSubHeadingListEnd")
                continue
            if inside_projects and line.strip().startswith("\section{") and not "\section{Projects}" in line:
                inside_projects = False
                output_lines.append(line)
            elif not inside_projects:
                output_lines.append(line)

        final_tex = "\n".join(output_lines)
        st.code(final_tex, language="latex")
        st.download_button("📥 Download Updated .tex", final_tex, file_name="updated_resume.tex", mime="text/plain")
