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
   STUDENTHUB
   MODERN PROFESSIONAL STUDENT MANAGEMENT DASHBOARD

   Main Colors
   Navy       : #0f172a
   Deep Navy  : #172554
   Indigo     : #4f46e5
   Blue       : #2563eb
   Slate      : #64748b
   Background : #f8fafc
========================================================= */


/* =========================================================
   GLOBAL PAGE
========================================================= */

html {
    background: #f8fafc !important;
}

body {
    background: #f8fafc !important;

    font-family:
        "Inter",
        "Segoe UI",
        Arial,
        sans-serif !important;

    color: #0f172a !important;
}


/* Main centered dashboard */

.gradio-container,
[class*="gradio-container"] {

    width: 100% !important;

    max-width: 1400px !important;

    margin-left: auto !important;
    margin-right: auto !important;

    padding:
        0 35px 45px 35px !important;

    background: #f8fafc !important;

    box-sizing: border-box !important;
}


/* =========================================================
   TOP HEADER
========================================================= */

.top-header {

    position: relative;

    width: 100%;

    background:
        linear-gradient(
            135deg,
            #0f172a 0%,
            #172554 48%,
            #312e81 100%
        );

    color: white;

    padding: 28px 32px;

    margin: 0 0 32px 0;

    border-radius:
        0 0 24px 24px;

    box-shadow:
        0 14px 32px
        rgba(15, 23, 42, 0.14);

    overflow: hidden;

    box-sizing: border-box;
}


/* Header decorative glow */

.top-header::before {

    content: "";

    position: absolute;

    width: 280px;
    height: 280px;

    right: -100px;
    top: -150px;

    background:
        rgba(99, 102, 241, 0.16);

    border-radius: 50%;

    pointer-events: none;
}


.top-header::after {

    content: "";

    position: absolute;

    width: 120px;
    height: 120px;

    left: -55px;
    bottom: -75px;

    background:
        rgba(37, 99, 235, 0.10);

    border-radius: 50%;

    pointer-events: none;
}


/* Header content */

.header-content {

    position: relative;

    z-index: 2;

    display: flex;

    align-items: center;

    justify-content: space-between;

    gap: 25px;
}


/* Header left section */

.header-left {

    display: flex;

    align-items: center;

    gap: 15px;
}


/* Logo */

.header-logo {

    width: 58px;
    height: 58px;

    min-width: 58px;

    display: flex;

    align-items: center;

    justify-content: center;

    background:
        rgba(255, 255, 255, 0.11);

    border:
        1px solid
        rgba(255, 255, 255, 0.17);

    border-radius: 15px;

    font-size: 26px;

    box-shadow:
        inset 0 1px 0
        rgba(255,255,255,0.12),

        0 5px 15px
        rgba(0,0,0,0.12);
}


/* Application title */

.header-title {

    color: #ffffff !important;

    font-size: 27px;

    font-weight: 800;

    letter-spacing: -0.6px;

    line-height: 1.15;

    margin: 0;
}


/* Header subtitle */

.header-subtitle {

    color: #cbd5e1;

    font-size: 12px;

    margin-top: 6px;

    letter-spacing: 0.15px;
}


/* Online status */

.header-status {

    display: inline-flex;

    align-items: center;

    gap: 7px;

    background:
        rgba(255, 255, 255, 0.09);

    border:
        1px solid
        rgba(255, 255, 255, 0.17);

    color: #dbeafe;

    padding: 9px 14px;

    border-radius: 999px;

    font-size: 12px;

    font-weight: 650;

    white-space: nowrap;

    backdrop-filter: blur(10px);

    box-shadow:
        0 4px 12px
        rgba(0,0,0,0.08);
}


/* =========================================================
   PAGE INTRODUCTION
========================================================= */

.page-intro {

    margin:
        0 0 25px 0;

    padding:
        0 3px;
}


.page-intro h1 {

    color: #0f172a;

    font-size: 29px;

    font-weight: 800;

    letter-spacing: -0.7px;

    line-height: 1.2;

    margin:
        0 0 7px 0;
}


