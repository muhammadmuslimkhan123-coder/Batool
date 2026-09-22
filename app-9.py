import streamlit as st
from datetime import date

SCHOOL_NAME = "Govt Girls High School Mandi Town, Bhakkar"
LOCATION = "Mandi Town, Bhakkar, Punjab, Pakistan"
PRINCIPAL = "Masooma Batool"
CONTACT = "03308995876"
EMAIL = "gg_hs_mandi_bhakkar@example.com"

st.set_page_config(
    page_title="Govt Girls High School Mandi Town Bhakkar",
    page_icon="🏫",
    layout="wide"
)

st.title("🏫 " + SCHOOL_NAME)
st.subheader("School Management & Information Portal")

st.info(
    "Welcome to the official school portal. "
    "Here you can find school information, notices, admission details, "
    "classes, events and contact information."
)

st.sidebar.title("📚 School Portal")
menu = st.sidebar.radio(
    "Select Section",
    [
        "Home", "About School", "Principal Message", "Teachers & Staff",
        "Classes & Subjects", "News & Notices", "Events", "Achievements",
        "Gallery", "Admissions", "Student Information", "Downloads", "Contact Us"
    ]
)

if menu == "Home":
    st.header("🏠 Welcome")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("School Type", "Government")
    with col2:
        st.metric("School Level", "Girls High School")
    with col3:
        st.metric("Location", "Bhakkar")

    st.markdown("---")
    st.subheader("School Introduction")
    st.write(
        f"{SCHOOL_NAME} is a government girls high school located in "
        f"{LOCATION}. The school provides educational facilities and a "
        "learning environment for female students."
    )
    st.success("🎓 Education • Discipline • Character Building • Success")

elif menu == "About School":
    st.header("🏫 About Our School")
    st.write("School Name:", SCHOOL_NAME)
    st.write("Location:", LOCATION)
    st.write("Principal:", PRINCIPAL)
    st.write("Contact Number:", CONTACT)

    st.subheader("Our Mission")
    st.write(
        "To provide quality education, develop confidence and promote "
        "discipline, knowledge and positive character among students."
    )
    st.subheader("Our Vision")
    st.write(
        "To prepare students for a successful educational and professional "
        "future through knowledge, skills and values."
    )
    st.subheader("School Facilities")
    for facility in [
        "📚 Library", "🔬 Science Laboratory", "💻 Computer Education",
        "🏃 Playground", "🚰 Clean Drinking Water", "🚻 Sanitation Facilities",
        "🪑 Classrooms", "🌳 School Environment"
    ]:
        st.write("•", facility)

elif menu == "Principal Message":
    st.header("👩‍🏫 Principal's Message")
    st.write("Principal:", PRINCIPAL)
    st.success(
        "Welcome to Govt Girls High School Mandi Town, Bhakkar. Our goal is "
        "to provide students with quality education and a positive learning "
        "environment. We encourage our students to work hard, respect others "
        "and become responsible members of society."
    )

elif menu == "Teachers & Staff":
    st.header("👩‍🏫 Teachers & Staff")
    teachers = [
        ("1", "Masooma Batool", "Principal"),
        ("2", "Teacher 1", "Subject Teacher"),
        ("3", "Teacher 2", "Subject Teacher"),
        ("4", "Teacher 3", "Subject Teacher"),
        ("5", "Teacher 4", "Subject Teacher")
    ]
    st.table({
        "No.": [x[0] for x in teachers],
        "Name": [x[1] for x in teachers],
        "Designation": [x[2] for x in teachers]
    })

elif menu == "Classes & Subjects":
    st.header("📚 Classes & Subjects")
    classes = {
        "Class 6": ["English", "Urdu", "Mathematics", "Science", "Computer", "Islamiat"],
        "Class 7": ["English", "Urdu", "Mathematics", "Science", "Computer", "Islamiat"],
        "Class 8": ["English", "Urdu", "Mathematics", "Science", "Computer", "Islamiat"],
        "Class 9": ["English", "Urdu", "Mathematics", "Physics", "Chemistry", "Biology", "Computer", "Islamiat"],
        "Class 10": ["English", "Urdu", "Mathematics", "Physics", "Chemistry", "Biology", "Computer", "Islamiat"]
    }
    selected_class = st.selectbox("Select Class", list(classes.keys()))
    st.subheader(selected_class)
    for subject in classes[selected_class]:
        st.write("📘", subject)

