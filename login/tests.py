from django.test import TestCase
from login.models import user_info


class Db_tests(TestCase):
    def test_check_user_info_queries(self):
        create_info = user_info.objects.create(name="kev", date_created="90/10/23", email="rrwe!@gmail.com", age=23)
        create_info.save()
        user_name = user_info.objects.get(name="kev")
        self.assertEqual(str(user_name), "kev")
