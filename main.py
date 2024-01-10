from datetime import date, datetime, timedelta

DAY: timedelta = timedelta(days=1)

input_date: str = input("Input your birthday date: ")
current_date: datetime = datetime.strptime(input_date, "%d.%m.%Y")
age: int = 0

# every day till the end of the current year
while (current_date <= datetime.today().replace(day=31, month=12)):
    print(current_date.strftime(f"Year: %Y : %a | Your age is {age}"))
    next_year: date = current_date.replace(year=current_date.year + 1)

    # expected is one weekday later than last year
    expected_weekday = (current_date + DAY).strftime("%a")
    next_weekday = (next_year).strftime("%a")

    if next_weekday != expected_weekday:
        print("Stolen Weekday:", expected_weekday)

    current_date = next_year
    age += 1