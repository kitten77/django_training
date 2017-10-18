from django.db import models

# Create your models here.
# kjapp kladd for ett contact form kan endres etter vært
# depId default = 1
# employeeId default=1
# userid if logged in get user id else default = 1
# subject
# message
# date for når det er sendt melding til appen
# read or not read that is the question

class ContactMessage(models.Model):
    employeeId = models.IntegerField(default=1)
    depId = models.IntegerField(default=1)
    uId = models.IntegerField(default=1)
    subject = models.CharField(max_length=31)
    message = models.TextField(max_length=1000)
    post_date = models.DateField('date posted', auto_now_add=True)
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.subject} on {self.post_date.strftime('%Y-%m-%d')}"
