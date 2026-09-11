import gradio as gr
import requests
import os


# =========================================================
# CONFIGURATION
# =========================================================

API_URL = os.getenv(
    "API_URL",
    f"http://127.0.0.1:{os.getenv('PORT', '8000')}"
)


# =========================================================
# CUSTOM CSS
# =========================================================

CUSTOM_CSS = """

/* =========================================================
   GLOBAL
========================================================= */

body {
    background: #f4f7fb !important;
    font-family: "Inter", "Segoe UI", Arial, sans-serif !important;
}

.gradio-container {
    max-width: 1250px !important;
    margin: auto !important;
    padding: 0 24px 30px 24px !important;
}


/* =========================================================
   TOP HEADER
========================================================= */

.top-header {
    background: linear-gradient(
        135deg,
        #0f172a,
        #1e3a8a
    );

    color: white;

    padding: 26px 30px;

    border-radius: 0 0 18px 18px;

    margin-bottom: 28px;

    box-shadow:
        0 8px 25px rgba(15, 23, 42, 0.12);
}

.header-content {
    display: flex;

    align-items: center;

    justify-content: space-between;

    gap: 20px;
}

.header-left {
    display: flex;

    align-items: center;

    gap: 15px;
}

.header-logo {
    width: 52px;
    height: 52px;

    display: flex;

    align-items: center;
    justify-content: center;

    background: rgba(255,255,255,0.14);

    border: 1px solid rgba(255,255,255,0.18);

    border-radius: 14px;

    font-size: 25px;
}

.header-title {
    font-size: 25px;

    font-weight: 750;

    margin: 0;
}

.header-subtitle {
    color: #cbd5e1;

    font-size: 13px;

    margin-top: 4px;
}

.header-status {
    background: rgba(255,255,255,0.12);

    border: 1px solid rgba(255,255,255,0.18);

    color: #dbeafe;

    padding: 8px 13px;

    border-radius: 20px;

    font-size: 12px;

    font-weight: 600;
}


/* =========================================================
   PAGE INTRO
========================================================= */

.page-intro {
    margin-bottom: 22px;
}

.page-intro h1 {
    color: #0f172a;

    font-size: 28px;

    font-weight: 750;

    margin: 0 0 5px 0;
}

.page-intro p {
    color: #64748b;

    font-size: 14px;

    margin: 0;
}


/* =========================================================
   STAT CARDS
========================================================= */

.stat-card {
    background: white;

    border: 1px solid #e2e8f0;

    border-radius: 14px;

    padding: 19px;

    min-height: 118px;

    box-shadow:
        0 3px 12px rgba(15, 23, 42, 0.05);

    transition: 0.2s ease;
}

.stat-card:hover {
    transform: translateY(-2px);

    box-shadow:
        0 7px 18px rgba(15, 23, 42, 0.08);
}

.stat-icon {
    font-size: 23px;

    margin-bottom: 10px;
}

.stat-label {
    color: #64748b;

    font-size: 12px;

    font-weight: 650;

    text-transform: uppercase;

    letter-spacing: 0.3px;
}

.stat-value {
    color: #0f172a;

    font-size: 28px;

    font-weight: 750;

    margin-top: 4px;
}


/* =========================================================
   MAIN CONTENT CARD
========================================================= */

.content-card {
    background: white !important;

    border: 1px solid #e2e8f0 !important;

    border-radius: 15px !important;

    padding: 23px !important;

    margin-top: 20px !important;

    box-shadow:
        0 3px 12px rgba(15, 23, 42, 0.04) !important;
}

.section-heading {
    color: #0f172a;

    font-size: 19px;

    font-weight: 700;

    margin-bottom: 4px;
}

.section-description {
    color: #64748b;

    font-size: 13px;

    margin-bottom: 18px;
}


/* =========================================================
   TABS
========================================================= */

.tabs-container {
    margin-top: 24px;
}

button[role="tab"] {
    font-weight: 650 !important;

    color: #64748b !important;

    border-radius: 8px !important;
}

button[role="tab"][aria-selected="true"] {
    color: #1d4ed8 !important;

    border-bottom: 2px solid #2563eb !important;
}


/* =========================================================
   BUTTONS
========================================================= */

button {
    border-radius: 9px !important;

    font-weight: 650 !important;
}

.primary-btn button {
    background: #2563eb !important;

    color: white !important;

    border: none !important;
}

.primary-btn button:hover {
    background: #1d4ed8 !important;
}

.delete-btn button {
    background: #dc2626 !important;

    color: white !important;

    border: none !important;
}

.delete-btn button:hover {
    background: #b91c1c !important;
}

.secondary-btn button {
    background: #f1f5f9 !important;

    color: #334155 !important;

    border: 1px solid #cbd5e1 !important;
}


/* =========================================================
   INPUTS
========================================================= */

input,
textarea,
.gr-input {
    border-radius: 9px !important;

    border-color: #cbd5e1 !important;
}

input:focus,
textarea:focus {
    border-color: #2563eb !important;

    box-shadow:
        0 0 0 2px rgba(37, 99, 235, 0.12) !important;
}


/* =========================================================
   INFORMATION BOX
========================================================= */

.info-box {
    background: #eff6ff;

    border: 1px solid #bfdbfe;

    color: #1e40af;

    padding: 13px 15px;

    border-radius: 9px;

    font-size: 13px;

    margin: 15px 0;
}


/* =========================================================
   WARNING BOX
========================================================= */

.warning-box {
    background: #fef2f2;

    border: 1px solid #fecaca;

    color: #991b1b;

    padding: 13px 15px;

    border-radius: 9px;

    font-size: 13px;

    margin: 15px 0;
}


/* =========================================================
   TABLE
========================================================= */

.table-card {
    background: white !important;

    border: 1px solid #e2e8f0 !important;

    border-radius: 15px !important;

    padding: 22px !important;

    margin-top: 20px !important;
}


/* =========================================================
   STATUS MESSAGE
========================================================= */

.status-message textarea {
    background: #f8fafc !important;

    font-weight: 600 !important;
}


/* =========================================================
   FOOTER
========================================================= */

.app-footer {
    text-align: center;

    color: #94a3b8;

    font-size: 12px;

    padding: 30px 0 10px 0;
}

.app-footer hr {
    border: none;

    border-top: 1px solid #e2e8f0;

    margin-bottom: 18px;
}


/* =========================================================
   MOBILE
========================================================= */

@media (max-width: 700px) {

    .gradio-container {
        padding: 0 12px 20px 12px !important;
    }

    .header-content {
        flex-direction: column;

        align-items: flex-start;
    }

    .header-status {
        align-self: flex-start;
    }

    .page-intro h1 {
        font-size: 24px;
    }

}

"""


