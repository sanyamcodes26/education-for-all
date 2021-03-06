from django.db import models

from auth_prime.models import User_Credential

# Create your models here.

# ----------------------------------------------

class Coordinator(models.Model):
    coordinator_id = models.AutoField(primary_key=True, null=False, blank=False, unique=True)

    user_credential_id = models.ForeignKey(User_Credential, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.coordinator_id} | {self.user_credential_id.user_f_name} | {self.user_credential_id.user_l_name}"

class Subject(models.Model):
    subject_id = models.AutoField(primary_key=True, null=False, blank=False, unique=True)

    coordinator_id_1 = models.ForeignKey(Coordinator, related_name='coordinator_id_1', null=True, blank=False, on_delete=models.SET_NULL)
    coordinator_id_2 = models.ForeignKey(Coordinator, related_name='coordinator_id_2',  null=True, blank=True, on_delete=models.SET_NULL)
    coordinator_id_3 = models.ForeignKey(Coordinator, related_name='coordinator_id_3',  null=True, blank=True, on_delete=models.SET_NULL)
    coordinator_id_4 = models.ForeignKey(Coordinator, related_name='coordinator_id_4',  null=True, blank=True, on_delete=models.SET_NULL)
    coordinator_id_5 = models.ForeignKey(Coordinator, related_name='coordinator_id_5',  null=True, blank=True, on_delete=models.SET_NULL)

    subject_name = models.CharField(max_length=512, null=False, blank=False)
    subject_description = models.TextField()

    def __str__(self):
        return f"{self.subject_id} | {self.subject_name}"

# ----------------------------------------------

class Video(models.Model):
    video_id = models.AutoField(primary_key=True, null=False, blank=False, unique=True)

    video_name = models.CharField(max_length=512, null=False, blank=False)
    video_url = models.URLField(max_length=1024, null=False, blank=False)

    def __str__(self):
        return f"{self.video_id} | {self.videl_name}"

class Forum(models.Model):
    forum_id = models.AutoField(primary_key=True, null=False, blank=False, unique=True)

    forum_name = models.CharField(max_length=512)

    def __str__(self):
        return f"{self.forum_id} | {self.forum_name}"

class Reply(models.Model):
    reply_id = models.AutoField(primary_key=True, null=False, blank=False, unique=True)

    forum_id = models.ForeignKey(Forum, null=True, blank=True, on_delete=models.CASCADE)
    user_credential_id = models.ForeignKey(User_Credential, null=True, blank=True, on_delete=models.SET_NULL)

    reply_body = models.TextField()
    reply_upvote = models.IntegerField()
    reply_downvote = models.IntegerField()

    def __str__(self):
        if(self.user_credential_id == None):
            return f"{self.reply_id} | {self.forum_id.forum_name} | NULL"
        else:
            return f"{self.reply_id} | {self.forum_id.forum_name} | {self.user_credential_id.user_f_name}"

class Lecture(models.Model):
    lecture_id = models.AutoField(primary_key=True, null=False, blank=False, unique=True)

    lecture_name = models.CharField(max_length=512, null=False, blank=False)
    lecture_body_1 = models.TextField(null=True, blank=True)
    lecture_body_2 = models.TextField(null=True, blank=True)
    lecture_external_url = models.URLField()

    def __str__(self):
        return f"{self.lecture_id} | {self.lecture_name}"

class Assignment(models.Model):
    assignment_id = models.AutoField(primary_key=True, null=False, blank=False, unique=True)

    assignment_name = models.CharField(max_length=512)
    assignment_body_1 = models.TextField(null=False, blank=False)
    assignment_body_2 = models.TextField(null=True, blank=True)
    assignment_external_url = models.URLField()

    def __str__(self):
        return f"{self.assignment_id} | {self.asignment_name}"

# ----------------------------------------------

class Post(models.Model):
    post_id = models.AutoField(primary_key=True, null=False, blank=False, unique=True)

    user_credential_id = models.ForeignKey(User_Credential, null=True, blank=True, on_delete=models.SET_NULL)
    subject_id = models.ForeignKey(Subject, null=True, blank=True, on_delete=models.SET_NULL)
    video_id = models.ForeignKey(Video, null=True, blank=True, on_delete=models.SET_NULL)
    forum_id = models.ForeignKey(Forum, null=True, blank=True, on_delete=models.SET_NULL)
    lecture_id = models.ForeignKey(Lecture, null=True, blank=True, on_delete=models.SET_NULL)
    assignment_id = models.ForeignKey(Assignment, null=True, blank=True, on_delete=models.SET_NULL)

    post_name = models.CharField(max_length=1024)
    post_body = models.TextField()
    post_views = models.PositiveBigIntegerField()
    post_upvote = models.IntegerField()
    pos_downvote = models.IntegerField()

    def __str__(self):
        if(self.user_credential_id == None):
            user_credential_id = 'NULL'
        else:
            user_credential_id = self.user_credential_id.user_credential_id
        
        if(self.subject_id == None):
            subject_id = 'NULL'
        else:
            subject_id = self.subject_id.subject_id
        
        if(self.video_id == None):
            video_id = 'NULL'
        else:
            video_id = self.video_id.video_id
        
        if(self.forum_id == None):
            forum_id = 'NULL'
        else:
            forum_id = self.forum_id.forum_id
        
        if(self.assignment_id == None):
            assignment_id = 'NULL'
        else:
            assignment_id = self.assignment_id.assignment_id
        
        if(self.lecture_id == None):
            lecture_id = 'NULL'
        else:
            lecture_id = self.lecture_id.lecture_id
        
        return f"{self.post_id} | {user_credential_id} | {subject_id} | {video_id} | {forum_id} | {lecture_id} | {assignment_id}"