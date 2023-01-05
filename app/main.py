from fastapi import FastAPI, Body
from app.server.database import add_student, retrieve_students, retrieve_student,\
update_student_data,delete_student_data
from app.server.models.student import StudentSchema, UpdateStudentModel
from app.server.models.response import response_model, error_response_model
from app.server.routes.student import router as StudentRouter
import json
import uvicorn


app = FastAPI()


app.include_router(StudentRouter, tags=["Student"], prefix="/student")



@app.post("/",response_description="Student data added")
async def add_student_data(student: StudentSchema = Body(...)):
	new_student = await add_student(student.dict())
	return response_model(new_student, "Student added successfully.")


@app.get("/", response_description="Students data fetched successfully.")
async def get_students_data():
	students = await retrieve_students()
	if students:
		return response_model(students, "Students data retrieved successfully")
	return response_model(students, "Empty list returned.")


@app.get("/{id}", response_description="find student data.")
async def get_student_data(id):
	student = await retrieve_student(id)
	if student:
		return response_model(student,"Students data retrieved successfully.")
	return response_model(student,"Empty list returned.")


@app.put("/{id}")
async def update_student_data(id: str, req: UpdateStudentModel = Body(...)):
	req = {k:v for k,v in req.dict().items() if v is not None}
	updated_student = await update_student_data(id, req)
	if updated_student:
		message = "Student with id : {} updated successfully.".format(id)
		return message
	return error_response_model


@app.delete("/{id}")
async def delete_student_data(id: str):
	deleted_student = delete_student_data(id)
	if deleted_student:
		message = "Student with id : {} deleted successfully.".format(id)
		return message
	message = "An error occurred", 404, "Student with id {0} doesn't exist".format(id)
	return message




if __name__=="__main__":
	uvicorn.run("server.app:app",host="0.0.0.0",port=8000,reload=True)	