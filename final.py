import pygame
import sys
import random
import time
from pygame.locals import MOUSEBUTTONDOWN, QUIT, KEYDOWN, K_ESCAPE,RESIZABLE

pygame.init()
screen_size = (1000,600)
screen_width, screen_height = screen_size
screen = pygame.display.set_mode(screen_size,RESIZABLE,32)
pygame.display.set_caption('Lonely Majong')

t1_image_filename = 'Image/MJt1.gif'
t2_image_filename = 'Image/MJt2.gif'
t3_image_filename = 'Image/MJt3.gif'
t4_image_filename = 'Image/MJt4.gif'
t5_image_filename = 'Image/MJt5.gif'
t6_image_filename = 'Image/MJt6.gif'
t7_image_filename = 'Image/MJt7.gif'
t8_image_filename = 'Image/MJt8.gif'
t9_image_filename = 'Image/MJt9.gif'

s1_image_filename = 'Image/MJs1.gif'
s2_image_filename = 'Image/MJs2.gif'
s3_image_filename = 'Image/MJs3.gif'
s4_image_filename = 'Image/MJs4.gif'
s5_image_filename = 'Image/MJs5.gif'
s6_image_filename = 'Image/MJs6.gif'
s7_image_filename = 'Image/MJs7.gif'
s8_image_filename = 'Image/MJs8.gif'
s9_image_filename = 'Image/MJs9.gif'

w1_image_filename = 'Image/MJw1.gif'
w2_image_filename = 'Image/MJw2.gif'
w3_image_filename = 'Image/MJw3.gif'
w4_image_filename = 'Image/MJw4.gif'
w5_image_filename = 'Image/MJw5.gif'
w6_image_filename = 'Image/MJw6.gif'
w7_image_filename = 'Image/MJw7.gif'
w8_image_filename = 'Image/MJw8.gif'
w9_image_filename = 'Image/MJw9.gif'

f1_image_filename = 'Image/MJf1.gif'
f2_image_filename = 'Image/MJf2.gif'
f3_image_filename = 'Image/MJf3.gif'
f4_image_filename = 'Image/MJf4.gif'

u1_image_filename = 'Image/MJd1.gif'
u2_image_filename = 'Image/MJd2.gif'
u3_image_filename = 'Image/MJd3.gif'

mjb_image_filename = 'Image/mjb.gif'
hu_image_filename = 'Image/hu.gif'
liu_image_filename = 'Image/liu.gif'
g_image_filename = 'Image/liu.gif'

background = pygame.image.load('Image/Nostalgy.gif').convert()
t1 = pygame.image.load(t1_image_filename).convert()
t2 = pygame.image.load(t2_image_filename).convert()
t3 = pygame.image.load(t3_image_filename).convert()
t4 = pygame.image.load(t4_image_filename).convert()
t5 = pygame.image.load(t5_image_filename).convert()
t6 = pygame.image.load(t6_image_filename).convert()
t7 = pygame.image.load(t7_image_filename).convert()
t8 = pygame.image.load(t8_image_filename).convert()
t9 = pygame.image.load(t9_image_filename).convert()

s1 = pygame.image.load(s1_image_filename).convert()
s2 = pygame.image.load(s2_image_filename).convert()
s3 = pygame.image.load(s3_image_filename).convert()
s4 = pygame.image.load(s4_image_filename).convert()
s5 = pygame.image.load(s5_image_filename).convert()
s6 = pygame.image.load(s6_image_filename).convert()
s7 = pygame.image.load(s7_image_filename).convert()
s8 = pygame.image.load(s8_image_filename).convert()
s9 = pygame.image.load(s9_image_filename).convert()

