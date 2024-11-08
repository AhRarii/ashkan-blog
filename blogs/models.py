from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BlogPost(models.Model):
    """A post the user can create."""
    title = models.CharField(max_length=200)
    text = models.TextField()
    date_added = models.DateField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Return a string representation of the model."""
        if len(self.text) > 50:
            return self.text[:50] + "..."
        else:
            return self.text