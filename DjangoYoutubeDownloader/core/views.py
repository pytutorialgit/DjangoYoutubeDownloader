from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import TemplateView
#modules
import re 
import json
# Pytube library
from pytube import YouTube




class Index(TemplateView):
	template_name = "index.html"





def youtube_downloader(request):

	if request.method == "POST":
		#Video Url
		url = request.POST.get("url", None)
		try:
			# Download
			yt = YouTube(url).streams.first().download("media")
			# initialize the link
			down_link = re.findall('(/media/.+)', yt)[0]

			return render(request, "index.html", {"down_link":down_link})
		
		except:
			return render(request, "index.html", {"msg":"Something Wong"})

	return render(request, "index.html")







#index page
class Index2(TemplateView):
	template_name = "index2.html"



# Get info of video
def get_video_info(request):
	if request.method == "POST":
		res = {}
		data = json.loads(request.body)
		try:
			yt = YouTube(data["url"])
			res['title'] = yt.title
			res['img'] = yt.thumbnail_url
			qualities = re.findall('res="(.+?)"', str(yt.streams))
			res['qualities'] = list(set(qualities)) 
			return JsonResponse(res, status=200)
		except:
			return JsonResponse({"msg": "Something went wrong"}, status=500)

	return JsonResponse({"response": "Page Not Allowed"}, status=405)		

			
#Youtube Downloader
def youtube_Downloader2(request):

	if request.method == "POST":
		data = json.loads(request.body)
		url = data["url"]
		quality = data["q"]
		youtube = YouTube(url).streams.filter(res=quality).first().download("media")

		return JsonResponse({"down_link":re.findall('(/media/.+)', youtube)[0]})

	return JsonResponse({"response": "Page Not Allowed"}, status=405)