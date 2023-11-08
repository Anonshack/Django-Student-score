from django.forms import model_to_dict
from rest_framework.response import Response
from .models import Student
from rest_framework.views import APIView


# class StudentsListView(ListAPIView):
#     # queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#
#     def get_queryset(self):
#         try:
#             pass_score = self.request.GET['pass_score']
#             queryset = Student.objects.filter(mark_score__gte=pass_score).values()
#         except:
#             queryset = Student.objects.all().values()
#         return queryset


class StudentsView(APIView):
    def get(self, request):
        try:
            pass_score = request.GET['pass_score']
            students = Student.objects.filter(mark_score__gte=pass_score).values()
        except:
            students = Student.objects.all().values()
        # students = Student.objects.filter(mark_score__gt=30).values()
        return Response({'students': list(students)})

    def post(self, request):
        new_student = Student.objects.create(
            name=request.data['name'],
            last_name=request.data['last_name'],
            mark_score=request.data['mark_score'],
            url=request.data['url'],
        )
        return Response({'new_student': model_to_dict(new_student)})

    def delete(self, request):
        try:
            student_id = request.data['student_id'];
            Student.objects.filter(pk=student_id).delete();
            return Response({'res': 'success'})
        except:
            return Response({'res': 'error'})