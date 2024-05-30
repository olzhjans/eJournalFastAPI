from fastapi import FastAPI, HTTPException
from models import Student, Score, session

app = FastAPI()


@app.post("/students")
async def add_student(first_name: str, last_name: str, group_name: str):
    student = Student(first_name=first_name, last_name=last_name, group_name=group_name)
    session.add(student)
    session.commit()
    return {"student added": {"first_name": student.first_name, "last_name": student.last_name,
                              "group_name": student.group_name}}


@app.get("/students/{student_id}")
async def get_student(student_id: int):
    student = session.query(Student).filter(Student.id == student_id).all()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

"""
@app.get("/all_students")
async def get_all_students():
    students_query = session.query(Student)
    return students_query.all()
"""


@app.patch("/students/{student_id}")
async def update_student(
    student_id: int,
    new_firstname: str = "",
    new_lastname: str = "",
    new_groupname: str = "",
):
    student_query = session.query(Student).filter(Student.id == student_id)
    student = student_query.first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    if new_firstname:
        student.first_name = new_firstname
    if new_lastname:
        student.last_name = new_lastname
    if new_groupname:
        student.group_name = new_groupname
    session.add(student)
    session.commit()
    return {"student updated": {"id": student_id, "first_name": student.first_name, "last_name": student.last_name,
                                "group_name": student.group_name}}


@app.delete("/students/{student_id}")
async def delete_student(student_id: int):
    student = session.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    session.delete(student)
    session.commit()
    return {"student deleted": {"student_id": student.id, "first_name": student.first_name,
                                "last_name": student.last_name, "group_name": student.group_name}}


@app.post("/score")
async def add_score(student_id: int, subject: str, score: int):
    student = session.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    new_score = Score(student_id=student_id, subject=subject, score=score)
    session.add(new_score)
    session.commit()
    return {"score added": {"student_id": student_id, "subject": subject, "score": score}}


@app.get("/score/{score_id}")
async def get_student_scores(score_id: int):
    score = session.query(Score).filter(Score.id == score_id).all()
    if not score:
        raise HTTPException(status_code=404, detail="Scores not found for student")
    return score

"""
@app.get("/all_scores")
async def get_all_scores():
    scores_query = session.query(Score)
    return scores_query.all()
"""


@app.patch("/score/{score_id}")
async def update_score(
    score_id: int,
    new_score: int = None,
):
    score = session.query(Score).filter(Score.id == score_id).first()
    if not score:
        raise HTTPException(status_code=404, detail="Score not found")
    if new_score is not None:
        score.score = new_score
    session.commit()
    return {"score updated": {"id": score_id, "subject": score.subject, "score": score.score}}


@app.delete("/score/{score_id}")
async def delete_score(score_id: int):
    score = session.query(Score).filter(Score.id == score_id).first()
    if not score:
        raise HTTPException(status_code=404, detail="Score not found")
    session.delete(score)
    session.commit()
    return {"score deleted": {"id": score_id, "subject": score.subject, "score": score.score}}