w1 = pygame.image.load(w1_image_filename).convert()
w2 = pygame.image.load(w2_image_filename).convert()
w3 = pygame.image.load(w3_image_filename).convert()
w4 = pygame.image.load(w4_image_filename).convert()
w5 = pygame.image.load(w5_image_filename).convert()
w6 = pygame.image.load(w6_image_filename).convert()
w7 = pygame.image.load(w7_image_filename).convert()
w8 = pygame.image.load(w8_image_filename).convert()
w9 = pygame.image.load(w9_image_filename).convert()

f1 = pygame.image.load(f1_image_filename).convert()
f2 = pygame.image.load(f2_image_filename).convert()
f3 = pygame.image.load(f3_image_filename).convert()
f4 = pygame.image.load(f4_image_filename).convert()

u1 = pygame.image.load(u1_image_filename).convert()
u2 = pygame.image.load(u2_image_filename).convert()
u3 = pygame.image.load(u3_image_filename).convert()

mjbk   = pygame.image.load(mjb_image_filename).convert()
hu_button = pygame.image.load(hu_image_filename).convert()
eat = pygame.image.load('Image/eat.gif').convert()
pon = pygame.image.load('Image/pon.gif').convert()
no = pygame.image.load('Image/no.gif').convert()
liu = pygame.image.load('Image/liu.gif').convert()
g = pygame.image.load('Image/g.gif').convert()
hu = pygame.image.load('Image/huresult.gif').convert()

def index_to_pic(index):
    if index == 1:
        return w1
    elif index == 2:
        return w2
    elif index == 3:
        return w3
    elif index == 4:
        return w4
    elif index == 5:
        return w5
    elif index == 6:
        return w6
    elif index == 7:
        return w7
    elif index == 8:
        return w8
    elif index == 9:
        return w9
    elif index == 11:
        return s1
    elif index == 12:
        return s2
    elif index == 13:
        return s3
    elif index == 14:
        return s4
    elif index == 15:
        return s5
    elif index == 16:
        return s6
    elif index == 17:
        return s7
    elif index == 18:
        return s8
    elif index == 19:
        return s9
    elif index == 21:
        return t1
    elif index == 22:
        return t2
    elif index == 23:
        return t3
    elif index == 24:
        return t4
    elif index == 25:
        return t5
    elif index == 26:
        return t6
    elif index == 27:
        return t7
    elif index == 28:
        return t8
    elif index == 29:
        return t9
    elif index == 31:
        return f1
    elif index == 33:
        return f2
    elif index == 35:
        return f3
    elif index == 37:
        return f4
    elif index == 41:
        return u1
    elif index == 43:
        return u2
    elif index == 45:
        return u3
    elif index == 51:
        return mjbk
    elif index == 52:
        return hu_button
    elif index == 53:
        return pon
    elif index == 54:
        return eat
    elif index ==55:
        return no
    elif index == 57:
        return liu
    elif index == 59:
        return g
    elif index == 61:
        return hu
    
for y in range(0, screen_height, background.get_height()):     #background
        for x in range(0, screen_width, background.get_width()):
            screen.blit(background, (x, y))
for x in range(240,700,mjbk.get_width()-6):
    screen.blit(mjbk, (x,50))

all_card = list(range(1,10))*4+list(range(11,20))*4+list(range(21,30))*4+list(range(31,38,2))*4+list(range(41,46,2))*4
handcard = []
drop_handcard = [] 
r_drop_handcard = []
r_handcard = []
cover_card = all_card[:]
#print(cover_card)
waste_card = []         # NO waste at first

check_eat = 0 
check_pong = 0
r_check_eat = 0 
r_check_pong = 0

win_flag = 0
win =0
flag = 0
mj_round = 0
t=16   # chance to pick card

def display_mj():
    x = 220
    y = 500
    for i in handcard:
        screen.blit(index_to_pic(i), (x,y))
        x += 36
        
def display_front_mj():
    x_f = 220
    y_f = 425
    t = 1
    for i in drop_handcard:
        screen.blit(index_to_pic(i),(x_f,y_f))
        if t%3 != 0:
            x_f += 36
        else:
            x_f += 50
        t += 1
        
