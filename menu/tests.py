from django.test import TestCase

from decouple import config
# Create your tests here.

print(config("DB_PORT"))
