from apps.university import models
from rest_framework import serializers

# REST framework serializer
# http://www.django-rest-framework.org/tutorial/quickstart


# class ClassesSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = models.StudentClasses
#         # json id field is called pk in Django-rest-framework
#         fields = 'id'

class StudentClassesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.StudentClasses
        fields = ['id']


class AreaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Area
        fields = ('id', 'area')


class CoursesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Courses
        fields = ('prefix', 'num', 'title', 'hr')


class InstructorsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Instructors
        fields = ['id']


class LocationsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Locations
        fields = ('id', 'campus', 'building', 'room')