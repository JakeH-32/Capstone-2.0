def calculate_situp_score(count):   
    if count >= 58:
        return 10
    elif count >= 55:
        return 9.5
    elif count >= 54:
        return 9.4
    elif count >= 53:
        return 9.2
    elif count >= 52:
        return 9.0
    elif count >= 51:
        return 8.8
    elif count >= 50:
        return 8.7
    elif count >= 49:
        return 8.5
    elif count >= 48:
        return 8.3
    elif count >= 47:
        return 8.0
    elif count >= 46:
        return 7.5
    elif count >= 45:
        return 7.0
    elif count >= 44:
        return 6.5
    elif count >= 43:
        return 6.3
    elif count >= 42:
        return 6.0
    else:
        return 0.0
    

def calculate_pushup_score(count):   
    if count >= 67:
        return 10
    elif count >= 62:
        return 9.5
    elif count >= 61:
        return 9.4
    elif count >= 60:
        return 9.3
    elif count >= 59:
        return 9.2
    elif count >= 58:
        return 9.1
    elif count >= 57:
        return 9.0
    elif count >= 56:
        return 8.9
    elif count >= 54:
        return 8.8
    elif count >= 53:
        return 8.7
    elif count >= 52:
        return 8.6
    elif count >= 51:
        return 8.5
    elif count >= 50:
        return 8.4
    elif count >= 49:
        return 8.3
    elif count >= 48:
        return 8.1
    elif count >= 47:
        return 8.0
    elif count >= 46:
        return 7.8
    elif count >= 45:
        return 7.7
    elif count >= 44:
        return 7.5
    elif count >= 43:
        return 7.3
    elif count >= 42:
        return 7.2
    elif count >= 41:
        return 7.0
    elif count >= 40:
        return 6.8
    elif count >= 39:
        return 6.5
    elif count >= 38:
        return 6.3
    elif count >= 37:
        return 6.0
    elif count >= 36:
        return 5.8
    elif count >= 35:
        return 5.5
    elif count >= 34:
        return 5.3
    elif count >= 33:
        return 5.0
    else:
        return 0.0


def calculate_waist_score(size):
    if size <= 35.0:
        return 20.0
    elif size <= 35.5:
        return 17.6
    elif size <= 36:
        return 17.0
    elif size <= 36.5:
        return 16.4
    elif size <= 37:
        return 15.8
    elif size <= 37.5:
        return 15.1
    elif size <= 38:
        return 14.4
    elif size <= 38.5:
        return 13.5
    elif size <= 39.0:
        return 12.6
    else:
        return 0.0


def calculate_run_score(time_in_seconds):
    if time_in_seconds <= 9 * 60 + 12:
        return 60.0
    elif time_in_seconds <= 9 * 60 + 34:
        return 59.7
    elif time_in_seconds <= 9 * 60 + 45:
        return 59.3
    elif time_in_seconds <= 9 * 60 + 58:
        return 58.9
    elif time_in_seconds <= 10 * 60 + 10:
        return 58.5
    elif time_in_seconds <= 10 * 60 + 23:
        return 57.9
    elif time_in_seconds <= 10 * 60 + 37:
        return 57.3
    elif time_in_seconds <= 10 * 60 + 51:
        return 56.6
    elif time_in_seconds <= 11 * 60 + 6:
        return 55.7
    elif time_in_seconds <= 11 * 60 + 22:
        return 54.8
    elif time_in_seconds <= 11 * 60 + 38:
        return 53.7
    elif time_in_seconds <= 11 * 60 + 56:
        return 52.4
    elif time_in_seconds <= 12 * 60 + 14:
        return 50.9
    elif time_in_seconds <= 12 * 60 + 33:
        return 49.2
    elif time_in_seconds <= 12 * 60 + 53:
        return 47.2
    elif time_in_seconds <= 13 * 60 + 14:
        return 44.9
    elif time_in_seconds <= 13 * 60 + 36:
        return 42.3
    else:
        return 0.0


