from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#declaring tuples to be able to post drafts and publish posts
STATUS = (
    (0, "Draft"),
    (1, "Publish")
)