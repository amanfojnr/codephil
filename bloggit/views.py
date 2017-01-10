from django.shortcuts import render, get_object_or_404
from .models import Post
from taggit.models import Tag
from django.db.models import Count

# Create your views here.

def post_list(request, tag_slug=None):
    """ list all posts with their tags in any """
    object_list = Post.published.all()
    tag = None

    # if there is a tag filter by tag
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        object_list = object_list.filter(tags__in=[tag])

    posts = object_list
    return render(request,
                    'bloggit/post/list.html',
                    {'posts' : posts,
                     'tag' : tag})

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                                   status='published',
                                   publish__year=year,
                                   publish__month=month,
                                   publish__day=day)

    # list of similar posts
    post_tags_ids = post.tags.values_list("id", flat=True)
    similar_posts = Post.published.filter(tags__in=post_tags_ids)\
    .exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags'))\
    .order_by('-same_tags','-publish')[:4]

    return render(request,
                    'bloggit/post/detail.html',
                    { 'post' : post,
                      'similar_posts' : similar_posts})
