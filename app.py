from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Anuradha Madurapperuma"
PAGE_ICON = ":wave:"
NAME = "Anuradha Madurapperuma"
DESCRIPTION = """
Data Scientist, PhD in Information Systems.
"""
EMAIL = "anuradhaerandathi@gmail.com"
SOCIAL_MEDIA = {
    "YouTube": "https://youtube.com/c/codingisfun",
    "LinkedIn": "linkedin.com/in/anuradha-madurapperuma-82211760",
    "GitHub": "https://github.com",
    "Twitter": "https://twitter.com",
}
#PROJECTS = {
 #   "🏆 Sales Dashboard - Comparing sales across three stores": "https://youtu.be/Sb0A9i6d320",
  #  "🏆 Income and Expense Tracker - Web app with NoSQL database": "https://youtu.be/3egaMfE9388",
   # "🏆 Desktop Application - Excel2CSV converter with user settings & menubar": "https://youtu.be/LzCfNanQ_9c",
    #"🏆 MyToolBelt - Custom MS Excel add-in to combine Python & Excel": "https://pythonandvba.com/mytoolbelt/",
#}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ 4 years of experience on working in data science project
- ✔️ 9 years of experience in research and academic sector
- ✔️ Strong hands on experience and knowledge in Python and Excel
- ✔️ Good understanding of statistical principles and their respective applications
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn, Pandas), SQL, Java, HTML
- 📊 Data Visulization: PowerBi, MS Excel, Plotly
- 📚 Modeling: Logistic regression, linear regression, Survival analysis, Machine learnign algorithms
- 🗄️ Databases: MySQL
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Tutor | University of Waikato**")
st.write("06/2020 - Present")
st.write(
    """
- ► Assignment marking/ preparation of marking schemes

- ► Managing Moodle, grade assigning, handling discussion forums. 

"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Lecturer | Sabaragamuwa University of Sri Lanka**")
st.write("10/2019 - 01/2018")
st.write(
    """
- ► Conduct lectures on data mining, machine learning, data structures, image processingSupervising students for their final year software projects.
- ► Supervising students for their final year software projects.
targets likely to renew, and presented analysis to leadership, which led to a YoY revenue increase of $300K
- Farmers Management System (FMS) as a E-Market of Farmers and Customers for Agricultural Products. R.T.Hendawitharana.
- Development of Web Application “Find the Criminal”. G. R.Darshana.
"""
)

# --- JOB 3
st.write('\n')
st.write("🚧", "**Program Manager-cum-Lecturer | Esoft Metro Campus**")
st.write("12/2014 - 12/2017")
st.write(
    """
- ► Managed BIT degree division, scheduled lecturer time slots, made class timetables, designed promotion campaigns.
- ► Worked as a student councilor
- ► Conducted Lectures on
o Object Oriented Programming Language
o System designing
"""
)

# --- JOB 4
st.write('\n')
st.write("🚧", "**Lecturer | University of Peradeniya**")
st.write("02/2014 - 11/2014")
st.write(
    """
- ► Assisted on theory and practical classes for undergraduates.
- ► Exam Invigilation, paper marking and mark sheet preparation.
- ► Presented planned lectures and class activities weekly, evaluated
the effectiveness of planned class works, make class assignment
and quizzes.

"""
)

# --- Projects & Accomplishments ---
#st.write('\n')
#st.subheader("Projects & Accomplishments")
#st.write("---")
#for project, link in PROJECTS.items():
#    st.write(f"[{project}]({link})")
