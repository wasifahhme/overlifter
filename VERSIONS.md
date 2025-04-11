
# OverLifter — Version History & Changelog

This document outlines the evolution of OverLifter across all major versions.

---

## v1.0 — Basic LaTeX Section Editor (Hardcoded)
- Basic editing of predefined sections (Experience, Education) via Streamlit
- Manually parsed `\section{}` blocks
- Edited raw LaTeX text directly
- Did not support subheadings, bullets, or structured editing

---

## v1.5 — File Upload Support
- Users could upload their `.tex` resume files
- Dynamically extracted sections from uploaded file
- Enabled download of updated `.tex`
- Still lacked block-level LaTeX awareness

---

## v2.0 — Split-Screen Editor UI
- Added split-screen view with editing on the left and `.tex` preview on the right
- Allowed visual verification before downloading updated file
- Formatting issues remained due to unstructured parsing

---

## v2.1 — ResumeItem Formatting Fix
- Introduced regeneration of `\resumeItem` bullets
- Wrapped bullets with `\resumeItemListStart` and `\resumeItemListEnd`
- Relied on regex, which caused issues with inconsistent formatting

---

## v2.2 — Regex-Free, Safer Rebuild (Alpha)
- Removed regex and switched to basic string parsing
- Isolated `\section{}` blocks with simple logic
- Unable to parse structured LaTeX blocks like `\resumeProjectHeading`

---

## v2.3 — First Field-by-Field Editing
- Parsed Projects section into structured fields:
  - Title
  - Tech stack
  - Date
  - Bullet points
- Enabled UI-based editing of each field
- Relied on regex, which caused breakage in some templates

---

## v2.3.1 — Regex-Free Rebuild with UI Tabs
- Fully removed regex
- Replaced with line-by-line parsing
- Tabbed UI allowed project-by-project editing
- Required explicit `\section{Projects}` to function properly

---

## v2.4 — Stable Regex-Free Parser
- Implemented line-by-line parsing throughout
- Identified `\resumeProjectHeading` blocks directly
- Bullet editing and addition supported
- Skipped projects if `\section{Projects}` was not present

---

## v2.4.1 — ProjectsFix Build
- Fixed detection of project blocks without requiring `\section{Projects}`
- Parsed projects based solely on `\resumeProjectHeading` and surrounding structure
- Provided clean `.tex` regeneration for use in Overleaf
- This version is the current base for continued development of Experience, Education, and future sections
