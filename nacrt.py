import numpy as np, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle, Polygon, Rectangle
from PIL import Image

L,W,Wt,H,T,R = 200,16,15,8,2,6
PH,PD,HD,FIL = 7,8,3,0.5
px = [L-20, L-20-97, 20]
fig = plt.figure(figsize=(16.54,11.69))  # A3
K='k'; DIM='#1f4e9c'
def dim(ax,p1,p2,off,text,horiz=True,fs=10,ext=True):
    (x1,y1),(x2,y2)=p1,p2
    if horiz:
        y=off
        if ext:
            ax.plot([x1,x1],[y1,y],color=DIM,lw=.5); ax.plot([x2,x2],[y2,y],color=DIM,lw=.5)
        ax.annotate('',(x1,y),(x2,y),arrowprops=dict(arrowstyle='<|-|>',color=DIM,lw=.7,mutation_scale=8))
        ax.text((x1+x2)/2,y,text,ha='center',va='bottom',color=DIM,fontsize=fs,
                bbox=dict(fc='white',ec='none',pad=.5))
    else:
        x=off
        if ext:
            ax.plot([x1,x],[y1,y1],color=DIM,lw=.5); ax.plot([x2,x],[y2,y2],color=DIM,lw=.5)
        ax.annotate('',(x,y1),(x,y2),arrowprops=dict(arrowstyle='<|-|>',color=DIM,lw=.7,mutation_scale=8))
        ax.text(x,(y1+y2)/2,text,ha='center',va='center',color=DIM,fontsize=fs,rotation=90,
                bbox=dict(fc='white',ec='none',pad=.5))

fig.text(.03,.965,'Lyžina (kolejnice) šuplíku – kontrolní náčrtek',fontsize=20,weight='bold')
fig.text(.03,.94,'Rozměry v mm · tloušťka plastu 2 mm · měřítko neodpovídá tisku papíru',fontsize=11,color='#444')

# --- 1. Pohled na zadní stranu (s výstupky)
ax=fig.add_axes([.03,.62,.94,.29]); ax.set_aspect('equal'); ax.axis('off')
ax.set_title('1) Pohled na zadní stranu (strana s výstupky, šíře 16)',loc='left',fontsize=12)
ax.add_patch(FancyBboxPatch((R,-W/2+R),L-2*R,W-2*R,boxstyle=f'round,pad={R}',fc='#e8eef6',ec=K,lw=1.3))
# obrys predni strany (15) skryte
ax.add_patch(FancyBboxPatch((R,-Wt/2+R-0.0),L-2*R,Wt-2*R,boxstyle=f'round,pad={R-0.5}',fc='none',ec='#888',lw=.6,ls='--'))
for i,x in enumerate(px):
    ax.add_patch(Circle((x,0),PD/2+FIL,fc='none',ec='#888',lw=.6))
    ax.add_patch(Circle((x,0),PD/2,fc='white',ec=K,lw=1.2))
    ax.add_patch(Circle((x,0),HD/2,fc='#333',ec=K))
    ax.plot([x,x],[-11,11],color='r',lw=.5,ls='-.')
    ax.text(x+5,8.6,f'výstupek {i+1}',fontsize=8,color='#555')
ax.plot([-4,L+4],[0,0],color='r',lw=.5,ls='-.')
dim(ax,(L-20,0),(L,0),-14,'20')
dim(ax,(px[1],0),(px[0],0),-14,'97')
dim(ax,(0,0),(20,0),-14,'20')
dim(ax,(px[2],0),(px[1],0),-14,'63 (dopočet)',fs=9)
dim(ax,(0,-W/2),(L,-W/2),-22,'200 (celková délka)')
dim(ax,(L,-W/2),(L,W/2),L+8,'16',horiz=False)
ax.annotate('R6',(L-R+R*np.cos(.8),W/2-R+R*np.sin(.8)),(L+3,15),color=DIM,fontsize=10,
            arrowprops=dict(arrowstyle='-',color=DIM,lw=.6))
