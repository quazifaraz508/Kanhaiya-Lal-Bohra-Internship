from django.shortcuts import render
from .models import StudentDetails
from .serializer import StundetsSerializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework import viewsets,status, permissions
from rest_framework.response import Response
from .tasks import send_welcome_email
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAdminUser

# Create your views here.
@csrf_exempt
@api_view(['GET', 'POST', 'DELETE'])
def Students_list(request):
    if request.method == 'GET':
        studets_list = StudentDetails.objects.all()
        stundet_serializer = StundetsSerializers(studets_list, many= True)
        return Response(stundet_serializer.data)
    
    elif request.method == 'POST':
        stundet_serializer = StundetsSerializers(data = request.data) 
        if stundet_serializer.is_valid():
            stundet_serializer.save()
            send_welcome_email.delay(stundet_serializer.data['student_email'])
            
        else:
            return Response(stundet_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(stundet_serializer.errors, status=400)
    
    elif request.method == 'DELETE':
        
        student_id = request.data.get('id')
        if not request.user.is_superuser:
            return Response({'error': 'Only superusers can delete records.'}, status=403)

        try:
            student = StudentDetails.objects.get(id=student_id)
            student.delete()
            return Response({'message': f'Student with id {student_id} deleted.'})
        except StudentDetails.DoesNotExist:
            return Response({'error': 'Student not found.'}, status=404)

    # fallback in case some other method slips through
    return Response({"error": "Method not allowed"}, status=405)