def display_rfront_mj():
    xf = 240
    yf = 110
    t = 1
    for i in r_drop_handcard:
        screen.blit(index_to_pic(i),(xf,yf))
        if t%3 != 0:
            xf += 36
        else:
            xf += 50
        t += 1
        
def display_waste_mj():
    x = 270
    y = 200
    if len(waste_card) >= 1:
        for i in waste_card:
            screen.blit(index_to_pic(i),(x,y))
            x+=36
            if x > 750:
                x = 270
                y += 50

def display_all():
    for y in range(0, screen_height, background.get_height()):     #background
        for x in range(0, screen_width, background.get_width()):
            screen.blit(background, (x, y))
    for x in range(240,700,mjbk.get_width()-6):
        screen.blit(mjbk, (x,50))
    
    display_mj()
    display_front_mj()
    display_rfront_mj()
    display_waste_mj()
    pygame.display.update()
        
# create handcard(hdcd)
def create_new_hdcd(card_length,cover_card,handcard,r_handcard):
    for i in range(card_length):
        new_card = random.choice(cover_card)
        cover_card.remove(new_card)
        handcard.append(new_card) 
    handcard = sorted(handcard)
    for i in range(card_length):
        new_card = random.choice(cover_card)
        cover_card.remove(new_card)
        r_handcard.append(new_card) 
    r_handcard = sorted(r_handcard)
    return r_handcard,handcard
    
# robot get cover_card
def rob_get_cover(cover_card,r_handcard):
    global r_check_eat
    global r_check_pong
    if r_check_eat == 0 and r_check_pong == 0:
        r_new_card = random.choice(cover_card)#隨機選一張加入對家手牌
        cover_card.remove(r_new_card)
        r_handcard.append(r_new_card)
        r_handcard.sort()#整理

    return r_handcard,cover_card
        

# robot throw card
def robot_throw(waste_card,r_handcard):
    global r_check_pong
    global r_check_eat
    r_check_pong =0
    r_check_eat = 0
    throw_l = r_handcard[:]
    keep_l = []   
    for i in range(len(r_handcard)-1):
        if r_handcard[i] == r_handcard[i+1] and r_handcard[i] not in keep_l :
            keep_l.append(r_handcard[i])
            keep_l.append(r_handcard[i+1])
            throw_l.remove(r_handcard[i])
            throw_l.remove(r_handcard[i+1])
        elif r_handcard[i] == r_handcard[i+1] and r_handcard[i] in keep_l :
            keep_l.append(r_handcard[i+1])
            throw_l.remove(r_handcard[i+1])
        elif r_handcard[i]+1 == r_handcard[i+1] and r_handcard[i] not in keep_l :
            keep_l.append(r_handcard[i])
            keep_l.append(r_handcard[i+1])
            throw_l.remove(r_handcard[i])
            throw_l.remove(r_handcard[i+1])
        elif r_handcard[i]+1 == r_handcard[i+1] and r_handcard[i] in keep_l :
            keep_l.append(r_handcard[i+1])
            throw_l.remove(r_handcard[i+1])
    if len(throw_l)>0:
        throw = random.choice(throw_l)
        r_handcard.remove(throw)
        waste_card.append(throw)
    else:
        throw = random.choice(r_handcard)
        r_handcard.remove(throw)
        waste_card.append(throw)
    return waste_card, r_handcard

#robot pong:
def robot_check_pong(waste_card,r_drop_handcard,r_handcard):
    global r_check_pong
    if len(waste_card) != 0:
        p_throw =waste_card[-1]
        a = r_handcard[:]
        for i in range(len(r_handcard)):
            #如果手牌中有對方剛打出來的牌，而且牌數 >2
            if r_handcard[i] == p_throw and a.count(p_throw)>=2:
                pong = p_throw
                waste_card.remove(pong)
                a.remove(pong)
                a.remove(pong)
                r_drop_handcard+[pong]*3
                r_check_pong = 1
        r_handcard = a[:]
    display_all()

