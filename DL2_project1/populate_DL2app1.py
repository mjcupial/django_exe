import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','DL2_project1.settings')

import django
django.setup()

### FAKE POP SCRIPT
import random
from DL2_app1.models import AccessRecord, Webpage, Topic
from faker import Faker

fakegen = Faker()
print(fakegen.email())