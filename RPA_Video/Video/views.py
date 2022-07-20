from django.http import HttpResponse
from django.shortcuts import render
from .models import Video
from django.core.files.uploadedfile import InMemoryUploadedFile
import uuid
from moviepy.editor import VideoFileClip

CONFIG = { 'ALLOWED_TYPES': ['video/mp4', 'video/mkv'],
            'MAX_UPLOAD_SIZE': 1024 * 1024 * 1024, # 1GB = 1024 * 1024 * 1024 bytes
            'MAX_VIDEO_LENGTH': 60 * 10 # 10 minutes = 60 * 10 seconds

}

# Create your views here.


def upload(request):
    '''This function handles the upload of a video using '/upload' endpoint. It validates the constraints and then saves the video to the database.'''

    if request.method == 'POST':
        uploaded_video = request.FILES['video']
        msg, duration = validate_constraints(uploaded_video)
        if msg is None: # NO any constraints violation upload to DB
            video_title =  uploaded_video.name
            prev_name = str(uploaded_video.name)

            # generate a random name for the video
            uploaded_video.name = str(uuid.uuid4()) + '.' + prev_name.split('.')[-1]

            video_size = round(uploaded_video.size/(1024*1024),2)
            video = Video(title = video_title ,video=uploaded_video, size=video_size, length=duration)
            video.save()
            return HttpResponse('Video uploaded successfully')
        else:
            return HttpResponse(msg)
    return render(request,'index.html')

def validate_constraints(uploaded_video: InMemoryUploadedFile):
    '''This function validates the constraints of the video using validate function. It returns a tuple containing the error message if any validation fails and video duration.'''

    message = None
    clip = VideoFileClip(uploaded_video.temporary_file_path())
    duration = clip.duration
    size = uploaded_video.size
    content_type = uploaded_video.content_type

    message = validate(size,duration,content_type)
    del clip
    return message, duration


def list_videos(request):
    '''This function lists all the videos in the database or as per the search query.'''
    date = request.GET.get('date')
    size = request.GET.get('size')
    minSize = request.GET.get('minsize')
    maxSize = request.GET.get('maxsize')
    length = request.GET.get('length')
    minLength = request.GET.get('minlength')
    maxLength = request.GET.get('maxlength')
    title = request.GET.get('title')

    videos = Video.objects.all()

    if date is not None:
        videos = videos.filter(upload_date=date)
    if size is not None:
        size = float(size)
        videos = videos.filter(size=size)
    if minSize is not None:
        minSize = float(minSize)
        videos = videos.filter(size__gte = minSize)
    if maxSize is not None:
        maxSize = float(maxSize)
        videos = videos.filter(size__lte = maxSize)
    if length is not None:
        length = float(length)*60.0 
        videos = videos.filter(length=length)
    if minLength is not None:
        minLength = float(minLength)*60.0
        videos = videos.filter(length__gte = minLength)
    if maxLength is not None:
        maxLength = float(maxLength)*60.0
        videos = videos.filter(length__lte = maxLength)
    if title is not None:
        videos = videos.filter(title=title)
    return render(request,'videos.html',{'videos':videos})


def validate_compute_cost(request):
    '''This function validates the constraints of the video and computes cost of using service. It renders total cost if no constraints violation is found. Otherwise it rentders a string containing the error message.'''
    if request.method == 'POST':
        size = float(request.POST.get('size'))
        length = float(request.POST.get('length'))
        vid_type = str(request.POST.get('vid_type'))
        
        #Perform validation
        message = validate(size,length,vid_type)


        if message is None:
            cost = compute_cost(size,length)
            return HttpResponse('Total cost: $' + str(cost))
        else:
            return HttpResponse(message)

    return render(request,'compute_cost.html')

def compute_cost(size,length):
    '''This function computes the cost of using service. It returns the cost.'''
    cost = 0
    if size < 500.0:
        cost = 5.0
    else:
        cost = 12.5
    if length < (6 + (18.0/60.0)):
        cost += 12.5
    else:
        cost += 20.0
    return cost

def validate(size,length,vid_type):
    '''This function validates the constraints of the video. It returns None if no constraints violation is found. Otherwise it returns a string containing the error message.'''

    message = None
    if vid_type not in CONFIG['ALLOWED_TYPES']:
        message = 'Invalid file type. Allowed types: ' + str(CONFIG['ALLOWED_TYPES'])

    if size > CONFIG['MAX_UPLOAD_SIZE']:
        message = 'File size is too big. Max allowed size: ' + str(CONFIG['MAX_UPLOAD_SIZE']/(1024*1024*1024)) + ' GB'

    if length > CONFIG['MAX_VIDEO_LENGTH']:
        message = 'Video is too long. Max allowed length: ' + str(CONFIG['MAX_VIDEO_LENGTH']/60.0) + ' minutes'
    return message
