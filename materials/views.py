from rest_framework import viewsets
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from .models import Course, Lesson
from .serializers import CourseSerializer, CourseListSerializer, LessonSerializer


class CourseViewSet(viewsets.ModelViewSet):
    """
    ViewSet для модели Course.
    Реализует CRUD операции: список, создание, получение, обновление, удаление.
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get_serializer_class(self):
        """
        Используем упрощенный сериализатор для списка курсов.
        """
        if self.action == 'list':
            return CourseListSerializer
        return CourseSerializer


class LessonListCreateAPIView(ListCreateAPIView):
    """
    Generic-класс для получения списка уроков и создания нового урока.
    """
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """
    Generic-класс для получения, обновления и удаления урока.
    """
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

