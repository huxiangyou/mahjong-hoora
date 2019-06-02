# -*- coding: utf-8 -*-
#!/usr/bin/python3
#python 3.7.1 3.7.2

"""
version 0.0 coded by Hu Xiangyou on December 17, 2018
version 1.0 coded by Hu Xiangyou on February 9, 2019
version 1.1 coded by Hu Xiangyou on February 20, 2019
version 1.2 coded by Hu Xiangyou on March 20, 2019

manage tehai of mahjong

for details, check README.md
"""

import datetime
from lang import romaji, kanji, katakana, ja, zh
s=zh # change "zh" to other language if you need: romaji, kanji, katakana, ja, zh

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
			import sys
			sys.exit()
		elif tehai.lower() in ("help","帮助","幫助","ヘルプ"):
			print()
			print(s.help)
			return
		elif tehai.lower() in ("about",):
			print()
			print("胡祥又","Hu Xiangyou")
			print("version 0.0","December 17, 2018")
			print("version 1.0","February 9, 2019")
			print("version 1.1","February 20, 2019")
			print("version 1.2","March 20, 2019")
			print(s.help)
			return
		elif tehai.lower() in ("example","examples"):
			print()
			print("1112345678999m")
			print("19m19p19s1234567z")
			print("234234234m222p5m")
			print("1112223334445z")
			print("2233445566778s")
			print(s.help)
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
		if tehai.lower() in dir(s):
			print(vars(s)[tehai])
			return

	for i in (' ','!','"','#','$','%','&','\'','(',')','*','+',',','-','.','/',':',';','<','=','>','?','@','[','\\',']','^','_','`','{','|','}','~','　'):
		tehai=tehai.replace(i,'')
	if tehai=='':
		return None

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

	manzu.sort()
	pinzu.sort()
	soozu.sort()
	jihai.sort()

	#count tehai
	manzu9=[0]*10
	pinzu9=[0]*10
	soozu9=[0]*10
	jihai9=[0]*8
	for i in manzu:
		manzu9[i]+=1
	for i in pinzu:
		pinzu9[i]+=1
	for i in soozu:
		soozu9[i]+=1
	for i in jihai:
		jihai9[i]+=1

	tehai9=manzu9+pinzu9+soozu9+jihai9
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
	yakuman_level=s.yakuman_level_list

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

	if sum(tehai9)==jihai9[5]==18:
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

	if not dahai and sum(tehai9)>60:
		if input(s.low_speed+" (y/n)")=='n':
			return
	start_time=datetime.datetime.now()

	for tsumohai in ((1,2,3,4,5,6,7,8,9,11,12,13,14,15,16,17,18,19,21,22,23,24,25,26,27,28,29,31,32,33,34,35,36,37) if not number_only else (1,2,3,4,5,6,7,8,9)):
		karaten=False

		if tsumo==False:
			tehai9[tsumohai]+=1
			if 0<tsumohai<10:
				manzu9[tsumohai]+=1
			elif 10<tsumohai<20:
				pinzu9[tsumohai-10]+=1
			elif 20<tsumohai<30:
				soozu9[tsumohai-20]+=1
			elif 30<tsumohai<38:
				jihai9[tsumohai-30]+=1
			if tehai9[tsumohai]==5:
				karaten=True

		hoora=False
		hoorakei=[]
		hoorakei_=[]
		yaku=[]
		hansuu=[]
		yakuman=[]
		fuusuu_calculate=lambda fuu,han: str(((fuu*(2**(han+2))*4)//100+1)*100)

		#kokushimusou
		if sum(tehai9)==14 and manzu9[1]>=1 and manzu9[9]>=1 and pinzu9[1]>=1 and pinzu9[9]>=1 and soozu9[1]>=1 and soozu9[9]>=1 and all(jihai9[1:]) and not any(manzu9[2:9]+pinzu9[2:9]+soozu9[2:9]):
			hoora=True
			hoorakei_temp=[['jantou',hai[tehai9.index(2)][0],hai[tehai9.index(2)][0],None,hai[tehai9.index(2)][1]]]
			for i in range(38):
				if tehai9[i]==1:
					hoorakei_temp.append(['tanpai',hai[i][0],None,None,hai[i][1]])
			hoorakei_.append(hoorakei_temp)
			if tehai9[tsumohai]==2:
				yaku.append([s.kokushimusoujuusanmen])
				hansuu.append(26)
				yakuman.append(True)
			else:
				yaku.append([s.kokushimusou])
				hansuu.append(13)
				yakuman.append(True)

		#chiitoitsu
		if sum(tehai9)==14 and tehai9.count(2)==7:
			hoora=True
			hoorakei_temp=[]
			for i in range(38):
				if tehai9[i]==2:
					hoorakei_temp.append(['toitsu',hai[i][0],hai[i][0],None,hai[i][1] if not number_only else ''])
			hoorakei_.append(hoorakei_temp)
			yaku.append([])
			hansuu.append(0)
			yakuman.append(False)

		#analyse tehai
		tehai_temp=[]
		hoorakei_temp=[]

		#jantou
		for jantou_i in range(len(tehai9)):
			if tehai9[jantou_i]>=2:
				hoorakei_temp.append([['jantou',hai[jantou_i][0],hai[jantou_i][0],None,hai[jantou_i][1]]])
				tehai_temp.append(tehai9.copy())
				tehai_temp[-1][jantou_i]-=2

		#mentsu
		for i in range(mentsusuu+1):
			for tehai_left_i in range(len(tehai_temp)):
				if tehai_temp[tehai_left_i]==None:
					continue
				elif sum(tehai_temp[tehai_left_i])==0:
					hoora=True
					hoorakei_temp[tehai_left_i].sort(key=lambda elem: (elem[0],elem[4],elem[1],elem[2],elem[3]))
					if hoorakei_temp[tehai_left_i] not in hoorakei_:
						hoorakei_.append(hoorakei_temp[tehai_left_i])
					yaku.append([])
					hansuu.append(0)
					yakuman.append(False)
					continue
				for hai_picked in range(len(tehai_temp[tehai_left_i])):
					if tehai_temp[tehai_left_i][hai_picked]==0:
						continue
					elif hai_picked<28 and tehai_temp[tehai_left_i][hai_picked]>=3 and tehai_temp[tehai_left_i][hai_picked+1]>=1 and tehai_temp[tehai_left_i][hai_picked+2]>=1:
						#both kootsu and shuntsu may exist
						#copy one for shuntsu
						hoorakei_temp.append(hoorakei_temp[tehai_left_i].copy())
						tehai_temp.append(tehai_temp[tehai_left_i].copy())
						#kootsu
						tehai_temp[tehai_left_i][hai_picked]-=3
						hoorakei_temp[tehai_left_i].append(['kootsu',hai[hai_picked][0],hai[hai_picked][0],hai[hai_picked][0],hai[hai_picked][1]])
						#shuntsu
						tehai_temp[-1][hai_picked]-=1
						tehai_temp[-1][hai_picked+1]-=1
						tehai_temp[-1][hai_picked+2]-=1
						hoorakei_temp[-1].append(['shuntsu',hai[hai_picked][0],hai[hai_picked+1][0],hai[hai_picked+2][0],hai[hai_picked][1]])
						break
					elif tehai_temp[tehai_left_i][hai_picked]>=3:
						#only kootsu may exist
						tehai_temp[tehai_left_i][hai_picked]-=3
						hoorakei_temp[tehai_left_i].append(['kootsu',hai[hai_picked][0],hai[hai_picked][0],hai[hai_picked][0],hai[hai_picked][1]])
						break
					elif hai_picked<28 and tehai_temp[tehai_left_i][hai_picked]>=1 and tehai_temp[tehai_left_i][hai_picked+1]>=1 and tehai_temp[tehai_left_i][hai_picked+2]>=1:
						#only shuntsu may exist
						tehai_temp[tehai_left_i][hai_picked]-=1
						tehai_temp[tehai_left_i][hai_picked+1]-=1
						tehai_temp[tehai_left_i][hai_picked+2]-=1
						hoorakei_temp[tehai_left_i].append(['shuntsu',hai[hai_picked][0],hai[hai_picked+1][0],hai[hai_picked+2][0],hai[hai_picked][1]])
						break
					else:
						#neither kootsu nor shuntsu may exist
						hoorakei_temp[tehai_left_i]=None
						tehai_temp[tehai_left_i]=None
						break

		if hoora:
			hoorakei_.sort()

		for hoorakei_i in range(len(hoorakei_)):

			#yaku
			if sum(tehai9)>14:
				pass
			else:
				#chiitoitsu
				if len(hoorakei_[hoorakei_i])==7 and all(i[0]=='toitsu' for i in hoorakei_[hoorakei_i]):
					yaku[hoorakei_i].append(s.chiitoitsu)
					hansuu[hoorakei_i]+=2

				#tanyaochuu
				if sum(tehai9)==14 and manzu9[1]+manzu9[9]+pinzu9[1]+pinzu9[9]+soozu9[1]+soozu9[9]+sum(jihai9)==0:
					yaku[hoorakei_i].append(s.tanyaochuu)
					hansuu[hoorakei_i]+=1

				#yakuhai
				#not checking chanfon and menfon
				#ton
				if ['kootsu',1,1,1,'z'] in hoorakei_[hoorakei_i]:
					yaku[hoorakei_i].append(s.yakuhai_ton+s.question_mark)
					hansuu[hoorakei_i]+=1
				#nan
				if ['kootsu',2,2,2,'z'] in hoorakei_[hoorakei_i]:
					yaku[hoorakei_i].append(s.yakuhai_nan+s.question_mark)
					hansuu[hoorakei_i]+=1
				#shaa
				if ['kootsu',3,3,3,'z'] in hoorakei_[hoorakei_i]:
					yaku[hoorakei_i].append(s.yakuhai_shaa+s.question_mark)
					hansuu[hoorakei_i]+=1
				#pei
				if ['kootsu',4,4,4,'z'] in hoorakei_[hoorakei_i]:
					yaku[hoorakei_i].append(s.yakuhai_pei+s.question_mark)
					hansuu[hoorakei_i]+=1
				if (['kootsu',1,1,1,'z'] in hoorakei_[hoorakei_i] and ['kootsu',2,2,2,'z'] in hoorakei_[hoorakei_i] and ['kootsu',3,3,3,'z'] in hoorakei_[hoorakei_i]) or \
				(['kootsu',1,1,1,'z'] in hoorakei_[hoorakei_i] and ['kootsu',2,2,2,'z'] in hoorakei_[hoorakei_i] and ['kootsu',4,4,4,'z'] in hoorakei_[hoorakei_i]) or \
				(['kootsu',1,1,1,'z'] in hoorakei_[hoorakei_i] and ['kootsu',3,3,3,'z'] in hoorakei_[hoorakei_i] and ['kootsu',4,4,4,'z'] in hoorakei_[hoorakei_i]) or \
				(['kootsu',2,2,2,'z'] in hoorakei_[hoorakei_i] and ['kootsu',3,3,3,'z'] in hoorakei_[hoorakei_i] and ['kootsu',4,4,4,'z'] in hoorakei_[hoorakei_i]):
					hansuu[hoorakei_i]-=1
				#haku
				if ['kootsu',5,5,5,'z'] in hoorakei_[hoorakei_i]:
					yaku[hoorakei_i].append(s.yakuhai_haku+(str(hoorakei_[hoorakei_i].count(['kootsu',5,5,5,'z'])) if hoorakei_[hoorakei_i].count(['kootsu',5,5,5,'z'])>1 else ''))
					hansuu[hoorakei_i]+=hoorakei_[hoorakei_i].count(['kootsu',5,5,5,'z'])
				#hatsu
				if ['kootsu',6,6,6,'z'] in hoorakei_[hoorakei_i]:
					yaku[hoorakei_i].append(s.yakuhai_hatsu+(str(hoorakei_[hoorakei_i].count(['kootsu',6,6,6,'z'])) if hoorakei_[hoorakei_i].count(['kootsu',6,6,6,'z'])>1 else ''))
					hansuu[hoorakei_i]+=hoorakei_[hoorakei_i].count(['kootsu',6,6,6,'z'])
				#chun
				if ['kootsu',7,7,7,'z'] in hoorakei_[hoorakei_i]:
					yaku[hoorakei_i].append(s.yakuhai_chun+(str(hoorakei_[hoorakei_i].count(['kootsu',7,7,7,'z'])) if hoorakei_[hoorakei_i].count(['kootsu',7,7,7,'z'])>1 else ''))
					hansuu[hoorakei_i]+=hoorakei_[hoorakei_i].count(['kootsu',7,7,7,'z'])

				#pinfu
				#not checking chanfon and menfon
				if len(hoorakei_[hoorakei_i])==5 and \
				all(i[0]=='shuntsu' for i in hoorakei_[hoorakei_i][1:])and \
				hoorakei_[hoorakei_i][0]!=['jantou',5,5,None,'z'] and \
				hoorakei_[hoorakei_i][0]!=['jantou',6,6,None,'z'] and \
				hoorakei_[hoorakei_i][0]!=['jantou',7,7,None,'z']:
					if tsumo==False:
						if ((hai[tsumohai][0]==hoorakei_[hoorakei_i][1][1]!=7 or hai[tsumohai][0]==hoorakei_[hoorakei_i][1][3]!=3) and hai[tsumohai][1]==hoorakei_[hoorakei_i][1][4]) or \
						((hai[tsumohai][0]==hoorakei_[hoorakei_i][2][1]!=7 or hai[tsumohai][0]==hoorakei_[hoorakei_i][2][3]!=3) and hai[tsumohai][1]==hoorakei_[hoorakei_i][2][4]) or \
						((hai[tsumohai][0]==hoorakei_[hoorakei_i][3][1]!=7 or hai[tsumohai][0]==hoorakei_[hoorakei_i][3][3]!=3) and hai[tsumohai][1]==hoorakei_[hoorakei_i][3][4]) or \
						((hai[tsumohai][0]==hoorakei_[hoorakei_i][4][1]!=7 or hai[tsumohai][0]==hoorakei_[hoorakei_i][4][3]!=3) and hai[tsumohai][1]==hoorakei_[hoorakei_i][4][4]):
							if hoorakei_[hoorakei_i][0][4]=='z':
								yaku[hoorakei_i].append(s.pinfu+s.question_mark)
								hansuu[hoorakei_i]+=1
							else:
								yaku[hoorakei_i].append(s.pinfu)
								hansuu[hoorakei_i]+=1
					else:
						yaku[hoorakei_i].append(s.pinfu+s.question_mark)
						hansuu[hoorakei_i]+=1

				#iipeekoo
				#not checking menzenchin
				if len(hoorakei_[hoorakei_i])>=5:
					if (hoorakei_[hoorakei_i][-1]==hoorakei_[hoorakei_i][-2] and hoorakei_[hoorakei_i][-1][0]==hoorakei_[hoorakei_i][-2][0]=='shuntsu') or \
					(hoorakei_[hoorakei_i][-1]==hoorakei_[hoorakei_i][-3] and hoorakei_[hoorakei_i][-1][0]==hoorakei_[hoorakei_i][-3][0]=='shuntsu') or \
					(hoorakei_[hoorakei_i][-1]==hoorakei_[hoorakei_i][-4] and hoorakei_[hoorakei_i][-1][0]==hoorakei_[hoorakei_i][-4][0]=='shuntsu') or \
					(hoorakei_[hoorakei_i][-2]==hoorakei_[hoorakei_i][-3] and hoorakei_[hoorakei_i][-2][0]==hoorakei_[hoorakei_i][-3][0]=='shuntsu') or \
					(hoorakei_[hoorakei_i][-2]==hoorakei_[hoorakei_i][-4] and hoorakei_[hoorakei_i][-2][0]==hoorakei_[hoorakei_i][-4][0]=='shuntsu') or \
					(hoorakei_[hoorakei_i][-3]==hoorakei_[hoorakei_i][-4] and hoorakei_[hoorakei_i][-3][0]==hoorakei_[hoorakei_i][-4][0]=='shuntsu'):
						yaku[hoorakei_i].append(s.iipeekoo)
						hansuu[hoorakei_i]+=1

				#sanshokudoujun
				if len(hoorakei_[hoorakei_i])==5:
					if (hoorakei_[hoorakei_i][1][1:4]==hoorakei_[hoorakei_i][2][1:4]==hoorakei_[hoorakei_i][3][1:4] and hoorakei_[hoorakei_i][1][0]==hoorakei_[hoorakei_i][2][0]==hoorakei_[hoorakei_i][3][0]=='shuntsu' and (hoorakei_[hoorakei_i][1][4],hoorakei_[hoorakei_i][2][4],hoorakei_[hoorakei_i][3][4])==('m','p','s')) or \
					(hoorakei_[hoorakei_i][1][1:4]==hoorakei_[hoorakei_i][2][1:4]==hoorakei_[hoorakei_i][4][1:4] and hoorakei_[hoorakei_i][1][0]==hoorakei_[hoorakei_i][2][0]==hoorakei_[hoorakei_i][4][0]=='shuntsu' and (hoorakei_[hoorakei_i][1][4],hoorakei_[hoorakei_i][2][4],hoorakei_[hoorakei_i][4][4])==('m','p','s')) or \
					(hoorakei_[hoorakei_i][1][1:4]==hoorakei_[hoorakei_i][3][1:4]==hoorakei_[hoorakei_i][4][1:4] and hoorakei_[hoorakei_i][1][0]==hoorakei_[hoorakei_i][3][0]==hoorakei_[hoorakei_i][4][0]=='shuntsu' and (hoorakei_[hoorakei_i][1][4],hoorakei_[hoorakei_i][3][4],hoorakei_[hoorakei_i][4][4])==('m','p','s')) or \
					(hoorakei_[hoorakei_i][2][1:4]==hoorakei_[hoorakei_i][3][1:4]==hoorakei_[hoorakei_i][4][1:4] and hoorakei_[hoorakei_i][2][0]==hoorakei_[hoorakei_i][3][0]==hoorakei_[hoorakei_i][4][0]=='shuntsu' and (hoorakei_[hoorakei_i][2][4],hoorakei_[hoorakei_i][3][4],hoorakei_[hoorakei_i][4][4])==('m','p','s')):
						yaku[hoorakei_i].append(s.sanshokudoujun)
						hansuu[hoorakei_i]+=2#not counting kuisagari

				#ikkitsuukan
				if (['shuntsu',1,2,3,''] in hoorakei_[hoorakei_i] and ['shuntsu',4,5,6,''] in hoorakei_[hoorakei_i] and ['shuntsu',7,8,9,''] in hoorakei_[hoorakei_i]) or \
				(['shuntsu',1,2,3,'m'] in hoorakei_[hoorakei_i] and ['shuntsu',4,5,6,'m'] in hoorakei_[hoorakei_i] and ['shuntsu',7,8,9,'m'] in hoorakei_[hoorakei_i]) or \
				(['shuntsu',1,2,3,'p'] in hoorakei_[hoorakei_i] and ['shuntsu',4,5,6,'p'] in hoorakei_[hoorakei_i] and ['shuntsu',7,8,9,'p'] in hoorakei_[hoorakei_i]) or \
				(['shuntsu',1,2,3,'s'] in hoorakei_[hoorakei_i] and ['shuntsu',4,5,6,'s'] in hoorakei_[hoorakei_i] and ['shuntsu',7,8,9,'s'] in hoorakei_[hoorakei_i]):
					yaku[hoorakei_i].append(s.ikkitsuukan)
					hansuu[hoorakei_i]+=2#not counting kuisagari

				#honchantaiyaochuu
				if len(hoorakei_[hoorakei_i])==5 and \
				(((1 in hoorakei_[hoorakei_i][0] or 9 in hoorakei_[hoorakei_i][0]) and (hoorakei_[hoorakei_i][0][4]!='z')) or 'z' in hoorakei_[hoorakei_i][0]) and \
				(((1 in hoorakei_[hoorakei_i][1] or 9 in hoorakei_[hoorakei_i][1]) and (hoorakei_[hoorakei_i][1][4]!='z')) or 'z' in hoorakei_[hoorakei_i][1]) and \
				(((1 in hoorakei_[hoorakei_i][2] or 9 in hoorakei_[hoorakei_i][2]) and (hoorakei_[hoorakei_i][2][4]!='z')) or 'z' in hoorakei_[hoorakei_i][2]) and \
				(((1 in hoorakei_[hoorakei_i][3] or 9 in hoorakei_[hoorakei_i][3]) and (hoorakei_[hoorakei_i][3][4]!='z')) or 'z' in hoorakei_[hoorakei_i][3]) and \
				(((1 in hoorakei_[hoorakei_i][4] or 9 in hoorakei_[hoorakei_i][4]) and (hoorakei_[hoorakei_i][4][4]!='z')) or 'z' in hoorakei_[hoorakei_i][4]) and \
				(hoorakei_[hoorakei_i][1][0]=='shuntsu' or hoorakei_[hoorakei_i][2][0]=='shuntsu' or hoorakei_[hoorakei_i][3][0]=='shuntsu' or hoorakei_[hoorakei_i][4][0]=='shuntsu') and \
				0<sum(jihai9)<14:
					yaku[hoorakei_i].append(s.honchantaiyaochuu)
					hansuu[hoorakei_i]+=2#not counting kuisagari

				#toitoihoo
				if len(hoorakei_[hoorakei_i])==5 and all(i[0]=='kootsu' for i in hoorakei_[hoorakei_i][1:]):
					yaku[hoorakei_i].append(s.toitoihoo)
					hansuu[hoorakei_i]+=2

				#sanankoo
				#not checking fuuro
				if len(hoorakei_[hoorakei_i])>=4:
					if hoorakei_[hoorakei_i][1][0]==hoorakei_[hoorakei_i][2][0]==hoorakei_[hoorakei_i][3][0]=='kootsu':
						if tsumo==False:
							if (hai[tsumohai][1]==hoorakei_[hoorakei_i][0][4] and hai[tsumohai][0] in hoorakei_[hoorakei_i][0]) or \
							(len(hoorakei_[hoorakei_i])>=5 and hai[tsumohai][1]==hoorakei_[hoorakei_i][4][4] and hai[tsumohai][0] in hoorakei_[hoorakei_i][4]):
								yaku[hoorakei_i].append(s.sanankoo)
								hansuu[hoorakei_i]+=2
							else:
								yaku[hoorakei_i].append(s.sanankoo+s.question_mark)
								hansuu[hoorakei_i]+=2
						else:
							yaku[hoorakei_i].append(s.sanankoo+s.question_mark)
							hansuu[hoorakei_i]+=2

				#honroutou
				if sum(tehai9)>=14 and \
				manzu9[1]+manzu9[9]+pinzu9[1]+pinzu9[9]+soozu9[1]+soozu9[9]+sum(jihai9)==sum(tehai9) and \
				sum(jihai9)>0 and manzu9[1]+manzu9[9]+pinzu9[1]+pinzu9[9]+soozu9[1]+soozu9[9]>0 and \
				s.kokushimusou not in yaku[hoorakei_i] and s.kokushimusoujuusanmen not in yaku[hoorakei_i]:
					yaku[hoorakei_i].append(s.honroutou)
					hansuu[hoorakei_i]+=2

				#sanshokudookoo
				if len(hoorakei_[hoorakei_i])>=5:
					if (hoorakei_[hoorakei_i][1][1:4]==hoorakei_[hoorakei_i][2][1:4]==hoorakei_[hoorakei_i][3][1:4] and hoorakei_[hoorakei_i][1][0]==hoorakei_[hoorakei_i][2][0]==hoorakei_[hoorakei_i][3][0]=='kootsu' and (hoorakei_[hoorakei_i][1][4],hoorakei_[hoorakei_i][2][4],hoorakei_[hoorakei_i][3][4])==('m','p','s')) or \
					(hoorakei_[hoorakei_i][1][1:4]==hoorakei_[hoorakei_i][2][1:4]==hoorakei_[hoorakei_i][4][1:4] and hoorakei_[hoorakei_i][1][0]==hoorakei_[hoorakei_i][2][0]==hoorakei_[hoorakei_i][4][0]=='kootsu' and (hoorakei_[hoorakei_i][1][4],hoorakei_[hoorakei_i][2][4],hoorakei_[hoorakei_i][4][4])==('m','p','s')) or \
					(hoorakei_[hoorakei_i][1][1:4]==hoorakei_[hoorakei_i][3][1:4]==hoorakei_[hoorakei_i][4][1:4] and hoorakei_[hoorakei_i][1][0]==hoorakei_[hoorakei_i][3][0]==hoorakei_[hoorakei_i][4][0]=='kootsu' and (hoorakei_[hoorakei_i][1][4],hoorakei_[hoorakei_i][3][4],hoorakei_[hoorakei_i][4][4])==('m','p','s')) or \
					(hoorakei_[hoorakei_i][2][1:4]==hoorakei_[hoorakei_i][3][1:4]==hoorakei_[hoorakei_i][4][1:4] and hoorakei_[hoorakei_i][2][0]==hoorakei_[hoorakei_i][3][0]==hoorakei_[hoorakei_i][4][0]=='kootsu' and (hoorakei_[hoorakei_i][2][4],hoorakei_[hoorakei_i][3][4],hoorakei_[hoorakei_i][4][4])==('m','p','s')):
						yaku[hoorakei_i].append(s.sanshokudookoo)
						hansuu[hoorakei_i]+=2

				#shousangen
				if (['jantou',5,5,None,'z'] in hoorakei_[hoorakei_i] and ['kootsu',6,6,6,'z'] in hoorakei_[hoorakei_i] and ['kootsu',7,7,7,'z'] in hoorakei_[hoorakei_i]) or \
				(['kootsu',5,5,5,'z'] in hoorakei_[hoorakei_i] and ['jantou',6,6,None,'z'] in hoorakei_[hoorakei_i] and ['kootsu',7,7,7,'z'] in hoorakei_[hoorakei_i]) or \
				(['kootsu',5,5,5,'z'] in hoorakei_[hoorakei_i] and ['kootsu',6,6,6,'z'] in hoorakei_[hoorakei_i] and ['jantou',7,7,None,'z'] in hoorakei_[hoorakei_i]):
					yaku[hoorakei_i].append(s.shousangen)
					hansuu[hoorakei_i]+=2

				#honiisoo
				if sum(tehai9)>=14 and sum(jihai9)>0 and \
				((sum(manzu9)>0 and sum(pinzu9)==0 and sum(soozu9)==0) or \
				(sum(manzu9)==0 and sum(pinzu9)>0 and sum(soozu9)==0) or \
				(sum(manzu9)==0 and sum(pinzu9)==0 and sum(soozu9)>0)):
					yaku[hoorakei_i].append(s.honiisoo)
					hansuu[hoorakei_i]+=3#not counting kuisagari

				#junchantaiyaochuu
				if len(hoorakei_[hoorakei_i])==5 and \
				((1 in hoorakei_[hoorakei_i][0] or 9 in hoorakei_[hoorakei_i][0]) and hoorakei_[hoorakei_i][0][4]!='z') and \
				((1 in hoorakei_[hoorakei_i][1] or 9 in hoorakei_[hoorakei_i][1]) and hoorakei_[hoorakei_i][1][4]!='z') and \
				((1 in hoorakei_[hoorakei_i][2] or 9 in hoorakei_[hoorakei_i][2]) and hoorakei_[hoorakei_i][2][4]!='z') and \
				((1 in hoorakei_[hoorakei_i][3] or 9 in hoorakei_[hoorakei_i][3]) and hoorakei_[hoorakei_i][3][4]!='z') and \
				((1 in hoorakei_[hoorakei_i][4] or 9 in hoorakei_[hoorakei_i][4]) and hoorakei_[hoorakei_i][4][4]!='z') and \
				(hoorakei_[hoorakei_i][1][0]=='shuntsu' or hoorakei_[hoorakei_i][2][0]=='shuntsu' or hoorakei_[hoorakei_i][3][0]=='shuntsu' or hoorakei_[hoorakei_i][4][0]=='shuntsu'):
					yaku[hoorakei_i].append(s.junchantaiyaochuu)
					hansuu[hoorakei_i]+=3#not counting kuisagari

				#ryanpeekoo
				#not checking menzenchin
				if len(hoorakei_[hoorakei_i])>=5 and hoorakei_[hoorakei_i][-1][0]==hoorakei_[hoorakei_i][-2][0]==hoorakei_[hoorakei_i][-3][0]==hoorakei_[hoorakei_i][-4][0]=='shuntsu':
					if (hoorakei_[hoorakei_i][-1]==hoorakei_[hoorakei_i][-2] and hoorakei_[hoorakei_i][-3]==hoorakei_[hoorakei_i][-4]) or \
					(hoorakei_[hoorakei_i][-1]==hoorakei_[hoorakei_i][-3] and hoorakei_[hoorakei_i][-2]==hoorakei_[hoorakei_i][-4]) or \
					(hoorakei_[hoorakei_i][-1]==hoorakei_[hoorakei_i][-4] and hoorakei_[hoorakei_i][-2]==hoorakei_[hoorakei_i][3]):
						yaku[hoorakei_i].append(s.ryanpeekoo)
						hansuu[hoorakei_i]+=3
						if s.iipeekoo in yaku[hoorakei_i]:
							yaku[hoorakei_i].remove(s.iipeekoo)
							hansuu[hoorakei_i]-=1
						# if s.chiitoitsu in yaku[0]:
						# 	yaku[0]=[]
						# 	hoorakei_[0]=[]

				#chiniisoo
				if sum(tehai9)>=14 and (sum(manzu9)==sum(tehai9) or sum(pinzu9)==sum(tehai9) or sum(soozu9)==sum(tehai9)):
					yaku[hoorakei_i].append(s.chiniisoo)
					hansuu[hoorakei_i]+=6#not counting kuisagari

				#suuankoo
				#not checking menzenchin
				if len(hoorakei_[hoorakei_i])>=5 and hoorakei_[hoorakei_i][1][0]==hoorakei_[hoorakei_i][2][0]==hoorakei_[hoorakei_i][3][0]==hoorakei_[hoorakei_i][4][0]=='kootsu':
					if tsumo==False:
						if hai[tsumohai][0]==hoorakei_[hoorakei_i][0][1] and hai[tsumohai][1]==hoorakei_[hoorakei_i][0][4]:
							yaku[hoorakei_i].append(s.suuankootanki)
							hansuu[hoorakei_i]+=26
							yakuman[hoorakei_i]=True
						else:
							yaku[hoorakei_i].append(s.sanankoo+s.ideographic_comma+s.toitoihoo+' ('+s.suuankoo+s.question_mark+')')
							hansuu[hoorakei_i]+=4
							yakuman[hoorakei_i]=False
					else:
						yaku[hoorakei_i].append(s.suuankoo+s.question_mark)
						hansuu[hoorakei_i]+=13
						yakuman[hoorakei_i]=True
					if s.toitoihoo in yaku[hoorakei_i]:
						yaku[hoorakei_i].remove(s.toitoihoo)
						hansuu[hoorakei_i]-=2
					if s.sanankoo+s.question_mark in yaku[hoorakei_i]:
						yaku[hoorakei_i].remove(s.sanankoo+s.question_mark)
						hansuu[hoorakei_i]-=2
					if s.sanankoo in yaku[hoorakei_i]:
						yaku[hoorakei_i].remove(s.sanankoo)
						hansuu[hoorakei_i]-=2

				#daisangen
				if ['kootsu',5,5,5,'z'] in hoorakei_[hoorakei_i] and ['kootsu',6,6,6,'z'] in hoorakei_[hoorakei_i] and ['kootsu',7,7,7,'z'] in hoorakei_[hoorakei_i]:
					yaku[hoorakei_i].append(s.daisangen)
					hansuu[hoorakei_i]+=13
					yakuman[hoorakei_i]=True
					if s.yakuhai_haku in yaku[hoorakei_i]:
						yaku[hoorakei_i].remove(s.yakuhai_haku)
						hansuu[hoorakei_i]-=1
					if s.yakuhai_hatsu in yaku[hoorakei_i]:
						yaku[hoorakei_i].remove(s.yakuhai_hatsu)
						hansuu[hoorakei_i]-=1
					if s.yakuhai_chun in yaku[hoorakei_i]:
						yaku[hoorakei_i].remove(s.yakuhai_chun)
						hansuu[hoorakei_i]-=1

				#tsuuiisoo
				if sum(tehai9)>=14 and sum(jihai9)==sum(tehai9):
					yaku[hoorakei_i].append(s.tsuuiisoo)
					hansuu[hoorakei_i]+=13
					yakuman[hoorakei_i]=True

				#shousuushii
				if (['jantou',1,1,None,'z'] in hoorakei_[hoorakei_i] and ['kootsu',2,2,2,'z'] in hoorakei_[hoorakei_i] and ['kootsu',3,3,3,'z'] in hoorakei_[hoorakei_i] and ['kootsu',4,4,4,'z'] in hoorakei_[hoorakei_i]) or \
				(['kootsu',1,1,1,'z'] in hoorakei_[hoorakei_i] and ['jantou',2,2,None,'z'] in hoorakei_[hoorakei_i] and ['kootsu',3,3,3,'z'] in hoorakei_[hoorakei_i] and ['kootsu',4,4,4,'z'] in hoorakei_[hoorakei_i]) or \
				(['kootsu',1,1,1,'z'] in hoorakei_[hoorakei_i] and ['kootsu',2,2,2,'z'] in hoorakei_[hoorakei_i] and ['jantou',3,3,None,'z'] in hoorakei_[hoorakei_i] and ['kootsu',4,4,4,'z'] in hoorakei_[hoorakei_i]) or \
				(['kootsu',1,1,1,'z'] in hoorakei_[hoorakei_i] and ['kootsu',2,2,2,'z'] in hoorakei_[hoorakei_i] and ['kootsu',3,3,3,'z'] in hoorakei_[hoorakei_i] and ['jantou',4,4,None,'z'] in hoorakei_[hoorakei_i]):
					yaku[hoorakei_i].append(s.shousuushii)
					hansuu[hoorakei_i]+=13
					yakuman[hoorakei_i]=True

				#ryuuiisoo
				if sum(tehai9)>=14 and soozu9[2]+soozu9[3]+soozu9[4]+soozu9[6]+soozu9[8]+jihai9[6]==sum(tehai9):
					yaku[hoorakei_i].append(s.ryuuiisoo)
					hansuu[hoorakei_i]+=13
					yakuman[hoorakei_i]=True

				#chinroutou
				if sum(tehai9)>=14 and \
				manzu9[1]+manzu9[9]+pinzu9[1]+pinzu9[9]+soozu9[1]+soozu9[9]==sum(tehai9):
					yaku[hoorakei_i].append(s.chinroutou)
					hansuu[hoorakei_i]+=13
					yakuman[hoorakei_i]=True
					if s.toitoihoo in yaku[hoorakei_i]:
						yaku[hoorakei_i].remove(s.toitoihoo)
						hansuu[hoorakei_i]-=2

				#chuurenpouton
				#not checking menzenchin
				if sum(tehai9)==14 and \
				(manzu9[1]>=3 and manzu9[2]>=1 and manzu9[3]>=1 and manzu9[4]>=1 and manzu9[5]>=1 and manzu9[6]>=1 and manzu9[7]>=1 and manzu9[8]>=1 and manzu9[9]>=3) or \
				(pinzu9[1]>=3 and pinzu9[2]>=1 and pinzu9[3]>=1 and pinzu9[4]>=1 and pinzu9[5]>=1 and pinzu9[6]>=1 and pinzu9[7]>=1 and pinzu9[8]>=1 and pinzu9[9]>=3) or \
				(soozu9[1]>=3 and soozu9[2]>=1 and soozu9[3]>=1 and soozu9[4]>=1 and soozu9[5]>=1 and soozu9[6]>=1 and soozu9[7]>=1 and soozu9[8]>=1 and soozu9[9]>=3):
					if tsumo==False:
						if (hai[tsumohai][0]==1 and manzu9[1]+pinzu9[1]+soozu9[1]==4) or \
						(hai[tsumohai][0]==2 and manzu9[2]+pinzu9[2]+soozu9[2]==2) or \
						(hai[tsumohai][0]==3 and manzu9[3]+pinzu9[3]+soozu9[3]==2) or \
						(hai[tsumohai][0]==4 and manzu9[4]+pinzu9[4]+soozu9[4]==2) or \
						(hai[tsumohai][0]==5 and manzu9[5]+pinzu9[5]+soozu9[5]==2) or \
						(hai[tsumohai][0]==6 and manzu9[6]+pinzu9[6]+soozu9[6]==2) or \
						(hai[tsumohai][0]==7 and manzu9[7]+pinzu9[7]+soozu9[7]==2) or \
						(hai[tsumohai][0]==8 and manzu9[8]+pinzu9[8]+soozu9[8]==2) or \
						(hai[tsumohai][0]==9 and manzu9[9]+pinzu9[9]+soozu9[9]==4):
							yaku[hoorakei_i].append(s.junseichuurenpouton)
							hansuu[hoorakei_i]+=26
							yakuman[hoorakei_i]=True
						else:
							yaku[hoorakei_i].append(s.chuurenpouton)
							hansuu[hoorakei_i]+=13
							yakuman[hoorakei_i]=True
					else:
						yaku[hoorakei_i].append(s.chuurenpouton)
						hansuu[hoorakei_i]+=13
						yakuman[hoorakei_i]=True
					if s.chiniisoo in yaku[hoorakei_i]:
						yaku[hoorakei_i].remove(s.chiniisoo)
						hansuu[hoorakei_i]-=6#not checking kuisagari

				#daisuushii
				if ['kootsu',1,1,1,'z'] in hoorakei_[hoorakei_i] and ['kootsu',2,2,2,'z'] in hoorakei_[hoorakei_i] and ['kootsu',3,3,3,'z'] in hoorakei_[hoorakei_i] and ['kootsu',4,4,4,'z'] in hoorakei_[hoorakei_i]:
					yaku[hoorakei_i].append(s.daisuushii)
					hansuu[hoorakei_i]+=26
					yakuman[hoorakei_i]=True
					yaku[hoorakei_i].remove(s.yakuhai_ton+s.question_mark)
					yaku[hoorakei_i].remove(s.yakuhai_nan+s.question_mark)
					yaku[hoorakei_i].remove(s.yakuhai_shaa+s.question_mark)
					yaku[hoorakei_i].remove(s.yakuhai_pei+s.question_mark)
					hansuu[hoorakei_i]-=3
					if len(hoorakei_[hoorakei_i])==5 and s.toitoihoo in yaku[hoorakei_i]:
						yaku[hoorakei_i].remove(s.toitoihoo)
						hansuu[hoorakei_i]-=2

			#print hoorakei
			if tsumo:
				print(s.hoora+" |",end="")
				if not hoorakei_[hoorakei_i][0][0]=='toitsu':
					print(" ",end="")
				for j in hoorakei_[hoorakei_i]:
					for k in j[1:]:
						if k:
							print(k,end="")
					print("" if j[0]=='toitsu' and j==hoorakei_[hoorakei_i][-1] else " ",end="")
				print("|",end="")
				if yakuman[hoorakei_i] and hansuu[hoorakei_i]>=13:
					print(" "+yakuman_level[hansuu[hoorakei_i]//13],end=s.colon)
				elif not yakuman[hoorakei_i] and hansuu[hoorakei_i]>=13:
					print(" "+s.kazoeyakuman+"("+str(hansuu[hoorakei_i])+s.han+")",end=s.colon)
				elif hansuu[hoorakei_i]>0:
					print(str(hansuu[hoorakei_i]).rjust(2)+s.han,end=s.colon)
				for j in yaku[hoorakei_i]:
					print(j,end=(s.ideographic_comma if yaku[hoorakei_i].index(j)!=len(yaku[hoorakei_i])-1 else ""))
				print()
			elif tsumo==False:
				tenpai=True
				if dahai and not number_only:
					print(s.da,"["+hai_[hai.index(dahai)]+"]",end=" ")
				elif dahai and number_only:
					print(s.da,"["+str(dahai[0])+"]",end=" ")
				if karaten:
					print(s.karaten,"["+hai_[tsumohai],end="] |")
				else:
					print(s.tenpai,"["+hai_[tsumohai],end="] |")
					if tsumohai not in agarihai:
						agarihai.append(tsumohai)
				if not hoorakei_[hoorakei_i][0][0]=='toitsu':
					print(" ",end="")
				for j in hoorakei_[hoorakei_i]:
					for k in j[1:]:
						if k:
							print(k,end="")
					print("" if j[0]=='toitsu' and j==hoorakei_[hoorakei_i][-1] else " ",end="")
				print("|",end="")
				if yakuman[hoorakei_i] and yakuman[hoorakei_i]!=True:
					print(" "+yakuman[hoorakei_i],end=s.colon)
				elif yakuman[hoorakei_i] and hansuu[hoorakei_i]>=13:
					print(" "+yakuman_level[hansuu[hoorakei_i]//13],end=s.colon)
				elif not yakuman[hoorakei_i] and hansuu[hoorakei_i]>=13:
					print(" "+s.kazoeyakuman+"("+str(hansuu[hoorakei_i])+s.han+")",end=s.colon)
				elif hansuu[hoorakei_i]>0:
					print(str(hansuu[hoorakei_i]).rjust(2)+s.han,end=s.colon)
				for j in yaku[hoorakei_i]:
					print(j,end=(s.ideographic_comma if yaku[hoorakei_i].index(j)!=len(yaku[hoorakei_i])-1 else ""))
				print()

		if tsumo and not hoora:
			if beginning_cosmos:
				pass
			else:
				print(s.not_hoora)
			break

		if hoora and not karaten:
			if max(hansuu)>=13:
				kouten.append(max(hansuu)//13*13)
			else:
				kouten.append(max(hansuu))

		if tsumo:
			break
		if tsumo==False:
			tehai9[tsumohai]-=1
			if 0<tsumohai<10:
				manzu9[tsumohai]-=1
			elif 10<tsumohai<20:
				pinzu9[tsumohai-10]-=1
			elif 20<tsumohai<30:
				soozu9[tsumohai-20]-=1
			elif 30<tsumohai<38:
				jihai9[tsumohai-30]-=1

	#beginning of the cosmos
	if beginning_cosmos:
		print(s.hoora+" | 55z 5555z 5555z 5555z 5555z | "+s.beginning_of_the_cosmos+"(140"+s.fuu+"105"+s.han+" "+fuusuu_calculate(140,105)+s.ten+")"+s.colon+s.tsuuiisoo+s.ideographic_comma+s.sanankoo+s.ideographic_comma+s.suukantsu+s.ideographic_comma+s.rinshankaihou+s.ideographic_comma+s.yakuhai_haku+"4"+s.ideographic_comma+s.dora+"72")

	#tenpai
	if not dahai and tsumo==False and tenpai and agarihai and not number_only:
		agarihai_han=list(zip(agarihai,kouten))
		agarihai_han.sort(key=lambda elem: (elem[1],elem[0]))

		print()
		print(s.tenpai,end=s.colon)
		for i in range(len(agarihai_han)):
			print(hai_[agarihai_han[i][0]],end=" ")
			if (i!=len(agarihai_han)-1 and agarihai_han[i][1]!=agarihai_han[i+1][1]) or i==len(agarihai_han)-1 and sum(tehai9)<=14:
				if agarihai_han[i][1]>=13:
					print("("+yakuman_level[agarihai_han[i][1]//13],end=") ")
				else:
					print("("+str(agarihai_han[i][1])+s.han,end=") ")
		print()
	elif not dahai and tsumo==False and tenpai and agarihai and number_only:
		print()
		print(s.tenpai,end=s.colon)
		for i in range(len(agarihai)):
			print(hai_[agarihai[i]],end=" ")
		print()

	if not dahai and tsumo==False and not tenpai:
		print(s.nooten)

	end_time=datetime.datetime.now()
	time_spent=(end_time-start_time).total_seconds()//0.1*0.1
	if time_spent>1.0:
		print(s.time_spent1,time_spent,s.time_spent2)

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