.page-intro p {

    color: #64748b;

    font-size: 13px;

    line-height: 1.6;

    margin: 0;
}


/* =========================================================
   STATISTICS SECTION
========================================================= */


/* Space between statistic cards */

.gradio-container .row {

    gap: 20px !important;
}


/* Statistic card */

.stat-card {

    position: relative;

    min-height: 135px;

    background:
        #ffffff;

    border:
        1px solid #e2e8f0;

    border-radius:
        17px;

    padding:
        20px;

    box-sizing:
        border-box;

    overflow:
        hidden;

    box-shadow:
        0 5px 18px
        rgba(15, 23, 42, 0.045);

    transition:
        transform 0.22s ease,
        box-shadow 0.22s ease,
        border-color 0.22s ease;
}


/* Decorative circle */

.stat-card::after {

    content: "";

    position: absolute;

    width: 110px;
    height: 110px;

    right: -48px;
    top: -48px;

    background:
        #eef2ff;

    border-radius: 50%;

    pointer-events: none;
}


/* Additional subtle circle */

.stat-card::before {

    content: "";

    position: absolute;

    width: 48px;
    height: 48px;

    right: 17px;
    bottom: -25px;

    background:
        rgba(99, 102, 241, 0.045);

    border-radius: 50%;

    pointer-events: none;
}


/* Card hover */

.stat-card:hover {

    transform:
        translateY(-4px);

    border-color:
        #c7d2fe;

    box-shadow:
        0 13px 28px
        rgba(15, 23, 42, 0.09);
}


/* Statistic icon */

.stat-icon {

    position: relative;

    z-index: 2;

    width: 40px;
    height: 40px;

    display: flex;

    align-items: center;

    justify-content: center;

    background:
        #eef2ff;

    border:
        1px solid #e0e7ff;

    border-radius:
        11px;

    font-size:
        19px;

    margin-bottom:
        12px;
}


/* Statistic label */

.stat-label {

    position: relative;

    z-index: 2;

    color:
        #64748b;

    font-size:
        10px;

    font-weight:
        750;

    text-transform:
        uppercase;

    letter-spacing:
        0.9px;

    line-height:
        1.3;
}


/* Statistic number */

.stat-value {

    position: relative;

    z-index: 2;

    color:
        #0f172a;

    font-size:
        30px;

    font-weight:
        850;

    letter-spacing:
        -0.8px;

    line-height:
        1.1;

    margin-top:
        4px;
}


/* =========================================================
   NAVIGATION TABS
========================================================= */

.tabs-container {

    margin-top:
        30px !important;

    margin-bottom:
        0 !important;
}


/* Tab navigation background */

.tabs-container > div:first-child {

    background:
        #ffffff !important;

    border:
        1px solid #e2e8f0 !important;

    border-radius:
        12px !important;

    padding:
        5px !important;

    box-shadow:
        0 4px 14px
        rgba(15, 23, 42, 0.035);
}


/* Individual tab */

button[role="tab"] {

    color:
        #64748b !important;

    background:
        transparent !important;

    font-size:
        13px !important;

    font-weight:
        650 !important;

    border:
        none !important;

    border-radius:
        8px !important;

    padding:
        10px 15px !important;

    margin:
        0 2px !important;

    transition:
        background 0.18s ease,
        color 0.18s ease,
        transform 0.18s ease !important;
}


/* Tab hover */

button[role="tab"]:hover {

    color:
        #334155 !important;

    background:
        #f1f5f9 !important;

    transform:
        translateY(-1px);
}


/* Active tab */

button[role="tab"][aria-selected="true"] {

    color:
        #4338ca !important;

    background:
        #eef2ff !important;

    border:
        none !important;

    box-shadow:
        0 2px 6px
        rgba(79, 70, 229, 0.08);
}


/* =========================================================
   CONTENT CARDS
========================================================= */

.content-card,
.table-card {

    background:
        #ffffff !important;

    border:
        1px solid #e2e8f0 !important;

    border-radius:
        17px !important;

    padding:
        26px !important;

    margin-top:
        18px !important;

    box-shadow:
        0 5px 18px
        rgba(15, 23, 42, 0.045) !important;
}


