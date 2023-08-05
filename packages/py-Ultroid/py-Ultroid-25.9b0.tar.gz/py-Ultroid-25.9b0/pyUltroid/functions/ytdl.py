import asyncio
import os
import time

from telethon.tl.types import DocumentAttributeAudio
from youtubesearchpython.__future__ import VideosSearch

from .all import progress

# search youtube


async def get_yt_link(query):
    vid_ser = VideosSearch(query, limit=1)
    res = await vid_ser.next()
    results = res["result"]
    for i in results:
        link = i["link"]
    return link


async def download_yt(xx, event, link, ytd):
    c_time = time.time()
    info = ytd.extract_info(link, False)
    duration = round(info["duration"] / 60)
    title = info["title"]
    singer = info["uploader"]
    try:
        ytd.download([link])
    except Exception as e:
        return await xx.edit(f"**ERROR**:\n`{e}`")
    path_to_dl = os.path.join(f"{info['id']}.mp3")
    await ultroid_bot.send_file(
        event.chat_id,
        file=path_to_dl,
        supports_streaming=True,
        attributes=[
            DocumentAttributeAudio(
                duration=int(duration),
                title=str(title),
                performer=str(singer),
            )
        ],
        progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
            progress(d, t, xx, c_time, "Uploading...", title)
        ),
    )
    os.remove(path_to_dl)
    await xx.delete()
