# -*- coding: utf-8 -*-

# Sample Python code for youtube.search.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/guides/code_samples#python

import os
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors


def youtube_search(keys):
    #getting the secret file
    script_path = os.path.abspath(__file__) 
    path_list = script_path.split(os.sep)
    script_directory = path_list[0:len(path_list)-1]
    rel_path = "client_secret.json"
    path = "/".join(script_directory) + "/" + rel_path
    
    scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]
    
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = path
    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_console()
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)
    videos = []
    for key in keys:
        request = youtube.search().list(
            part="id,snippet",
            maxResults=25,
            q=key,
            relevanceLanguage="en",
            safeSearch="moderate",
            type="video",
            videoCaption="closedCaption"
            )
        response = request.execute()
        #print(response)
        #add to list of videos
        for item in response['items']:
            videos.append(item['id']['videoId'])

    # place videos into file
    with open('vidoes.txt','w') as f:
        f.write('\n'.join(videos))
keys = ['apple','surfing'] #fill in search keys to test
youtube_search(keys)
