# Import Django REST Framework tools for building web APIs.
from rest_framework.views import APIView       # Base class for API views
from rest_framework.response import Response   # Class to send JSON responses back
from rest_framework.permissions import AllowAny # Lets anyone access (no login needed)


# HealthCheckView is an API endpoint that answers "is the server running?".
# APIView is the base class; we subclass it to define our own endpoint.
class HealthCheckView(APIView):

    # permission_classes controls who can use this endpoint.
    # AllowAny means any visitor (logged in or not) can access it.
    permission_classes = [AllowAny]

    # The get() method runs when someone sends a GET request to this URL.
    # `request` holds information about the incoming web request.
    def get(self, request):

        # Return a JSON response telling the caller the API is healthy.
        # Response converts the Python dictionary into JSON automatically.
        return Response({
            "status": "healthy",
            "message": "Moodora API is running"
        })
