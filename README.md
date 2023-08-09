# Bilibili video crawler
This is a crawler for Bilibili videos. Given an `aid` or a `bvid`, it can download the video to your PC.

## Requirments
```txt
requests
```

## Usage
By entering `python main.py` in Powershell or cmd, you can start this program.

If you want to download 720P60 high frame rate, 1080P HD and above definition videos or member videos, please login to bilibili on the web side to get your SESSDATA and enter it first. Skipping this step means that you will be using the preset SESSDATA (the author's SESSDATA that I used during the test), which [may] lead to the inability to download high-definition videos.

If you don't know how to find your SESSDATA, press F12 or Fn+F12 in your browser and log in to Bilibili. Look for the following fields in the developer tools:
```json
    "cookies": "SESSDATA=xxx"
```
Whether you key in your own SESSDATA or not, you can enter the AV number or BV number of the video to start the download.

Thereafter you can choose the definition you want, and if the video is split into episodes, all the episodes will be downloaded. The video(s) will be stored in the same directory as main.py

Enjoy!
