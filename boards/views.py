from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from . models import Board, Topic, Post
# Create your views here.
def home(request):
    boards = Board.objects.all()
    return render(request,'boards/home.html',{"boards":boards})

def board_topics(request, pk):
    board = get_object_or_404(Board, id=pk)
    return render(request, 'boards/topics.html', {'board': board})

def new_topic(request, pk):
    board = get_object_or_404(Board, pk=pk)
    if request.method == "POST":
        subject = request.POST['subject']
        message = request.POST['message']

        user = User.objects.first()
        print(user)
        topic = Topic.objects.create(subject=subject,
                                     board=board,
                                     starter=user
                                     )

        post = Post.objects.create(message=message,
                                   topic=topic,
                                   created_by=user
                                   )

        return redirect('boards:board_topics',pk=board.pk)
    return render(request, 'boards/new_topic.html', {'board': board})
