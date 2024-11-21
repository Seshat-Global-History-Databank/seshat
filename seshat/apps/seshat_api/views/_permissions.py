from rest_framework.permissions import IsAdminUser

ONLY_ADMIN_PERMISSIONS = {
    "HEAD": [IsAdminUser],
    "OPTIONS": [IsAdminUser],
    "GET": [IsAdminUser],
    "POST": [IsAdminUser],
    "PUT": [IsAdminUser],
    "PATCH": [IsAdminUser],
    "DELETE": [IsAdminUser],
}
