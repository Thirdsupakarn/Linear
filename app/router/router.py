from fastapi import FastAPI

from ..models.model import *
from ..app import *
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Linear Gu ja bra")

origins = [
    "http://localhost:5173",
    "localhost:5173",
    "http://127.0.0.1:5173",
    "127.0.0.1:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


# @app.get("/{flight_instance_no}/view_seat_map" , tags=["Booking"])
# def view_seat_map(flight_instance_no):
#     return controller.get_seat_data(flight_instance_no)

@app.post("/main")
def get_data(dto:dto_user_input):
    try:
        inp = [dto.active_learning,dto.analytical,dto.communication,dto.complex_problem_solving,dto.creativity,dto.digital_quotience_literacy,dto.entrepreneurship,dto.integrity,dto.interpersonal_skills,dto.leadership,dto.resilience]
        output = main(inp)
        return output
    except:
        return "Invalid input"

# @app.put("/{user_id}/payment_method/pay_by_mobile_banking", tags=["Payment"])
# def pay_by_mobile_banking(user_id, booking_id, bank_account_info:bank_account_info):
#     Booking_details = controller.booking_details(user_id, booking_id)
#     payment = controller.pay(user_id, booking_id, Booking_details, 1, bank_account_info)
#     if payment:
#         return "mobilebanking payment is successful"

