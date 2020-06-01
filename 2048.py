# curses用来在终端上显示图形界面
import curses

# random模块用来生成随机数
from random import randrange, choice

# collections 提供了一个字典的子类 defaultdict。可以指定key值不存在时，value的默认值
from collections import defaultdict

# 有效输入键是最常见的W（上），A(左），S（下），D（右），R（重置），Q（退出），这里要考虑到大写键开启的情况，
# 获得有效键值列表
actions = ['Up', 'Left', 'Down', 'Right', 'Restart', 'Exit']

# ord（）函数以一个字符作为参数，返回参数对应的ASCII数值，便于和后面捕捉的键位关联
letter_codes = [ord(ch) for ch in 'WASDRQwasdrq']

actions_dict = dict(zip(letter_codes, actions * 2))


def main(stdscr):
    def init():
        # 初始化游戏棋盘
        return 'Game'

    def not_game(state):
        """
        画出GameOver或者Win的界面
        读取用户输入得到的action，判断是重启游戏还是结束游戏
        :param state:
        :return:
        """
        # 默认是当前状态，没有'Restart'或'Exit'行为就会一直保持当前状态
        responses = defaultdict(lambda: state)
        # 新建键值对，将行为和状态对应
        responses['Restart'], responses['Exit'] = 'Init', 'Exit'
        return responses[action]

    def game():
        # 画出当前棋盘状态
        # 读取用户输入得到aciton

        if action == 'Restart':
            return 'Init'
        if action == 'Exit':
            return 'Exit'
            # if 成功移动了一步:
            if 游戏胜利了:
                return ‘Win’
                if 游戏失败了:
                    return 'Gameover'

            return 'Gme'

        state_actions = {'Init': init,
                         'Win': lambda: not_game('Win'),
                         'Gameover': lambda: not_game('Gameover'),
                         'Game': game
                         }

        state = 'Init'

        # 状态机开始循环
        while state != 'Exit':
            state = state_actions[state]()

        def get_user_action(keyboard):
            char = 'N'
            while char not in actions_dict:
                # 返回按下键位的ASCII码值
                char = keyboard.getch()
            # 返回输入键位对应的行为
            return actions_dict[char]

        class GameField(object):
            def __init__(self, height=4, width=4, win=2048):
                self.height = height
                self.width = width
                self.win_value = 2048
                self.score = 0
                self.highscore = 0
                self.reset()

        def spawn(self):
            #从100中取一个随机数，如果这个随机数大于89，new_element等于4，否则等于2
            new_element=4 if randrange(100)>89 else 2
            #得到一个随机空白位置的元组坐标
            (i,j)=choice([(i,j) for i in range(self.width) for j in range(self.height) if self.field[i][j]==0])
            self.field[i][j]=new_element

        def reset(self):
            #更新分数
            if self.score>self.highscore:
                self.highscore=self.score
            self.score=0
            #初始化游戏开始界面
            self.field=[[0 for i in range(self.width)] for j in range(self.height)]
            self.spawn()
            self.spawn()

         def move_row_left(row):
             def tighten(row):

                 #把零散的非零单元挤到一块儿
                 #先将非零的元素全拿出来加入到新列表
                 new_row=[i for i in row if i != 0]
                 #按照原列表的大小，给新列表后面补零
                 new_row+=[0 for i in range(len(row) -len(new_row))]
                 return new_row


