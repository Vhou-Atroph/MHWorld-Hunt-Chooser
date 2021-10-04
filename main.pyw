from tkinter import *
import random

'''
VERSION 1

CONTRIBUTORS:
-Vhou-Atroph
'''

#Lists
questTypes=['Low Rank','High Rank','Master Rank']
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
window.geometry('180x150')
window.resizable(0,0)

#Options
options=Frame(window)
questChoice=StringVar(window)
questChoice.set('Low Rank')
choose=OptionMenu(options,questChoice,*questTypes)
wep=IntVar(window)
wepCheck=Checkbutton(options, text="Random weapon", variable=wep, onvalue=1, offvalue=0)
rollBtn=Button(options,text="Roll Hunt")

#Chosen Hunt
hunt=Label(options,text="Your rolled hunt \nwill go here!")
wepRoll=Label(options)

#Hunt Command
def rolltime():
  if questChoice.get()=='Low Rank': #questChoice is also the variable that is looked at when determining what kind of hunt to do.
    hunt.configure(text="Low Rank:\n"+random.choice(lrMonsters))
  if questChoice.get()=='High Rank':
    hunt.configure(text="High Rank:\n"+random.choice(hrMonsters))
  if questChoice.get()=='Master Rank':
    hunt.configure(text="Master Rank:\n"+random.choice(mrMonsters))
  if wep.get()==1:
    wepRoll.configure(text="Weapon: "+random.choice(weapons))
  else:
    wepRoll.configure(text="Weapon: Your choice!")

rollBtn.configure(command=rolltime)

#Pack
options.pack(pady=2,padx=2)
choose.pack()
wepCheck.pack()
rollBtn.pack(pady=2)
hunt.pack(pady=3)
wepRoll.pack()

window.mainloop()