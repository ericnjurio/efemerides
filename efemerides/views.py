from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from .serializers import CommemorationSerializer


@swagger_auto_schema(
    method='get',
    operation_description="Get commemorations details.",
    manual_parameters=(
        openapi.Parameter(
            'day',
            openapi.IN_QUERY,
            description="'day' filter",
            type=openapi.TYPE_STRING
        ),
    )
)
@api_view(['GET'])
def commemoration_detail(request):
    """Get commemorations details."""
    serializer = CommemorationSerializer(data=request.GET)
    serializer.is_valid(raise_exception=True)

    return Response(serializer.data, status.HTTP_200_OK)