/* =========================================================
   SECTION HEADINGS
========================================================= */

.section-heading {

    color:
        #0f172a;

    font-size:
        20px;

    font-weight:
        800;

    letter-spacing:
        -0.35px;

    line-height:
        1.25;

    margin-bottom:
        5px;
}


.section-description {

    color:
        #64748b;

    font-size:
        13px;

    line-height:
        1.6;

    margin-bottom:
        19px;
}


/* =========================================================
   BUTTONS
========================================================= */

button {

    border-radius:
        9px !important;

    font-weight:
        650 !important;

    transition:
        transform 0.16s ease,
        box-shadow 0.16s ease,
        background 0.16s ease,
        border-color 0.16s ease !important;
}


/* Button hover */

button:hover {

    transform:
        translateY(-1px);
}


/* =========================================================
   PRIMARY BUTTON
========================================================= */

.primary-btn button {

    background:
        linear-gradient(
            135deg,
            #4f46e5,
            #2563eb
        ) !important;

    color:
        #ffffff !important;

    border:
        none !important;

    box-shadow:
        0 5px 13px
        rgba(79, 70, 229, 0.20) !important;
}


.primary-btn button:hover {

    background:
        linear-gradient(
            135deg,
            #4338ca,
            #1d4ed8
        ) !important;

    box-shadow:
        0 8px 19px
        rgba(79, 70, 229, 0.27) !important;
}


/* =========================================================
   DELETE BUTTON
========================================================= */

.delete-btn button {

    background:
        #dc2626 !important;

    color:
        #ffffff !important;

    border:
        none !important;

    box-shadow:
        0 5px 12px
        rgba(220, 38, 38, 0.15) !important;
}


.delete-btn button:hover {

    background:
        #b91c1c !important;

    box-shadow:
        0 8px 17px
        rgba(220, 38, 38, 0.22) !important;
}


/* =========================================================
   SECONDARY BUTTON
========================================================= */

.secondary-btn button {

    background:
        #ffffff !important;

    color:
        #334155 !important;

    border:
        1px solid #cbd5e1 !important;
}


.secondary-btn button:hover {

    background:
        #f8fafc !important;

    border-color:
        #94a3b8 !important;
}


/* =========================================================
   INPUT FIELDS
========================================================= */

input,
textarea,
.gr-input {

    background:
        #ffffff !important;

    border:
        1px solid #cbd5e1 !important;

    border-radius:
        9px !important;

    color:
        #0f172a !important;

    font-size:
        13px !important;

    transition:
        border-color 0.2s ease,
        box-shadow 0.2s ease !important;
}


/* Input hover */

input:hover,
textarea:hover {

    border-color:
        #94a3b8 !important;
}


/* Input focus */

input:focus,
textarea:focus {

    border-color:
        #6366f1 !important;

    box-shadow:
        0 0 0 3px
        rgba(99, 102, 241, 0.11) !important;

    outline:
        none !important;
}


/* Input labels */

label span {

    color:
        #334155 !important;

    font-weight:
        650 !important;

    font-size:
        12px !important;
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

    border:
        1px solid #c7d2fe;

    color:
        #3730a3;

    padding:
        14px 16px;

    border-radius:
        10px;

    font-size:
        12px;

    line-height:
        1.55;

    margin:
        15px 0;
}


/* =========================================================
   WARNING BOX
========================================================= */

.warning-box {

    background:
        #fff7ed;

    border:
        1px solid #fed7aa;

    color:
        #9a3412;

    padding:
        14px 16px;

    border-radius:
        10px;

    font-size:
        12px;

    line-height:
        1.55;

    margin:
        15px 0;
}


/* =========================================================
   DATA TABLE
========================================================= */

.table-card .dataframe {

    width:
        100% !important;

    border:
        1px solid #e2e8f0 !important;

    border-radius:
        11px !important;

    overflow:
        hidden !important;

    box-shadow:
        0 2px 7px
        rgba(15, 23, 42, 0.025);
}


/* Table header */