def robot_check_eat(waste_card,r_drop_handcard,r_handcard):
    global r_check_pong
    global r_check_eat
    
    if len(waste_card) !=0:
        p_throw = waste_card[-1]
        if (r_check_pong == 0) and (p_throw+1 in r_handcard) and (p_throw+2 in r_handcard):#吃(後兩張)
            eat = p_throw
            waste_card.remove(eat)
            r_handcard.remove(eat+1)
            r_handcard.remove(eat+2)
            for i in range(3):
                r_drop_handcard.append(eat+i)
            r_check_eat = 1
        elif (r_check_pong == 0)  and (p_throw-1 in r_handcard) and (p_throw+1 in r_handcard):#吃(中洞)
            eat = p_throw
            waste_card.remove(eat)
            r_handcard.remove(eat-1)
            r_handcard.remove(eat+1)
            for i in range(3):
                r_drop_handcard.append(eat+i-1)
            r_check_eat = 1
        elif (r_check_pong == 0) and (p_throw-1 in r_handcard) and (p_throw-2 in r_handcard):#吃(前兩張)
            eat = p_throw
            waste_card.remove(eat)
            r_handcard.remove(eat-1)
            r_handcard.remove(eat-2)
            for i in range(3):
                r_drop_handcard.append(eat+i-2)
            r_check_eat = 1
    
    display_all()

def pla_check_hepai(handcard,waste_card=0):
    global win
    global win_flag
    if waste_card != 0 :
        if hepai(handcard +[waste_card[-1]]):
            win = 1
            win_flag = 1
    else:
        if hepai(handcard):
            win=1
            win_flag = 1
            

def pla_check_pong(waste_card,handcard,drop_handcard):
    global check_pong
    flag = 0
    r_throw = waste_card[-1]
    for pi in range(len(handcard)):#檢查能否"碰"
        if handcard[pi] == waste_card[-1] and handcard.count(r_throw)>=2 :
            screen.blit(index_to_pic(53),(800,500))
            screen.blit(index_to_pic(55),(900,500))
            pygame.display.update()
            wait = True
            while wait:
                for e in pygame.event.get(): 
                     #如果要碰就會將牌 移入drop_card中
                    if e.type == pygame.MOUSEBUTTONDOWN and (850>pygame.mouse.get_pos()[0]>800) and (550>pygame.mouse.get_pos()[1]>500):
                        check_pong = 1
                        waste_card.remove(r_throw)
                        handcard.remove(r_throw)
                        handcard.remove(r_throw)
                        for i in range(3):
                            drop_handcard.append(r_throw)
                        flag=1
                        wait = False
                        display_all()
                        break
                        
                    elif e.type == pygame.MOUSEBUTTONDOWN and (950>pygame.mouse.get_pos()[0]>900) and (550>pygame.mouse.get_pos()[1]>500):
                        flag=1
                        wait = False
                        display_all()
                        break
                        
            if flag == 1:
                flag = 0
                break
    
    display_all()

