from rest_framework import serializers
from rest_framework.serializers import SerializerMethodField

from courses.models import Course, Lesson, Subscription
from courses.validators import UrlValidator


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class LessonSerializer(serializers.ModelSerializer):
    validators = [UrlValidator(field="link_to_video")]

    class Meta:
        model = Lesson
        fields = "__all__"


class CourseDetailSerializer(serializers.ModelSerializer):
    number_of_lessons = SerializerMethodField()
    course_lessons = SerializerMethodField()
    subscription = SerializerMethodField()

    def get_number_of_lessons(self, course):
        return Lesson.objects.filter(course=course.id).count()

    def get_course_lessons(self, course):
        lessons = Lesson.objects.filter(course=course.id)
        return [(lesson.name, lesson.description) for lesson in lessons]

    def get_subscription(self, instance):
        user = self.context["request"].user
        return (
            Subscription.objects.all()
            .filter(user=user)
            .filter(course=instance)
            .exists()
        )

    class Meta:
        model = Course
        fields = ("name", "description", "course_lessons", "number_of_lessons", "subscription")


class SubscriptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subscription
        fields = "__all__"
