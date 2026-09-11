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
   STUDENTHUB - MODERN PROFESSIONAL UI
   Color Palette:
   Navy   : #0f172a
   Indigo : #4f46e5
   Blue   : #2563eb
   Slate  : #64748b
   Background : #f8fafc
========================================================= */


/* =========================================================
   GLOBAL PAGE
========================================================= */

body {
    background: #f8fafc !important;
    font-family: "Inter", "Segoe UI", Arial, sans-serif !important;
}

.gradio-container {
    max-width: 1280px !important;
    margin: 0 auto !important;
    padding: 0 28px 35px 28px !important;
    background: #f8fafc !important;
}


/* =========================================================
   TOP HEADER
========================================================= */

.top-header {
    position: relative;

    background:
        linear-gradient(
            135deg,
            #0f172a 0%,
            #172554 48%,
            #312e81 100%
        );

    color: white;

    padding: 30px 34px;

    margin: 0 -28px 32px -28px;

    border-radius: 0 0 24px 24px;

    box-shadow:
        0 12px 30px rgba(15, 23, 42, 0.15);

    overflow: hidden;
}


/* Decorative background glow */

.top-header::after {
    content: "";

    position: absolute;

    width: 220px;
    height: 220px;

    right: -70px;
    top: -100px;

    background: rgba(99, 102, 241, 0.18);

    border-radius: 50%;

    pointer-events: none;
}


.header-content {
    position: relative;
    z-index: 2;

    display: flex;

    align-items: center;

    justify-content: space-between;

    gap: 25px;
}


.header-left {
    display: flex;

    align-items: center;

    gap: 16px;
}


.header-logo {
    width: 58px;
    height: 58px;

    display: flex;

    align-items: center;
    justify-content: center;

    background: rgba(255, 255, 255, 0.12);

    border: 1px solid rgba(255, 255, 255, 0.18);

    border-radius: 16px;

    font-size: 27px;

    box-shadow:
        inset 0 1px 0 rgba(255,255,255,0.12);
}


.header-title {
    font-size: 28px;

    font-weight: 800;

    letter-spacing: -0.5px;

    margin: 0;
}


.header-subtitle {
    color: #cbd5e1;

    font-size: 13px;

    margin-top: 5px;

    letter-spacing: 0.1px;
}


.header-status {
    display: inline-flex;

    align-items: center;

    gap: 6px;

    background: rgba(255, 255, 255, 0.10);

    border: 1px solid rgba(255, 255, 255, 0.16);

    color: #dbeafe;

    padding: 9px 15px;

    border-radius: 999px;

    font-size: 12px;

    font-weight: 650;

    backdrop-filter: blur(8px);
}


/* =========================================================
   PAGE INTRODUCTION
========================================================= */

.page-intro {
    margin-bottom: 24px;

    padding-left: 2px;
}


.page-intro h1 {
    color: #0f172a;

    font-size: 30px;

    font-weight: 800;

    letter-spacing: -0.7px;

    margin: 0 0 6px 0;
}


.page-intro p {
    color: #64748b;

    font-size: 14px;

    line-height: 1.6;

    margin: 0;
}


/* =========================================================
   STATISTICS SECTION
========================================================= */

.stat-card {
    position: relative;

    background: #ffffff;

    border: 1px solid #e2e8f0;

    border-radius: 16px;

    padding: 20px;

    min-height: 125px;

    box-shadow:
        0 4px 14px rgba(15, 23, 42, 0.045);

    transition:
        transform 0.2s ease,
        box-shadow 0.2s ease,
        border-color 0.2s ease;

    overflow: hidden;
}


.stat-card::after {
    content: "";

    position: absolute;

    width: 90px;
    height: 90px;

    right: -35px;
    top: -35px;

    background: #eef2ff;

    border-radius: 50%;

    pointer-events: none;
}


.stat-card:hover {
    transform: translateY(-3px);

    border-color: #c7d2fe;

    box-shadow:
        0 10px 25px rgba(15, 23, 42, 0.08);
}


.stat-icon {
    position: relative;
    z-index: 2;

    width: 40px;
    height: 40px;

    display: flex;

    align-items: center;
    justify-content: center;

    background: #eef2ff;

    border-radius: 11px;

    font-size: 20px;

    margin-bottom: 12px;
}


.stat-label {
    position: relative;
    z-index: 2;

    color: #64748b;

    font-size: 11px;

    font-weight: 700;

    text-transform: uppercase;

    letter-spacing: 0.7px;
}


.stat-value {
    position: relative;
    z-index: 2;

    color: #0f172a;

    font-size: 29px;

    font-weight: 800;

    letter-spacing: -0.5px;

    margin-top: 3px;
}


/* =========================================================
   TABS
========================================================= */

.tabs-container {
    margin-top: 28px !important;
}


button[role="tab"] {
    color: #64748b !important;

    font-size: 14px !important;

    font-weight: 650 !important;

    border: none !important;

    border-radius: 9px !important;

    padding: 10px 15px !important;

    transition:
        background 0.2s ease,
        color 0.2s ease;
}


button[role="tab"]:hover {
    background: #f1f5f9 !important;

    color: #334155 !important;
}


button[role="tab"][aria-selected="true"] {
    color: #4338ca !important;

    background: #eef2ff !important;

    border-bottom: none !important;
}


/* =========================================================
   CONTENT CARDS
========================================================= */

.content-card,
.table-card {
    background: #ffffff !important;

    border: 1px solid #e2e8f0 !important;

    border-radius: 16px !important;

    padding: 25px !important;

    margin-top: 18px !important;

    box-shadow:
        0 4px 15px rgba(15, 23, 42, 0.045) !important;
}


