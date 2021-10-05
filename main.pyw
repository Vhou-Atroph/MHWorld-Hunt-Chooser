from tkinter import *
import random

'''
VERSION 1.1.1

CONTRIBUTORS:
-Vhou-Atroph
'''

#Lists
questTypes=['Low Rank','High Rank','Master Rank'] #I admit, World was my first Monster Hunter. I thought I would like the non-separated LR>HR>G format a lot better than jumping from Village to Hub, but I actually think Rise's quest system was a lot more fun! I miss investigations from World tho
lrMonsters=['Anjanath','Barroth','Diablos','Great Girros','Great Jagras','Jyuratodus','Kirin','Kulu-Ya-Ku','Legiana','Odogaron','Paolumu','Pukei-Pukei','Radobaan','Rathalos','Rathian','Tobi-Kadachi','Tzitzi-Ya-Ku']
hrMonsters=['Anjanath','Barroth','Diablos','Great Girros','Great Jagras','Jyuratodus','Kirin','Kulu-Ya-Ku','Legiana','Odogaron','Paolumu','Pukei-Pukei','Radobaan','Rathalos','Rathian','Tobi-Kadachi','Tzitzi-Ya-Ku',
#HR Exclusives:
'Ancient Leshen','Bazelgeuse','Behemoth','Deviljho','Black Diablos','Dodogama','Kulve Taroth','Kushala Daora','Lavasioth','Leshen','Lunastra','Nergigante','Azure Rathalos','Pink Rathian','Teostra','Uragaan','Vaal Hazak','Xeno\'Jiiva','Zorah Magdaros']
mrMonsters=['Anjanath','Barroth','Diablos','Great Girros','Great Jagras','Jyuratodus','Kirin','Kulu-Ya-Ku','Legiana','Odogaron','Paolumu','Pukei-Pukei','Radobaan','Rathalos','Rathian','Tobi-Kadachi','Tzitzi-Ya-Ku','Black Diablos','Dodogama','Kulve Taroth','Kushala Daora','Lavasioth','Lunastra','Azure Rathalos','Pink Rathian','Teostra','Uragaan',
#MR Exclusives:
'Alatreon','Fulgur Anjanath','Banbaro','Barioth','Frostfang Barioth','Seething Bazelgeuse','Beotodus','Brachydios','Raging Brachydios','Savage Deviljho','Fatalis','Glavenus','Acidic Glavenus','Shrieking Legiana','Namielle','Nargacuga','Ruiner Nergigante','Ebony Odogaron','Nightshade Paolumu','Coral Pukei-Pukei','Rajang','Furious Rajang','Silver Rathhalos','Gold Rathian','Safi\'Jiiva','Shara Ishvalda','Tigrex','Brute Tigrex','Viper Tobi-Kadachi','Blackveil Vaal Hazak','Velkhana','Yian Garuga','Scarred Yian Garuga','Zinogre','Stygian Zinogre']
weapons=['Hammer','Charge Blade','Greatsword','Hunting Horn','Longsword','Lance','Gunlance','Insect Glaive','Switch Axe','Dual Blades','Sword and Shield','Bow','Light Bowgun','Heavy Bowgun']

#Window
global window
window=Tk()
window.title("MHWorld: Random Hunt Chooser")
window.geometry('350x175')
window.resizable(0,0)

#Options
options=Frame(window) #Options feels like a better word than 'selections.' 
questChoice=StringVar(window)
questChoice.set('Low Rank')
choose=OptionMenu(options,questChoice,*questTypes)
wep=IntVar(window)
wepCheck=Checkbutton(options, text="Random weapon", variable=wep, onvalue=1, offvalue=0)
rollBtn=Button(options,text="Roll Hunt")

#Chosen Hunt
results=Frame(options)
hunt=Label(results,text="Your rolled hunt \nwill go here!")
wepRoll=Label(results)

#Monster Icons
defaultIcon=PhotoImage(file='icons/Unknown.png')
ico=Label(window,image=defaultIcon)

#Hunt Command
def rolltime():
  if questChoice.get()=='Low Rank':
    monster=random.choice(lrMonsters)
    newIcon=PhotoImage(file='icons/'+monster+'.png')
    ico.configure(image=newIcon)
    ico.image=newIcon
    hunt.configure(text="Low Rank:\n"+monster)
  if questChoice.get()=='High Rank':
    monster=random.choice(hrMonsters)
    newIcon=PhotoImage(file='icons/'+monster+'.png')
    ico.configure(image=newIcon)
    ico.image=newIcon
    hunt.configure(text="High Rank:\n"+monster)
  if questChoice.get()=='Master Rank':
    monster=random.choice(mrMonsters)
    newIcon=PhotoImage(file='icons/'+monster+'.png')
    ico.configure(image=newIcon)
    ico.image=newIcon
    hunt.configure(text="Master Rank:\n"+monster)
  if wep.get()==1:
    wepRoll.configure(text="Weapon:\n"+random.choice(weapons))
  else:
    wepRoll.configure(text="")

rollBtn.configure(command=rolltime)

#Pack
options.pack(pady=2,padx=2, side=LEFT)
choose.pack()
wepCheck.pack()
rollBtn.pack(pady=2)
results.pack()
hunt.pack(pady=3)
wepRoll.pack()
ico.pack(side=RIGHT)

window.mainloop()