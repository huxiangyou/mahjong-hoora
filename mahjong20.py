# -*- coding: utf-8 -*-
#!/usr/bin/python3
#python 3.7.1 3.7.2 3.7.3

"""
version 0.0 coded by Hu Xiangyou on December 17, 2018
version 1.0 coded by Hu Xiangyou on February 9, 2019
version 1.1 coded by Hu Xiangyou on February 20, 2019
version 1.2 coded by Hu Xiangyou on March 20, 2019
version 2.0 coded by Hu Xiangyou on April 14, 2019

Mahjong Hoora kai?
check hoora or tenpai in Japanese mahjong

for details, check README.md
"""

import datetime
import random
import sys
from lang import romaji, kanji, katakana, ja, zh
s=zh # change "zh" to other language if you need: romaji, kanji, katakana, ja, zh

def yaku_and_output(tehai9,hoorakei,tsumo,karaten,tsumohai,dahai,number_only):
	yaku=[]
	hansuu=0
	yakuman=False
	hai=('',[1,'m'],[2,'m'],[3,'m'],[4,'m'],[5,'m'],[6,'m'],[7,'m'],[8,'m'],[9,'m'],
	'',[1,'p'],[2,'p'],[3,'p'],[4,'p'],[5,'p'],[6,'p'],[7,'p'],[8,'p'],[9,'p'],
	'',[1,'s'],[2,'s'],[3,'s'],[4,'s'],[5,'s'],[6,'s'],[7,'s'],[8,'s'],[9,'s'],
	'',[1,'z'],[2,'z'],[3,'z'],[4,'z'],[5,'z'],[6,'z'],[7,'z'])
	hai_=('','1m','2m','3m','4m','5m','6m','7m','8m','9m',
	'','1p','2p','3p','4p','5p','6p','7p','8p','9p',
	'','1s','2s','3s','4s','5s','6s','7s','8s','9s',
	'','東','南','西','北','白','發','中')
	if number_only:
		hai=('',[1,''],[2,''],[3,''],[4,''],[5,''],[6,''],[7,''],[8,''],[9,''],'')
		hai_=('','1','2','3','4','5','6','7','8','9','')

	#kokushimusou
	if len(hoorakei)>1 and hoorakei[1][0]=='tanpai':
		if tehai9[tsumohai]==2:
			yaku.append(s.kokushimusoujuusanmen)
			hansuu+=26
		else:
			yaku.append(s.kokushimusou)
			hansuu+=13
		yakuman=True

	elif sum(tehai9)<=14:

		#chiitoitsu
		if hoorakei[0][0]=='toitsu':
			yaku.append(s.chiitoitsu)
			hansuu+=2

		#tanyaochuu
		if sum(tehai9)==14 and not tehai9[1] and not tehai9[9] and not tehai9[11] and not tehai9[19] and not tehai9[21] and not tehai9[29] and not any(tehai9[31:]):
			yaku.append(s.tanyaochuu)
			hansuu+=1

		#yakuhai
		#not checking chanfon or menfon
		#ton
		if ['kootsu',1,1,1,'z'] in hoorakei:
			yaku.append(s.yakuhai_ton+s.question_mark)
			hansuu+=1
		#nan
		if ['kootsu',2,2,2,'z'] in hoorakei:
			yaku.append(s.yakuhai_nan+s.question_mark)
			hansuu+=1
		#shaa
		if ['kootsu',3,3,3,'z'] in hoorakei:
			yaku.append(s.yakuhai_shaa+s.question_mark)
			hansuu+=1
		#pei
		if ['kootsu',4,4,4,'z'] in hoorakei:
			yaku.append(s.yakuhai_pei+s.question_mark)
			hansuu+=1
		if sum((i in yaku for i in (s.yakuhai_ton+s.question_mark,s.yakuhai_nan+s.question_mark,s.yakuhai_shaa+s.question_mark,s.yakuhai_pei+s.question_mark)))==3:
			hansuu-=1
		#haku
		if ['kootsu',5,5,5,'z'] in hoorakei:
			yaku.append(s.yakuhai_haku)
			hansuu+=1
		#hatsu
		if ['kootsu',6,6,6,'z'] in hoorakei:
			yaku.append(s.yakuhai_hatsu)
			hansuu+=1
		#chun
		if ['kootsu',7,7,7,'z'] in hoorakei:
			yaku.append(s.yakuhai_chun)
			hansuu+=1

		#pinfu
		#not checking chanfon or menfon
		if len(hoorakei)==5 and \
		all(i[0]=='shuntsu' for i in hoorakei[1:]) and \
		(hoorakei[0][4]!='z' or hoorakei[0][1]<5):
			if tsumo==False:
				if any(((tsumohai%10==i[1]!=7 or tsumohai%10==i[3]!=3) and hai[tsumohai][1]==i[4]) for i in hoorakei[1:]):
					if hoorakei[0][4]=='z':
						yaku.append(s.pinfu+s.question_mark)
					else:
						yaku.append(s.pinfu)
			else:
				yaku.append(s.pinfu+s.question_mark)
			hansuu+=1

		#iipeekoo
		#not checking menzenchin
		if any(i[0]=='shuntsu' and hoorakei.count(i)>=2 for i in hoorakei):
			yaku.append(s.iipeekoo)
			hansuu+=1

		#sanshokudoujun
		if any((['shuntsu',i,i+1,i+2,'m'] in hoorakei and ['shuntsu',i,i+1,i+2,'p'] in hoorakei and ['shuntsu',i,i+1,i+2,'s'] in hoorakei) for i in range(1,8)):
			yaku.append(s.sanshokudoujun)
			hansuu+=2#not counting kuisagari

		#ikkitsuukan
		if any((['shuntsu',1,2,3,i] in hoorakei and ['shuntsu',4,5,6,i] in hoorakei and ['shuntsu',7,8,9,i] in hoorakei) for i in ('','m','p','s')):
			yaku.append(s.ikkitsuukan)
			hansuu+=2#not counting kuisagari

		#honchantaiyaochuu
		if len(hoorakei)==5 and \
		all((i[1]==1 or i[3]==9 or i[4]=='z') for i in hoorakei) and \
		any(i[0]=='shuntsu' for i in hoorakei[1:]) and 0<sum(tehai9[31:])<14:
			yaku.append(s.honchantaiyaochuu)
			hansuu+=2#not counting kuisagari

		#toitoihoo
		if len(hoorakei)==5 and all(i[0]=='kootsu' for i in hoorakei[1:]):
			yaku.append(s.toitoihoo)
			hansuu+=2

		#sanankoo
		#not checking fuuro
		if sum(i[0]=='kootsu' for i in hoorakei)>=3:
			if tsumo==False and any(i[0]!='kootsu' and hai[tsumohai][1]==i[4] and tsumohai%10 in i for i in hoorakei) or s.toitoihoo in yaku:
				yaku.append(s.sanankoo)
			else:
				yaku.append(s.sanankoo+s.question_mark)
			hansuu+=2

		#honroutou
		if tehai9[1]+tehai9[9]+tehai9[11]+tehai9[19]+tehai9[21]+tehai9[29]+sum(tehai9[31:])==14 and 0<sum(tehai9[31:])<14:
			yaku.append(s.honroutou)
			hansuu+=2

		#sanshokudookoo
		if any((['kootsu',i,i,i,'m'] in hoorakei and ['kootsu',i,i,i,'p'] in hoorakei and ['kootsu',i,i,i,'s'] in hoorakei) for i in range(1,10)):
				yaku.append(s.sanshokudookoo)
				hansuu+=2

		#shousangen
		if (['jantou',5,5,None,'z']==hoorakei[0] and ['kootsu',6,6,6,'z'] in hoorakei and ['kootsu',7,7,7,'z'] in hoorakei) or \
		(['kootsu',5,5,5,'z']==hoorakei[0] and ['jantou',6,6,None,'z'] in hoorakei and ['kootsu',7,7,7,'z'] in hoorakei) or \
		(['kootsu',5,5,5,'z']==hoorakei[0] and ['kootsu',6,6,6,'z'] in hoorakei and ['jantou',7,7,None,'z'] in hoorakei):
			yaku.append(s.shousangen)
			hansuu+=2

		#honiisoo
		if sum(tehai9)==14 and 0<sum(tehai9[31:])<14 and \
		(not any(tehai9[11:30]) or not any(tehai9[1:10]+tehai9[21:30]) or not any(tehai9[1:20])):
			yaku.append(s.honiisoo)
			hansuu+=3#not counting kuisagari

		#junchantaiyaochuu
		if len(hoorakei)==5 and \
		all((i[1]==1 or i[3]==9 and i[4]!='z') for i in hoorakei) and \
		any(i[0]=='shuntsu' for i in hoorakei[1:]):
			yaku.append(s.junchantaiyaochuu)
			hansuu+=3#not counting kuisagari

		#ryanpeekoo
		#not checking menzenchin
		if sum(i[0]=='shuntsu' and hoorakei.count(i)>=2 for i in hoorakei)>=4:
			yaku.append(s.ryanpeekoo)
			hansuu+=3
			if s.iipeekoo in yaku:
				yaku.remove(s.iipeekoo)
				hansuu-=1
			# if s.chiitoitsu in yaku[0]:
			# 	yaku[0]=[]
			# 	hoorakeis[0]=[]

		#chiniisoo
		if sum(tehai9)==14 and (sum(tehai9[1:10])==14 or sum(tehai9[11:20])==14 or sum(tehai9[21:30])==14):
			yaku.append(s.chiniisoo)
			hansuu+=6#not counting kuisagari

		#suuankoo
		#not checking menzenchin
		if sum(i[0]=='kootsu' for i in hoorakei)>=4:
			if tsumo==False:
				if tsumohai%10==hoorakei[0][1] and hai[tsumohai][1]==hoorakei[0][4]:
					yaku.append(s.suuankootanki)
					hansuu+=26
					yakuman=True
				else:
					yaku.append(s.sanankoo+s.ideographic_comma+s.toitoihoo+' ('+s.suuankoo+s.question_mark+')')
					hansuu+=4
					yakuman=False
			else:
				yaku.append(s.suuankoo+s.question_mark)
				hansuu+=13
				yakuman=True
			if s.toitoihoo in yaku:
				yaku.remove(s.toitoihoo)
				hansuu-=2
			if s.sanankoo+s.question_mark in yaku:
				yaku.remove(s.sanankoo+s.question_mark)
				hansuu-=2
			if s.sanankoo in yaku:
				yaku.remove(s.sanankoo)
				hansuu-=2

		#daisangen
		if ['kootsu',5,5,5,'z'] in hoorakei and ['kootsu',6,6,6,'z'] in hoorakei and ['kootsu',7,7,7,'z'] in hoorakei:
			yaku.append(s.daisangen)
			hansuu+=13
			yakuman=True
			if s.yakuhai_haku in yaku:
				yaku.remove(s.yakuhai_haku)
				hansuu-=1
			if s.yakuhai_hatsu in yaku:
				yaku.remove(s.yakuhai_hatsu)
				hansuu-=1
			if s.yakuhai_chun in yaku:
				yaku.remove(s.yakuhai_chun)
				hansuu-=1

		#tsuuiisoo
		if sum(tehai9)==14==sum(tehai9[31:]):
			yaku.append(s.tsuuiisoo)
			hansuu+=13
			yakuman=True

		#shousuushii
		if hoorakei[0] in (['jantou',i,i,None,'z'] for i in range(1,5)) and all(i in hoorakei or hoorakei[0][1]==i[1] for i in (['kootsu',j,j,j,'z'] for j in range(1,5))):
			yaku.append(s.shousuushii)
			hansuu+=13
			yakuman=True

		#ryuuiisoo
		if sum(tehai9)==14==tehai9[22]+tehai9[23]+tehai9[24]+tehai9[26]+tehai9[28]+tehai9[36]:
			yaku.append(s.ryuuiisoo)
			hansuu+=13
			yakuman=True

		#chinroutou
		if sum(tehai9)==14==tehai9[1]+tehai9[9]+tehai9[11]+tehai9[19]+tehai9[21]+tehai9[29]:
			yaku.append(s.chinroutou)
			hansuu+=13
			yakuman=True
			if s.toitoihoo in yaku:
				yaku.remove(s.toitoihoo)
				hansuu-=2

		#chuurenpouton
		#not checking menzenchin
		if sum(tehai9)==14 and any(tehai9[i+1]>=3 and all(tehai9[i+2:i+9]) and tehai9[i+9]>=3 for i in (0,10,20)):
			if tsumo==False:
				if tsumohai%10 in (1,9) and tehai9[tsumohai]==4 or tehai9[tsumohai]==2:
					yaku.append(s.junseichuurenpouton)
					hansuu+=26
					yakuman=True
				else:
					yaku.append(s.chuurenpouton)
					hansuu+=13
					yakuman=True
			else:
				yaku.append(s.chuurenpouton)
				hansuu+=13
				yakuman=True
			if s.chiniisoo in yaku:
				yaku.remove(s.chiniisoo)
				hansuu-=6#not checking kuisagari

		#daisuushii
		if ['kootsu',1,1,1,'z'] in hoorakei and ['kootsu',2,2,2,'z'] in hoorakei and ['kootsu',3,3,3,'z'] in hoorakei and ['kootsu',4,4,4,'z'] in hoorakei:
			yaku.append(s.daisuushii)
			hansuu+=26
			yakuman=True
			yaku.remove(s.yakuhai_ton+s.question_mark)
			yaku.remove(s.yakuhai_nan+s.question_mark)
			yaku.remove(s.yakuhai_shaa+s.question_mark)
			yaku.remove(s.yakuhai_pei+s.question_mark)
			hansuu-=4
			if len(hoorakei)==5 and s.toitoihoo in yaku:
				yaku.remove(s.toitoihoo)
				hansuu-=2

	#output
	if dahai:
		print(s.da,"["+hai_[hai.index(dahai)]+"]",end=" ")
	if tsumo:
		print(s.hoora+" | ",end="")
	elif tsumo==False and karaten:
		print(s.karaten,"["+hai_[tsumohai],end="] | ")
	elif tsumo==False and not karaten:
		print(s.tenpai,"["+hai_[tsumohai],end="] | ")
	for j in hoorakei:
		for k in j[1:]:
			if k:
				print(k,end="")
		print(" ",end="")
	print("|",end="")
	if yakuman and hansuu>=13:
		print(" "+s.yakuman_level_list[hansuu//13],end=s.colon)
	elif not yakuman and hansuu>=13:
		print(" "+s.kazoeyakuman+"("+str(hansuu)+s.han+")",end=s.colon)
	elif hansuu>0:
		print(str(hansuu).rjust(3)+s.han,end=s.colon)
	for j in yaku:
		print(j,end=(s.ideographic_comma if yaku.index(j)!=len(yaku)-1 else ""))
	print()

	return hansuu

def main(tehai=None,dahai=False):
	global s
	#input tehai
	if tehai==None:
		try:
			tehai=input(s.ask_input_tehai+s.colon)
		except:
			return
	if True:
		if tehai.lower() in ("exit","退出","イグジスト"):
			sys.exit()
		elif tehai.lower() in ("help","帮助","幫助","ヘルプ"):
			print()
			print(s.help)
			return
		elif tehai.lower() in ("about","关于"):
			print()
			print("胡祥又 Hu Xiangyou\nversion 0.0 December 17, 2018\nversion 1.0 February 9, 2019\nversion 1.1 February 20, 2019\nversion 1.2 March 20, 2019\nversion 2.0 April 14, 2019")
			print(s.help)
			return
		elif tehai.lower() in ("example","examples","举例","舉例","例","例え","test","tests","测试","測試","テスト"):
			test=random.choice((
				"1112345678999m",#junseichuurenpouton
				"19m19p19s1234567z",#kokushimusoujuusanmen
				"234m234m234m222p5m",
				"1112223334445z",#daisuushii suankootanki tsuuiisoo
				"2233445566778s",#daichikurin
				"2223334446668s",#ryuuiisoo suankootanki
				"11p11155566677z",#shousangen or daisangen
				"1122334455667z",#daichisei
				"1234445677889p",#from majsoul 2018 TOP 14 by Yezhicha
				"22266688m22p222s",#from majsoul 2018 TOP 5 by Longling
				"11111111111122222222222233333333333344444444444455555555555666666777777888888999999",#test only
			))
			print(test)
			main(tehai=test)
			return
		elif tehai.lower() in ('lang','language','languages','语言','語言','言語'):
			print('romaji, kanji, kana, ja, zh')
			return
		elif tehai.lower() in ('romaji','ローマ字','罗马字','羅馬字'):
			s=romaji
			print(s.language_switched)
			return
		elif tehai.lower() in ('kanji','漢字','汉字'):
			s=kanji
			print(s.language_switched)
			return
		elif tehai.lower() in ('katakana','kana','カタカナ','片仮名','片假名','仮名','假名'):
			s=katakana
			print(s.language_switched)
			return
		elif tehai.lower() in ('tsuujou','general','ja','日本語','日语','日語','日本语','通常','一般'):
			s=ja
			print(s.language_switched)
			return
		elif tehai.lower() in ('zh','cn','中国語','中文'):
			s=zh
			print(s.language_switched)
			return
		elif tehai.lower() in dir(s):
			print(vars(s)[tehai])
			return

	for i in (' ','!','"','#','$','%','&','\'','(',')','*','+',',','-','.','/',':',';','<','=','>','?','@','[','\\',']','^','_','`','{','|','}','~','　'):
		tehai=tehai.replace(i,'')
	if tehai=='':
		return

	#manage tehai
	tehai_managed=[]
	shurui=''
	shurui_used=True
	for i in range(-1,-len(tehai)-1,-1):
		if tehai[i].isupper() or tehai[i] in ('東','南','西','北','白','發','中','东','発','发'):
			if shurui_used==False:
				tehai_managed.insert(0,['',shurui])
				shurui_used=True
			tehai_managed.insert(0,['',tehai[i]])
		elif tehai[i].islower() or tehai[i] in ('ｍ','ｗ','ｐ','ｓ','万','萬','筒','饼','餠','餅','索','条','條'):
			if shurui_used==False:
				tehai_managed.insert(0,['',shurui])
				shurui_used=True
			shurui=tehai[i]
			shurui_used=False
		elif tehai[i].isdecimal():
			tehai_managed.insert(0,[int(tehai[i]),shurui])
			if shurui!='':
				shurui_used=True
		else:
			if shurui_used==False:
				tehai_managed.insert(0,['',shurui])
				shurui_used=True
			tehai_managed.insert(0,['',tehai[i]])
	if shurui_used==False:
		tehai_managed.insert(0,['',shurui])

	#number only
	number_only=False
	if tehai.isdecimal():
		number_only=True
		tehai_managed=[[int(i),'m'] if i!=0 else [5,'m'] for i in tehai]

	#group tehai
	manzu=[]
	pinzu=[]
	soozu=[]
	jihai=[]
	tehai1=[]
	has_0=False
	has_0m=False
	has_0p=False
	has_0s=False
	invalid_input=False
	for i in tehai_managed:
		if i[1] in ('m','w','ｍ','ｗ','万' ,'萬'):
			if type(i[0])!=int and not i[0].isdecimal():
				if invalid_input and not dahai:
					print(str(i[0])+i[1],end=" ")
				elif not invalid_input and not dahai:
					print(s.has_invalid_input,str(i[0])+i[1],end=" ")
					invalid_input=True
			elif i[0]==0:
				if number_only:
					has_0=True
				else:
					has_0m=True
				manzu.append(5)
			else:
				manzu.append(i[0])
		elif i[1] in ('p','ｐ','筒','饼','餠','餅'):
			if type(i[0])!=int and not i[0].isdecimal():
				if invalid_input and not dahai:
					print(str(i[0])+i[1],end=" ")
				elif not invalid_input and not dahai:
					print(s.has_invalid_input,str(i[0])+i[1],end=" ")
					invalid_input=True
			elif i[0]==0:
				has_0p=True
				pinzu.append(5)
			else:
				pinzu.append(i[0])
		elif i[1] in ('s','ｓ','索','条','條'):
			if type(i[0])!=int and not i[0].isdecimal():
				if invalid_input and not dahai:
					print(str(i[0])+i[1],end=" ")
				elif not invalid_input and not dahai:
					print(s.has_invalid_input,str(i[0])+i[1],end=" ")
					invalid_input=True
			elif i[0]==0:
				has_0s=True
				soozu.append(5)
			else:
				soozu.append(i[0])
		elif i[1]=='z':
			if type(i[0])!=int and not i[0].isdecimal():
				if invalid_input and not dahai:
					print(str(i[0])+i[1],end=" ")
				elif not invalid_input and not dahai:
					print(s.has_invalid_input,str(i[0])+i[1],end=" ")
					invalid_input=True
			elif i[0] in [0,8,9]:
				if invalid_input and not dahai:
					print(str(i[0])+i[1],end=" ")
				elif not invalid_input and not dahai:
					print(s.has_invalid_input,str(i[0])+i[1],end=" ")
					invalid_input=True
			else:
				jihai.append(i[0])
		elif i[1] in ('E','Ｅ','東','东'):
			jihai.append(1)
		elif i[1] in ('S','Ｓ','南'):
			jihai.append(2)
		elif i[1] in ('W','Ｗ','西'):
			jihai.append(3)
		elif i[1] in ('N','Ｎ','北'):
			jihai.append(4)
		elif i[1] in ('P','D','Ｐ','Ｄ','白'):
			jihai.append(5)
		elif i[1] in ('F','H','R','Ｆ','Ｈ','Ｒ','發','発','发'):
			jihai.append(6)
		elif i[1] in ('C','Ｃ','中'):
			jihai.append(7)
		else:
			if invalid_input and not dahai:
				print(str(i[0])+i[1],end=" ")
			elif not invalid_input and not dahai:
				print(s.has_invalid_input,str(i[0])+i[1],end=" ")
				invalid_input=True

	if has_0:
		if invalid_input:
			print()
		print(s.has_0)
	elif has_0m or has_0p or has_0s:
		if invalid_input:
			print()
		if has_0m:
			print(s.has_0m)
		if has_0p:
			print(s.has_0p)
		if has_0s:
			print(s.has_0s)

	#count tehai
	tehai9=[0]*38
	for i in manzu:
		tehai9[i]+=1
	for i in pinzu:
		tehai9[i+10]+=1
	for i in soozu:
		tehai9[i+20]+=1
	for i in jihai:
		tehai9[i+30]+=1
	hai=('',[1,'m'],[2,'m'],[3,'m'],[4,'m'],[5,'m'],[6,'m'],[7,'m'],[8,'m'],[9,'m'],
	'',[1,'p'],[2,'p'],[3,'p'],[4,'p'],[5,'p'],[6,'p'],[7,'p'],[8,'p'],[9,'p'],
	'',[1,'s'],[2,'s'],[3,'s'],[4,'s'],[5,'s'],[6,'s'],[7,'s'],[8,'s'],[9,'s'],
	'',[1,'z'],[2,'z'],[3,'z'],[4,'z'],[5,'z'],[6,'z'],[7,'z'])
	hai_=('','1m','2m','3m','4m','5m','6m','7m','8m','9m',
	'','1p','2p','3p','4p','5p','6p','7p','8p','9p',
	'','1s','2s','3s','4s','5s','6s','7s','8s','9s',
	'','東','南','西','北','白','發','中')
	if number_only:
		hai=('',[1,''],[2,''],[3,''],[4,''],[5,''],[6,''],[7,''],[8,''],[9,''],'')
		hai_=('','1','2','3','4','5','6','7','8','9','')

	if sum(tehai9)==0:
		print()
		return False

	#show tehai
	if not dahai:
		print()
		print(s.tehai,end=s.colon)
		if not number_only:
			if len(manzu)>0:
				for i in manzu:
					print(str(i),end="")
				print("m",end=" ")
			if len(pinzu)>0:
				for i in pinzu:
					print(str(i),end="")
				print("p",end=" ")
			if len(soozu)>0:
				for i in soozu:
					print(str(i),end="")
				print("s",end=" ")
			if len(jihai)>0:
				for i in jihai:
					print(hai_[i+30],end="")
					print(end=" ")
		else:
			for i in manzu:
				print(str(i),end="")
			print(end=" ")
		print("("+str(sum(tehai9))+")\n")

		for i in range(len(tehai9)):
			if tehai9[i]>4:
				print(hai_[i]+s.more_than_4)

		if sum(tehai9)>14:
			print(str(sum(tehai9))+s.more_than_14)
			print()
		if sum(tehai9)<13:
			print(str(sum(tehai9))+s.less_than_13)
			print()

	mentsusuu=sum(tehai9)//3
	tenpai=False
	beginning_cosmos=False
	kouten=[]

	if sum(tehai9)==tehai9[35]==18:
		beginning_cosmos=True
		tsumo=True
	elif sum(tehai9)%3==2:
		tsumo=True
	elif sum(tehai9)%3==1:
		tsumo=False
		agarihai=[]
	elif sum(tehai9)%3==0:
		tsumo=None
		print(str(sum(tehai9))+s.taapai_or_shaopai)
		return

	if not dahai and 50<sum(tehai9):
		if input(s.low_speed)!='':
			return
	start_time=datetime.datetime.now()

	for tsumohai in ((1,2,3,4,5,6,7,8,9,11,12,13,14,15,16,17,18,19,21,22,23,24,25,26,27,28,29,31,32,33,34,35,36,37) if not number_only else (1,2,3,4,5,6,7,8,9)):
		karaten=False

		if tsumo==False:
			tehai9[tsumohai]+=1
			if tehai9[tsumohai]==5:
				karaten=True

		hoora=False
		hoorakeis=[]
		hansuu=[]

		#kokushimusou
		if sum(tehai9)==14 and tehai9[1] and tehai9[9] and tehai9[11] and tehai9[19] and tehai9[21] and tehai9[29] and all(tehai9[31:]) and not any(tehai9[2:9]) and not any(tehai9[12:19]) and not any(tehai9[22:29]):
			hoora=True
			hoorakei_temp=[['jantou',hai[tehai9.index(2)][0],hai[tehai9.index(2)][0],None,hai[tehai9.index(2)][1]]]
			for i in range(38):
				if tehai9[i]==1:
					hoorakei_temp.append(['tanpai',hai[i][0],None,None,hai[i][1]])
			hoorakeis.append(hoorakei_temp)
			hansuu.append(yaku_and_output(tehai9,hoorakei_temp,tsumo,karaten,tsumohai,dahai,number_only))

		#chiitoitsu
		if sum(tehai9)==14 and tehai9.count(2)==7:
			hoora=True
			hoorakei_temp=[]
			for i in range(38):
				if tehai9[i]==2:
					hoorakei_temp.append(['toitsu',hai[i][0],hai[i][0],None,hai[i][1] if not number_only else ''])
			hoorakeis.append(hoorakei_temp)
			hansuu.append(yaku_and_output(tehai9,hoorakei_temp,tsumo,karaten,tsumohai,dahai,number_only))

		#analyse tehai
		#jantou
		for jantou_i in range(38):
			if tehai9[jantou_i]>=2:
				hoorakei_temp=[['jantou',hai[jantou_i][0],hai[jantou_i][0],None,hai[jantou_i][1]]]
				tehai_temp=tehai9.copy()
				tehai_temp[jantou_i]-=2
			else:
				continue

			#mentsu
			for mentsu_i in range(mentsusuu+1):
				if tehai_temp==None:
					continue
				elif sum(tehai_temp)==0:
					hoora=True
					hoorakei_temp.sort(key=lambda elem: (elem[0],elem[4],elem[1],elem[2],elem[3]))
					if hoorakei_temp not in hoorakeis:
						hoorakeis.append(hoorakei_temp)
						hansuu.append(yaku_and_output(tehai9,hoorakei_temp,tsumo,karaten,tsumohai,dahai,number_only))
						#if sanrenkoo then change to 3-shuntsu
						hoorakei_new_num=1
						while hoorakei_new_num:
							temp=hoorakei_new_num
							hoorakei_new_num=0
							for hoorakei_i in hoorakeis[-temp:]:
								for mentsu_picked_i in hoorakei_i[1:]:
									if mentsu_picked_i[0]=='kootsu' and mentsu_picked_i[1]<=7 and mentsu_picked_i[4]!='z' and ['kootsu',mentsu_picked_i[1]+1,mentsu_picked_i[1]+1,mentsu_picked_i[1]+1,mentsu_picked_i[4]] in hoorakei_i and ['kootsu',mentsu_picked_i[1]+2,mentsu_picked_i[1]+2,mentsu_picked_i[1]+2,mentsu_picked_i[4]] in hoorakei_i:
										hoorakei_temp=hoorakei_i.copy()
										hoorakei_temp.remove(mentsu_picked_i)
										hoorakei_temp.remove(['kootsu',mentsu_picked_i[1]+1,mentsu_picked_i[1]+1,mentsu_picked_i[1]+1,mentsu_picked_i[4]])
										hoorakei_temp.remove(['kootsu',mentsu_picked_i[1]+2,mentsu_picked_i[1]+2,mentsu_picked_i[1]+2,mentsu_picked_i[4]])
										hoorakei_temp.extend([['shuntsu',mentsu_picked_i[1],mentsu_picked_i[1]+1,mentsu_picked_i[1]+2,mentsu_picked_i[4]]]*3)
										hoorakei_temp.sort(key=lambda elem: (elem[0],elem[4],elem[1],elem[2],elem[3]))
										if hoorakei_temp not in hoorakeis:
											hoorakeis.append(hoorakei_temp)
											hoorakei_new_num+=1
											hansuu.append(yaku_and_output(tehai9,hoorakei_temp,tsumo,karaten,tsumohai,dahai,number_only))
					continue
				for hai_picked in range(len(tehai_temp)):
					if tehai_temp[hai_picked]==0:
						continue
					elif tehai_temp[hai_picked]>=3:
						#kootsu exists
						tehai_temp[hai_picked]-=3
						hoorakei_temp.append(['kootsu',hai[hai_picked][0],hai[hai_picked][0],hai[hai_picked][0],hai[hai_picked][1]])
						break
					elif hai_picked<28 and tehai_temp[hai_picked] and tehai_temp[hai_picked+1] and tehai_temp[hai_picked+2]:
						#shuntsu exists
						tehai_temp[hai_picked]-=1
						tehai_temp[hai_picked+1]-=1
						tehai_temp[hai_picked+2]-=1
						hoorakei_temp.append(['shuntsu',hai[hai_picked][0],hai[hai_picked+1][0],hai[hai_picked+2][0],hai[hai_picked][1]])
						break
					else:
						#neither kootsu nor shuntsu exists
						hoorakei_temp=None
						tehai_temp=None
						break

		if hoora:
			hoorakeis.sort()

		if hoora and tsumo==False and not karaten and tsumohai not in agarihai:
			agarihai.append(tsumohai)

		if tsumo and not hoora:
			if beginning_cosmos:
				pass
			else:
				print(s.not_hoora)
			break

		if tsumo==False and hoora:
			tenpai=True

		if hoora and not karaten:
			if max(hansuu)>=13:
				kouten.append(max(hansuu)//13*13)
			else:
				kouten.append(max(hansuu))

		if tsumo:
			break
		if tsumo==False:
			tehai9[tsumohai]-=1

	#beginning of the cosmos
	if beginning_cosmos:
		print(s.hoora+" | 55z 5555z 5555z 5555z 5555z | "+s.beginning_of_the_cosmos+"(140"+s.fuu+"105"+s.han+" 90865195024359483499283685761351700"+s.ten+")"+s.colon+s.tsuuiisoo+s.ideographic_comma+s.sanankoo+s.ideographic_comma+s.suukantsu+s.ideographic_comma+s.rinshankaihou+s.ideographic_comma+s.yakuhai_haku+"4"+s.ideographic_comma+s.dora+"72")

	#tenpai
	if not dahai and tsumo==False and tenpai and agarihai and not number_only:
		agarihai_han=list(zip(agarihai,kouten))
		agarihai_han.sort(key=lambda elem: (elem[1],elem[0]))

		print()
		print(s.tenpai,end=s.colon)
		for agarihai_han_i in range(len(agarihai_han)):
			print(hai_[agarihai_han[agarihai_han_i][0]],end=" ")
			if(agarihai_han_i!=len(agarihai_han)-1 and agarihai_han[agarihai_han_i][1]!=agarihai_han[agarihai_han_i+1][1]) or agarihai_han_i==len(agarihai_han)-1 and sum(tehai9)<=14:
				if agarihai_han[agarihai_han_i][1]>=13:
					print("("+s.yakuman_level_list[agarihai_han[agarihai_han_i][1]//13],end=") ")
				else:
					print("("+str(agarihai_han[agarihai_han_i][1])+s.han,end=") ")
		print()
	elif not dahai and tsumo==False and tenpai and agarihai and number_only:
		print()
		print(s.tenpai,end=s.colon)
		for agarihai_i in agarihai:
			print(hai_[agarihai_i],end=" ")
		print()

	if not dahai and tsumo==False and not tenpai:
		print(s.nooten)

	end_time=datetime.datetime.now()
	time_spent=(end_time-start_time).total_seconds()
	if not dahai and time_spent>1.0:
		print(s.time_spent1,round(time_spent,1),s.time_spent2)

	#dahai
	if tsumo and not hoora:
		tehai_managed=list(zip(manzu,['m']*len(manzu)))+list(zip(pinzu,['p']*len(pinzu)))+list(zip(soozu,['s']*len(soozu)))+list(zip(jihai,['z']*len(jihai)))
		if number_only:
			tehai_managed=[(tehai_managed[i][0],'') for i in range(len(tehai_managed))]
		for sutehai_i in range(len(tehai_managed)):
			if list(tehai_managed[sutehai_i]) in hai and tehai_managed[sutehai_i]!=tehai_managed[sutehai_i-1]:
				tehai_managed_new=tehai_managed.copy()
				tehai_managed_new.remove(tehai_managed[sutehai_i])
				tehai_new=str(tehai_managed_new).replace('(','').replace(')','').replace('[','').replace(']','').replace(',','').replace(' ','').replace('\'','')
				main(tehai=tehai_new,dahai=list(tehai_managed[sutehai_i]))

while True:
	main()
	print("\n**************\n")