def pla_check_eat(waste_card,handcard,drop_handcard):
    #檢查能否吃(前面兩個或後面兩個或中洞)
    global check_pong
    global check_eat
    flag =0
    r_throw = waste_card[-1]
    c = handcard[:]
    if (check_pong==0):
        if ((waste_card[-1]+1) in handcard and (waste_card[-1]+2) in handcard) or ((waste_card[-1]-1) in handcard and (waste_card[-1]+1) in handcard) or ((waste_card[-1]-1) in handcard and (waste_card[-1]-2) in handcard):
            screen.blit(index_to_pic(54),(800,500))# 吃的圖示在(800,500)
            screen.blit(index_to_pic(55),(900,500))# 否的圖示在(900,500)
            pygame.display.update()
            wait1 = True
            while wait1:
                for e in pygame.event.get():
                    #如果按在吃附近
                    if e.type ==pygame.MOUSEBUTTONDOWN and (850>pygame.mouse.get_pos()[0]>800) and (550>pygame.mouse.get_pos()[1]>500):
                        
                        screen.blit(background,(800,500))
                        screen.blit(background,(900,500))
                        pygame.display.update()
                        time.sleep(0.5)
                        if (r_throw+1 in handcard and r_throw+2 in handcard):
                        #===這邊要出現「你要吃的是 index_to_pic(r_throw+1) ,index_to_pic(r_throw+2)嗎?」===
                            screen.blit(index_to_pic(54),(800,500))# 吃的圖示在(800,500)
                            screen.blit(index_to_pic(55),(900,500))# 否的圖示在(900,500)
                            screen.blit(index_to_pic(r_throw+1),(800,420))
                            screen.blit(index_to_pic(r_throw+2),(850,420))
                            pygame.display.update()
                            wait2 =True
                            while wait2:
                                for e in pygame.event.get():
                                    #吃第二遍(右吃)
                                    if e.type ==pygame.MOUSEBUTTONDOWN and (850>pygame.mouse.get_pos()[0]>800) and (550>pygame.mouse.get_pos()[1]>500):
                                        eat = waste_card[-1]
                                        waste_card.remove(eat)
                                        handcard.remove(eat+1)
                                        handcard.remove(eat+2)
                                        for i in range(3):
                                            drop_handcard.append(eat+i)
                                        check_eat = 1
                                        wait1 = False
                                        wait2 = False
                                        flag = 1
                                        display_all()
                                    elif e.type ==pygame.MOUSEBUTTONDOWN and (950>pygame.mouse.get_pos()[0]>900) and (550>pygame.mouse.get_pos()[1]>500):
                                        check_eat = 0
                                        wait1 = False
                                        wait2 = False
                                        display_all()
                        if flag == 1:
                            break
                            
                        display_all()
                        if (r_throw-1 in handcard and r_throw-2 in handcard) and check_eat ==0:
                            time.sleep(0.5)
                        #===這邊要出現「你要吃的是 index_to_pic(r_throw+1) ,index_to_pic(r_throw+2)嗎?」===
                            screen.blit(index_to_pic(54),(800,500))# 吃的圖示在(800,500)
                            screen.blit(index_to_pic(55),(900,500))# 否的圖示在(900,500)
                            screen.blit(index_to_pic(r_throw-1),(800,420))
                            screen.blit(index_to_pic(r_throw-2),(850,420))
                            pygame.display.update()
                            wait3 =True
                            while wait3:
                                for e in pygame.event.get():
                                    #吃第二遍(左吃)
                                    if e.type ==pygame.MOUSEBUTTONDOWN and (850>pygame.mouse.get_pos()[0]>800) and (550>pygame.mouse.get_pos()[1]>500):
                                        eat = waste_card[-1]
                                        waste_card.remove(eat)
                                        handcard.remove(eat-1)
                                        handcard.remove(eat-2)
                                        for i in range(3):
                                            drop_handcard.append(eat+i-2)
                                        check_eat = 1
                                        wait1 = False
                                        wait3 = False
                                        flag = 1
                                        display_all()
                                        
                                    elif e.type ==pygame.MOUSEBUTTONDOWN and (950>pygame.mouse.get_pos()[0]>900) and (550>pygame.mouse.get_pos()[1]>500):
                                        check_eat =0
                                        wait1 = False
                                        wait3 = False
                                        display_all()
                        if flag ==1:
                            break
                                        
                        display_all()
                        if (r_throw-1 in handcard and r_throw+1 in handcard) and check_eat ==0:
                            time.sleep(0.5)
                        #===這邊要出現「你要吃的是 index_to_pic(r_throw+1) ,index_to_pic(r_throw+2)嗎?」===
                            screen.blit(index_to_pic(54),(800,500))# 吃的圖示在(800,500)
                            screen.blit(index_to_pic(55),(900,500))# 否的圖示在(900,500)
                            screen.blit(index_to_pic(r_throw-1),(800,420))
                            screen.blit(index_to_pic(r_throw+1),(850,420))
                            pygame.display.update()
                            wait4 =True
                            while wait4:
                                for e in pygame.event.get():
                                    #吃第二遍(中吃)
                                    if e.type ==pygame.MOUSEBUTTONDOWN and (850>pygame.mouse.get_pos()[0]>800) and (550>pygame.mouse.get_pos()[1]>500):
                                        eat = waste_card[-1]
                                        waste_card.remove(eat)
                                        handcard.remove(eat-1)
                                        handcard.remove(eat+1)
                                        for i in range(3):
                                            drop_handcard.append(eat+i-1)
                                        check_eat = 1
                                        wait1 = False
                                        wait4 = False
                                        flag = 1
                                        display_all()
                                    elif e.type ==pygame.MOUSEBUTTONDOWN and (950>pygame.mouse.get_pos()[0]>900) and (550>pygame.mouse.get_pos()[1]>500):
                                        wait1 = False
                                        wait4 = False
                                        display_all()
                        
                        display_all()
                        if flag == 1:
                            break
                                
                                    
                                    
                    elif e.type ==pygame.MOUSEBUTTONDOWN and (950>pygame.mouse.get_pos()[0]>900) and (550>pygame.mouse.get_pos()[1]>500):
                        check_eat = 0
                        wait1 = False
                        display_all()
                        

