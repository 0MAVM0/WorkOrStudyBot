from aiogram import types
from loader import dp, bot
from aiogram.dispatcher import FSMContext

from states.work_place import ApplicationForWork

# lambda message: message.text.strip().lower() == "💼work place🏢"
@dp.message_handler(commands="work")
async def work_place_handler(message: types.Message):
    text = "*You have choosed✅ a 💼 Work 🏢 Place*\n\n"
    text += "Now, answer to some questions📃 please.\n\n"
    text += "*What is your full name?:*"
    await message.answer(text=text, parse_mode="Markdown")
    await ApplicationForWork.name.set()

@dp.message_handler(state=ApplicationForWork.name)
async def name_condition(message: types.Message, state: FSMContext):
    name = message.text
    await state.update_data( { "name" : name } )

    await message.answer("🕑 *Age:*", parse_mode="Markdown")
    await ApplicationForWork.age.set()

@dp.message_handler(state=ApplicationForWork.age)
async def age_condition(message: types.Message, state: FSMContext):
    age = message.text
    await state.update_data( { "age" : age } )

    await message.answer("📚 *Technology that you know:*", parse_mode="Markdown")
    await ApplicationForWork.technology.set()

@dp.message_handler(state=ApplicationForWork.technology)
async def technology_condition(message: types.Message, state: FSMContext):
    technology = message.text
    await state.update_data( { "technology" : technology } )

    await message.answer("📞 *Phone number:*", parse_mode="Markdown")
    await ApplicationForWork.phone_number.set()

@dp.message_handler(state=ApplicationForWork.phone_number)
async def phone_number_condition(message: types.Message, state: FSMContext):
    phone_number = message.text
    await state.update_data( { "phone_number" : phone_number } )

    await message.answer("🌐 *Area you live in:*", parse_mode="Markdown")
    await ApplicationForWork.area.set()

@dp.message_handler(state=ApplicationForWork.area)
async def area_condition(message: types.Message, state: FSMContext):
    area = message.text
    await state.update_data( { "area" : area } )

    await message.answer("💰 *How much salary do you want?:*", parse_mode="Markdown")
    await ApplicationForWork.salary.set()

@dp.message_handler(state=ApplicationForWork.salary)
async def salary_condition(message: types.Message, state: FSMContext):
    salary = message.text
    await state.update_data( { "salary" : salary } )

    await message.answer("👨🏻‍💻 *Occupation?:*", parse_mode="Markdown")
    await ApplicationForWork.occupation.set()

@dp.message_handler(state=ApplicationForWork.occupation)
async def occupation_condition(message: types.Message, state: FSMContext):
    occupation = message.text
    await state.update_data( { "occupation" : occupation } )

    await message.answer("👨🏻‍💻 *Work time?:\n\n*(9:00 - 18:00)", parse_mode="Markdown")
    await ApplicationForWork.work_time.set()

@dp.message_handler(state=ApplicationForWork.work_time)
async def work_time_condition(message: types.Message, state: FSMContext):
    work_time = message.text
    await state.update_data( { "work_time" : work_time } )

    await message.answer("🔎 *Purpose of working?:*", parse_mode="Markdown")
    await ApplicationForWork.purpose.set()

@dp.message_handler(state=ApplicationForWork.purpose)
async def purpose_condition(message: types.Message, state: FSMContext):
    purpose = message.text
    await state.update_data( { "purpose" : purpose } )

    data = await state.get_data()

    fields = [
        ("👨‍💼 Worker", "name"),
        ("🕑 Age", "age"),
        ("📚 Technology", "technology"),
        ("📞 Phone number", "phone_number"),
        ("🌐 Area", "area"),
        ("💰 Salary", "salary"),
        ("👨🏻‍💻 Occupation", "occupation"),
        ("🕰 Work time", "work_time"),
        ("🔎 Purpose", "purpose"),
    ]

    final_answer = "*Need a 💼 Work  🏢 Place*\n\n"

    for label, key in fields:
        value = data.get(key, None)
        final_answer += f"{label}: {value}\n"

    await message.answer(text = final_answer)
