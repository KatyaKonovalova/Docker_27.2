from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from courses.models import Course, Lesson
from users.models import User


class LessonTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="admin@example.ru")
        self.course = Course.objects.create(name="Test", description="...")
        self.lesson = Lesson.objects.create(
            name="Урок 1",
            description="Введение",
            course=self.course,
            owner=self.user,
        )
        self.client.force_authenticate(user=self.user)

    def test_lesson_retrieve(self):
        url = reverse("materials:lesson_retrieve", args=(self.lesson.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("lesson_name"), self.lesson.name)

    def test_lesson_create(self):
        url = reverse("materials:lesson_create")
        data = {"name": "Урок_2"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Lesson.objects.filter(name="Урок_2").count(), 1)

    def test_lesson_update(self):
        url = reverse("materials:lesson_update", args=(self.lesson.pk,))
        data = {"name": "Урок_2"}
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("name"), "Урок_2")

    def test_lesson_delete(self):
        url = reverse("materials:lesson_delete", args=(self.lesson.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Lesson.objects.all().count(), 0)

    def test_list_lesson(self):
        course = Course.objects.create(
            name="Тестовый курс",
            description="Тест",
        )

        Lesson.objects.create(
            name="Тестовый урок",
            description="Тест",
            link_to_video=course,
            owner=self.user,
        )

        response = self.client.get("/courses/lessons/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)


class CourseTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="admin@example.ru")
        self.course = Course.objects.create(
            name="Test", description="...", owner=self.user
        )
        self.lesson = Lesson.objects.create(
            name="Урок 1",
            description="Введение",
            course=self.course,
            owner=self.user,
        )
        self.client.force_authenticate(user=self.user)

    def test_course_retrieve(self):
        url = reverse("courses:course_detail", args=(self.course.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("name"), self.course.name)

    def test_course_create(self):
        url = reverse("courses:course_list")
        data = {"name": "Пошив брюк"}
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Course.objects.all().count(), 2)

    def test_course_update(self):
        url = reverse("materials:course_detail", args=(self.course.pk,))
        data = {"name": "Пошив юбки"}
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("name"), "Пошив юбки")

    def test_course_delete(self):
        url = reverse("materials:course_detail", args=(self.course.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Course.objects.all().count(), 0)

    def test_list_course(self):
        response = self.client.get(
            "/courses/",
        )
        print(response)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            {
                "count": 1,
                "next": None,
                "previous": None,
                "results": [
                    {
                        "id": 3,
                        "name": "Test",
                        "preview_course": None,
                        "description": "...",
                        "owner": None,
                        "subscription": False,
                        "course_lessons": [
                            {
                                "id": 4,
                                "name": "Урок 1",
                                "preview_lesson": None,
                                "description": "Введение",
                                "link_to_video": None,
                                "course": 5,
                                "owner": 4,
                            }
                        ],
                        "number_of_lessons": 1,
                    }
                ],
            },
        )