ax.annotate(f'Ø{PD} výstupek\nØ{HD} díra pro šroub',(px[1]+2.5,2.5),(px[1]+18,13),fontsize=9,color=DIM,
            arrowprops=dict(arrowstyle='-',color=DIM,lw=.6))
ax.text(0,-30,'← levý konec (zde chyběl výstupek)',ha='left',fontsize=9,color='#555')
ax.text(L,-30,'pravý konec →',ha='right',fontsize=9,color='#555')
ax.annotate('A',(px[1]-0,-11),(px[1]-0,-11),fontsize=11,weight='bold',color='r')
ax.set_xlim(-8,L+14); ax.set_ylim(-33,19)

# --- 2. Bokorys
ax=fig.add_axes([.03,.36,.94,.24]); ax.set_aspect('equal'); ax.axis('off')
ax.set_title('2) Bokorys (výstupky dolů = k montážní ploše)',loc='left',fontsize=12)
ax.add_patch(Rectangle((0,0),L,H,fc='#e8eef6',ec=K,lw=1.3))
ax.plot([T,L-T],[T,T],color='#888',lw=.7,ls='--')   # vnitrni dno
ax.plot([T,T],[T,H],color='#888',lw=.7,ls='--'); ax.plot([L-T,L-T],[T,H],color='#888',lw=.7,ls='--')
for x in px:
    ax.add_patch(Polygon([(x-PD/2,0),(x-PD/2,-PH+.5),(x-PD/2+.5,-PH),(x+PD/2-.5,-PH),(x+PD/2,-PH+.5),(x+PD/2,0)],fc='#e8eef6',ec=K,lw=1.2))
    ax.add_patch(Polygon([(x-PD/2-FIL,0),(x-PD/2,-FIL),(x+PD/2,-FIL),(x+PD/2+FIL,0)],fc='#e8eef6',ec=K,lw=.8))
    ax.plot([x-HD/2]*2,[-PH,T],color='#888',lw=.7,ls='--'); ax.plot([x+HD/2]*2,[-PH,T],color='#888',lw=.7,ls='--')
    ax.plot([x,x],[-PH-2,H+2],color='r',lw=.5,ls='-.')
dim(ax,(L,0),(L,H),L+6,'8',horiz=False)
dim(ax,(px[0]+PD/2,0),(px[0]+PD/2,-PH),px[0]+10,'7',horiz=False)
dim(ax,(0,H),(L,H),H+5,'200')
ax.text(px[1]+8,-5,'výstupek 7 mm nad zadní plochou',fontsize=9,color=DIM)
ax.text(40,H/2,'otevřená přední strana (šíře 15) je nahoře',fontsize=9,color='#555',va='center')
ax.set_xlim(-8,L+14); ax.set_ylim(-12,16)

# --- 3. Rez A-A
ax=fig.add_axes([.03,.03,.36,.31]); ax.set_aspect('equal'); ax.axis('off')
ax.set_title('3) Řez A–A vedený výstupkem (zvětšeno)',loc='left',fontsize=12)
z=0.5; # zuzeni na stranu
off=lambda zz: z*zz/H
outer=[(-W/2,0),(W/2,0),(W/2-off(H),H),(-W/2+off(H),H)]
ia=W/2-off(T)-T; ib=W/2-off(H)-T
inner=[(-ia,T),(ia,T),(ib,H),(-ib,H)]
# draw section as outer minus inner via hatch on wall polygons
walls=[[(-W/2,0),(W/2,0),(W/2,0),(ia,T),(-ia,T)],
       [(W/2,0),(W/2-off(H),H),(ib,H),(ia,T)],
       [(-W/2,0),(-ia,T),(-ib,H),(-W/2+off(H),H)]]
