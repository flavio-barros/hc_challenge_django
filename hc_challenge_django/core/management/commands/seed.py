from django.core.management.base import BaseCommand
from core.factory import UserFactory, ReportFactory, ReportResponseFactory, ReportsWithResponsesFactory
from core.models import Report
import random

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("--users", default=20, type=int)
        parser.add_argument("--reports", default=100, type=int)
        parser.add_argument("--report_responses", default=2, type=int)

    def handle(self, *args, **options):
        users = list()
        reports = list()
        for _ in range(0, options["users"]):
            user = UserFactory.create()
            users.append(user)
            
        for _ in range(0, options["reports"]):
            num_supervisors = random.randrange(2, 5)
            supervisors = list()
            for _ in range(0, num_supervisors):
                supervisors.append(users[random.randrange(len(users))])
            ReportsWithResponsesFactory.create(responses=2, supervisors = supervisors)


            
                