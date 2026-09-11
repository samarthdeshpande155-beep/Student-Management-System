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
    font-family: "Segoe UI", Arial, sans-serif !important;
    background: #f5f7fb !important;
}

.gradio-container {
    max-width: 1500px !important;
    margin: auto !important;
}


/* =========================================================
   MAIN HEADER
========================================================= */

.main-header {
    background: linear-gradient(
        135deg,
        #172554,
        #1d4ed8
    );

    color: white;

    padding: 25px 30px;

    border-radius: 18px;

    margin-bottom: 20px;

    box-shadow:
        0 8px 25px rgba(30, 64, 175, 0.18);
}

.main-header h1 {
    margin: 0;

    font-size: 30px !important;

    font-weight: 700 !important;

    color: white !important;
}

.main-header p {
    margin: 7px 0 0 0;

    color: #dbeafe !important;

    font-size: 14px !important;
}


/* =========================================================
   SIDEBAR
========================================================= */

.sidebar {
    background: white;

    border: 1px solid #e2e8f0;

    border-radius: 16px;

    padding: 20px;

    min-height: 500px;

    box-shadow:
        0 4px 16px rgba(15, 23, 42, 0.05);
}

.sidebar-title {
    font-size: 18px;

    font-weight: 700;

    color: #172554;

    margin-bottom: 5px;
}

.sidebar-subtitle {
    font-size: 12px;

    color: #64748b;

    margin-bottom: 20px;
}


/* =========================================================
   WELCOME
========================================================= */

.welcome-title {
    font-size: 28px;

    font-weight: 700;

    color: #172554;

    margin-bottom: 5px;
}

.welcome-text {
    color: #64748b;

    font-size: 14px;

    margin-bottom: 20px;
}


/* =========================================================
   STAT CARDS
========================================================= */

.stat-card {
    background: white;

    border: 1px solid #e2e8f0;

    border-radius: 15px;

    padding: 20px;

    min-height: 115px;

    box-shadow:
        0 4px 16px rgba(15, 23, 42, 0.05);
}

.stat-icon {
    font-size: 24px;

    margin-bottom: 8px;
}

.stat-label {
    color: #64748b;

    font-size: 12px;

    font-weight: 600;

    text-transform: uppercase;
}

.stat-value {
    color: #172554;

    font-size: 30px;

    font-weight: 700;

    margin-top: 4px;
}


/* =========================================================
   CONTENT CARD
========================================================= */

.content-card {
    background: white;

    border: 1px solid #e2e8f0;

    border-radius: 16px;

    padding: 22px;

    box-shadow:
        0 4px 16px rgba(15, 23, 42, 0.04);
}


/* =========================================================
   SECTION TITLE
========================================================= */

.section-title {
    font-size: 21px;

    font-weight: 700;

    color: #172554;

    margin-bottom: 4px;
}

.section-subtitle {
    font-size: 13px;

    color: #64748b;

    margin-bottom: 18px;
}


/* =========================================================
   INFO BOX
========================================================= */

.info-box {
    background: #eff6ff;

    border: 1px solid #bfdbfe;

    border-radius: 10px;

    padding: 13px 15px;

    color: #1e40af;

    font-size: 13px;
}


/* =========================================================
   WARNING BOX
========================================================= */

.warning-box {
    background: #fff7ed;

    border: 1px solid #fed7aa;

    border-radius: 10px;

    padding: 13px 15px;

    color: #9a3412;

    font-size: 13px;
}


/* =========================================================
   BUTTONS
========================================================= */

button {
    border-radius: 9px !important;

    font-weight: 600 !important;
}


/* =========================================================
   INPUTS
========================================================= */

input,
textarea {
    border-radius: 9px !important;
}


/* =========================================================
   FOOTER
========================================================= */

.footer {
    text-align: center;

    padding: 25px 10px;

    color: #64748b;

    font-size: 12px;
}


/* =========================================================
   MOBILE
========================================================= */

