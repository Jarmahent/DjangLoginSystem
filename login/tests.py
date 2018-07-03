from django.test import TestCase
from login.models import user_info
# Create your tests here.


class db_tests(TestCase):
    def check_user_info_queries(self):
        create = user_info.objects.create(name="kev", date_created="90/10/23", email="rrwe!@gmail.com", age=23)
        create.save()
        user_name = user_info.objects.get(name="kev")
        user_email = user_info.objects.get(email="rrwe!@gmail.com")
        user_date = user_info.objects.get(date_created="90/10/23")
        user_age = user_info.objects.get(age=23)
        self.assertEqual(user_age, 23)
        self.assertEqual(user_date, "90/10/23")
        self.assertEqual(user_email, "rrwe!@gmail.com")
        self.assertEqual(user_name, "kev")
