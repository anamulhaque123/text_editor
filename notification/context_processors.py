from. models import Notification


def notifications(request):
    if request.user.is_authenticated:
        return{'notifications': request.user.notifications.filter()}

    else:
        return{'notifications':[]}   