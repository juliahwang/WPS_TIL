###### 20170531 [pair-programming]

## views.py

#### (1) post_add(request):

폼을 생성하지 않고 바로 데이터를 가져오는 방법에 대해서 배웠다. 

```python 
def post_add(request):
    if request.method == "GET":
        context = {
        	post: Post.objects.get(P)
        }
        return render(request, 'blog/post_add.html', context)
    elif request.method == 'POST':
        data = request.POST
        post = Post.objects.create(
            author=User.objects.first(),
            title=data['titlebox'],
            text=data['textbox'],
        )
        print('request: ', request.POST)
        return redirect('post_detail', pk=post.pk)
```