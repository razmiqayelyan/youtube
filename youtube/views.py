# from django.shortcuts import render
# from django.http import HttpResponse
# from pytube import YouTube
# # Create your views here.

# def index(request):
# 	return render(request, 'index.html')

# def download(request):
# 	if request.method == 'POST':
# 		video_url = request.POST['video_url']
# 	# video_url = 'https://www.youtube.com/watch?v=4AJIYTM9JDw&list=RD4AJIYTM9JDw&start_radio=1'
# 		yt = YouTube(video_url)
# 		thumbnail_url = yt.thumbnail_url
# 		title = yt.title
# 		length = yt.length
# 		desc = yt.description
# 		view = yt.views
# 		rating = yt.rating
# 		age_restricted = yt.age_restricted

		

# 	return render(request, 'index.html', {'title':title,
# 			'thumbnail_url':thumbnail_url,
# 			'video_url':video_url})

# def downloading(request):
# 	if request.method == POST:
# 		formatRadio = request.POST['formatRadio']
# 	return render(request, 'index.html')

  
from django.shortcuts import render, redirect
from django.http import HttpResponse
from pytube import YouTube

# Create your views here.
def index(request):
	return redirect('home')

def greetings(request):
	res = render(request,'index.html')
	return res

def download(request):
    if request.method == 'POST':
        video_url=request.POST['video_url']
        # video_url = 'https://www.youtube.com/watch?v=LIlmQ8xhRRI'
        yt = YouTube(video_url)
        thumbnail_url = yt.thumbnail_url
        title = yt.title
        length = yt.length
        desc = yt.description
        view = yt.views
        rating = yt.rating
        age_restricted = yt.age_restricted
        res = render(request,'index.html',{"title":title,"thumbnail_url":thumbnail_url,"video_url":video_url})
        return res
    else:
        res = render(request,'index.html')
        return res

def downloading(request):
	if request.method == 'POST':
		formatRadio = request.POST['formatRadio']
		
		video_url_d = request.POST['video_url_d']
		# print(formatRadio)
		# print(qualityRadio)   
		yt = YouTube(video_url_d)
		print(yt)
		print("Downloading start ....")
		if formatRadio == "audio":
			yt.streams.filter(type = formatRadio).last().download()
		else:
			yt.streams.filter(type = formatRadio,resolution='720p').first().download()
		print("Downloding completed")
	res = render(request,'index.html',{"msg":"downloading completed"})
	return res