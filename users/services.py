from .models import User

def users():
    user_qs = User.objects.all().values('id', 'username', 'email')
    return {
        "users": list(user_qs),
        "message": "Users retrieved successfully"
    }