# =========================================================
# API FUNCTIONS
# =========================================================

def get_students():

    try:

        response = requests.get(
            f"{API_URL}/students",
            timeout=10
        )

        if response.status_code == 200:

            result = response.json()

            return result.get("data", [])

        return []

    except Exception:

        return []


# =========================================================
# FORMAT STUDENTS
# =========================================================

def format_students(students):

    return [

        [
            student.get("id"),
            student.get("name"),
            student.get("course"),
            student.get("marks")
        ]

        for student in students

    ]


# =========================================================
# CALCULATE STATISTICS
# =========================================================

def calculate_stats(students):

    total = len(students)

    if total == 0:
        return 0, 0, 0

    marks = [
        student.get("marks", 0)
        for student in students
    ]

    average = round(
        sum(marks) / total,
        2
    )

    highest = max(marks)

    return total, average, highest


# =========================================================
# STAT CARD HTML
# =========================================================

def total_card(value):

    return f"""
    <div class="stat-card">

        <div class="stat-icon">
            👨‍🎓
        </div>

        <div class="stat-label">
            Total Students
        </div>

        <div class="stat-value">
            {value}
        </div>

    </div>
    """


def average_card(value):

    return f"""
    <div class="stat-card">

        <div class="stat-icon">
            📊
        </div>

        <div class="stat-label">
            Average Marks
        </div>

        <div class="stat-value">
            {value}
        </div>

    </div>
    """


