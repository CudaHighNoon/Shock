import pygame, sys, time, math, random
pygame.init(); hx2=0; hy2=0; dc=0; state="running"
darkgrey=[100,100,100]; yellow=[255,255,0]; click="false"
x=650;y=500; i=0; i2=0; dc=0;p1s=0; p2s=0; p1t=0;p2t=0
y1=0; x1=0; xp=1070; yp=600; status="none";ht=0
wlst=[]; whlth=[]; wposx=[];wposy=[];wbr=[]
nlst=[];nhlth=[];nposx=[];nposy=[];nbr=[]
blst=[];bhlth=[];bposx=[];bposy=[];bbr=[]
screen= pygame.display.set_mode([1200,720]); dc=0;
#
i=0; hx1=650; hy1=500; hy2=500; hx2=xp+400;bc1=200;bc2=200;
bd1=200;bd2=200
white=[255,255,255]; red=[255,0,0]; blue=[0,0,255]
green=[0,255,0]; black=[0,0,0];fire1="false"; b1=200; b2=200;fire2="false";level=1; grey=[200,200,200];
b1grey=[200,200,200]; b2grey=[200,200,200];purple=[0,200,200]
player=pygame.image.load('player.png')
#spwnwarrior spawns in a warrior
def spwn():
    for mob in wlst:
        mobx=random.randint(400,1200); wposx.insert(mob-1,mobx);wposy.insert(mob-1,random.randint(0,200));wbr.insert(mob-1,15);whlth.insert(mob-1,100)
    for nec in nlst:
        necx=random.randint(400,1200); nposx.insert(nec-1,necx);nposy.insert(nec-1,random.randint(0,200));nbr.insert(nec-1,15);nhlth.insert(nec-1,100)
    for brute in blst:
        brutex=random.randint(400,1200); bposx.insert(brute-1,brutex);bposy.insert(brute-1,random.randint(0,200));bbr.insert(brute-1,15);bhlth.insert(brute-1,500)
 #Gui
def Guifnc():
     backpnl=pygame.draw.line(screen,blue,(400,200),(1250,200),100)
     pygame.draw.line(screen,black,(600,220),(1000,220),85)
     
def reset():
    wposy.clear();wposx.clear();whlth.clear();wbr.clear();wlst.clear();nlst.clear();nhlth.clear();wbr.clear();nposy.clear();nposx.clear()
    blst.clear();bhlth.clear();bbr.clear();bposy.clear();bposx.clear()
def mobai():
    global dc,state,wlst,blst,nlst
    for war in wlst:
        if state=="running" and whlth[war-1]>0:
            warx=wposx[war-1];
            wposy[war-1]+=2
            renwar=pygame.draw.circle(screen,red,(warx,int(wposy[war-1])),20);
            if fire1=="true":
                if renwar.colliderect(hitscnp1):
                    whlth[war-1]-=6; wbr[war-1]-=1.5
                    if whlth[war-1]<=0:
                        dc+=1;
            if fire2=="true":
                if renwar.colliderect(hitscnp2):
                    whlth[war-1]-=6; wbr[war-1]-=1.5
                    if whlth[war-1]<=0:
                         dc+=1;
            pygame.draw.line(screen,green,(warx+wbr[war-1],int(wposy[war-1]+16)),(warx-15,int(wposy[war-1]+16)),5)
            if wposy[war-1]>=650:
                state="lose";
    for ncr in nlst:
        if state=="running" and nhlth[ncr-1]>0:
            nposx[ncr-1]+=random.randint(-15,15);
            if nposx[ncr-1]<650:
                nposx[ncr-1]+=20
            if nposx[ncr-1]>1280:
                nposx[ncr-1]-=20
            necx=nposx[ncr-1];
            nposy[ncr-1]+=6
            renncr=pygame.draw.line(screen,purple,(necx,int(nposy[ncr-1])),(necx+30,int(nposy[ncr-1])),30)
            
            if hitscnp2.colliderect(renncr):
                    nhlth[ncr-1]-=6; nbr[ncr-1]-=.15
                    if nhlth[ncr-1]<=0:
                        dc+=1;
            if hitscnp1.colliderect(renncr):
                    nhlth[ncr-1]-=6; nbr[ncr-1]-=.15
                    if nhlth[ncr-1]<=0:
                        dc+=1; 
            pygame.draw.line(screen,green,(necx+nbr[ncr-1],int(nposy[ncr-1]+16)),(necx-15,int(nposy[ncr-1]+16)),5)
            if nposy[ncr-1]==650:state="lose"
    for br in blst:
        if state=="running" and bhlth[br-1]>0:
            bx=bposx[br-1];
            bposy[br-1]+=2
            renbr=pygame.draw.circle(screen,grey,(bx,int(bposy[br-1])),30);
            if fire1=="true":
                if hitscnp1.colliderect(renbr):
                    bhlth[br-1]-=6; bbr[br-1]-=.1
                    if bhlth[br-1]<=0:
                        dc+=1;
            if fire2=="true":
                if hitscnp2.colliderect(renbr):
                    bhlth[br-1]-=6;bbr[br-1]-=.15
                    if bhlth[br-1]<=0:
                        dc+=1;
            pygame.draw.line(screen,green,(bx+bbr[br-1],int(bposy[br-1]+35)),(bx-15,int(bposy[br-1]+35)),5)
            if bposy[br-1]==650:state="lose"