.table-card th {

    background:
        #f8fafc !important;

    color:
        #334155 !important;

    font-size:
        12px !important;

    font-weight:
        750 !important;

    border-bottom:
        1px solid #e2e8f0 !important;

    padding:
        13px 11px !important;
}


/* Table cells */

.table-card td {

    color:
        #475569 !important;

    font-size:
        12px !important;

    border-color:
        #eef2f7 !important;

    padding:
        12px 11px !important;
}


/* Table row hover */

.table-card tr:hover td {

    background:
        #f8fafc !important;
}


/* =========================================================
   STATUS MESSAGE
========================================================= */

.status-message textarea {

    background:
        #f8fafc !important;

    border:
        1px solid #e2e8f0 !important;

    color:
        #334155 !important;

    font-weight:
        600 !important;

    font-size:
        12px !important;
}


/* =========================================================
   FOOTER
========================================================= */

.app-footer {

    text-align:
        center;

    color:
        #94a3b8;

    font-size:
        11px;

    line-height:
        1.7;

    padding:
        35px 0 8px 0;
}


.app-footer b {

    color:
        #64748b;

    font-weight:
        700;
}


.app-footer hr {

    border:
        none;

    border-top:
        1px solid #e2e8f0;

    margin:
        0 0 18px 0;
}


/* =========================================================
   GRADIO CLEANUP
========================================================= */

.gradio-container .form {

    border-color:
        #e2e8f0 !important;
}


/* Remove excessive default block shadows */

.gradio-container .block {

    box-shadow:
        none;
}


/* =========================================================
   LARGE TABLET
========================================================= */

@media (max-width: 1100px) {

    .gradio-container,
    [class*="gradio-container"] {

        max-width:
            100% !important;

        padding:
            0 25px 40px 25px !important;
    }


    .top-header {

        padding:
            26px 28px;
    }

}


/* =========================================================
   TABLET / MOBILE
========================================================= */

@media (max-width: 700px) {

    .gradio-container,
    [class*="gradio-container"] {

        width:
            100% !important;

        max-width:
            100% !important;

        padding:
            0 15px 30px 15px !important;
    }


    /* Mobile header */

    .top-header {

        width:
            100%;

        margin:
            0 0 25px 0;

        padding:
            23px 20px;

        border-radius:
            0 0 18px 18px;
    }


    .header-content {

        flex-direction:
            column;

        align-items:
            flex-start;

        gap:
            15px;
    }


    .header-left {

        align-items:
            center;
    }


    .header-status {

        align-self:
            flex-start;
    }


    .header-title {

        font-size:
            23px;
    }


    .header-subtitle {

        font-size:
            11px;
    }


    /* Page title */

    .page-intro {

        margin-bottom:
            20px;
    }


    .page-intro h1 {

        font-size:
            25px;
    }


    .page-intro p {

        font-size:
            12px;
    }


    /* Cards */

    .content-card,
    .table-card {

        padding:
            18px !important;
    }


    /* Tabs */

    button[role="tab"] {

        font-size:
            12px !important;

        padding:
            9px 10px !important;
    }


    /* Statistics */

    .stat-card {

        min-height:
            120px;
    }

}


/* =========================================================
   EXTRA SMALL DEVICES
========================================================= */

@media (max-width: 450px) {

    .gradio-container,
    [class*="gradio-container"] {

        padding:
            0 12px 25px 12px !important;
    }


    .top-header {

        padding:
            21px 17px;
    }


    .header-left {

        align-items:
            flex-start;
    }


    .header-logo {

        width:
            48px;

        height:
            48px;

        min-width:
            48px;

        font-size:
            21px;
    }


    .header-title {

        font-size:
            20px;
    }


    .header-subtitle {

        font-size:
            10px;
    }


    .page-intro h1 {

        font-size:
            22px;
    }


    .stat-card {

        min-height:
            108px;

        padding:
            16px;
    }


    .stat-value {

        font-size:
            25px;
    }


    .stat-label {

        font-size:
            9px;
    }


    .content-card,
    .table-card {

        padding:
            15px !important;
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