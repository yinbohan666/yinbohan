import streamlit as st
from PIL import Image
from PIL import ImageEnhance
import time

page = st.sidebar.radio('我的首页',["我的推荐","图片处理","智慧词典","留言区","应用集"])

def page_1():
    st.write(':one::dark_sunglasses:动漫推荐:dark_sunglasses:')
    with st.expander('国漫推荐'):
        st.write("《完美世界》《剑来》")
        audio_file = open('知我.mp3','rb')
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format='audio/mp3')
    with st.expander('日漫推荐'):
        st.write("《咒术回战》《进击的巨人》")
    st.write("----------------------------------------------------------------------------------")
    st.write(':two::movie_camera:电影推荐:movie_camera:')
    with st.expander('高分电影'):
        st.write("《星际穿越》《绿皮书》")
    with st.expander('经典电影'):
        st.write("《唐伯虎点秋香》《肖申克的救赎》")
    st.write("----------------------------------------------------------------------------------")    
    st.write(':three::musical_note:音乐推荐:musical_note:')
    with st.expander('纯音乐推荐'):
        st.write("《A Little Story》《One Sweetest》")
    with st.expander('电音推荐'):
        st.write("《Nevada》《China-X》")
    st.write("----------------------------------------------------------------------------------")    
    st.write(':four::computer:游戏推荐:computer:')
    with st.expander('端游：P社'):
        st.write("《钢铁雄心4》《群星》")
    with st.expander('手游'):
        st.write("《原神》《我的世界》")

def img_change(img, rc, gc, bc):
    width, height = img.size
    img_array = img.load()
    for i in range(width):
        for j in range(height):
            r = img_array[i,j][rc]
            g = img_array[i,j][gc]
            b = img_array[i,j][bc]
            img_array[i,j] = (r,g,b)
    return img


    
def page_2():
    st.write(':computer:图片处理:computer:')
    uploaded_file = st.file_uploader('上传图片',type = ['png', 'jpg', 'jpeg']) 
    if uploaded_file:
        # tab1,tab2,tab3,tab4,tab5 = st.tabs(["原图","改色1","改色2","亮度","对比度"])
        col1, col2 = st.columns([3, 2])
        with col1:
            img = Image.open(uploaded_file)
            st.image(img)
        with col2:
            ti = st.toggle('原图')
            ch = st.toggle('改色1')
            bw = st.toggle('改色2')
            br = st.toggle('提高亮度')
            co = st.toggle('增强对比度')
            
        # ex = st.toggle('开关')
        # if ex:
        #     st.write('开启')
        # else:
        #     st.write('关闭')
        # ti = st.toggle('原图')
        # ch = st.toggle('改色1')
        # bw = st.toggle('改色2')
        # br = st.toggle('提高亮度')
        # co = st.toggle('增强对比度')
        message = ''
        b = st.button('开始处理')
        if b:
            if ti:
                message += '原图'
                tab1 = st.tabs(['原图'])
                img = Image.open(uploaded_file)
                st.image(img)
            if ch:
                message += '改色'
                tab2 = st.tabs(['改色'])
                img = Image.open(uploaded_file)
                st.image(img_change(img,1,2,0))
            if bw:
                message += '改色'
                tab3 = st.tabs(['改色'])
                img = Image.open(uploaded_file)
                st.image(img_change(img,1,0,2))
            if br:
                message += '提高亮度'
                tab4 = st.tabs(['亮度'])
                img = Image.open(uploaded_file)
                l = ImageEnhance.Brightness(img)
                st.image(l.enhance(2.25))
            if co:
                message += '增强对比度'
                tab5 = st.tabs(['对比度'])
                img = Image.open(uploaded_file)
                e = ImageEnhance.Contrast(img)
                st.image(e.enhance(2))
            
        st.write('你将会得到一张', message, '的图片')
        # img = Image.open(uploaded_file)
       
        # with tab1:
        #     img = Image.open(uploaded_file)
        #     st.image(img)
        # with tab2:
        #     img = Image.open(uploaded_file)
        #     st.image(img_change(img,1,2,0))
        # with tab3:
        #     img = Image.open(uploaded_file)
        #     st.image(img_change(img,1,0,2))
        # with tab4:
        #     img = Image.open(uploaded_file)
        #     l = ImageEnhance.Brightness(img)
        #     st.image(l.enhance(2.25))
        # with tab5:
        #     img = Image.open(uploaded_file)
        #     e = ImageEnhance.Contrast(img)
        #     st.image(e.enhance(2))
        # st.write(uploaded_file.name)
        # st.write(uploaded_file.size)
        # st.write(uploaded_file.type)


        
