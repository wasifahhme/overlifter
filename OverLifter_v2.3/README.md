
# OverLifter v2.3 🚀

**Now fully LaTeX-structure aware.**

## 🔧 What’s Fixed in v2.3
- ✅ Preserves all structural LaTeX blocks like \resumeSubheading
- ✅ Only edits \resumeItem bullets
- ✅ No more corrupted commands like `esumeItem`
- ✅ Safe string replacement logic — no regex
- ✅ Template-safe and job-seeker-friendly

## 🧰 Requirements
- Python 3.8+
- Streamlit (`pip install streamlit`)

## 🛠 How to Run
1. Open Terminal
2. Navigate to this folder:
   ```
   cd path/to/overlifter_v2.3
   ```
3. Run the app:
   ```
   streamlit run overlifter_v2.3.py
   ```

In your browser:
- Upload your `.tex`
- Edit only bullet points (`\resumeItem`)
- Preview full `.tex` live
- Download final clean LaTeX

Perfect for Overleaf resumes. Works with real-world templates.
