# Welcome to the "eJournal" project
This project is a backend server written in Python.

## Functionality
- CRUD students
- CRUD scores

## Requirements
- Python 3.11 or higher
- PostgreSQL

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/olzhjans/eJournalFastAPI
   ```
2. Install Python from https://www.python.org/downloads/
3. Create virtual environment
   ```bash
   cd path/to/project
   python -m venv venv
   ```
4. Activate virtual environment:  
   `Windows`
   ```bash
   venv\Scripts\activate
   ```
   `MacOS/Linux`
   ```bash
   source venv/bin/activate
   ```
5. Install dependencies from `requirements.txt`
   ```bash
   pip install -r requirements.txt
   ```
6. Install pgAdmin4 from https://www.pgadmin.org/download/
7. Create `eJournal` database in pgAdmin4:
8. Create `students` and `scores` tables:
   ```bash
   CREATE TABLE scores (
   id SERIAL PRIMARY KEY,
   student_id INTEGER NOT NULL,
   subject VARCHAR(255) NOT NULL,
   score INTEGER NOT NULL,
   FOREIGN KEY (student_id) REFERENCES students(id)
   );
   ```
   ```bash
   CREATE TABLE students (
   id SERIAL PRIMARY KEY,
   first_name VARCHAR(50) NOT NULL,
   last_name VARCHAR(50) NOT NULL,
   group_name VARCHAR(10) NOT NULL
   );
   ```

## Using the API
### Run project:
   ```bash
   uvicorn main:app --reload
   ```
### Open in browser to test API:
   http://localhost:8000/docs

### Students operating
`POST /students/` — add new student.  
`GET /students/{student_id}` — get student info.  
`PATCH /students/{student_id}` — update student info.  
`DELETE /students/{student_id}` — delete student.

### Scores operating
`POST /scores/` — add new score.  
`GET /scores/{score_id}` — get score info.  
`PATCH /scores/{score_id}` — update score info.  
`DELETE /scores/{score_id}` — delete score.