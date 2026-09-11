import gradio as gr
import requests


# =========================================================
# CONFIGURATION
# =========================================================

API_URL = "http://127.0.0.1:8000"


# =========================================================
# CUSTOM CSS
# =========================================================

CUSTOM_CSS = """

/* ========================================================
   GLOBAL
======================================================== */

* {
    box-sizing: border-box;
}

body {
    font-family: "Inter", "Segoe UI", Arial, sans-serif !important;
    background: #f4f7fb !important;
}

.gradio-container {
    max-width: 1450px !important;
    margin: auto !important;
    padding: 0 !important;
}


/* ========================================================
   TOP HEADER
======================================================== */

.top-header {
    background: linear-gradient(
        135deg,
        #0b1f3a 0%,
        #123c73 55%,
        #2563a6 100%
    );

    padding: 30px 38px;
    border-radius: 0 0 24px 24px;

    color: white;

    box-shadow:
        0 10px 30px rgba(15, 43, 91, 0.20);
}

.top-header h1 {
    margin: 0;
    font-size: 34px !important;
    font-weight: 750 !important;
    color: white !important;
}

.top-header p {
    margin-top: 8px;
    margin-bottom: 0;

    color: #dbeafe !important;
    font-size: 15px !important;
}


/* ========================================================
   STATUS BADGE
======================================================== */

.system-status {
    display: inline-flex;

    align-items: center;
    gap: 8px;

    margin-top: 18px;

    padding: 7px 13px;

    border-radius: 30px;

    background: rgba(255,255,255,0.12);

    color: #e0f2fe;

    font-size: 13px;
}


/* ========================================================
   DASHBOARD CARDS
======================================================== */

.stat-card {
    background: white;

    border: 1px solid #e6ebf2;

    border-radius: 18px;

    padding: 23px;

    min-height: 135px;

    box-shadow:
        0 5px 20px rgba(15, 23, 42, 0.06);

    transition: 0.2s ease;
}

.stat-card:hover {
    transform: translateY(-2px);

    box-shadow:
        0 10px 28px rgba(15, 23, 42, 0.09);
}

.stat-icon {
    font-size: 24px;
    margin-bottom: 10px;
}

.stat-title {
    color: #64748b;

    font-size: 13px;

    font-weight: 650;

    letter-spacing: 0.3px;
}

.stat-number {
    color: #0f2b5b;

    font-size: 32px;

    font-weight: 750;

    margin-top: 5px;
}


/* ========================================================
   PAGE HEADINGS
======================================================== */

.page-title {
    color: #0f2b5b;

    font-size: 25px;

    font-weight: 750;

    margin-bottom: 3px;
}

.page-subtitle {
    color: #64748b;

    font-size: 14px;

    margin-bottom: 22px;
}


/* ========================================================
   CONTENT CARDS
======================================================== */

.content-card {
    background: white;

    border: 1px solid #e5eaf1;

    border-radius: 18px;

    padding: 25px;

    box-shadow:
        0 5px 18px rgba(15, 23, 42, 0.045);
}


/* ========================================================
   FORM LABELS
======================================================== */

label {
    font-weight: 600 !important;
}


/* ========================================================
   INPUTS
======================================================== */

input,
textarea {

    border-radius: 10px !important;

}


/* ========================================================
   BUTTONS
======================================================== */

button {

    border-radius: 10px !important;

    font-weight: 650 !important;

}

.primary-action {

    min-height: 45px !important;

}


/* ========================================================
   TABLE
======================================================== */

table {

    border-radius: 12px !important;

}


/* ========================================================
   INFO BOX
======================================================== */

.info-box {

    background: #eff6ff;

    border: 1px solid #bfdbfe;

    border-radius: 12px;

    padding: 14px 17px;

    color: #1e40af;

    font-size: 13px;

}


/* ========================================================
   DANGER BOX
======================================================== */

.danger-box {

    background: #fff1f2;

    border: 1px solid #fecdd3;

    border-radius: 12px;

    padding: 14px 17px;

    color: #9f1239;

    font-size: 13px;

}


/* ========================================================
   SUCCESS STATUS
======================================================== */

.status-success {

    background: #ecfdf5;

    border: 1px solid #a7f3d0;

    color: #047857;

}


/* ========================================================
   FOOTER
======================================================== */

.footer {

    text-align: center;

    padding: 30px 20px;

    color: #64748b;

    font-size: 13px;

}


/* ========================================================
   MOBILE
======================================================== */

@media (max-width: 800px) {

    .top-header {

        padding: 25px;

    }

    .top-header h1 {

        font-size: 27px !important;

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
# FORMAT TABLE
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
# REFRESH EVERYTHING
# =========================================================

def refresh_all():

    students = get_students()

    total, average, highest = calculate_stats(
        students
    )

    return (

        format_students(students),

        f"""
        <div class="stat-card">

            <div class="stat-icon">👨‍🎓</div>

            <div class="stat-title">
                TOTAL STUDENTS
            </div>

            <div class="stat-number">
                {total}
            </div>

        </div>
        """,

        f"""
        <div class="stat-card">

            <div class="stat-icon">📊</div>

            <div class="stat-title">
                AVERAGE MARKS
            </div>

            <div class="stat-number">
                {average}
            </div>

        </div>
        """,

        f"""
        <div class="stat-card">

            <div class="stat-icon">🏆</div>

            <div class="stat-title">
                HIGHEST MARKS
            </div>

            <div class="stat-number">
                {highest}
            </div>

        </div>
        """
    )


# =========================================================
# ADD STUDENT
# =========================================================

def add_student(name, course, marks):

    if not name or not name.strip():

        students = get_students()

        return (
            "⚠️ Please enter student name.",
            *refresh_all()
        )

    if not course or not course.strip():

        return (
            "⚠️ Please enter course.",
            *refresh_all()
        )

    if marks is None:

        return (
            "⚠️ Please enter marks.",
            *refresh_all()
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
                *refresh_all()
            )

        return (
            f"❌ Failed to add student: {response.text}",
            *refresh_all()
        )

    except Exception as e:

        return (
            f"❌ Backend connection error: {e}",
            *refresh_all()
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
            *refresh_all()
        )

    if not name or not name.strip():

        return (
            "⚠️ Please enter student name.",
            *refresh_all()
        )

    if not course or not course.strip():

        return (
            "⚠️ Please enter course.",
            *refresh_all()
        )

    if marks is None:

        return (
            "⚠️ Please enter marks.",
            *refresh_all()
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
                *refresh_all()
            )

        return (
            f"❌ Failed to update student: {response.text}",
            *refresh_all()
        )

    except Exception as e:

        return (
            f"❌ Backend connection error: {e}",
            *refresh_all()
        )


# =========================================================
# DELETE STUDENT
# =========================================================

def delete_student(student_id):

    if student_id is None:

        return (
            "⚠️ Please enter Student ID.",
            *refresh_all()
        )

    try:

        response = requests.delete(

            f"{API_URL}/students/{int(student_id)}",

            timeout=10

        )

        if response.status_code == 200:

            return (
                "✅ Student deleted successfully!",
                *refresh_all()
            )

        return (
            f"❌ Failed to delete student: {response.text}",
            *refresh_all()
        )

    except Exception as e:

        return (
            f"❌ Backend connection error: {e}",
            *refresh_all()
        )


# =========================================================
# INITIAL DASHBOARD VALUES
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

) as app:


    # =====================================================
    # HEADER
    # =====================================================

    gr.HTML(

        """
        <div class="top-header">

            <h1>
                🎓 Student Management System
            </h1>

            <p>
                Centralized student record and academic
                information management dashboard
            </p>

            <div class="system-status">
                ● System Connected
            </div>

        </div>
        """

    )


    # =====================================================
    # DASHBOARD
    # =====================================================

    gr.Markdown("")


    with gr.Row():

        total_students = gr.HTML(

            f"""
            <div class="stat-card">

                <div class="stat-icon">
                    👨‍🎓
                </div>

                <div class="stat-title">
                    TOTAL STUDENTS
                </div>

                <div class="stat-number">
                    {initial_total}
                </div>

            </div>
            """

        )


        average_marks = gr.HTML(

            f"""
            <div class="stat-card">

                <div class="stat-icon">
                    📊
                </div>

                <div class="stat-title">
                    AVERAGE MARKS
                </div>

                <div class="stat-number">
                    {initial_average}
                </div>

            </div>
            """

        )


        highest_marks = gr.HTML(

            f"""
            <div class="stat-card">

                <div class="stat-icon">
                    🏆
                </div>

                <div class="stat-title">
                    HIGHEST MARKS
                </div>

                <div class="stat-number">
                    {initial_highest}
                </div>

            </div>
            """

        )


    gr.Markdown("")


    # =====================================================
    # NAVIGATION
    # =====================================================

    with gr.Tabs():


        # =================================================
        # DASHBOARD / STUDENTS
        # =================================================

        with gr.Tab("🏠 Dashboard"):


            gr.HTML(

                """
                <div class="page-title">
                    Student Records
                </div>

                <div class="page-subtitle">
                    Monitor and manage all registered students.
                </div>
                """

            )


            with gr.Group(elem_classes="content-card"):

                with gr.Row():

                    refresh_button = gr.Button(

                        "🔄 Refresh Records",

                        variant="primary",

                        elem_classes="primary-action"

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

                    label="Student Database",

                    interactive=False

                )


        # =================================================
        # ADD STUDENT
        # =================================================

        with gr.Tab("➕ Add Student"):


            gr.HTML(

                """
                <div class="page-title">
                    Register New Student
                </div>

                <div class="page-subtitle">
                    Add a new student record to the database.
                </div>
                """

            )


            with gr.Group(elem_classes="content-card"):


                gr.HTML(

                    """
                    <div class="info-box">

                        💡 Student ID is generated
                        automatically by the database.

                    </div>
                    """

                )


                gr.Markdown("")


                with gr.Row():

                    with gr.Column():

                        add_name = gr.Textbox(

                            label="👤 Student Name",

                            placeholder="Enter full name"

                        )


                    with gr.Column():

                        add_course = gr.Textbox(

                            label="📚 Course",

                            placeholder="e.g. Computer Science"

                        )


                add_marks = gr.Number(

                    label="📊 Marks",

                    minimum=0,

                    maximum=100,

                    precision=0

                )


                gr.Markdown("")


                add_button = gr.Button(

                    "➕ Register Student",

                    variant="primary",

                    elem_classes="primary-action"

                )


                add_status = gr.Textbox(

                    label="System Message",

                    interactive=False

                )


        # =================================================
        # UPDATE STUDENT
        # =================================================

        with gr.Tab("✏️ Update Student"):


            gr.HTML(

                """
                <div class="page-title">
                    Update Student Record
                </div>

                <div class="page-subtitle">
                    Modify the academic or personal information
                    of an existing student.
                </div>
                """

            )


            with gr.Group(elem_classes="content-card"):


                gr.HTML(

                    """
                    <div class="info-box">

                        🔎 Enter the Student ID of the
                        record you want to modify.

                    </div>
                    """

                )


                gr.Markdown("")


                update_id = gr.Number(

                    label="🆔 Student ID",

                    minimum=1,

                    precision=0

                )


                with gr.Row():

                    with gr.Column():

                        update_name = gr.Textbox(

                            label="👤 Student Name",

                            placeholder="Enter updated name"

                        )


                    with gr.Column():

                        update_course = gr.Textbox(

                            label="📚 Course",

                            placeholder="Enter updated course"

                        )


                update_marks = gr.Number(

                    label="📊 Marks",

                    minimum=0,

                    maximum=100,

                    precision=0

                )


                gr.Markdown("")


                update_button = gr.Button(

                    "✏️ Update Record",

                    variant="primary",

                    elem_classes="primary-action"

                )


                update_status = gr.Textbox(

                    label="System Message",

                    interactive=False

                )


                gr.Markdown("### Current Records")


                update_table = gr.Dataframe(

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

                    interactive=False

                )


        # =================================================
        # DELETE STUDENT
        # =================================================

        with gr.Tab("🗑️ Delete Student"):


            gr.HTML(

                """
                <div class="page-title">
                    Remove Student Record
                </div>

                <div class="page-subtitle">
                    Delete an existing student record
                    from the database.
                </div>
                """

            )


            with gr.Group(elem_classes="content-card"):


                gr.HTML(

                    """
                    <div class="danger-box">

                        ⚠️ Deleting a student record
                        permanently removes it from the database.

                    </div>
                    """

                )


                gr.Markdown("")


                delete_id = gr.Number(

                    label="🆔 Student ID",

                    minimum=1,

                    precision=0

                )


                gr.Markdown("")


                delete_button = gr.Button(

                    "🗑️ Delete Student",

                    variant="stop",

                    elem_classes="primary-action"

                )


                delete_status = gr.Textbox(

                    label="System Message",

                    interactive=False

                )


                gr.Markdown("### Remaining Records")


                delete_table = gr.Dataframe(

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

                    interactive=False

                )


    # =====================================================
    # FOOTER
    # =====================================================

    gr.HTML(

        """
        <div class="footer">

            <hr>

            <b>🎓 Student Management System</b>

            <br><br>

            Gradio Frontend
            &nbsp; • &nbsp;
            FastAPI Backend
            &nbsp; • &nbsp;
            Supabase PostgreSQL

            <br>

            <span>
                Student Record Management Platform
            </span>

        </div>
        """

    )


    # =====================================================
    # REFRESH BUTTON
    # =====================================================

    refresh_button.click(

        fn=refresh_all,

        inputs=[],

        outputs=[

            students_table,

            total_students,

            average_marks,

            highest_marks

        ]

    )


    # =====================================================
    # ADD BUTTON
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
    # UPDATE BUTTON
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

            update_table,

            total_students,

            average_marks,

            highest_marks

        ]

    )


    # =====================================================
    # DELETE BUTTON
    # =====================================================

    delete_button.click(

        fn=delete_student,

        inputs=[

            delete_id

        ],

        outputs=[

            delete_status,

            delete_table,

            total_students,

            average_marks,

            highest_marks

        ]

    )


# =========================================================
# LAUNCH
# =========================================================

app.launch()