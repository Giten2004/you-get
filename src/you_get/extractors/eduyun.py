# -*- coding: utf-8 -*-
from ..common import *
from ..extractor import VideoExtractor

import urllib

__all__ = ['eduyun']

# class eduyun(VideoExtractor):
#     name = "eduyun"

#     stream_types = [
#         {'id': '360P', 'qualityType': '360p'}
#     ] 

#     def prepare(self, **kwargs):
#         # scrape the html
#         content = get_content(self.url)

#         '''
#             file: "https://d006.eduyun.cn/videoworks/mda-kihb02muhf976fcp/ykt_tbkt_hls_1080_7_CJ_1/video/找规律.m3u8",
#             image: "https://d006.eduyun.cn/videoworks/mda-kihb02muhf976fcp/ykt_tbkt_hls_1080_7_CJ_1/pic/找规律00001000.jpg"
#         '''
#         # extract title
#         self.title = match1(content, r'file: ".*/(.+)[\.]m3u8')
#         # extract m3u8 url
#         self.m3u8_url = match1(content, r'file: "([^"]+)"')

     

#             # size = float('inf')
#         container = 'mp4'
#         stream_id = "360P"
#         quality = "360p"
            
#         stream_data = dict(src=self.m3u8_url, size=0, container=container, quality=quality)
#         self.streams[stream_id] = stream_data


#     def extract(self, **kwargs):
#         pass

def eduyun_video_download(url, output_dir='.', merge=True, info_only=False, **kwargs):
    content = get_content(url)
    # extract title
    title = match1(content, r'file: ".*/(.+)[\.]m3u8')
    # extract m3u8 url
    m3u8_url = match1(content, r'file: "([^"]+)"')

    m3u8_url = urllib.parse.quote(m3u8_url, safe='/:?=&')

    headers = {
        "Referer": url
    }
    urls = general_m3u8_extractor(m3u8_url, headers)
    download_urls(urls, title, 'mp4', 0, output_dir=output_dir, refer=url, merge=merge, **kwargs)

site_info = "eduyun.cn"
download = eduyun_video_download
download_playlist = playlist_not_supported('eduyun')