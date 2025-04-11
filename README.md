
# OverLifter

OverLifter is an intelligent LaTeX resume editor designed for non-technical users. It provides a structured, interactive interface for editing LaTeX resumes without the need to manually navigate or modify `.tex` files.

Built entirely without regular expressions, OverLifter parses LaTeX line-by-line, allowing precise control over each section while preserving formatting, style, and compatibility with platforms like Overleaf.

## Table of Contents
- [Features](#features)
- [Tech Stack](#tech-stack)
- [How to Run](#how-to-run)
- [Usage Notes](#usage-notes)
- [Version History](#version-history)
- [Project Status](#project-status)
- [Contributing](#contributing)
- [License](#license)

## Features

- Fully regex-free LaTeX parsing and regeneration
- Real-time editing of the "Projects" section, including:
  - Project title
  - Tech stack
  - Dates
  - Bullet points (add/edit)
- Automatic `.tex` regeneration preserving all template formatting
- Download-ready `.tex` file for Overleaf or PDF export
- Clean and intuitive tabbed interface built with Streamlit
- Foundation laid for future editing of Experience, Education, Skills, etc.

## Tech Stack

- Python
- Streamlit
- Custom line-by-line LaTeX parser (no regex)

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/OverLifter.git
   cd OverLifter
   ```

2. Install dependencies:
   ```bash
   pip install streamlit
   ```

3. Launch the application:
   ```bash
   streamlit run overlifter_v2.4.1.py
   ```

4. Upload your `.tex` file and begin editing through the web interface.

## Usage Notes

OverLifter is optimized for LaTeX resumes using `\resumeProjectHeading`, `\resumeItemListStart`, and related macros.  
We recommend using a template based on the one by [Jake Gutierrez](https://github.com/jakegut/resume-template).

You can upload your `.tex` resume file and start editing immediately.

## Version History

See [VERSIONS.md](VERSIONS.md) for a detailed changelog of all OverLifter releases.

## Project Status

Current: Stable (v2.4.1)  
Next: Support for Experience, Education, and Skills sections.

## Roadmap

- [x] Projects section parsing and editing
- [ ] Experience section with nested roles and bullets
- [ ] Education editor
- [ ] Custom section creator (UI tab-based)
- [ ] AI-based bullet suggestions

## Contributing

Contributions are welcome. If you'd like to extend OverLifter to additional resume sections, improve UI components, or propose ideas, feel free to open a pull request or issue.

## License

This project is open source and available under the MIT License.
