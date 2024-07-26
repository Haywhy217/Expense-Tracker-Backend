import jwt
from datetime import datetime,timezone
from django.conf import settings


def create_jwt_token(user):
  payload ={
    "user_id": user.id,
    "exp": datetime.now(timezone.utc) + settings.JWT_EXPIRATION_DELTA,
    "iat": datetime.now(timezone.utc)
  }


  token= jwt.encode(payload,settings.SECRET_KEY,algorithm="HS256")
  return token

def decode_jwt_token(token):

  try:
    payload = jwt.decode(token, settings.SECRET_KEY, algorithms={'HS256'})
    return payload['user_id']
  except jwt.ExpiredSignatureError:
    return "Token Expired"
  except jwt.InvalidTokenError:
    return "Invalid Token"
  