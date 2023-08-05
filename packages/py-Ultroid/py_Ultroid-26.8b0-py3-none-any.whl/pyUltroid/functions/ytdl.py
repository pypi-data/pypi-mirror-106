import os
import time

from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
from telethon.tl.types import DocumentAttributeAudio, DocumentAttributeVideo
from youtubesearchpython.__future__ import VideosSearch

from .all import uploader

# search youtube


async def get_yt_link(query):
    vid_ser = VideosSearch(query, limit=1)
    res = await vid_ser.next()
    results = res["result"]
    for i in results:
        link = i["link"]
    return link


async def download_yt(xx, event, link, ytd):
    st = time.time()
    info = ytd.extract_info(link, False)
    duration = info["duration"]
    title = info["title"]
    singer = info["uploader"]
    try:
        ytd.download([link])
    except Exception as e:
        return await xx.edit(f"**ERROR**:\n`{e}`")
    dir = os.listdir()
    if f"{info['id']}.mp3" in dir:
        kk = f"{info['id']}.mp3"
        if f"{kk}.jpg" in dir:
            thumb = f"{kk}.jpg"
        elif f"{kk}.webp" in dir:
            thumb = f"{kk}.webp"
        else:
            thumb = "resources/extras/ultroid.jpg"
        caption = f"`{title}`\n`From YouTubeMusic`"
    elif f"{info['id']}.mp4" in dir:
        kk = f"{info['id']}.mp4"
        tm = f"{info['id']}"
        if f"{tm}.jpg" in dir:
            thumb = f"{tm}.jpg"
        elif f"{tm}.webp" in dir:
            thumb = f"{tm}.webp"
        else:
            thumb = "resources/extras/ultroid.jpg"
        caption = f"`{title}`\n`From YouTube`"
    else:
        return
    res = await uploader(kk, kk, st, xx, "Uploading...")
    metadata = extractMetadata(createParser(res.name))
    wi = 512
    hi = 512
    duration = 0
    if metadata.has("width"):
        wi = metadata.get("width")
    if metadata.has("height"):
        hi = metadata.get("height")
    if metadata.has("duration"):
        duration = metadata.get("duration").seconds
    if metadata.has("artist"):
        metadata.get("artist")
    if kk.endswith(".mp4"):
        await event.client.send_file(
            event.chat_id,
            file=res,
            caption=caption,
            supports_streaming=True,
            thumb=thumb,
            attributes=[
                DocumentAttributeVideo(
                    duration=duration,
                    w=wi,
                    h=hi,
                )
            ],
        )
    else:
        await event.client.send_file(
            event.chat_id,
            file=res,
            caption=caption,
            supports_streaming=True,
            thumb=thumb,
            attributes=[
                DocumentAttributeAudio(
                    duration=duration,
                    title=title,
                    performer=singer,
                )
            ],
        )
    os.remove(kk)
    os.remove(thumb)
    await xx.delete()
