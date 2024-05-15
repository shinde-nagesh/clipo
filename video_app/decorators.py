import jwt
from functools import wraps
from rest_framework.exceptions import AuthenticationFailed
from .models import CustomUser  # Ensure the model is correctly referenced

def jwt_authentication_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        try:
            token = token.split(" ")[1]
            decoded_token = jwt.decode(token, 'secret', algorithms=['HS256'])
            user_id = decoded_token.get('id')
            user = CustomUser.objects.get(pk=user_id)
            request.user = user
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')
        except jwt.InvalidTokenError:
            raise AuthenticationFailed('Invalid token!')
        except CustomUser.DoesNotExist:
            raise AuthenticationFailed('User not found!')

        return view_func(request, *args, **kwargs)

    return wrapper