def highest_card(value):

    return f"""
    <div class="stat-card">

        <div class="stat-icon">
            🏆
        </div>

        <div class="stat-label">
            Highest Marks
        </div>

        <div class="stat-value">
            {value}
        </div>

    </div>
    """


# =========================================================
# REFRESH DASHBOARD
# =========================================================

def refresh_dashboard():

    students = get_students()

    total, average, highest = calculate_stats(
        students
    )

    return (
        format_students(students),
        total_card(total),
        average_card(average),
        highest_card(highest)
    )


# =========================================================
# ADD STUDENT
# =========================================================

def add_student(name, course, marks):

    if not name or not name.strip():

        return (
            "⚠️ Please enter student name.",
            *refresh_dashboard()
        )

    if not course or not course.strip():

        return (
            "⚠️ Please enter course.",
            *refresh_dashboard()
        )

    if marks is None:

        return (
            "⚠️ Please enter marks.",
            *refresh_dashboard()
        )

    try:

        marks = int(marks)

        if marks < 0 or marks > 100:

            return (
                "⚠️ Marks must be between 0 and 100.",
                *refresh_dashboard()
            )

        response = requests.post(

            f"{API_URL}/students",

            params={
                "name": name.strip(),
                "course": course.strip(),
                "marks": marks
            },

            timeout=10
        )

        if response.status_code == 200:

            return (
                "✅ Student added successfully!",
                *refresh_dashboard()
            )

        return (
            f"❌ Failed to add student: {response.text}",
            *refresh_dashboard()
        )

    except ValueError:

        return (
            "⚠️ Marks must be a valid number.",
            *refresh_dashboard()
        )

    except Exception as e:

        return (
            f"❌ Backend connection error: {e}",
            *refresh_dashboard()
        )


# =========================================================
# UPDATE STUDENT
# =========================================================

def update_student(
    student_id,
    name,
    course,
    marks
):

    if student_id is None:

        return (
            "⚠️ Please enter Student ID.",
            *refresh_dashboard()
        )

    if not name or not name.strip():

        return (
            "⚠️ Please enter student name.",
            *refresh_dashboard()
        )

    if not course or not course.strip():

        return (
            "⚠️ Please enter course.",
            *refresh_dashboard()
        )

    if marks is None:

        return (
            "⚠️ Please enter marks.",
            *refresh_dashboard()
        )

    try:

        student_id = int(student_id)

        marks = int(marks)

        if marks < 0 or marks > 100:

            return (
                "⚠️ Marks must be between 0 and 100.",
                *refresh_dashboard()
            )

        response = requests.put(

            f"{API_URL}/students/{student_id}",

            params={
                "name": name.strip(),
                "course": course.strip(),
                "marks": marks
            },

            timeout=10
        )

        if response.status_code == 200:

            return (
                "✅ Student updated successfully!",
                *refresh_dashboard()
            )

        return (
            f"❌ Failed to update student: {response.text}",
            *refresh_dashboard()
        )

    except ValueError:

        return (
            "⚠️ Student ID and marks must be valid numbers.",
            *refresh_dashboard()
        )

    except Exception as e:

        return (
            f"❌ Backend connection error: {e}",
            *refresh_dashboard()
        )


# =========================================================
# DELETE STUDENT
# =========================================================

def delete_student(student_id):

    if student_id is None:

        return (
            "⚠️ Please enter Student ID.",
            *refresh_dashboard()
        )

    try:

        student_id = int(student_id)

        response = requests.delete(

            f"{API_URL}/students/{student_id}",

            timeout=10
        )

        if response.status_code == 200:

            return (
                "✅ Student deleted successfully!",
                *refresh_dashboard()
            )

        return (
            f"❌ Failed to delete student: {response.text}",
            *refresh_dashboard()
        )

    except ValueError:

        return (
            "⚠️ Student ID must be a valid number.",
            *refresh_dashboard()
        )

    except Exception as e:

        return (
            f"❌ Backend connection error: {e}",
            *refresh_dashboard()
        )


