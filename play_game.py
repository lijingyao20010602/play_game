# -*- coding: utf-8 -*-
import tkinter as tk

font = ("华文行楷", 17)   # 正常Label格式
key = False

def get_story():
    '''不要作弊哟'''
    fight_lose = {
        'text':'你勇敢地和邻居家里的蒙面歹徒搏斗，\n然而，你被制服了。',
    }

    road_lose = {
        'text':'你跑到大街上，拦下来一辆最近经过的车呼救：\n然而，车里的人却不是路人，而是另一个歹徒，\n你被制服了。',
    }

    neighbor = {
        'text':'你跑到邻居家，疯狂敲门。\n然而，打开门的却不是邻居，\n而是另一个蒙面歹徒，你选择：',
        'b1text': '和他搏斗',
        'b2text': '转身逃跑',
        'b1': fight_lose,
        'b2': road_lose,
        'key': 'lose'
    }

    over_door = {
        'text':'跑到室外后，你选择：',
        'b1text': '跑到邻居家呼救',
        'b2text': '跑到大街上呼救',
        'b1': neighbor,
        'b2': road_lose,
        'key': 'b2_lose'
    }

    window_lose = {
        'text':'你向窗外跑去，打算翻窗逃跑。\n突然，窗外出现另一个蒙面歹徒的脸，你被制服了'
    }

    tv_table = {
        'text':'你抱头蹲下，告诉他钱在电视柜里。他起身走向电视柜，你选择：',
        'b1text': '向窗户跑去，打算翻窗逃跑',
        'b2text': '向门口跑去',
        'b1': window_lose,
        'b2': over_door,
        'key': 'b1_lose'
    }

    opendoor = {
        'text':'你发现门外是一个遇到蒙面歹徒，他手里握着一把刀。\n你选择：',
        'b1text': '抱头蹲下',
        'b2text': '向窗户跑去，打算翻窗逃跑',
        'b1': tv_table,
        'b2': window_lose,
        'key': 'b2_lose'
    }

    win = {
        'text': '他吓得立马松开了手，刀扎在你的腿上，却没有鲜血流出。\n原来这是一把橡胶制成的假刀。两个蒙面歹徒拉下面罩，\n原来是你的两个小伙伴给你的一个小恶作剧，\n你把他们揍了一顿。'
    }

    door_lose = {
        'text': '打开门后，门口出现另一个蒙面歹徒在守株待兔，\n你被制服了。'
    }

    not_move = {
        'text':'不敢乱动，告诉他钱在电视柜里，他起身走向电视柜，你选择：',
        'b1text': '向门口跑去',
        'b2text': '向窗户跑去',
        'b1': door_lose,
        'b2': over_door,
        'key': 'b1_lose'
    }

    watch_tv = {
        'text':'突然，一个蒙面歹徒出现在你的身后，把刀架在了你的脖子上，你选择',
        'b1text': '不敢乱动',
        'b2text': '掏出口袋里的苹果刀和他搏斗',
        'b1': not_move,
        'b2': win,
        'key': 'b2_key'
    }

    close_tv = {
        'text':'突然，你听到了一阵细细簌簌的声音。\n回头一看，正好看到一个歹徒翻窗进入，你选择：',
        'b1text': '向门口跑去',
        'b2text': '先向门口跑去，当他追过来之后向绕向窗户',
        'b1': door_lose,
        'b2': over_door,
        'key': 'b1_lose'
    }

    closedoor = {
        'text':'门外敲了一会儿，敲门声就停下了。你选择：',
        'b1text': '继续看电视',
        'b2text': '关掉电视',
        'b1': watch_tv,
        'b2': close_tv,
        'key': None
    }

    basestory = {
        'text':'突然，你听见一阵敲门声，你选择：',
        'b1text': '开门',
        'b2text': '不开',
        'b1': opendoor,
        'b2': closedoor,
        'key': None
    }

    story = {
        'text':'背景：你家住在一楼，窗户在门的对侧。\n夜黑风高的一天，你独自在家看电视，\n突然感觉有些口渴，家里还有一些苹果和可乐，你选择：',
        'b1text': '吃苹果',
        'b2text': '喝可乐',
        'b1': basestory,
        'b2': basestory,
        'key': 'b1_getkey'
    }
    return story


class basedesk():
    def __init__(self, master):
        self.root = master
        self.root.config()
        self.root.title('大冒险')
        self.root.geometry('750x150')
        Init(self.root)        


class Init():
    def __init__(self, master):
        self.master = master
        self.master.config()
        self.face = tk.Frame(self.master,)
        self.face.pack()
        self.texts = get_story()
        global key
        key = False
        label = tk.Label(self.face, text="准备好开始一场惊险刺激的冒险了吗？", font=font).pack()
        b = tk.Button(self.face, text='开始冒险', command=self.begin)
        b.pack()
        
    def begin(self,):       
        self.face.destroy()
        BaseChoices(self.master, self.texts)      
 

class Lose():
    def __init__(self, master, texts):
        self.master = master
        self.master.config()
        self.face = tk.Frame(self.master,)
        self.face.pack()
        self.texts = texts
        print(self.texts['text'])
        tk.Label(self.face, text=self.texts['text'], font=font).pack()
        tk.Label(self.face, text="游戏失败，你输了", fg='red', font=font).pack()
        b = tk.Button(self.face, text='重新开始', command=self.begin)
        b.pack()
        
    def begin(self,):       
        self.face.destroy()
        Init(self.master)  


class Win():
    def __init__(self, master, texts):
        self.master = master
        self.master.config()
        self.face = tk.Frame(self.master,)
        self.face.pack()
        self.texts = texts
        print(self.texts['text'])
        tk.Label(self.face, text=self.texts['text'], font=font).pack()
        tk.Label(self.face, text="恭喜你通关！", fg='green', font=font).pack()
        b = tk.Button(self.face, text='再玩一次', command=self.begin)
        b.pack()
        
    def begin(self,):       
        self.face.destroy()
        Init(self.master)  


class BaseChoices():
    def __init__(self, master, texts):
        global key
        self.master = master
        self.master.config()
        self.face = tk.Frame(self.master,)
        self.face.pack()
        self.texts = texts
        print(self.texts['text'])
        tk.Label(self.face, text=self.texts['text'], font=font).pack()
        if self.texts['key'] != 'b1_key' or key:
            b1 = tk.Button(self.face, text=self.texts['b1text'], command=self.b1)
            b1.pack()
        if self.texts['key'] != 'b2_key' or key:
            b2 = tk.Button(self.face, text=self.texts['b2text'], command=self.b2)
            b2.pack()

    def b1(self):
        self.next('b1')
        
    def b2(self):
        self.next('b2')
    
    def next(self, s):
        self.face.destroy()
        if self.texts['key'] == '{}_lose'.format(s) or self.texts['key'] == 'lose':
            Lose(self.master, texts=self.texts[s])
        elif self.texts['key'] == '{}_key'.format(s):
            Win(self.master, texts=self.texts[s])
        else:
            if self.texts['key'] == '{}_getkey'.format(s):
                global key
                key = True
            BaseChoices(self.master, texts=self.texts[s])
        

if __name__ == '__main__':    
