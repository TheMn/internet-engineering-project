from datetime import datetime


def time_now(request):
    return {'time_now': datetime.now()}