@media (max-width: 800px) {

    .main-header {
        padding: 20px;
    }

    .main-header h1 {
        font-size: 24px !important;
    }

    .welcome-title {
        font-size: 23px;
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

        response = requests.post(

            f"{API_URL}/students",

            params={
                "name": name.strip(),
                "course": course.strip(),
                "marks": int(marks)
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

        response = requests.put(

            f"{API_URL}/students/{int(student_id)}",

            params={
                "name": name.strip(),
                "course": course.strip(),
                "marks": int(marks)
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

        response = requests.delete(

            f"{API_URL}/students/{int(student_id)}",

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

    except Exception as e:

        return (
            f"❌ Backend connection error: {e}",
            *refresh_dashboard()
        )


# =========================================================
# INITIAL DATA
# =========================================================

initial_students = get_students()

initial_total, initial_average, initial_highest = calculate_stats(
    initial_students
)


# =========================================================
# GRADIO APPLICATION
# =========================================================

with gr.Blocks(
    title="Student Management System",
    css=CUSTOM_CSS,
    theme=gr.themes.Soft(
        primary_hue="blue",
        secondary_hue="slate",
        neutral_hue="slate"
    )
) as demo:


    # =====================================================
    # HEADER
    # =====================================================

    gr.HTML(
        """
        <div class="main-header">

            <h1>
                🎓 StudentHub
            </h1>

            <p>
                Student Management System
                • Academic Record Management
            </p>

        </div>
        """
    )


    # =====================================================
    # MAIN LAYOUT
    # =====================================================

    with gr.Row(equal_height=False):


        # =================================================
        # SIDEBAR
        # =================================================

        with gr.Column(
            scale=1,
            min_width=220
        ):

            gr.HTML(
                """
                <div class="sidebar">

                    <div class="sidebar-title">
                        StudentHub
                    </div>

                    <div class="sidebar-subtitle">
                        Management Panel
                    </div>

                </div>
                """
            )

            dashboard_button = gr.Button(
                "🏠  Dashboard",
                variant="primary"
            )

            add_nav_button = gr.Button(
                "➕  Add Student"
            )

            update_nav_button = gr.Button(
                "✏️  Update Student"
            )

            delete_nav_button = gr.Button(
                "🗑️  Delete Student"
            )

            refresh_nav_button = gr.Button(
                "🔄  Refresh Data"
            )


        # =================================================
        # MAIN CONTENT
        # =================================================

        with gr.Column(
            scale=5
        ):


            # =============================================
            # WELCOME
            # =============================================

            gr.HTML(
                """
                <div class="welcome-title">
                    Welcome to StudentHub 👋
                </div>

                <div class="welcome-text">
                    Manage student information,
                    academic records and marks from one place.
                </div>
                """
            )


            # =============================================
            # STATISTICS
            # =============================================

            with gr.Row():

                total_students = gr.HTML(
                    total_card(initial_total)
                )

                average_marks = gr.HTML(
                    average_card(initial_average)
                )

                highest_marks = gr.HTML(
                    highest_card(initial_highest)
                )


            gr.Markdown("")


            # =============================================
            # DASHBOARD TABLE
            # =============================================

            with gr.Group(
                elem_classes="content-card"
            ):

                gr.HTML(
                    """
                    <div class="section-title">
                        Student Records
                    </div>

                    <div class="section-subtitle">
                        View all students currently stored
                        in the database.
                    </div>
                    """
                )

                refresh_button = gr.Button(
                    "🔄 Refresh Student Records",
                    variant="primary"
                )

                students_table = gr.Dataframe(

                    value=format_students(
                        initial_students
                    ),

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


            gr.Markdown("")


            # =============================================
            # ADD STUDENT
            # =============================================

            with gr.Group(
                elem_classes="content-card"
            ):

                gr.HTML(
                    """
                    <div class="section-title">
                        ➕ Add New Student
                    </div>

                    <div class="section-subtitle">
                        Register a new student in the database.
                    </div>

                    <div class="info-box">
                        💡 Student ID will be generated
                        automatically by Supabase.
                    </div>
                    """
                )

                gr.Markdown("")


                with gr.Row():

                    add_name = gr.Textbox(
                        label="Student Name",
                        placeholder="Enter full name"
                    )

                    add_course = gr.Textbox(
                        label="Course",
                        placeholder="Enter course"
                    )


                add_marks = gr.Number(
                    label="Marks",
                    minimum=0,
                    maximum=100,
                    precision=0
                )


                add_button = gr.Button(
                    "➕ Register Student",
                    variant="primary"
                )


                add_status = gr.Textbox(
                    label="System Message",
                    interactive=False
                )


            gr.Markdown("")


            # =============================================
            # UPDATE STUDENT
            # =============================================

            with gr.Group(
                elem_classes="content-card"
            ):

                gr.HTML(
                    """
                    <div class="section-title">
                        ✏️ Update Student
                    </div>

                    <div class="section-subtitle">
                        Modify an existing student record.
                    </div>

                    <div class="info-box">
                        🔎 Enter the Student ID and
                        updated information.
                    </div>
                    """
                )

                gr.Markdown("")


                update_id = gr.Number(
                    label="Student ID",
                    minimum=1,
                    precision=0
                )


                with gr.Row():

                    update_name = gr.Textbox(
                        label="Student Name",
                        placeholder="Updated name"
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
                    variant="primary"
                )


                update_status = gr.Textbox(
                    label="System Message",
                    interactive=False
                )


            gr.Markdown("")


            # =============================================
            # DELETE STUDENT
            # =============================================

            with gr.Group(
                elem_classes="content-card"
            ):

                gr.HTML(
                    """
                    <div class="section-title">
                        🗑️ Delete Student
                    </div>

                    <div class="section-subtitle">
                        Permanently remove a student record.
                    </div>

                    <div class="warning-box">
                        ⚠️ This action permanently deletes
                        the selected record from the database.
                    </div>
                    """
                )

                gr.Markdown("")


                delete_id = gr.Number(
                    label="Student ID",
                    minimum=1,
                    precision=0
                )


                delete_button = gr.Button(
                    "🗑️ Delete Student",
                    variant="stop"
                )


                delete_status = gr.Textbox(
                    label="System Message",
                    interactive=False
                )


    # =====================================================
    # FOOTER
    # =====================================================

    gr.HTML(
        """
        <div class="footer">

            <hr>

            <b>🎓 StudentHub</b>

            <br>

            Student Management System

            <br><br>

            Gradio • FastAPI • Supabase PostgreSQL

        </div>
        """
    )


    # =====================================================
    # REFRESH EVENTS
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


    refresh_nav_button.click(

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
# DO NOT ADD demo.launch()
#
# Backend/main.py imports this demo object and mounts
# the Gradio application using FastAPI.
#
# Run the complete application from the project root:
#
# uvicorn Backend.main:app --reload
#
# =========================================================