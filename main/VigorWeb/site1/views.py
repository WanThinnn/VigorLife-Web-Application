from .models import NewsItem
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.mail import send_mail
from VigorWeb.settings import EMAIL_HOST_USER
import random
import json
from django.db.models import Sum
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
import feedparser
from bs4 import BeautifulSoup
from .forms import *
import base64
import requests
from django.views import View
from django.conf import settings

# Function to translate text using Google Translate API
def translate_text(text, target_language='vi'):
    api_key = 'AIzaSyAXguVX7Uu2lhlFfIaEVP6Wd6nSIiYbkUg'
    url = f'https://translation.googleapis.com/language/translate/v2?key={api_key}'
    data = {
        'q': text,
        'source': 'en',
        'target': target_language,
        'format': 'text'
    }
    response = requests.post(url, data=data)
    result = response.json()
    return result['data']['translations'][0]['translatedText']

class ImageUploadView(View):
    template_name = 'site1/upload.html'

    def post(self, request, *args, **kwargs):
        if 'image' in request.FILES:
            image_file = request.FILES['image']
            image_data = base64.b64encode(image_file.read()).decode('utf-8')

            vision_api_key = 'AIzaSyAXguVX7Uu2lhlFfIaEVP6Wd6nSIiYbkUg'
            vision_url = f'https://vision.googleapis.com/v1/images:annotate?key={vision_api_key}'

            request_payload = {
                "requests": [
                    {
                        "image": {"content": image_data},
                        "features": [{"type": "LABEL_DETECTION"}],
                        "imageContext": {"languageHints": ["vi"]}
                    }
                ]
            }

            response = requests.post(vision_url, json=request_payload)
            response_data = response.json()

            if 'responses' in response_data and 'labelAnnotations' in response_data['responses'][0]:
                labels = response_data['responses'][0]['labelAnnotations']
                translated_labels = [translate_text(label['description']) for label in labels]
            else:
                translated_labels = []

            return render(request, self.template_name, {'labels': translated_labels})

        return render(request, self.template_name)

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

# Create your views here.


@csrf_exempt
def search(request):
    if request.method == "POST":
        searched = request.POST["searched"]
        keys = Fruit.objects.filter(name__icontains=searched)
        key1 = Food.objects.filter(name__icontains=searched)
        key2 = NewsItem.objects.filter(title__icontains=searched)
    return render(request, 'site1/search.html', {"searched": searched, "keys":  keys, "key1": key1, "key2": key2})


def autosuggest(request):
    print(request.GET)
    query_original = request.GET.get('term')
    queryset = Fruit.objects.filter(name__icontains=query_original)
    queryset1 = Food.objects.filter(name__icontains=query_original)
    queryset2 = NewsItem.objects.filter(title__icontains=query_original)
    mylist = []
    mylist += [x.name for x in queryset]
    mylist += [x.name for x in queryset1]
    mylist += [x.title for x in queryset2]
    return JsonResponse(mylist, safe=False)


def home(request):
    return render(request, 'site1/home.html')

def verify(request):
    return render(request, 'site1/verify.html')

def introduction(request):
    return render(request, 'site1/introduction.html')


def heallthinfo(request):
    return render(request, 'site1/heallthinfo.html')

def forgotpass(request):
     return render(request, 'site1/forgot.html')
def changepass(request):
     return render(request, 'site1/changepass.html')
class PostListView(ListView):
    queryset = Post.objects.all().order_by('-date')
    template_name = 'site1/blog.html'
    context_object_name = 'Posts'
    paginate_by = 10


class PostDetailView(DetailView):
    model = Post
    template_name = 'site1/post.html'


def post(request, pk, title):
    post = get_object_or_404(Post, pk=pk, title=title)
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST, author=request.user, post=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path)
    return render(request, "site1/post.html", {"post": post, "form": form})


def reply_cmt(request, pk, title):
    post = get_object_or_404(Post, pk=pk, title=title)
    form = RelyCommentForm()
    if request.method == "POST":
        author_id = request.POST.get('author')
        comment_id = request.POST.get('comment')
        comment = get_object_or_404(Comment, pk=comment_id, author=author_id)
        form = RelyCommentForm(
            request.POST, author=request.user, comment=comment)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path)
    return render(request, "site1/post.html", {"post": post, "form": form})


