from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.utils import timezone

from .models import Attendance
from .serializers import AttendanceSerializer


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def attendance(request):

    if request.method == "POST":

        today = timezone.localdate()

        if Attendance.objects.filter(user=request.user, date=today).exists():
            return Response({"message": "Attendance already marked"})

        Attendance.objects.create(user=request.user)

        return Response({"message": "Attendance marked successfully"})

    records = Attendance.objects.filter(user=request.user)

    serializer = AttendanceSerializer(records, many=True)

    return Response(serializer.data)