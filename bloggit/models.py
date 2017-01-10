from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from taggit.managers import TaggableManager

# model managers
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,self).get_queryset()\
                                            .filter(status='published')

# Create your models here.
STATUS_CHOICES = (
    ('draft', 'Draft'),
    ('published', 'Published'),
    )

class Post(models.Model):
    """ this class will be used to create post objects
        the member variables are

        author      author of the post
        title       heading of the post
        slug        slug representation of title for better SEO
        content     body of the post
        publish     date published for post
        updated     date updated for the post
        created     date created for the post
        status      publication status of post
    """

    author  = models.ForeignKey(User,
                                  related_name='created_posts')
    title   = models.CharField(max_length=250)
    slug    = models.SlugField(max_length=250,
                                unique_for_date='publish')
    content = models.TextField()
    publish = models.DateField(default=timezone.now)
    updated = models.DateField(auto_now_add=True)
    created = models.DateField(auto_now=True)
    status  = models.CharField(max_length=10,
                                choices=STATUS_CHOICES,
                                default='draft')

    # managers
    objects = models.Manager()   # default manager
    published = PublishedManager()
    tags = TaggableManager()

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('bloggit:detail',
                        args=[self.publish.year,
                              self.publish.strftime('%m'),
                              self.publish.strftime('%d'),
                              self.slug])