def wpnrnd():
    global p1t,p2t
    if fire1=="true" and p1t<200:
            hitscnp1=pygame.draw.line(screen,yellow,(500,690),(hx1,hy1),1)
            p1t+=1;b1grey[0]+=.15;b1grey[1]-=.5;b1grey[2]-=.5
    elif fire1=="false" and p1t>=0:
            p1t-=1;
            b1grey[0]-=.15;b1grey[1]+=.5;b1grey[2]+=.5
    if fire2=="true"and p2t<200:
            hitscnp2=pygame.draw.line(screen,yellow,(1085,690),(hx2,hy2),1);
            p2t+=1;b2grey[0]+=.1;b2grey[1]-=.4;b2grey[2]-=.4
    elif fire2=="false" and p2t>=0:
            p2t-=1;
            b2grey[0]-=.1;b2grey[1]+=.4;b2grey[2]+=.4  
def gmobjs():
    pygame.draw.line(screen,[150,150,150],(400,650),(745,650),27)
    cswll1= pygame.draw.line(screen,darkgrey,(400,650),(740,650),20)
    pygame.draw.line(screen,[150,150,150],(1200,650),(855,650),27)
    cswll2= pygame.draw.line(screen,darkgrey,(1200,650),(860,650),20)
    pygame.draw.line(screen,[50,50,50],(400,690),(1200,690),50)
    barrelp1=pygame.draw.line(screen,b1grey,(500,690),(x,y),15)
    barrelp2=pygame.draw.line(screen,b2grey,(1085,690),(xp,yp),15)
    p1=pygame.draw.circle(screen, blue,(500,690),30)
    p2=pygame.draw.circle(screen,blue,(1085, 690), 30)
#game anouncements
#
 # functions for rounds           
def r1():
    wlst.extend([1,2])
    spwn();
def r2():
    reset()
    wlst.extend([1,2,3,4])
    spwn();
def r3():
    reset()
    wlst.extend([1,2,3,4,5,6,7,8])
    spwn();