def page_3():
    st.write("智慧词典")
    if 'counter' not in st.session_state:
        st.session_state.counter = 0
    with open('words_space.txt','r',encoding='utf-8') as f:
        words_list = f.read().split('\n')
    for i in range(len(words_list)):
        words_list[i] = words_list[i].split('#')
    words_dict = {}
    for i in words_list:
        words_dict[i[1]] = [int(i[0]),i[2]]
        
    word = st.text_input("请输入要查询的单词")
    roading = st.progress(0, '开始加载')
    for i in range(1, 101, 1):
        time.sleep(0.02)
        roading.progress(i, '正在加载'+str(i)+'%')
    roading.progress(100, '加载完毕！')
    if word in words_dict:
        st.session_state.counter +=1
        st.write(words_dict[word][1])
        st.write(f"查询次数{st.session_state.counter}")
        st.snow()
    else:
        st.balloons()
        st.write("很抱歉，查询不到该单词")
    print(words_dict)
    


def page_4():
    st.write("留言区")
    with open('leave_messages.txt','r',encoding='utf-8') as f:
        messages_list = f.read().split('\n')
    for i in range(len(messages_list)):
        messages_list[i] = messages_list[i].split('#')
    for i in messages_list:
        if i[1] == '阿短':
            with st.chat_message('🙍‍♂️'):
                st.write(i[1],':',i[2])
        if i[1] == '编程猫':
            with st.chat_message('😺'):
                st.write(i[1],':',i[2])
    name = st.selectbox('我是...',['阿短','编程猫'])
    new_message = st.text_input('想要留言的内容')
    if st.button('点我留言'):
        messages_list.append([str(int(messages_list[-1][0])+1),name,new_message])
        with open('leave_messages.txt','w',encoding='utf-8') as f:
            message = ''
            for i in messages_list:
                message += i[0] + '#' + i[1] + '#' + i[2] +'\n'
            message = message[:-1]
            f.write(message)
                


def page_5():
    st.write("应用集")
    st.write('除了本主站之外，我还将我的有趣内容分享在了其他网站中')
    go = st.selectbox('你的支持是我最大的动力，去支持一下up吧！', ['百度一下', '央视网', '我的bilibili', '腾讯视频', '饿了么'])
    if go == '百度一下':
        st.link_button('百度一下，你就知道', 'https://www.baidu.com/')
    elif go == '央视网':
        st.link_button('央视网_世界就在眼前 ', 'https://www.cctv.com/')
    elif go == '我的bilibili':
        st.link_button('哔哩哔哩 (゜-゜)つロ 干杯~-bilibili ', 'https://www.bilibili.com/')
    elif go == '腾讯视频':
        st.link_button('腾讯视频-中国领先的在线视频媒体平台,海量高清视频在线观看', 'https://v.qq.com/')
    elif go == '饿了么':
        st.link_button('饿了就点饿了么', 'https://www.ele.me/')





if page == "我的推荐":
    page_1()
elif page == "图片处理":
    page_2()
elif page == "智慧词典":
    page_3()
elif page == "留言区":
    page_4()
elif page == "应用集":
    page_5()