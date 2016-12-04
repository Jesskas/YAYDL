from django.db import models

# The initial youtube video data
class YTVideo(models.Model):
    video_id = models.CharField(max_length=200)
    def __str__(self):
        return self.video_id

# A copy of the original video, downloaded
class LocalVideo(models.Model):
    ytvideo = models.ForeignKey(YTVideo, on_delete=models.CASCADE)
    video_quality = models.CharField(max_length=200)
    def __str__(self):
        return ytvideo.video_id + "-" + self.video_quality

# A copy of the original video, downloaded
class LocalAudio(models.Model):
    ytvideo = models.ForeignKey(YTVideo, on_delete=models.CASCADE)
    audio_quality = models.CharField(max_length=200)
    def __str__(self):
        return ytvideo.video_id + "-" + self.audio_quality




# import datetime
#
# from django.db import models
# from django.utils import timezone
#
# # Has a question and a publication date
# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')
#     def __str__(self):
#         return self.question_text
#     def was_published_recently(self):
#         return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
#
# # Has a choice and a vote tally
# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)
#     def __str__(self):
#         return self.choice_text
#
# # Each Choice is associated with a Question.
