from django.shortcuts import render

def index(request):
    return render(request, 'index.html', {'name' : 'hyeonah'})
# request에 맞게 그려주세요 index.html을
# 딕셔너리 name의 값을 hyeonah로 해주세요.
# 키 값 'name'이 변수로 사용됨