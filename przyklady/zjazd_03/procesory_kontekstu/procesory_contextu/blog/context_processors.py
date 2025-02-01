from .models import Post, PostStatus

def post_counts(request):
    if request.user.is_superuser:
        draft_posts = Post.objects.filter(status=PostStatus.DRAFT).count()
        published_posts = Post.objects.filter(status=PostStatus.PUBLISHED).count()
        return {"draft_posts": draft_posts, "published_posts": published_posts}
    return {}