def write_blog(request):
    if request.method == 'POST':
        blog_form = BlogForm(request.POST, author=request.user)
        image_form = ImageUploadForm(request.POST, request.FILES)
        if blog_form.is_valid() and image_form.is_valid():
            post = blog_form.save()
            # Lấy danh sách hình ảnh từ form tải lên
            images = request.FILES.getlist('images')
            # Lấy danh sách tiêu đề từ form
            titles = request.POST.getlist('title')
            for image, title in zip(images, titles):
                # Lưu hình ảnh vào cơ sở dữ liệu
                Image.objects.create(image=image, post=post, title=title)
            return redirect('post', pk=post.pk, title=post.title)
    else:
        blog_form = BlogForm(author=request.user)
        image_form = ImageUploadForm()
    return render(request, 'site1/write_blog.html', {'blog_form': blog_form, 'image_form': image_form})


def loseweight(request):
    return render(request, 'site1/loseweight_exercise.html')


def calo(request):
    import json
    import requests
    if request.method == 'POST':
        query = request.POST['query']
        api_url = 'https://api.api-ninjas.com/v1/nutrition?query='
        api_request = requests.get(
            api_url + query, headers={'X-Api-Key': '9nIgsnVfHFA7sVgBPbho6Q==soVB8dv5tTBqJpfH'})
        try:
            api = json.loads(api_request.content)
            print(api_request.content)

            if isinstance(api, list) and len(api) > 0:
                calo = api[0].get('calories', 0)
                jog = calo / 378 * 60
                yoga = calo / 223 * 60
                gym = calo / 483 * 60
                walk = calo / 294 * 60

                context = {
                    'api': api,
                    'jog': jog,
                    'yoga': yoga,
                    'gym': gym,
                    'walk': walk,
                }
            else:
                context = {
                    'api': "oops! There was an error"
                }
        except Exception as e:
            context = {
                'api': "oops! There was an error"
            }
            print(e)
        return render(request, 'site1/calo.html', context)
    else:
        return render(request, 'site1/calo.html', {'query': 'Enter a valid query'})


def tools(request):
    return render(request, 'site1/tools.html')


def verifyOTP(request):
    if request.method == 'POST':
        userOTP = request.POST.get('otp')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 == password2:
            form = User(username=username, email=email, first_name=first_name,
                        last_name=last_name, password=password1)
            form.save()

        print("OTP: ", userOTP)

    return JsonResponse({'data': 'Hello'}, status=200)


def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        user_name = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        form = UserCreationForm(request.POST)
        if form.is_valid():
            #form.save()
            otp = random.randint(100000, 999999)
            subject = "[Vigor Life] - Đăng ký thành viên"
            message = f"""
            Xin chào,

            Chúng tôi nhận được yêu cầu tạo tài khoản mới cho email này của bạn trên trang web vigorlife.id.vn. Để hoàn tất quá trình này, vui lòng nhập mã xác thực sau:

            Mã xác thực của bạn là: {otp}

            Nếu bạn không yêu cầu tạo tài khoản hoặc không nhớ đến yêu cầu này, vui lòng bỏ qua email này. 
            Nếu bạn cần thêm sự trợ giúp hoặc có bất kỳ câu hỏi nào, vui lòng liên hệ với chúng tôi qua email này. 

            Trân trọng,
            Vigor Life Team.
            """
            send_mail(subject, message, settings.EMAIL_HOST_USER, [email], fail_silently=True)
            messages.success(request, 'OTP has been sent to your email')
            return render(request, 'site1/verify.html', {'otp': otp, 'first_name': first_name, 'last_name': last_name, 'email': email, 'username': user_name, 'password1': password1, 'password2': password2})
        else:
            print("Form error: ", form.errors)
            messages.error(request, form.errors)
    else:
        form = RegistrationForm()
    context = {'form': form}
    return render(request, 'site1/register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or Password is incorrect')

    context = {}
    return render(request, 'site1/login.html', context)


def logoutPage(request):
    logout(request)
    return redirect('login')


# def fruit(request, name, calo):
#     fruit = Fruit.objects.filter(name=name, calories=calo).first()  # Sử dụng first() thay vì get()
#     return render(request, "site1/fruits.html", {"fruit": fruit})


class FruitListView(ListView):
    model = Fruit
    template_name = 'site1/fruits.html'
    context_object_name = 'fruits'

    def get_queryset(self):
        classification = self.kwargs.get('classification')
        if classification:
            return Fruit.objects.filter(classification=classification).order_by('-name')
        return Fruit.objects.all().order_by('-name')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['classification'] = self.kwargs.get('classification')
        return context