# =========================================================
# EMPTY INITIAL VALUES
# =========================================================

# IMPORTANT:
#
# Do not call get_students() here.
#
# FastAPI imports this file while the server is starting.
# At that moment the API may not yet be available.
#
# The actual database data is loaded using demo.load()
# after the browser opens.

EMPTY_TABLE = []


# =========================================================
# GRADIO APPLICATION
# =========================================================

with gr.Blocks(
    title="StudentHub"
) as demo:


    # =====================================================
    # TOP HEADER
    # =====================================================

    gr.HTML(
        """
        <div class="top-header">

            <div class="header-content">

                <div class="header-left">

                    <div class="header-logo">
                        🎓
                    </div>

                    <div>

                        <div class="header-title">
                            StudentHub
                        </div>

                        <div class="header-subtitle">
                            Student Management System
                            • Academic Record Management
                        </div>

                    </div>

                </div>


                <div class="header-status">
                    ● System Online
                </div>

            </div>

        </div>
        """
    )


    # =====================================================
    # PAGE INTRODUCTION
    # =====================================================

    gr.HTML(
        """
        <div class="page-intro">

            <h1>
                Student Dashboard
            </h1>

            <p>
                Manage student records, courses and academic
                performance from one place.
            </p>

        </div>
        """
    )


    # =====================================================
    # STATISTICS
    # =====================================================

    with gr.Row():

        total_students = gr.HTML(
            total_card(0),
            scale=1
        )

        average_marks = gr.HTML(
            average_card(0),
            scale=1
        )

        highest_marks = gr.HTML(
            highest_card(0),
            scale=1
        )


    # =====================================================
    # NAVIGATION TABS
    # =====================================================

    with gr.Tabs(
        elem_classes="tabs-container"
    ):


        # =================================================
        # DASHBOARD TAB
        # =================================================

        with gr.Tab("📋 Student Records"):

            with gr.Group(
                elem_classes="table-card"
            ):

                gr.HTML(
                    """
                    <div class="section-heading">
                        Student Records
                    </div>

                    <div class="section-description">
                        View all student records currently
                        stored in the database.
                    </div>
                    """
                )


                with gr.Row():

                    refresh_button = gr.Button(
                        "🔄 Refresh Records",
                        variant="primary",
                        elem_classes="primary-btn"
                    )


                students_table = gr.Dataframe(

                    value=EMPTY_TABLE,

                    headers=[
                        "Student ID",
                        "Student Name",
                        "Course",
                        "Marks"
                    ],

                    datatype=[
                        "number",
                        "str",
                        "str",
                        "number"
                    ],

                    interactive=False,

                    label="Database Records"
                )


        # =================================================
        # ADD STUDENT TAB
        # =================================================

        with gr.Tab("➕ Add Student"):

            with gr.Group(
                elem_classes="content-card"
            ):

                gr.HTML(
                    """
                    <div class="section-heading">
                        Add New Student
                    </div>

                    <div class="section-description">
                        Register a new student in the system.
                    </div>

                    <div class="info-box">
                        💡 Student ID will be generated
                        automatically by Supabase.
                    </div>
                    """
                )


                with gr.Row():

                    add_name = gr.Textbox(
                        label="Student Name",
                        placeholder="Enter full name"
                    )

                    add_course = gr.Textbox(
                        label="Course",
                        placeholder="Example: Computer Science"
                    )


                add_marks = gr.Number(
                    label="Marks",
                    minimum=0,
                    maximum=100,
                    precision=0
                )


                add_button = gr.Button(
                    "➕ Register Student",
                    variant="primary",
                    elem_classes="primary-btn"
                )


                add_status = gr.Textbox(
                    label="System Message",
                    interactive=False,
                    elem_classes="status-message"
                )


        # =================================================
        # UPDATE STUDENT TAB
        # =================================================

        with gr.Tab("✏️ Update Student"):

            with gr.Group(
                elem_classes="content-card"
            ):

                gr.HTML(
                    """
                    <div class="section-heading">
                        Update Student
                    </div>

                    <div class="section-description">
                        Modify the details of an existing
                        student record.
                    </div>

                    <div class="info-box">
                        🔎 Enter the Student ID along with
                        the updated information.
                    </div>
                    """
                )


                update_id = gr.Number(
                    label="Student ID",
                    minimum=1,
                    precision=0
                )


                with gr.Row():

                    update_name = gr.Textbox(
                        label="Student Name",
                        placeholder="Updated student name"
                    )

                    update_course = gr.Textbox(
                        label="Course",
                        placeholder="Updated course"
                    )


                update_marks = gr.Number(
                    label="Marks",
                    minimum=0,
                    maximum=100,
                    precision=0
                )


                update_button = gr.Button(
                    "✏️ Update Student",
                    variant="primary",
                    elem_classes="primary-btn"
                )


                update_status = gr.Textbox(
                    label="System Message",
                    interactive=False,
                    elem_classes="status-message"
                )


        # =================================================
        # DELETE STUDENT TAB
        # =================================================

        with gr.Tab("🗑️ Delete Student"):

            with gr.Group(
                elem_classes="content-card"
            ):

                gr.HTML(
                    """
                    <div class="section-heading">
                        Delete Student
                    </div>

                    <div class="section-description">
                        Permanently remove a student record
                        from the database.
                    </div>

                    <div class="warning-box">
                        ⚠️ Warning: this action permanently
                        deletes the selected record.
                    </div>
                    """
                )


                delete_id = gr.Number(
                    label="Student ID",
                    minimum=1,
                    precision=0
                )


                delete_button = gr.Button(
                    "🗑️ Delete Student",
                    variant="stop",
                    elem_classes="delete-btn"
                )


                delete_status = gr.Textbox(
                    label="System Message",
                    interactive=False,
                    elem_classes="status-message"
                )


    # =====================================================
    # FOOTER
    # =====================================================

    gr.HTML(
        """
        <div class="app-footer">

            <hr>

            <b>🎓 StudentHub</b>

            <br>

            Student Management System

            <br><br>

            FastAPI • Gradio • Supabase PostgreSQL

        </div>
        """
    )


    # =====================================================
    # PAGE LOAD
    # =====================================================

    demo.load(

        fn=refresh_dashboard,

        inputs=[],

        outputs=[
            students_table,
            total_students,
            average_marks,
            highest_marks
        ]

    )


    # =====================================================
    # REFRESH EVENT
    # =====================================================

    refresh_button.click(

        fn=refresh_dashboard,

        inputs=[],

        outputs=[
            students_table,
            total_students,
            average_marks,
            highest_marks
        ]

    )


    # =====================================================
    # ADD EVENT
    # =====================================================

    add_button.click(

        fn=add_student,

        inputs=[
            add_name,
            add_course,
            add_marks
        ],

        outputs=[
            add_status,
            students_table,
            total_students,
            average_marks,
            highest_marks
        ]

    )


    # =====================================================
    # UPDATE EVENT
    # =====================================================

    update_button.click(

        fn=update_student,

        inputs=[
            update_id,
            update_name,
            update_course,
            update_marks
        ],

        outputs=[
            update_status,
            students_table,
            total_students,
            average_marks,
            highest_marks
        ]

    )


    # =====================================================
    # DELETE EVENT
    # =====================================================

    delete_button.click(

        fn=delete_student,

        inputs=[
            delete_id
        ],

        outputs=[
            delete_status,
            students_table,
            total_students,
            average_marks,
            highest_marks
        ]

    )


# =========================================================
# IMPORTANT
# =========================================================
#
# DO NOT ADD:
#
# demo.launch()
#
# Backend/main.py mounts this Gradio application
# inside FastAPI.
#
# Run from the project root:
#
# uvicorn Backend.main:app --reload
#
# =========================================================