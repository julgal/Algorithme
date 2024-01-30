def convert_seconds(seconds):
    hours = seconds // 3600
    seconds = seconds -3600 * hours

    minutes = seconds // 60
    seconds = seconds - minutes * 60
    return hours, minutes, seconds
