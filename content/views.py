from django.shortcuts import render
from rest_framework.views import APIView
from content.models import Feed


class Main(APIView):
    def get(self, request):
        feed_list = Feed.objects.all().order_by('-id')
        return render(request, 'Insta_Clone/main.html', context=dict(feed_list=feed_list))