# Create your views here.
from django.contrib.auth.decorators import login_required, user_passes_test
#from myblog.blog.models import*
from django.template import Context, loader
from django.http import HttpResponse
from django.forms import ModelForm
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from models import Post, Comment
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.core.paginator import Paginator, InvalidPage, EmptyPage


def main(request):
    post_list = Post.objects.all()
    
    t=loader.get_template('blog/post_list.html')
    c=Context({'post_list':post_list,'user':request})
    #return HttpResponse(post_list)
    return HttpResponse(t.render(c))

class CommentForm(ModelForm):
    class Meta:
        model= Comment
        exclude=['post','author']

def add_comment(request, pk):
    """Add a new comment."""
    p = request.POST

    if p.has_key('body') and p['body']:
        author = 'Anonymous'
        if p['author']: author = p['author']
        comment = Comment(post=Post.objects.get(pk=pk))

        # save comment form
        cf = CommentForm(p, instance=comment)
        cf.fields['author'].required = False
        comment = cf.save(commit=False)

        # save comment instance
        comment.author = author
        notify = True
        if request.user.username == 'ak': notify = False
        comment.save(notify=notify)
    return HttpResponseRedirect(reverse('post_detail.html', args=[pk]))

def post(request, pk):
    """Single post with comments and a comment form."""
    post = Post.objects.get(pk=int(pk))
    comments = Comment.objects.filter(post=post)
    d = dict(post=post, comments=comments, form=CommentForm(), user=request.user)
    d.update(csrf(request))
    return render_to_response('post_detail.html', d)


def post_list(request):
    """Main listing."""
    posts = Post.objects.all().order_by("-created")
    paginator = Paginator(posts, 4)

    try: page = int(request.GET.get("page", '1'))
    except ValueError: page = 1

    try:
        posts = paginator.page(page)
    except (InvalidPage, EmptyPage):
        posts = paginator.page(paginator.num_pages)

    return render_to_response("blog/post_list.html", dict(posts=posts, user=request.user))

def post(request, pk):
    """Single post with comments and a comment form."""
    post = Post.objects.get(pk=int(pk))
    d = dict(post=post, user=request.user)
    return render_to_response('post_detail.html', d)

def see_post_details(user):
    return user.is_authenticated()

@csrf_exempt
@user_passes_test(see_post_details,login_url='/reg/sorry/')
#@login_required
def post_detail(request, id, showComments=False):
    post=Post.objects.get(pk=id)
    if request.method == 'POST':
        comment = Comment(post=post)
        comment.author=request.session['username']
        form = CommentForm(request.POST,instance=comment)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(request.path)
    else:
        form = CommentForm()

    me=post.comment_set.all()
    t=loader.get_template('blog/post_detail.html')
    
    if showComments is None:
        c=Context({'post':post,})
        return HttpResponse(t.render(c))
    else:
        c=Context({'post':post,'comments':me,'form' : form, 'user':request})
        return HttpResponse(t.render(c))
    
def post_search(request, term):
    post=Post.objects.filter(body__contains=term)
    t=loader.get_template('blog/post_search.html')
    c=Context({'post_list':post,'search':term,'user':request})
    return HttpResponse(t.render(c))

def home(request):
    t=loader.get_template('base.html')
    c=Context({'user':request})
    return HttpResponse(t.render(c))

@csrf_exempt
def edit_comment(request,id):
    comment=Comment.objects.get(pk=id)
    post_com=Post.objects.get(pk=comment.post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST,instance=comment)
        if form.is_valid():

            form.save()
        return HttpResponseRedirect(post_com.get_absolute_url())
    else:
        form = CommentForm(initial={'body':comment.body})
        #form.fields['author'].widget.attrs['readonly'] = True

    return render_to_response('blog/edit_comment.html',{'user':request,'form':form})


