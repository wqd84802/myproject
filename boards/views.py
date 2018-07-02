from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from .models import Board, Topic, Post
from .forms import NewTopicForm
# Create your views here.
def home(request):
    boards = Board.objects.all()
    return render(request,'boards/home.html',{"boards":boards})

def board_topics(request, pk):
    board = get_object_or_404(Board, id=pk)
    return render(request, 'boards/topics.html', {'board': board})
# def new_topic(request, pk):
#     board = get_object_or_404(Board, pk=pk)
#     user = User.objects.first()  # TODO: get the currently logged in user
#     if request.method == 'POST':
#         form = NewTopicForm(request.POST)
#         if form.is_valid():
#             topic = form.save(commit=False)
#             topic.board = board
#             topic.starter = user
#             topic.save()
#             post = Post.objects.create(
#                 message=form.cleaned_data.get('message'),
#                 topic=topic,
#                 created_by=user
#             )
#             return redirect('board_topics', pk=board.pk)  # TODO: redirect to the created topic page
#     else:
#         form = NewTopicForm()
#     return render(request, 'boards/new_topic.html', {'board': board, 'form': form})
#
def new_topic(request, pk):
    board = get_object_or_404(Board, pk=pk)
    user = User.objects.first()
    if request.method == 'POST':
        form = NewTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.board = board
            topic.starter = user
            topic.save()
            post = Post.objects.create(
                message=form.cleaned_data.get('message'),
                topic = topic,
                created_by = user
            )
            return redirect('boards:board_topics', pk)
    else:
        form = NewTopicForm()
    return render(request, 'boards/new_topic.html', {'board':board, "form": form})
