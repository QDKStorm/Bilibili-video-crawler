import requests

info_url='https://api.bilibili.com/x/web-interface/view'
videostream_url='https://api.bilibili.com/x/player/playurl'
SESSDATA='1e4c46c5%2C1707042377%2C2c5dc%2A82MBcoBVB8Q4YF82sdnVa0Lczx9GUecVk2AipPF9azuocofUxl8PrDiui4dm7lazzKe-kRegAANgA'
qn=0

def parse_videostream_url(avid,cids,qn):
    rets=[]
    for cid in cids:
        params={
            'avid':avid,
            'cid':cid,
            'qn':qn,
        }
        headers={
            "User-Agent":'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
            "Accept":'*/*',
            'Accept-Encoding':'gzip, deflate, br',
            'Connection':'keep-alive',
            'Cookie':f'SESSDATA={SESSDATA}',
        }
        response=requests.get(videostream_url,params=params,headers=headers)
        rets.append(response.json()['data']['durl'][0]['url'])
    # print(response.json()['data']['support_formats'])
    return rets

def download_from_urls(videourls,video_title):
    headers={
        "User-Agent":'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
        "Accept":'*/*',
        'Accept-Encoding':'gzip, deflate, br',
        'Connection':'keep-alive',
        'Cookie':f'SESSDATA={SESSDATA}',
        'Referer':'https://api.bilibili.com/x/web-interface/view?aid=170001',
    }
    video_title=video_title.replace('/','')
    video_title=video_title.replace('\\','')
    video_title=video_title.replace(':','')
    video_title=video_title.replace('*','')
    video_title=video_title.replace('?','')
    video_title=video_title.replace('"','')
    video_title=video_title.replace('<','')
    video_title=video_title.replace('>','')
    video_title=video_title.replace('|','')
    cnt=0
    if(len(videourls)==1):
        response=requests.get(videourls[0],headers=headers)
        with open(f'{video_title}.mp4','wb') as f:
            f.write(response.content)
    else:
        for videourl in videourls:
            response=requests.get(videourl,headers=headers)
            cnt=cnt+1
            with open(f'{video_title}_{cnt}.mp4','wb') as f:
                f.write(response.content)

if __name__ =='__main__':
    print('')
    print('如欲下载720P60 高帧率、1080P 高清及以上清晰度的视频，请在网页端登录bilibili后获取您的SESSDATA并在此输入，跳过此步骤意味着您将使用预设的SESSDATA，这【有可能】导致无法下载高清晰度的视频。')
    print('输入SESSDATA时请不要输入“SESSDATA=”，请直接输入“SESSDATA=”后的内容并回车')
    print('')
    print('随后您可选择输入以下任意一项来开始下载：')
    print('    视频AV号，如：av170001 或 170001')
    print('    视频BV号，如：BV17x411w7KC 或 17x411w7KC')
    params={}
    while True:
        start=input()
        if start=='':
            continue
        elif len(start)>20:
            SESSDATA=start
            print('\033[1;32;40mSESSDATA已设定，请继续输入视频AV号或BV号\033[0m')
        elif (start[0]=='a' and start[1]=='v') or (start.isdigit()):
            if start[0]=='a' and start[1]=='v':
                params={
                    "aid":start[2:],
                }
            else:
                params={
                    "aid":start,
                }
            break
        else:
            if(start[0]=='B' and start[1]=='V'):
                params={
                    "bvid":start[2:],
                }
            else:
                params={
                    "bvid":start,
                }
            break
    try:
        response=requests.get(info_url,params=params)
        aid=response.json()['data']['aid']
        print('\033[1;32;40m已找到指定的视频\033[0m')
    except:
        print('\033[1;31;40m或许您的输入有误... \033[0m')
        exit()
    cids=[]
    for i in response.json()['data']['pages']:
        cids.append(i['cid'])
    video_title=response.json()['data']['title']
    params={
        "avid":aid,
        "cid":cids[0],
        "qn":16,
    }
    headers={
        "User-Agent":'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
        "Accept":'*/*',
        'Accept-Encoding':'gzip, deflate, br',
        'Connection':'keep-alive',
        'Cookie':f'SESSDATA={SESSDATA}',
    }
    response=requests.get(videostream_url,params=params,headers=headers)
    print('以下是本视频支持的视频清晰度及其对应的代码：')
    for i in response.json()['data']['support_formats']:
        print(i['quality'],': ',i['new_description'])
    try:
        qn=int(input('请输入您需要的清晰度对应的代码：'))
    except:
        print('\033[1;31;40m或许您的输入有误... \033[0m')
        exit()
    for i in range(0,5):
        videourls=parse_videostream_url(aid,cids,qn)
        if videourls != []:
            break
    if(videourls == []):
        print('出现了迷之错误')
    else:
        print('\033[1;32;40mDownloading...\033[0m')
        download_from_urls(videourls,video_title)

# 单P 1pt4y1T7V3
# 多P 1ps411V79B
# 多P 1SW4y1v7WN