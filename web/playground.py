from googleapiclient.discovery import build
import train
import pandas as pd

api_key = 'AIzaSyCNHCKp9krbNIR1Jc6fqovX5Ke4p4mpvxE'

def video_comments(video_link):
    result=video_link.index('=')+1
    video_id=video_link[result:]
    replies = []
    youtube = build('youtube', 'v3',developerKey=api_key)
    video_response=youtube.commentThreads().list(part='snippet,replies',videoId=video_id).execute()
 
    while video_response:
        for item in video_response['items']:
            comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
            replies.append(comment)
            replycount = item['snippet']['totalReplyCount']
            if replycount>0:
                for reply in item['replies']['comments']:
                    reply = reply['snippet']['textDisplay']
                    replies.append(reply)
        return replies
  
  
def analyze(videoLink):
  lists=[]
  lists=video_comments(videoLink)
  natija=[]
  natija.append(len(lists))
  pos=0
  neg=0
  for comment in lists:
    result=train.query(comment)
    for oneComment in result:
      if oneComment[0]['label']== "LABEL_1":
        pos+=1
      else:
        neg+=1
  natija.append(pos)
  natija.append(neg)
  return natija

nat=[]
nat=analyze("https://www.youtube.com/watch?v=XpaELzL4u38")
print(nat)
