from django.test import TestCase
from .models import ToDo


class TodoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Todo.objects.create(title="first todo",body='a body here')

# Create your tests here.
