from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder



from app.server.database import (
	add_student,
	retrieve_student,
	retrieve_students,
	delete_student_data,
	update_student_data,
	)


from app.server.models.student import(
	ErrorResponseModel,
    ResponseModel,
    StudentSchema,
    UpdateStudentModel,
	)


router = APIRouter()