#player get cover_card
def pla_get_cover(cover_card,handcard):
    global check_eat
    global check_pong
    if check_eat == 0 and check_pong == 0:
        new_card = random.choice(cover_card)#隨機選一張加入對家手牌
        cover_card.remove(new_card)
        
        handcard.append(new_card)
        handcard.sort()#整理
        print('自己抽牌')
        display_all()
    else:
        check_pong =0
        check_eat = 0
        display_all()
            
def pla_select_and_throw(handcard,waste_card):
    wait =True
    while wait:
        for e in pygame.event.get():
            if (e.type == pygame.MOUSEBUTTONDOWN) and (724 > pygame.mouse.get_pos()[0] > 220) and (553 > pygame.mouse.get_pos()[1] > 500):
                i = (pygame.mouse.get_pos()[0]-220)//36 
                pick = handcard[i]
                handcard.remove(pick)
                waste_card.append(pick)
                print(pick)
                pygame.display.update()
                wait =False
                
def hepai(a:list):
    '''Judge cards hepai. For excample:a=[1,2,3,4,4]

a=list,萬：1-9，條：11

-19，筒：21-29，東南西北風：31,33,35,37，中發白：41,43,45。'''
    a=sorted(a)
    #print(a)

    #牌面檢查，是否屬於本規定的範圍内。
    #all_card=list(range(1,10))+list(range(11,20))+list(range(21,30))+list(range(31,38,2))+list(range(41,46,2))
    #print(all_card)
    for x in set(a):
        if a.count(x)>4:#某張牌的數量超過4，不正確。
            return False
        if x not in all_card:
            print('參數錯誤：输入的牌型{}不在範圍内。'.format(x))
            return False

    #牌數检查。
    if len(a)%3!=2:
        print('和牌失败：牌數不正確。')
        return False
    
    #是否有對子檢查。
    double=[]
    for x in set(a):
        if a.count(x)>=2:
            double.append(x)
    #print(double)
    if len(double)==0:
        #print('和牌失敗：無對子')
        return False
    
    #7對子檢查（不常見，可以放到後面進行判斷）
    #對子的檢查，特徵1：必须是14张；特徵2:一個牌型，有2張，或4張。特别注意有4張的情况。
    if len(a)==14:
        for x in set(a):
            if a.count(x) not in [2,4]:
                break
        else:
