from datetime import datetime

def validate_future_date(future_date):
    try:
        if (" " in future_date):
            future_inter = datetime.strptime(future_date, "%m %d %Y")
            future_inter2 = future_inter.strftime("%m-%d-%Y")
            future = datetime.strptime(future_inter2, "%m-%d-%Y")
        else:
            future = datetime.strptime(future_date, "%m-%d-%Y")
    except:
        return 0

    if (future > datetime.now()):
        return 1
    else:
        return 0