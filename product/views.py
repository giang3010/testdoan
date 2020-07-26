from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
# Create your views here.
from product.models import CommentForm, Comment

def index(request):
    return HttpResponse("This is my product site")

def addcomment(request,id):
   url = request.META.get('HTTP_REFERER')
   if request.method == 'POST':  # check post
      form = CommentForm(request.POST)
      if form.is_valid():
         data = Comment()  # create relation with model
         data.comment = form.cleaned_data['comment']
         data.rate = form.cleaned_data['rate']
         data.product_id=id
         current_user= request.user
         data.user_id=current_user.id
         data.save()  # save data to table
         messages.success(request, "Bình luận của bạn đã được gửi, cảm ơn bạn đã quan tâm.")
         return HttpResponseRedirect(url)

   return HttpResponseRedirect(url)

def addreplycomment(request,id):
   url = request.META.get('HTTP_REFERER')
   if request.method == 'POST':  # check post
      form = CommentForm(request.POST)
      if form.is_valid():
         content = request.POST.get('comment')
         reply_id = request.POST.get('comment_id')
         comment_qs = None
         if reply_id:
            comment_qs = Comment.objects.get(id = reply_id)
         comment = Comment.objects.create(product_id=id, user_id= request.user,comment=content,reply=comment_qs,)
         comment.save()  # save data to table
         messages.success(request, "Bình luận của bạn đã được gửi.")
         return HttpResponseRedirect(url)

   return HttpResponseRedirect(url)