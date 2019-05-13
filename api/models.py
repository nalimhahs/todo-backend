from django.db import models

# Create your models here.

class Note(models.Model):

    title = models.CharField(max_length=25, null=True)
    content = models.TextField()
    isRemainder = models.BooleanField()
    createdDate = models.DateTimeField(auto_now_add=True)
    editedDate = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey('auth.User', related_name='notes', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.title is None:
            self.title = self.content[:10] + '...'
        super(Note, self).save(*args, **kwargs)
