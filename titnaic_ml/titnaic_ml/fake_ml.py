def prediction(user_age):
    if user_age > 10:
        result = 'the person will die (over age)'
    else:
        result = 'the person live(less age)'
    return result
