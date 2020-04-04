from pendulum import timezone


def convert_time(original_datetime):
    thailand = timezone('Asia/Bangkok')
    converted_time = thailand.convert(original_datetime)
    return converted_time