def r4():
    reset()
    wlst.extend([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
    spwn();
def r5():
    reset()
    wlst.extend([1,2]);nlst.extend([1,2,3])
    spwn();
def r6():
    reset()
    wlst.extend([1,2,3,4]);nlst.extend([1,2,3,4,5,6])
    spwn()
def r7():
    reset()
    wlst.extend([1,2,3,4,5]); nlst.extend([1,2,3,4]);blst.extend([1,2])
    spwn()
def r8():
    reset()
    wlst.extend([1,2,3,4,5,6]);nlst.extend([1,2,3,4,5,6])
    blst.extend([1,2,3,4])
    spwn()
def r9():
    reset()
    blst.extend([1,2,3,4,5,6,7,8,9,10]);
    spwn()
def r10():
    reset(); blst.extend([1,2,3,4,5,6,7]);
    nlst.extend([1,2,3,4,5,6,7]); wlst.extend([1,2,3,4,5,6,7,8,9])

#game statements
#
while True:
    pygame.time.delay(60)
    x = 70*math.cos(i) + 500
    y = 70*math.sin(i) + 690
    hx1=500*math.cos(i)+500
    hy1=500*math.sin(i)+690
    xp = 70*math.cos(i2) + 1085
    yp = 70*math.sin(i2) + 690
    hx2=500*math.cos(i2)+1085
    hy2=500*math.sin(i2)+690
    if level==1 and status=="none" and state=="running":
        dc=0; status="running";r1();
    if dc==2 and level==1 and state=="running":
        level=2; print("start");print(dc); dc=0
        print("r2");r2()
    if dc==4 and level==2 and state=="running":
        dc=0;level=3;r3();
    if dc==8 and level==3 and state=="running":
        dc=0;r4(); print(level);level=4;
    if dc==16 and level==4 and state=="running":
        dc=0; level=5;r5();
    if dc==5and level==5 and state=="running":
        dc=0; level=6;r6();
    if dc==10 and level==6 and state=="running":
        print(dc);dc=0;r7(); print(level);level=7;
    if dc==11 and level==7 and state=="running":
        dc=0; level=8;r8();
    if dc==16 and level==8 and state=="running":
        dc=0; level=9;r9();
    if dc==23 and level==9 and state=="running":
        dc=0; level=10;r10();print("203 Error: Uncontrolled spawn rate; reboot failed player must kill them")
    screen.fill(black)
    gmobjs()
    #warrior AI
    pygame.draw.line(screen,black,(600,220),(1000,220),85)
    if fire1=="true" and p1t<200:
                hitscnp1=pygame.draw.line(screen,yellow,(500,690),(hx1,hy1),1)
                p1t+=1;b1grey[0]+=.1;b1grey[1]-=.4;b1grey[2]-=.4;
    elif fire1=="false" and p1t>=0:
                p1t-=1;
                b1grey[0]-=.1;b1grey[1]+=.4;b1grey[2]+=.4
    if fire2=="true"and p2t<200:
                hitscnp2=pygame.draw.line(screen,yellow,(1085,690),(hx2,hy2),1);
                p2t+=1;b2grey[0]+=.1;b2grey[1]-=.4;b2grey[2]-=.4
    elif fire2=="false" and p2t>=0:
                p2t-=1;
                b2grey[0]-=.1;b2grey[1]+=.4;b2grey[2]+=.4
    wpnrnd()
    mobai()
    if state=="lose":
            mousx,mousy=pygame.mouse.get_pos()
            lossmn=pygame.draw.line(screen,grey,(700,400),(850,400),150)
            srtbtn=pygame.draw.line(screen,green,(720,430),(750,430),20)
            pygame.draw.line(screen,white,(745,380),(805,380),40)
            pygame.draw.line(screen,white,(755,400),(795,400),20)
            pygame.draw.line(screen,black,(755,380),(765,380),5)
            pygame.draw.line(screen,black,(795,380),(785,380),5)
            mouse=pygame.draw.circle(screen,black,(mousx,mousy),1)
            if mouse.colliderect(srtbtn)and click=="true":
                state="running";dc=0;level=1;status="none"; click=="false"; reset() 
    #------------------
    #Guifnc()
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        if event.type==pygame.MOUSEBUTTONDOWN or keys[pygame.K_SPACE]:click="true"
        elif event.type==pygame.MOUSEBUTTONUP:click="false"
        if keys[pygame.K_d]:i+=.07
        if keys[pygame.K_a]:i-=.07
        if keys[pygame.K_l]:i2+=.07
        if keys[pygame.K_j]:i2-=.07
        elif not keys[pygame.K_j]:movep2="n"
        if keys[pygame.K_p] and p2t<200:
            fire2="true";
        elif not keys[pygame.K_p]:fire2="false"
        if keys[pygame.K_c] and p1t<200:
            fire1="true";
        elif not keys[pygame.K_c]:fire1="false"
        break
    if fire1=="true":
        pygame.draw.circle(screen,yellow,(int(x),int(y)),10)
    if fire2=="true":
        pygame.draw.circle(screen,yellow,(int(xp),int(yp)),10)
    pygame.display.update()