elif menu == "News & Notices":
    st.header("📢 News & Notices")
    for notice in [
        "School admissions are open.",
        "Students should maintain regular attendance.",
        "Monthly tests will be conducted according to the school schedule.",
        "Students should follow school discipline rules.",
        "Parents are requested to stay connected with the school."
    ]:
        st.warning("📢 " + notice)

elif menu == "Events":
    st.header("📅 School Events")
    for event_name, event_date in [
        ("Independence Day", "14 August"),
        ("Annual Sports Day", "School Schedule"),
        ("Science Exhibition", "School Schedule"),
        ("Parents Meeting", "School Schedule"),
        ("Annual Prize Distribution", "School Schedule")
    ]:
        st.write(f"🎉 **{event_name}** — {event_date}")

elif menu == "Achievements":
    st.header("🏆 School Achievements")
    for achievement in [
        "🏆 Academic performance",
        "🏅 Student participation in competitions",
        "🥇 Sports activities",
        "📚 Educational activities",
        "🎨 Co-curricular activities"
    ]:
        st.success(achievement)

elif menu == "Gallery":
    st.header("🖼️ School Gallery")
    st.write("School photographs can be added here by uploading image files.")
    uploaded_images = st.file_uploader(
        "Upload School Images",
        type=["jpg", "jpeg", "png"],
        accept_multiple_files=True
    )
    if uploaded_images:
        columns = st.columns(3)
        for index, image in enumerate(uploaded_images):
            with columns[index % 3]:
                st.image(image, caption=image.name, use_container_width=True)

elif menu == "Admissions":
    st.header("📝 Online Admission Information")
    st.write(
        "Students/parents can contact the school for current admission "
        "requirements, dates and required documents."
    )
    st.subheader("Admission Inquiry Form")
    name = st.text_input("Student Name")
    father_name = st.text_input("Father/Guardian Name")
    class_name = st.selectbox(
        "Apply For Class",
        ["Class 6", "Class 7", "Class 8", "Class 9", "Class 10"]
    )
    phone = st.text_input("Contact Number")
    address = st.text_area("Address")

    if st.button("Submit Admission Inquiry"):
        if name and father_name and phone and address:
            st.success("Admission inquiry submitted successfully.")
            st.write("Student:", name)
            st.write("Father/Guardian:", father_name)
            st.write("Class:", class_name)
            st.write("Contact:", phone)
        else:
            st.error("Please fill all required fields.")

elif menu == "Student Information":
    st.header("🎓 Student Information")
    student_name = st.text_input("Student Name")
    roll_number = st.text_input("Roll Number")
    student_class = st.selectbox(
        "Class", ["Class 6", "Class 7", "Class 8", "Class 9", "Class 10"]
    )

    if st.button("Search Student"):
        if student_name and roll_number:
            st.info(
                f"Student: {student_name}\n\n"
                f"Roll Number: {roll_number}\n\n"
                f"Class: {student_class}"
            )
        else:
            st.warning("Please enter student name and roll number.")

elif menu == "Downloads":
    st.header("📥 Downloads")
    st.write(
        "School documents such as syllabus, date sheets, notices and other "
        "files can be uploaded here."
    )
    uploaded_file = st.file_uploader(
        "Upload School Document",
        type=["pdf", "docx", "txt"]
    )
    if uploaded_file:
        st.success(f"File uploaded: {uploaded_file.name}")
        st.download_button(
            label="⬇️ Download File",
            data=uploaded_file.getvalue(),
            file_name=uploaded_file.name
        )

elif menu == "Contact Us":
    st.header("📞 Contact Us")
    st.write("🏫 School:", SCHOOL_NAME)
    st.write("📍 Location:", LOCATION)
    st.write("👩‍🏫 Principal:", PRINCIPAL)
    st.write("📱 Contact:", CONTACT)
    st.write("📧 Email:", EMAIL)

    st.subheader("Contact Form")
    visitor_name = st.text_input("Your Name")
    visitor_phone = st.text_input("Your Phone Number")
    message = st.text_area("Your Message")

    if st.button("Send Message"):
        if visitor_name and visitor_phone and message:
            st.success("Your message has been submitted.")
        else:
            st.error("Please complete all fields.")

st.markdown("---")
st.caption(
    f"© {date.today().year} {SCHOOL_NAME} | School Information Portal"
)
