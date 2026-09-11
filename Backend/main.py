from fastapi import FastAPI
from supabase import create_client
from dotenv import load_dotenv
import os

# Load variables from .env
load_dotenv()

# Create FastAPI application
app = FastAPI()


# Get Supabase credentials
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")


# Connect Python to Supabase
supabase = create_client(
    SUPABASE_URL,
    SUPABASE_KEY
)


# =========================================================
# 1. VIEW ALL STUDENTS
# =========================================================

@app.get("/students")
def view_students():

    response = (
        supabase
        .table("Students")
        .select("*")
        .execute()
    )

    return {
        "message": "Students fetched successfully",
        "data": response.data
    }



# =========================================================
# 2. ADD STUDENT
# =========================================================

@app.post("/students")
def add_student(name: str, course: str, marks: int):

    student = {
        "name": name,
        "course": course,
        "marks": marks
    }

    response = (
        supabase
        .table("Students")
        .insert(student)
        .execute()
    )

    return {
        "message": "Student added successfully",
        "data": response.data
    }


# =========================================================
# 3. UPDATE STUDENT
# =========================================================

@app.put("/students/{student_id}")
def update_student(
    student_id: int,
    name: str,
    course: str,
    marks: int
):

    student = {
        "name": name,
        "course": course,
        "marks": marks
    }

    response = (
        supabase
        .table("Students")
        .update(student)
        .eq("id", student_id)
        .execute()
    )

    return {
        "message": "Student updated successfully",
        "data": response.data
    }


# =========================================================
# 4. DELETE STUDENT
# =========================================================

@app.delete("/students/{student_id}")
def delete_student(student_id: int):

    response = (
        supabase
        .table("Students")
        .delete()
        .eq("id", student_id)
        .execute()
    )

    return {
        "message": "Student deleted successfully",
        "data": response.data
    }