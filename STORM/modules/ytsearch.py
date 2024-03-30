from pyrogram import Client
from googleapiclient.discovery import build

def youtube_search(api_key, query, max_results=5):
    youtube = build('youtube', 'v3', developerKey=api_key)
    request = youtube.search().list(
        part='snippet',
        q=query,
        maxResults=max_results
    )
    response = request.execute()
    return response['items']
@Client.on_message()
async def handle_message(client, message):
    if message.text.startswith('.ytsearch'):
        query = message.text.replace('.ytsearch', '').strip()
        api_key = 'AIzaSyAlKB8YvGpSbsHX7pwlDi3CVMODUqHFGkw'
        results = youtube_search(api_key, query)
        for result in results:
            video_id = result['id']['videoId']
            title = result['snippet']['title']
            description = result['snippet']['description']
            video_url = f"https://www.youtube.com/watch?v={video_id}"
            response_text = f"<b>{title}</b>\n{description}\n{video_url}"
            await client.send_message(message.chat.id, response_text, parse_mode='html')