.section-heading {
    color: #0f172a;

    font-size: 20px;

    font-weight: 750;

    letter-spacing: -0.25px;

    margin-bottom: 5px;
}


.section-description {
    color: #64748b;

    font-size: 13px;

    line-height: 1.6;

    margin-bottom: 19px;
}


/* =========================================================
   BUTTONS
========================================================= */

button {
    border-radius: 9px !important;

    font-weight: 650 !important;

    transition:
        transform 0.15s ease,
        box-shadow 0.15s ease,
        background 0.15s ease !important;
}


button:hover {
    transform: translateY(-1px);
}


/* Primary */

.primary-btn button {
    background:
        linear-gradient(
            135deg,
            #4f46e5,
            #2563eb
        ) !important;

    color: #ffffff !important;

    border: none !important;

    box-shadow:
        0 4px 12px rgba(79, 70, 229, 0.20) !important;
}


.primary-btn button:hover {
    background:
        linear-gradient(
            135deg,
            #4338ca,
            #1d4ed8
        ) !important;

    box-shadow:
        0 7px 17px rgba(79, 70, 229, 0.25) !important;
}


/* Delete */

.delete-btn button {
    background: #dc2626 !important;

    color: #ffffff !important;

    border: none !important;

    box-shadow:
        0 4px 10px rgba(220, 38, 38, 0.14) !important;
}


.delete-btn button:hover {
    background: #b91c1c !important;
}


/* Secondary */

.secondary-btn button {
    background: #f8fafc !important;

    color: #334155 !important;

    border: 1px solid #cbd5e1 !important;
}


.secondary-btn button:hover {
    background: #f1f5f9 !important;
}


/* =========================================================
   INPUT FIELDS
========================================================= */

input,
textarea,
.gr-input {
    background: #ffffff !important;

    border: 1px solid #cbd5e1 !important;

    border-radius: 9px !important;

    color: #0f172a !important;

    transition:
        border-color 0.2s ease,
        box-shadow 0.2s ease !important;
}


input:hover,
textarea:hover {
    border-color: #94a3b8 !important;
}


input:focus,
textarea:focus {
    border-color: #6366f1 !important;

    box-shadow:
        0 0 0 3px rgba(99, 102, 241, 0.12) !important;
}


/* Input labels */

label span {
    color: #334155 !important;

    font-weight: 650 !important;
}


/* =========================================================
   INFORMATION BOX
========================================================= */

.info-box {
    background:
        linear-gradient(
            135deg,
            #eff6ff,
            #eef2ff
        );

    border: 1px solid #c7d2fe;

    color: #3730a3;

    padding: 14px 16px;

    border-radius: 10px;

    font-size: 13px;

    line-height: 1.5;

    margin: 16px 0;
}


/* =========================================================
   WARNING BOX
========================================================= */

.warning-box {
    background: #fff7ed;

    border: 1px solid #fed7aa;

    color: #9a3412;

    padding: 14px 16px;

    border-radius: 10px;

    font-size: 13px;

    line-height: 1.5;

    margin: 16px 0;
}


/* =========================================================
   DATA TABLE
========================================================= */

.table-card .dataframe {
    border-radius: 10px !important;

    overflow: hidden !important;

    border: 1px solid #e2e8f0 !important;
}


.table-card th {
    background: #f8fafc !important;

    color: #334155 !important;

    font-weight: 700 !important;

    border-bottom: 1px solid #e2e8f0 !important;
}


.table-card td {
    color: #475569 !important;

    border-color: #eef2f7 !important;
}


.table-card tr:hover td {
    background: #f8fafc !important;
}


/* =========================================================
   STATUS MESSAGE
========================================================= */

.status-message textarea {
    background: #f8fafc !important;

    border-color: #e2e8f0 !important;

    color: #334155 !important;

    font-weight: 600 !important;
}


/* =========================================================
   FOOTER
========================================================= */

.app-footer {
    text-align: center;

    color: #94a3b8;

    font-size: 12px;

    line-height: 1.7;

    padding: 32px 0 10px 0;
}


.app-footer b {
    color: #64748b;
}


.app-footer hr {
    border: none;

    border-top: 1px solid #e2e8f0;

    margin: 0 0 18px 0;
}


/* =========================================================
   REMOVE SOME DEFAULT GRADIO VISUAL NOISE
========================================================= */

.gradio-container .block {
    border-radius: 12px;
}


.gradio-container .form {
    border-color: #e2e8f0 !important;
}


/* =========================================================
   MOBILE RESPONSIVE
========================================================= */

@media (max-width: 700px) {

    .gradio-container {
        padding: 0 14px 25px 14px !important;
    }

    .top-header {
        margin-left: -14px;
        margin-right: -14px;

        padding: 24px 20px;

        border-radius: 0 0 18px 18px;
    }

    .header-content {
        flex-direction: column;

        align-items: flex-start;
    }

    .header-status {
        align-self: flex-start;
    }

    .header-title {
        font-size: 24px;
    }

    .header-subtitle {
        font-size: 12px;
    }

    .page-intro h1 {
        font-size: 25px;
    }

    .content-card,
    .table-card {
        padding: 18px !important;
    }

}


/* =========================================================
   EXTRA SMALL DEVICES
========================================================= */

@media (max-width: 450px) {

    .header-left {
        align-items: flex-start;
    }

    .header-logo {
        width: 48px;
        height: 48px;

        font-size: 22px;
    }

    .header-title {
        font-size: 21px;
    }

    .page-intro h1 {
        font-size: 22px;
    }

    .stat-card {
        padding: 16px;

        min-height: 110px;
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