from django.db import models

from django.db import models
from django.utils.six import python_2_unicode_compatible

@python_2_unicode_compatible
class Comment(models.Model):
	name=models.CharField(max_length=100)
	email=models.EmailField(max_length=255)
	url=models.URLField(blank=True)
	text=models.TextField()
	created_time=models.DateTimeField(auto_now_add=True)

	post=models.ForeignKey('blog.Post')
#由于一个评论只能属于一篇文章，所以在评论中设置外键链接被关联的文章。一对多，文章是一，评论是多
	
	def __str__(self):
		return self.text[:20]
