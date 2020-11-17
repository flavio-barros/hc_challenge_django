import factory
from core import models
from django.contrib.auth.models import User
import random

class UserFactory(factory.django.DjangoModelFactory): 
    class Meta:
        model = User
    username = factory.Faker('user_name')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    email = factory.Faker('ascii_email')

class ReportFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Report
    message = factory.Faker('sentence', nb_words=50)
    author = factory.Iterator(User.objects.all())

    @factory.post_generation
    def supervisors(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for supervisor in extracted:
                self.supervisors.add(supervisor)


class ReportResponseFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.ReportResponse
    message = factory.Faker('sentence', nb_words=50)
    author = factory.Iterator(User.objects.all())
    report = factory.SubFactory(ReportFactory)

class ReportsWithResponsesFactory(ReportFactory):

    @factory.post_generation
    def responses(obj, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for i in range(extracted):
                ReportResponseFactory(report=obj)

