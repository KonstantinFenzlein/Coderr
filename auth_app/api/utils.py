from rest_framework.authtoken.models import Token
from rest_framework.response import Response


def build_token_response(user, status_code):                                            # Erstellt eine Antwort mit einem Authentifizierungstoken für den angegebenen Benutzer. Wenn der Benutzer erfolgreich registriert oder angemeldet wurde, wird ein Token generiert (oder abgerufen), und die Antwort enthält das Token sowie grundlegende Informationen über den Benutzer.
    token, _ = Token.objects.get_or_create(user=user)
    return Response(
        {
            "token": token.key,
            "username": user.username,
            "email": user.email,
            "user_id": user.id,
        },
        status=status_code,
    )
