from rest_framework import serializers
from rest_framework.serializers import SerializerMethodField

from courses.models import Course, Lesson


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"


class CourseDetailSerializer(serializers.ModelSerializer):
    number_of_lessons = SerializerMethodField()
    lessons_date = SerializerMethodField()

    def get_number_of_lessons(self, course):
        return Lesson.objects.filter(course=course.id).count()

    def get_lessons_date(self, course):
        lessons = Lesson.objects.filter(course=course.id)
        return [(lesson.name, lesson.description) for lesson in lessons]

    class Meta:
        model = Course
        fields = ("name", "description", "number_of_lessons", "lessons_date")
