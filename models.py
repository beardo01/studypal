from django.db import models

# Used for the lists holding foriegn keys
from django.core.validators import validate_comma_separated_integer_list

# Used for the default DateTimeField value
from datetime import datetime, date

# Used so timeline can have different models as its owner
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

# Create your models here.
class User(models.Model):
	# ID is automatically generated
	name = models.CharField(max_length=50)
	email = models.EmailField()
	phone = models.CharField(max_length=25, default=None)
	password = models.CharField(max_length=50)

class Group(models.Model):
	# ID is automatically generated
	name = models.CharField(max_length=50)
	privacy = models.PositiveSmallIntegerField()
	description = models.TextField(default=None)
	members = models.ManyToManyField('User')

class Chat(models.Model):
	# ID is automatically generated
	group_id = models.OneToOneField (
		'Group',
		on_delete=models.CASCADE,
	) # Group has a chat (1..1)
	important = models.TextField (
		max_length=None,
		validators=[validate_comma_separated_integer_list],
	) # Holds a list of Message IDs where important = true
	solved = models.TextField (
		max_length=None,
		validators=[validate_comma_separated_integer_list],
	) # Holds a list of Message IDs where solved = true
	unsolved = models.TextField (
		max_length=None,
		validators=[validate_comma_separated_integer_list],
	) # Holds a list of Message IDs where solved = false

class Message(models.Model):
	# ID is automatically generated
	chat_id = models.ForeignKey (
		'Chat',
		on_delete=models.CASCADE,
	) # Chat has many messages (1..*)
	author = models.ForeignKey('User') # User has many messages (1..*)
	create_date = models.DateTimeField(default=datetime.now)
	content = models.TextField()

	# Pinning system
	important = models.BooleanField(default=False)
	solved = models.BooleanField(default=False)
	replies = models.TextField (
		max_length=None,
		validators=[validate_comma_separated_integer_list],
	) # Holds a list of Reply IDs where message_id = self
	answer = models.OneToOneField('Reply')

class Reply(models.Model):
	# ID is automatically generated
	message_id = models.ForeignKey('Message') # Message has many replies (1..*)
	author = models.ForeignKey('User') # User has many messages (1..*)
	create_date = models.DateTimeField(default=datetime.now)
	content = models.TextField()
	answer = models.BooleanField(default=False)

class Timeline(models.Model):
	# ID is automatically generated

	# Allow the class to have a generic foreign key
	content_type = models.ForeignKey (
		ContentType, 
		on_delete=models.CASCADE,
		unique=True,
	)
	object_id = models.PositiveIntegerField() # ID of owner (User, Group)
	content_object = GenericForeignKey (
		'content_type', 
		'object_id',
	) # Object that the Timeline is owned by (User, Group)
	
	timeline_items = models.TextField (
		max_length=None,
		validators=[validate_comma_separated_integer_list],
	) # Holds a list of TimelineItem IDs where timeline_id = self
	start = models.DateTimeField(default=datetime.now)
	end = models.DateTimeField(default=datetime.now) # Updated by user action

class TimelineItem(models.Model):
	# ID is automatically generated
	timeline_id = models.ForeignKey(
		'Timeline',
		on_delete=models.CASCADE,
	) # Timeline has many timeline items (1..*)
	item_type = models.PositiveSmallIntegerField()
	start = models.DateTimeField()
	end = models.DateTimeField()
	title = models.CharField(max_length=50)
	description = models.TextField(default=None)
	location = models.CharField(max_length=100)
	author = models.ForeignKey('User') # User has many timeline items (1..*)

	# Repeat system
	repeat_frequency = models.PositiveSmallIntegerField() # 0 = Daily, 1 = Weekly...
	repeat_end = models.DateTimeField()

class TimelineItemRepeat(models.Model):
	# ID is automatically generated
	timelineitem_id =  models.ForeignKey (
		'TimelineItem',
		on_delete=models.CASCADE,
	) # TimelineItem has many timeline item repeats (1..*)
	item_type = models.PositiveSmallIntegerField()
	start = models.DateTimeField()
	end = models.DateTimeField()
	title = models.CharField(max_length=50)
	description = models.TextField(default=None)
	location = models.CharField(max_length=100)
	author = models.ForeignKey('User') # User has many timeline items (1..*)

class Resource(models.Model):
	# ID is automatically generated
	group_id = models.OneToOneField (
		'Group',
		on_delete=models.CASCADE,
	) # Group has one resource page (1..1)

class ResourceItem(models.Model):
	# ID is automatically generated
	resource_id = models.ForeignKey (
		'Resource',
		on_delete=models.CASCADE,
	) # Resource has many resource items (1..*)
	link = models.URLField()
	added = models.DateTimeField(default=datetime.now)
	author = models.ForeignKey('User') # User has many resource items (1..*)