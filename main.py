from pytube import Playlist, YouTube
from alive_progress import alive_bar
import os

def getUrlsPlaylist(url):
  try:
    pl = Playlist(url)
    return pl
  except Exception as e:    
    print(f'An error occurred while getting the list:\n{e}')
    return


def downloadAudio():
  url = str(input('Enter the url of the playlist: '))
  print('\n')
  links = getUrlsPlaylist(url)
  steps = links.length

  with alive_bar(steps) as bar:
    for link in links:
      yt = YouTube(link)
      audio = yt.streams.filter(only_audio=True).first()
      outFile = audio.download()
      base, ext = os.path.splitext(outFile)
      newFile = base+'.mp3'
      os.rename(outFile, newFile)
      bar()
  print(f'\nPlaylist downloaded successfully')
    

downloadAudio()
