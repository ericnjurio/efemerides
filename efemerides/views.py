from rest_framework import status
from rest_framework.response import Response

from rest_framework.decorators import api_view

from .serializers import CommemorationSerializer


@api_view(['GET'])
def commemoration_detail(request):
    """Get commemorations details."""
    serializer = CommemorationSerializer(data=request.GET)
    serializer.is_valid(raise_exception=True)

    return Response(serializer.data, status.HTTP_200_OK)
