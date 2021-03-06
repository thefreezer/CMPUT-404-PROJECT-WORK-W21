from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponseBadRequest,HttpResponse
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status
from ..author_serializer import AuthorSerializer,PostSerializer,CommentSerializer,LikeSerializer
from ..models import Author, Post, Comment, Like
from ..formatters import post_formater, comment_formatter, like_formatter
import json





@api_view(["GET","POST"])
def general_post(request,author_id):
    if request.method == "POST":
        new_post = Post()
        json_data = request.data
        auth = get_object_or_404(Author, pk=author_id)
        new_post.author_id = auth
        for k,v in json_data.items():
            setattr(new_post, k, v)
        new_post.save()
        notify_friends(author_id)
        return HttpResponse(str(new_post.post_id),status=status.HTTP_200_OK)
    if request.method == "GET":
        response = {}
        response["type"] = "posts"
        response["items"] = []
        posts = Post.objects.filter(author_id=author_id)
        for i in range(0,len(posts)):
            new_formatted = post_formater(posts[i],True)
            response["items"].append(new_formatted)

        return JsonResponse(response, safe=False)
        
    


@api_view(["GET","POST","PUT","DELETE"])
def post_operation(request,author_id,post_id):
    if(request.method == "GET"):
        data = get_object_or_404(Post,pk=post_id)
        formatted = post_formater(data,True)
        return JsonResponse(formatted, safe=False)

    if(request.method == "POST"):
        post = get_object_or_404(Post,pk=post_id)
        json_data = request.data

        for k,v in json_data.items():
            setattr(post,k,v)
        post.save()
        return HttpResponse("post altered")
    if(request.method == "PUT"):
        pass
    if(request.method == "DELETE"):
        data = get_object_or_404(Post,pk=post_id)
        data.delete()
        return HttpResponse("post deleted",status=status.HTTP_200_OK)
    return HttpResponse("TODO general post operation")


@api_view(["GET"])
def get_post_likes(request, author_id, post_id):
    response = {}
    response["type"] = "liked"
    response["items"] = []
    likes = Like.objects.filter(author_id=author_id,post_id=post_id,comment_id=None)
    for i in range(0,len(likes)):
        new_like = like_formatter(likes[i],True)
        response["items"].append(new_like)
    return JsonResponse(response, safe=False)


@api_view(["GET", "POST"])
def general_comments(request, author_id, post_id):
    #GET
    #queryset
    #comment = Comments.objects.filter(auther_id=author_id,post_id=post_id)
    #for(i in range(0,len(comment)):
    #   Specific instance
    #   comment[i].comment_id
    #ser = CommentSerializer(comment,many=True)
    if(request.method == "GET"):
        comments = Comment.objects.filter(post_id=post_id)
        ser = CommentSerializer(comments,many=True)
        return JsonResponse(ser.data,safe=False)
    elif(request.method == "POST"):
        
        json_data = request.data
        commenter_id = json_data["author_id"]
        json_data.pop("author_id")
        commenter = get_object_or_404(Author,pk=commenter_id)
        post = get_object_or_404(Post,pk=post_id)
        new_comment = Comment(author_id=commenter,post_id=post)
        for k,v in json_data.items():
            setattr(new_comment, k, v)
        new_comment.save()
        post.commentCount +=1
        post.save()
        return HttpResponse(new_comment.comment_id)    
    return HttpResponse("TODO General comment return")


@api_view(["GET"])
def get_comment_likes(request, author_id, post_id, comment_id):
    response = {}
    response["type"] = "liked"
    response["items"] = []
    likes = Like.objects.filter(author_id=author_id,post_id=post_id,comment_id=comment_id)
    for i in range(0,len(likes)):
        new_like = like_formatter(likes[i],True)
        response["items"].append(new_like)
    return JsonResponse(response, safe=False)


#not sure if this path is even necessary
@api_view(["GET","POST","DELETE"])
def specific_comments(request, author_id, post_id, comment_id):
    if(request.method == "GET"):
        data = get_object_or_404(Comment,pk=comment_id)
        response = comment_formatter(data)
        return JsonResponse(response, safe=False)
    if(request.method == "POST"):
        json_data = request.data
        data = get_object_or_404(Comment,pk=comment_id)
        for k,v in json_data.items():
            setattr(data,k,v)
        data.save()
        return HttpResponse("comment updated")        

    if(request.method == "DELETE"):
        data = get_object_or_404(Comment,pk=comment_id)
        data.delete()
        return HttpResponse("comment deleted")

#later need to tie this all in with inbox
def notify_friends(author_id):
    pass
