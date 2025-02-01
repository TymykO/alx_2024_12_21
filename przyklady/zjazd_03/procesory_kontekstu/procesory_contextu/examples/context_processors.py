from .models import Notification
def global_settings(request):
    return {
        "app_name": "ramblownica",
        "version": "0.0.1",
    }


def unread_notifications(request):
    if request.user.is_authenticated:
        return {"unread_notifications": Notification.objects.filter(user=request.user, read=False).count()}
    return {}
