# Question 1
KEYS_PATTERN = r"{(.*?)}"
TEST_TEXT = """{name}, ваша запись изменена:
⌚️ {day_month} в {start_time}
👩 {master}
Услуги:
{services}
управление записью {record_link}"""
LIST_KEYS = [
    "name",
    "day_month",
    "day_of_week",
    "start_time",
    "end_time",
    "master",
    "services",
]

# Question 2
EXAMPLE_LIST = [
    ["665587", 2],
    ["669532", 1],
    [
        "669537",
        2,
    ],
    ["669532", 1],
    ["665587", 1],
]

# Question 3
JSON_OLD = {
    "company_id": 111111,
    "resource": "record",
    "resource_id": 406155061,
    "status": "create",
    "data": {
        "id": 11111111,
        "company_id": 111111,
        "services": [
            {
                "id": 9035445,
                "title": "Стрижка",
                "cost": 1500,
                "cost_per_unit": 1500,
                "first_cost": 1500,
                "amount": 1,
            }
        ],
        "goods_transactions": [],
        "staff": {"id": 1819441, "name": "Мастер"},
        "client": {
            "id": 130345867,
            "name": "Клиент",
            "phone": "79111111111",
            "success_visits_count": 2,
            "fail_visits_count": 0,
        },
        "clients_count": 1,
        "datetime": "2022-01-25T11:00:00+03:00",
        "create_date": "2022-01-22T00:54:00+03:00",
        "online": False,
        "attendance": 0,
        "confirmed": 1,
        "seance_length": 3600,
        "length": 3600,
        "master_request": 1,
        "visit_id": 346427049,
        "created_user_id": 10573443,
        "deleted": False,
        "paid_full": 0,
        "last_change_date": "2022-01-22T00:54:00+03:00",
        "record_labels": "",
        "date": "2022-01-22 10:00:00",
    },
}
JSON_NEW = {
    "company_id": 111111,
    "resource": "record",
    "resource_id": 406155061,
    "status": "create",
    "data": {
        "id": 11111111,
        "company_id": 111111,
        "services": [
            {
                "id": 22222225,
                "title": "Стрижка",
                "cost": 1500,
                "cost_per_unit": 1500,
                "first_cost": 1500,
                "amount": 1,
            }
        ],
        "goods_transactions": [],
        "staff": {"id": 1819441, "name": "Мастер"},
        "client": {
            "id": 130345867,
            "name": "Клиент",
            "phone": "79111111111",
            "success_visits_count": 2,
            "fail_visits_count": 0,
        },
        "clients_count": 1,
        "datetime": "2022-01-25T13:00:00+03:00",
        "create_date": "2022-01-22T00:54:00+03:00",
        "online": False,
        "attendance": 2,
        "confirmed": 1,
        "seance_length": 3600,
        "length": 3600,
        "master_request": 1,
        "visit_id": 346427049,
        "created_user_id": 10573443,
        "deleted": False,
        "paid_full": 1,
        "last_change_date": "2022-01-22T00:54:00+03:00",
        "record_labels": "",
        "date": "2022-01-22 10:00:00",
    },
}
DIFF_LIST = ["services", "staff", "datetime"]

# Question 4
DB_URL = "mongodb://localhost:27017/"
EXPIRY_TIME = 60 * 60 * 24


# Question 5
def send_email():
    return {"status": "Email sent successfully"}


def process_data():
    return {"status": "Data processed successfully"}


FUNCTION_MAP = {
    "send_email": send_email,
    "process_data": process_data,
}