for w in walls: ax.add_patch(Polygon(w,fc='#cfdcec',ec='none',hatch='///'))
ax.add_patch(Polygon(outer,fc='none',ec=K,lw=1.4)); ax.add_patch(Polygon(inner,fc='white',ec=K,lw=1.2))
ax.plot([-ib,ib],[H,H],color='white',lw=2.5)  # otevrena strana
for s in (1,-1):
    ax.add_patch(Polygon([(s*(PD/2+FIL),0),(s*PD/2,-FIL),(s*PD/2,-PH+.5),(s*(PD/2-.5),-PH),(s*HD/2,-PH),(s*HD/2,0)],fc='#cfdcec',ec=K,lw=1.2,hatch='///'))
ax.add_patch(Rectangle((-HD/2,-PH),HD,PH+T,fc='white',ec='none'))
ax.plot([-HD/2,-HD/2],[-PH,T],color=K,lw=1); ax.plot([HD/2,HD/2],[-PH,T],color=K,lw=1)
ax.plot([0,0],[-PH-1.5,H+1.5],color='r',lw=.5,ls='-.')
dim(ax,(-W/2,0),(W/2,0),-PH-3.5,'16 (zadní strana)',fs=9)
dim(ax,(-W/2+off(H),H),(W/2-off(H),H),H+3.2,'15 (přední strana)',fs=9)
dim(ax,(-ib,H),(ib,H),H+1.2,'≈11',fs=9,ext=False)
dim(ax,(-ia,T),(ia,T),T+1.6,'≈12',fs=9,ext=False)
dim(ax,(W/2,0),(W/2-off(H),H),W/2+2.5,'8',horiz=False,fs=9)
dim(ax,(-W/2,0),(-W/2,T),-W/2-1.8,'2',horiz=False,fs=9)
dim(ax,(-PD/2,0),(-PD/2,-PH),-W/2-1.8,'7',horiz=False,fs=9)
ax.annotate(f'Ø{HD}',(HD/2,-3),(5.5,-5.5),color=DIM,fontsize=9,arrowprops=dict(arrowstyle='-',color=DIM,lw=.6))
ax.annotate(f'Ø{PD}',(PD/2,-4.5),(7,-8.5),color=DIM,fontsize=9,arrowprops=dict(arrowstyle='-',color=DIM,lw=.6))
ax.annotate('zkosení 0,5 mm\nna každé straně',(W/2-off(H)/2,H/2),(9.5,11),color=DIM,fontsize=8.5,
            arrowprops=dict(arrowstyle='-',color=DIM,lw=.6))
ax.set_xlim(-12,17); ax.set_ylim(-12,13)

# --- 3D nahledy
for i,(f,t) in enumerate([('/tmp/p.png','3D – strana s výstupky'),('/tmp/p2.png','3D – vnitřek profilu')]):
    a=fig.add_axes([.42+i*.285,.02,.27,.17]); a.imshow(Image.open(f)); a.axis('off'); a.set_title(t,loc='left',fontsize=10)

fig.text(.42,.325,'Předpoklady k ověření:',fontsize=11,weight='bold')
fig.text(.42,.315,
 '• Výstupky vyčnívají 7 mm ze zadní (16 mm) strany ven, jako na fotce; průměr výstupku 8 mm.\n'
 '• Díra Ø3 prochází výstupkem i dnem. Pro šroub do dřeva doporučuji tisknout Ø3,2–3,4 (parametr v .scad).\n'
 '• Pata výstupku je zesílena kuželem 0,5 mm (původní díl praskal právě tam), špička sražena 0,5 mm.\n'
 '• Konce jsou uzavřené, v půdorysu zaoblené R6; zkosení stěn (16→15) je po celém obvodu.\n'
 '• Tisk: otevřenou stranou na podložku, výstupky nahoru; dno (12 mm) se přemostí bez podpěr.',
 fontsize=9.5,va='top',linespacing=1.6)
fig.savefig('lyzina_nacrtek.pdf'); fig.savefig('lyzina_nacrtek.png',dpi=110)
