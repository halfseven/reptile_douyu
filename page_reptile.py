import json
import requests


url_next = 'https://www.douyu.com/gapi/rkc/directory/0_0/'  # 数据请求页面
start_headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36',
}
start_page = 1
end_page = 5
all_room_list = []  # 所有房间信息列表
room_type_list = []
for i in range(start_page, end_page + 1):
    text_i = str(i)
    next_url = url_next + text_i  # 拼接完整的请求url
    print(next_url)
    #         path = '/gapi/rkc/directory/0_0/'+text_i
    page_text = requests.get(url=next_url, headers=start_headers).text
    dic_page_info = json.loads(page_text)

    dic_data_info = dic_page_info['data']
    dic_room_info = dic_data_info['rl']
    # print(dic_room_info)
    for i in dic_room_info:
        room_num = i['rid']
        room_title = i['rn']
        room_name = i['nn']
        room_type = i['c2name']
        room_rank = i['ol']
        dic_room = {
            '房间号码': room_num,
            '房间标题': room_title,
            '直播类型': room_type,
            '主播名': room_name,
            '热度': room_rank
        }
        room_type_list.append(room_type)
        all_room_list.append(dic_room)
    file = open('douyu.txt', 'w+')
    file.write(str(room_type_list))
    file.close()

