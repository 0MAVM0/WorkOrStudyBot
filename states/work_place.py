from aiogram.dispatcher.filters.state import StatesGroup, State

class ApplicationForWork(StatesGroup):
    name = State()
    age = State()
    technology = State()
    phone_number = State()
    area = State()
    salary = State()
    occupation = State()
    work_time = State()
    purpose = State()
