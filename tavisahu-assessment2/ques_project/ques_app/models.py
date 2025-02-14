from django.db import models

# Create your models here.
class QuestionPaper(models.Model):
    q_id = models.IntegerField(primary_key=True)
    subject = models.CharField(max_length=100)
    question = models.CharField(max_length=100)
    
    def __str__(self):
        return self.q_id