def ListFruit(request):
    return render(request, 'site1/list_fruits.html')


def FruitsPage(request, classification, name):
    # Bạn có thể xử lý classification và name ở đây nếu cần
    fruit = get_object_or_404(Fruit, name=name, classification=classification)
    context = {
        'classification': classification,
        'name': name,
        'fruit': fruit,
        # Thêm các dữ liệu cần thiết vào context nếu cần
    }
    return render(request, 'site1/fruit_in_page.html', context)


class FoodListView(ListView):
    model = Food
    template_name = 'site1/foods.html'
    context_object_name = 'foods'

    def get_queryset(self):
        classification = self.kwargs.get('classification')
        if classification:
            return Food.objects.filter(classification=classification).order_by('-name')
        return Food.objects.all().order_by('-name')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['classification'] = self.kwargs.get('classification')
        return context


def ListFoods(request):
    return render(request, 'site1/list_foods.html')

def account(request):
    return render(request, 'site1/account.html')


def FoodsPage(request, classification, name):
    food = get_object_or_404(Food, name=name, classification=classification)
    context = {
        'classification': classification,
        'name': name,
        'food': food,
    }
    return render(request, 'site1/food_in_page.html', context)


def ListNews(request):
    return render(request, 'site1/list_news.html')

# def News(request, type):
#     rss_feed_url = ''
#     if type == 'suc-khoe':
#         rss_feed_url = "https://vnexpress.net/rss/suc-khoe.rss"
#     elif type == 'the-thao':
#         rss_feed_url = "https://vnexpress.net/rss/the-thao.rss"

#     items_rss = []
#     if rss_feed_url:
#         feed = feedparser.parse(rss_feed_url)
#         for item in feed.entries:
#             title = item.get("title")
#             pub_date = item.get("published")
#             link = item.get("link")
#             description = item.get("summary")
#             description_soup = BeautifulSoup(description, 'html.parser')
#             description_text = description_soup.get_text()
#             img_tag = description_soup.find("img")
#             img_src = './static/site1/images/news_img.jpg'
#             if img_tag:
#                 img_src = img_tag["src"]

#             item = {
#                 "title": title,
#                 "pub_date": pub_date,
#                 "link": link,
#                 "description_text": description_text,
#                 "image": img_src,
#             }
#             items_rss.append(item)

#     return render(request, 'site1/news.html', {"items_rss": items_rss, "type": type})


def News(request, type):
    rss_feed_url = ''
    if type == 'suc-khoe':
        rss_feed_url = "https://vnexpress.net/rss/suc-khoe.rss"
    elif type == 'the-thao':
        rss_feed_url = "https://vnexpress.net/rss/the-thao.rss"
    elif type == 'khoa-hoc':
        rss_feed_url = "https://vnexpress.net/rss/khoa-hoc.rss"

    items_rss = []
    if rss_feed_url:
        feed = feedparser.parse(rss_feed_url)
        for item in feed.entries:
            title = item.get("title")
            pub_date = item.get("published")
            link = item.get("link")
            description = item.get("summary")
            description_soup = BeautifulSoup(description, 'html.parser')
            description_text = description_soup.get_text()
            img_tag = description_soup.find("img")
            img_src = './static/site1/images/news_img.jpg'
            if img_tag:
                img_src = img_tag["src"]

            # Convert pub_date to Django compatible format
            if pub_date:
                try:
                    parsed_date = datetime.strptime(pub_date, "%a, %d %b %Y %H:%M:%S %z")
                    pub_date = parsed_date.strftime("%Y-%m-%d %H:%M:%S%z")
                except ValueError as e:
                    # Handle the exception or set pub_date to None
                    pub_date = None

            # Check if the item already exists in the database
            if not NewsItem.objects.filter(link=link).exists():
                # Save the new item to the database
                news_item = NewsItem(
                    title=title,
                    pub_date=pub_date,
                    link=link,
                    description_text=description_text,
                    image=img_src,
                    type=type
                )
                news_item.save()

            item_data = {
                "title": title,
                "pub_date": pub_date,
                "link": link,
                "description_text": description_text,
                "image": img_src,
            }
            items_rss.append(item_data)

    return render(request, 'site1/news.html', {"items_rss": items_rss, "type": type})

