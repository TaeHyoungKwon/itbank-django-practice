import json
from django.shortcuts import render


def test(request):
    return render(request, 'testapp/index.html')


def tag_example(request, tag_id=None):
    data = {
        1: {'tag': 'a', 'example': '<a href="#">링크</a>'},
        2: {'tag': 'b', 'example': '<b>볼드</b>'},
        3: {'tag': 'li', 'example': '<li>목록</li>'},
    }
    print(data.get(tag_id))
    return render(request, 'testapp/tag.html', data.get(tag_id))


def test_file_io(request, text=None):

    fo = open("/Users/thkwon/workspace/develop/Django/myweb/src/testapp/a.json",
              "r", encoding="utf-8")
    data = json.loads(fo.read())
    return render(request, 'testapp/test_file_io.html', data)


def html_link(request):
    data = {"data": ["test", "tag/1", "test_file_io"]}
    return render(request, 'testapp/html_link.html', data)
