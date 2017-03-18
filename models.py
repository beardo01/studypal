from django.db import models

# Used for the default DateTimeField value
from datetime import datetime, date

# Used so timeline can have different models as its owner
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

# Create your models here.
class User(models.Model):
	# ID is automatically created
	name = models.CharField(max_length=50)
	email = models.EmailField()
	phone = models.CharField(max_length=25, default=None)
	password = models.CharField()
	groups = models.ManyToManyField(Group)

class Group(models.Model):
	# ID is automatically created
	name = models.CharField(max_length=50)
	privacy = models.PositiveSmallIntegerField()
	description = models.TextField(default=None)
	members = models.ManyToManyField(User)

class Chat(models.Model):
	# ID is automatically created
	group_id = models.ForeignKey(
		'Group',
		on_delete=models.CASCADE, # When a group is deleted, delete the chat.
		)

class Message(models.Model):
	# ID is automatically generated
	chat_id = models.ForeignKey(Chat)
	author = models.ForeignKey(User)
	create_date = models.DateTimeField(default=datetime.now)
	content = models.TextField()

	# Pinning system
	important = models.BooleanField(default=False)
	solved = models.BooleanField(default=False)
	replies = models.ManyToManyField(Reply)
	answer = models.ForeignKey(Reply)

class Reply(models.Model):
	# ID is automatically generated
	message_id = models.ForeignKey(Message)
	author = models.ForeignKey(User)
	create_date = models.DateTimeField(default=datetime.now)
	content = models.TextField()
	# answer should be in Message

class Timeline(models.Model):
	# ID is automatically generated

	# Allow the class to have a generic foreign key
	timeline_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
	timeline_id = models.PositiveIntegerField()
	timeline_object = GenericForeignKey('timeline_type', 'timeline_id')

	start = models.DateTimeField(default=datetime.now)
	end = models.DateTimeField(default=datetime.now)