##            print('和牌:7對子。',a)
            return True

    #十三么。
    if len(a)==14:
        gtws=[1, 9, 11, 19, 21, 29, 31, 33, 35, 37, 41, 43, 45] #[1,9,11,19,21,29]+list(range(31,38,2))+list(range(41,46,2)) #用固定的表示方法，計算速度加快。
        #print(gtws)
        for x in gtws:
            if 1<=a.count(x)<=2:
                pass
            else:
                break
        else:
            print('胡！')
            return True

    #常規和牌檢測。
    a1=a.copy()
    a2=[] #a2存放和牌分组的结果。
    for x in double:
        #print('double',x)
        #print(a1[0] in a1 and (a1[0]+1) in a1 and (a1[0]+2) in a1)
        a1.remove(x)
        a1.remove(x)
        a2.append((x,x))
        for i in range(int(len(a1)/3)):
            #print('i-',i)
            if a1.count(a1[0])==3:
                #列表移除
                a2.append((a1[0],)*3)
                a1=a1[3:]
                #print(a1)
            elif a1[0] in a1 and a1[0]+1 in a1 and a1[0]+2 in a1:#11,2222,33，和牌结果22,123,123，則連續的3個可能不是相鄰的。
                a2.append((a1[0],a1[0]+1,a1[0]+2))
                a1.remove(a1[0]+2)
                a1.remove(a1[0]+1)
                a1.remove(a1[0])
                #print(a1)

            else:
                a1=a.copy()
                a2=[]
                #print('重置')
                break
        else:
            print('和牌成功,结果：',a2)
            return True
    
    #如果上述没有返回和牌成功，这里需要返回和牌失败。
    else:
        #print('和牌失敗：遍歷完成。')
        return False

create_new_hdcd(13,cover_card,handcard,r_handcard)
handcard.sort()
r_handcard.sort()

print(f"r_handcard:{r_handcard}")
print(f"handcard:{handcard}")

running = True
while running:
    check_pong =0
    check_eat =0
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
                sys.exit()
        elif event.type == QUIT:
            running = False
            sys.exit()
    
    display_all()

    print(f"r_handcard_again:{r_handcard},{len(r_handcard)}")
    print(f"handcard_again:{handcard},{len(handcard)}")
    
    robot_check_pong(waste_card,r_drop_handcard,r_handcard)
    robot_check_eat(waste_card,r_drop_handcard,r_handcard)
    rob_get_cover(cover_card,r_handcard)
    time.sleep(1)
    robot_throw(waste_card,r_handcard)
    
    display_all()
    
    print(f"我是對家打的牌:{waste_card[-1]}\n")
    print(f"給你看對家手牌:{r_handcard},長度:{len(r_handcard)}\n")
    
    pla_check_hepai(handcard,waste_card)
    if win_flag == 1:
        break
    
    pla_check_pong(waste_card,handcard,drop_handcard)
    pla_check_eat(waste_card,handcard,drop_handcard)
    
    if check_pong == 1:
        print("我碰")
    if check_eat ==1:
        print("我吃")
    
    if mj_round>=t:
        break

    pla_get_cover(cover_card,handcard)    
    pla_check_hepai(handcard)
    
    if win_flag ==1:
        break
    if check_pong==1:
        pla_select_and_throw(handcard,waste_card)
        print(f"我碰過了\n這是新手牌:{handcard},長度:{len(handcard)}\n")
        
    elif check_eat==1:
        pla_select_and_throw(handcard,waste_card)
        print(f"我吃飽了\n這是新手牌:{handcard},長度:{len(handcard)}\n")
    pla_select_and_throw(handcard,waste_card)
    print(f"這是新手牌:{handcard},長度:{len(handcard)}\n")

    time.sleep(1)
    mj_round+=1
    
time.sleep(1)
if win ==1:
    screen.blit(index_to_pic(61),(250,50))
    pygame.display.update()
else:
    screen.blit(index_to_pic(57),(350,250))
    screen.blit(index_to_pic(59),(550,250))
    pygame.display.update()