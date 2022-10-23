from model import User, Disease, Post, Comment, db
from .utils import update_views
from flask import (Flask, render_template, request, flash, session, redirect, make_response, jsonify)
from datetime import datetime

def home(request):
    forums = Disease.objects.all()
    num_posts = Post.objects.all().count()
    num_users = User.objects.all().count()
    num_categories = forums.count()
    try:
        last_post = Post.objects.latest("date")
    except:
        last_post = []

    context = {
        "forums":forums,
        "num_posts":num_posts,
        "num_users":num_users,
        "num_categories":num_categories,
        "last_post":last_post,
        "title": "OZONE forum app"
    }
    return render(request, "forums.json", context)

def detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.user.is_authenticated:
        author = User.objects.get(user=request.user)
    
    if "comment-form" in request.POST:
        comment = request.POST.get("comment")
        new_comment, created = Comment.objects.get_or_create(user=author, content=comment)
        post.comments.add(new_comment.id)

    context = {
        "post":post,
        "title": "OZONE: "+post.title,
    }
    update_views(request, post)

    return render(request, "detail.json", context)

def posts(request, slug):
    category = get_object_or_404(Disease, slug=slug)
    posts = Post.objects.filter(approved=True, categories=category)
    paginator = Paginator(posts, 5)
    page = request.GET.get("page")
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages) 

    context = {
        "posts":posts,
        "forum": category,
        "title": "OZONE: Posts"
    }

    return render(request, "posts.json", context)

# @login_required
def create_post(request):
    """Create a Post"""

    user_id = session.get("user_id")

    disease_id = request.get_json().get("diseaseId")
    subject = request.get_json().get("subject")
    body = request.get_json().get("body")

    post = Post.create_post(disease_id, user_id, subject, body, date_created=datetime.now(), edit=False, date_edited=None, comments=[])

    db.session.add(post)
    db.session.commit()

    post_json = post.to_dict()

    return jsonify({"postAdded": post_json})



def latest_posts(request):
    posts = Post.objects.all().filter(approved=True)[:10]
    context = {
        "posts":posts,
        "title": "OZONE: Latest 10 Posts"
    }

    return render(request, "latest-posts.json", context)

def search_result(request):

    return render(request, "search.json")


def delete_post(request,id):
    post = Post.objects.get(id=id)
    if request.user.is_authenticated and request.user == post.author:
        Post.objects.filter(id=id).delete()
        return redirect('posts:mypost')
    return redirect('posts_errorpage.json')

def edit_post(request):
    post = Post.objects.get(id=id)
    if request.user.is_authenticated and request.user == post.author:
        if request.method == 'POST':
        form = PostCreateForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('posts:mypost')

        else:
            form = PostCreateForm(instance=post)

        args = {}
        args.update(csrf(request))
        args['form'] = form

    return render_to_response('posts/post_edit.json', args)

