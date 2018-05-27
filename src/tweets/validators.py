from django.core.exceptions import ValidationError
from django.db import models

# Create your models here.
def validate_content(value):
	content = value
	if content == "":
		raise ValidationError("Content cannot be blank")
	return value