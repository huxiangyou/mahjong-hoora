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

import time
import sys
import test
from lang import romaji, kanji, katakana, ja, zh
s=zh # change "zh" to other language if you need: romaji, kanji, katakana, ja, zh

def output_hai(tehai1,is_number_only=False):
	if not is_number_only:
		if tehai1<30:
			return str(tehai1%10)+('m','p','s')[tehai1//10]
		else:
			return ('東','南','西','北','白','發','中')[tehai1-31]
	else:
		return str(tehai1)

def output_hais(tehai1,is_number_only=False,traditional=False,end=""):
	if not is_number_only:
		has_manzu=any(i in tehai1 for i in range(1,10))
		has_pinzu=any(i in tehai1 for i in range(11,20))
		has_soozu=any(i in tehai1 for i in range(21,30))
		has_jihai=any(i in tehai1 for i in range(31,38))
		for i in tehai1:
			if i==None:
				pass
			elif 0<i<10:
				print(i,end="")
			elif 10<i<20:
				if has_manzu:
					print("m",end=" ")
					has_manzu=False
				print(i-10,end="")
			elif 20<i<30:
				if has_manzu:
					print("m",end=" ")
					has_manzu=False
				if has_pinzu:
					print("p",end=" ")
					has_pinzu=False
				print(i-20,end="")
			elif 30<i<38:
				if has_manzu:
					print("m",end=" ")
					has_manzu=False
				if has_pinzu:
					print("p",end=" ")
					has_pinzu=False
				if has_soozu:
					print("s",end=" ")
					has_soozu=False
				if not traditional:
					print(('東','南','西','北','白','發','中')[i-31],end="")
				else:
					print(i-30,end="")
		if has_manzu:
			print("m",end="")
			has_manzu=False
		if has_pinzu:
			print("p",end="")
			has_pinzu=False
		if has_soozu:
			print("s",end="")
			has_soozu=False
		if has_jihai and traditional:
			print("z",end="")
	else:
		for i in tehai1:
			if i==None:
				pass
			else:
				print(i,end="")
	print(end=end)

def yaku_and_output(tehai9,hoorakei,did_tsumo,is_karaten,tsumohai,dahai,is_number_only):
	yaku=[]
	hansuu=0
	is_yakuman=False

	#kokushimusou
	if len(hoorakei)>1 and hoorakei[1][0]=='tp':
		if tehai9[tsumohai]==2:
			yaku.append(s.kokushimusoujuusanmen)
			hansuu+=26
		else:
			yaku.append(s.kokushimusou)
			hansuu+=13
		is_yakuman=True

	elif sum(tehai9)<=14:

		#chiitoitsu
		if hoorakei[0][0]=='t':
			yaku.append(s.chiitoitsu)
			hansuu+=2

		#tanyaochuu
		if sum(tehai9)==14 and not tehai9[1] and not tehai9[9] and not tehai9[11] and not tehai9[19] and not tehai9[21] and not tehai9[29] and not any(tehai9[31:]):
			yaku.append(s.tanyaochuu)
			hansuu+=1

		#yakuhai
		#not checking chanfon or menfon
		#ton
		if ['k',31,31,31] in hoorakei:
			yaku.append(s.yakuhai_ton+s.question_mark)
			hansuu+=1
		#nan
		if ['k',32,32,32] in hoorakei:
			yaku.append(s.yakuhai_nan+s.question_mark)
			hansuu+=1
		#shaa
		if ['k',33,33,33] in hoorakei:
			yaku.append(s.yakuhai_shaa+s.question_mark)
			hansuu+=1
		#pei
		if ['k',34,34,34] in hoorakei:
			yaku.append(s.yakuhai_pei+s.question_mark)
			hansuu+=1
		if sum((i in yaku for i in (s.yakuhai_ton+s.question_mark,s.yakuhai_nan+s.question_mark,s.yakuhai_shaa+s.question_mark,s.yakuhai_pei+s.question_mark)))==3:
			hansuu-=1
		#haku
		if ['k',35,35,35] in hoorakei:
			yaku.append(s.yakuhai_haku)
			hansuu+=1
		#hatsu
		if ['k',36,36,36] in hoorakei:
			yaku.append(s.yakuhai_hatsu)
			hansuu+=1
		#chun
		if ['k',37,37,37] in hoorakei:
			yaku.append(s.yakuhai_chun)
			hansuu+=1

		#pinfu
		#not checking chanfon or menfon
		if len(hoorakei)==5 and all(i[0]=='s' for i in hoorakei[1:]) and hoorakei[0][1]<35:
			if did_tsumo==False and tsumohai<30:
				if any((tsumohai==i[1] and tsumohai not in (7,17,27)) or (tsumohai==i[3] and tsumohai not in (3,13,23)) for i in hoorakei[1:]):
					if hoorakei[0][1]>30:
						yaku.append(s.pinfu+s.question_mark)
					else:
						yaku.append(s.pinfu)
					hansuu+=1
			else:
				yaku.append(s.pinfu+s.question_mark)
				hansuu+=1

		#iipeekoo
		#not checking menzenchin
		if any(i[0]=='s' and hoorakei.count(i)>=2 for i in hoorakei):
			yaku.append(s.iipeekoo)
			hansuu+=1

		#sanshokudoujun
		if any(['s',i,i+1,i+2] in hoorakei and ['s',i+10,i+11,i+12] in hoorakei and ['s',i+20,i+21,i+22] in hoorakei for i in range(1,8)):
			yaku.append(s.sanshokudoujun)
			hansuu+=2#not counting kuisagari

		#ikkitsuukan
		if any(['s',1+i,2+i,3+i] in hoorakei and ['s',4+i,5+i,6+i] in hoorakei and ['s',7+i,8+i,9+i] in hoorakei for i in (0,10,20)):
			yaku.append(s.ikkitsuukan)
			hansuu+=2#not counting kuisagari

		#honchantaiyaochuu
		if len(hoorakei)==5 and all(i[1] in (1,11,21,9,19,29) or i[3] in (9,19,29) or i[1]>30 for i in hoorakei) and any(i[0]=='s' for i in hoorakei) and 0<sum(tehai9[31:])<14:
			yaku.append(s.honchantaiyaochuu)
			hansuu+=2#not counting kuisagari

		#toitoihoo
		if len(hoorakei)==5 and all(i[0]=='k' for i in hoorakei[1:]):
			yaku.append(s.toitoihoo)
			hansuu+=2

		#sanankoo
		#not checking fuuro
		if sum(i[0]=='k' for i in hoorakei)>=3:
			if did_tsumo==False and any(i[0]!='k' and tsumohai in i for i in hoorakei) or s.toitoihoo in yaku:
				yaku.append(s.sanankoo)
			else:
				yaku.append(s.sanankoo+s.question_mark)
			hansuu+=2

		#honroutou
		if tehai9[1]+tehai9[9]+tehai9[11]+tehai9[19]+tehai9[21]+tehai9[29]+sum(tehai9[31:])==14 and 0<sum(tehai9[31:])<14:
			yaku.append(s.honroutou)
			hansuu+=2

		#sanshokudookoo
		if any((['k',i,i,i] in hoorakei and ['k',i+10,i+10,i+10] in hoorakei and ['k',i+20,i+20,i+20] in hoorakei) for i in range(1,10)):
				yaku.append(s.sanshokudookoo)
				hansuu+=2

		#shousangen
		if (['j',35,35,None]==hoorakei[0] and ['k',36,36,36] in hoorakei and ['k',37,37,37] in hoorakei) or \
		(['k',35,35,35] in hoorakei and ['j',36,36,None]==hoorakei[0] and ['k',37,37,37] in hoorakei) or \
		(['k',35,35,35] in hoorakei and ['k',36,36,36] in hoorakei and ['j',37,37,None]==hoorakei[0]):
			yaku.append(s.shousangen)
			hansuu+=2

		#honiisoo
		if sum(tehai9)==14 and 0<sum(tehai9[31:])<14 and (not any(tehai9[11:30]) or not any(tehai9[1:10]+tehai9[21:30]) or not any(tehai9[1:20])):
			yaku.append(s.honiisoo)
			hansuu+=3#not counting kuisagari

		#junchantaiyaochuu
		if len(hoorakei)==5 and all(i[1] in (1,11,21,9,19,29) or i[3] in (9,19,29) and i[1]<30 for i in hoorakei) and any(i[0]=='s' for i in hoorakei):
			yaku.append(s.junchantaiyaochuu)
			hansuu+=3#not counting kuisagari

		#ryanpeekoo
		#not checking menzenchin
		if sum(i[0]=='s' and hoorakei.count(i)>=2 for i in hoorakei)>=4:
			yaku.append(s.ryanpeekoo)
			yaku.remove(s.iipeekoo)
			hansuu+=2

		#chiniisoo
		if sum(tehai9)==14 and (sum(tehai9[1:10])==14 or sum(tehai9[11:20])==14 or sum(tehai9[21:30])==14):
			yaku.append(s.chiniisoo)
			hansuu+=6#not counting kuisagari

		#suuankoo
		#not checking menzenchin
		if sum(i[0]=='k' for i in hoorakei)>=4:
			if did_tsumo==False:
				if tsumohai==hoorakei[0][1]:
					yaku.append(s.suuankootanki)
					hansuu+=26
					is_yakuman=True
				else:
					yaku.append(s.sanankoo+s.ideographic_comma+s.toitoihoo+' ('+s.suuankoo+s.question_mark+')')
					hansuu+=4
					is_yakuman=False
			else:
				yaku.append(s.suuankoo+s.question_mark)
				hansuu+=13
				is_yakuman=True
			yaku.remove(s.toitoihoo)
			hansuu-=2
			if s.sanankoo+s.question_mark in yaku:
				yaku.remove(s.sanankoo+s.question_mark)
				hansuu-=2
			if s.sanankoo in yaku:
				yaku.remove(s.sanankoo)
				hansuu-=2

		#daisangen
		if ['k',35,35,35] in hoorakei and ['k',36,36,36] in hoorakei and ['k',37,37,37] in hoorakei:
			yaku.append(s.daisangen)
			is_yakuman=True
			yaku.remove(s.yakuhai_haku)
			yaku.remove(s.yakuhai_hatsu)
			yaku.remove(s.yakuhai_chun)
			hansuu+=10

		#tsuuiisoo
		if sum(tehai9)==14==sum(tehai9[31:]):
			yaku.append(s.tsuuiisoo)
			hansuu+=13
			is_yakuman=True

		#shousuushii
		if any(hoorakei[0]==['j',i,i,None] for i in range(31,35)) and all(hoorakei[0]==['j',i,i,None] or ['k',i,i,i] in hoorakei for i in range(31,35)):
			yaku.append(s.shousuushii)
			hansuu+=13
			is_yakuman=True

		#ryuuiisoo
		if sum(tehai9)==14==tehai9[22]+tehai9[23]+tehai9[24]+tehai9[26]+tehai9[28]+tehai9[36]:
			yaku.append(s.ryuuiisoo)
			hansuu+=13
			is_yakuman=True

		#chinroutou
		if sum(tehai9)==14==tehai9[1]+tehai9[9]+tehai9[11]+tehai9[19]+tehai9[21]+tehai9[29]:
			yaku.append(s.chinroutou)
			hansuu+=13
			is_yakuman=True
			if s.toitoihoo in yaku:
				yaku.remove(s.toitoihoo)
				hansuu-=2

		#chuurenpouton
		#not checking menzenchin
		if sum(tehai9)==14 and any(tehai9[i+1]>=3 and all(tehai9[i+2:i+9]) and tehai9[i+9]>=3 for i in (0,10,20)):
			if did_tsumo==False:
				if tsumohai%10 in (1,9) and tehai9[tsumohai]==4 or tehai9[tsumohai]==2:
					yaku.append(s.junseichuurenpouton)
					hansuu+=26
					is_yakuman=True
				else:
					yaku.append(s.chuurenpouton)
					hansuu+=13
					is_yakuman=True
			else:
				yaku.append(s.chuurenpouton)
				hansuu+=13
				is_yakuman=True
			yaku.remove(s.chiniisoo)
			hansuu-=6#not checking kuisagari

		#daisuushii
		if ['k',31,31,31] in hoorakei and ['k',32,32,32] in hoorakei and ['k',33,33,33] in hoorakei and ['k',34,34,34] in hoorakei:
			yaku.append(s.daisuushii)
			is_yakuman=True
			yaku.remove(s.yakuhai_ton+s.question_mark)
			yaku.remove(s.yakuhai_nan+s.question_mark)
			yaku.remove(s.yakuhai_shaa+s.question_mark)
			yaku.remove(s.yakuhai_pei+s.question_mark)
			hansuu+=22
			if s.toitoihoo in yaku:
				yaku.remove(s.toitoihoo)
				hansuu-=2

	#output
	if dahai:
		print(s.da,"["+output_hai(dahai,is_number_only)+"]",end=" ")
	if did_tsumo:
		print(s.hoora+" | ",end="")
	elif did_tsumo==False and is_karaten:
		print(s.karaten,"["+output_hai(tsumohai,is_number_only),end="] | ")
	elif did_tsumo==False and not is_karaten:
		print(s.tenpai,"["+output_hai(tsumohai,is_number_only),end="] | ")
	for j in hoorakei:
		output_hais(j[1:],is_number_only,True," ")
	print("|",end="")
	if is_yakuman and hansuu>=13:
		print(" "+s.yakuman_level_list[hansuu//13],end=s.colon)
	elif not is_yakuman and hansuu>=13:
		print(" "+s.kazoeyakuman+"("+str(hansuu)+s.han+")",end=s.colon)
	elif hansuu>0:
		print(str(hansuu).rjust(3)+s.han,end=s.colon)
	for j in yaku:
		print(j,end=(s.ideographic_comma if yaku.index(j)!=len(yaku)-1 else ""))
	print()

	return hansuu

def main(tehai=None,tehai1=None,dahai=False,is_number_only=False):
	global s
	#input tehai
	if tehai1==None:
		if tehai==None:
			try:
				tehai=input(s.ask_input_tehai+s.colon)
				tehai_lower=tehai.lower()
			except:
				print("ERROR")
				return
			if tehai_lower in ("exit","退出","イグジスト"):
				sys.exit()
			elif tehai_lower in ("help","帮助","幫助","ヘルプ"):
				print()
				print(s.help)
				return
			elif tehai_lower in ("about","关于"):
				print()
				print("胡祥又 Hu Xiangyou\nversion 2.0.1\n\nversion 0.0 December 17, 2018\nversion 1.0 February 9, 2019\nversion 1.1 February 20, 2019\nversion 1.2 March 20, 2019\nversion 2.0 April 14, 2019")
				return
			elif tehai_lower in ("example","examples","举例","舉例","例","例え","test","tests","测试","測試","テスト"):
				main(tehai=test.test())
				return
			elif tehai_lower in ('lang','language','languages','语言','語言','言語','げんご'):
				print('romaji, kanji, kana, ja, zh')
				return
			elif tehai_lower in ('romaji','ローマ字','罗马字','羅馬字'):
				s=romaji
				print(s.language_switched)
				return
			elif tehai_lower in ('kanji','漢字','汉字'):
				s=kanji
				print(s.language_switched)
				return
			elif tehai_lower in ('katakana','kana','カタカナ','片仮名','片假名','仮名','假名'):
				s=katakana
				print(s.language_switched)
				return
			elif tehai_lower in ('tsuujou','general','ja','日本語','日语','日語','日本语','通常','一般'):
				s=ja
				print(s.language_switched)
				return
			elif tehai_lower in ('zh','cn','中国語','中文'):
				s=zh
				print(s.language_switched)
				return
			elif tehai_lower in dir(s) and tehai_lower[0]!='_':
				print(eval('s.'+tehai_lower))
				return

		for i in (' ','!','"','#','$','%','&','\'','(',')','*','+',',','-','.','/',':',';','<','=','>','?','@','[','\\',']','^','_','`','{','|','}','~','　'):
			tehai=tehai.replace(i,'')
		if tehai=='':
			return

		#manage tehai
		tehai1=[]
		shurui_now=None
		shurui_used=True
		invalid_inputs=[]
		has_0=False
		has_0m=False
		has_0p=False
		has_0s=False
		#number only
		if tehai.isdecimal():
			is_number_only=True
			if '0' in tehai:
				has_0=True
			tehai1=[int(i) if i!='0' else 5 for i in tehai]
		else:
			tehai=tehai[::-1]
			for tehai_i in tehai:
				if tehai_i in ('E','Ｅ','東','东'):
					tehai1.append(31)
				elif tehai_i in ('S','Ｓ','南'):
					tehai1.append(32)
				elif tehai_i in ('W','Ｗ','西'):
					tehai1.append(33)
				elif tehai_i in ('N','Ｎ','北'):
					tehai1.append(34)
				elif tehai_i in ('P','D','Ｐ','Ｄ','白'):
					tehai1.append(35)
				elif tehai_i in ('F','H','R','Ｆ','Ｈ','Ｒ','發','発','发'):
					tehai1.append(36)
				elif tehai_i in ('C','Ｃ','中'):
					tehai1.append(37)
				elif tehai_i in ('m','w','ｍ','ｗ','万','萬'):
					if not shurui_used:
						invalid_inputs.insert(0,('m','p','s','z')[shurui_now])
					shurui_now=0
					shurui_used=False
				elif tehai_i in ('p','ｐ','筒','饼','餠','餅'):
					if not shurui_used:
						invalid_inputs.insert(0,('m','p','s','z')[shurui_now])
					shurui_now=1
					shurui_used=False
				elif tehai_i in ('s','ｓ','索','条','條'):
					if not shurui_used:
						invalid_inputs.insert(0,('m','p','s','z')[shurui_now])
					shurui_now=2
					shurui_used=False
				elif tehai_i in ('z','ｚ','字'):
					if not shurui_used:
						invalid_inputs.insert(0,('m','p','s','z')[shurui_now])
					shurui_now=3
					shurui_used=False
				elif tehai_i.isdecimal():
					if shurui_now!=None:
						if tehai_i=='0' and shurui_now in (0,1,2):
							tehai1.append(5+shurui_now*10)
							if shurui_now==0:
								has_0m=True
							elif shurui_now==1:
								has_0p=True
							elif shurui_now==2:
								has_0s=True
						elif tehai_i in ('0','8','9') and shurui_now==3:
							invalid_inputs.insert(0,tehai_i+'z')
							shurui_used=True
						else:
							tehai1.append(int(tehai_i)+shurui_now*10)
						shurui_used=True
					else:
						invalid_inputs.insert(0,tehai_i)
				else:
					if not shurui_used:
						invalid_inputs.insert(0,('m','p','s','z')[shurui_now])
						shurui_used=True
					invalid_inputs.insert(0,tehai_i)
			if shurui_used==False:
				invalid_inputs.insert(0,('m','p','s','z')[shurui_now])

		if invalid_inputs:
			print(s.has_invalid_input,end=s.colon)
			for i in invalid_inputs:
				print(i,end=" ")
			print()

		if has_0:
			print(s.has_0)
		elif has_0m:
			print(s.has_0m)
		elif has_0p:
			print(s.has_0p)
		elif has_0s:
			print(s.has_0s)

	tehai1.sort()

	#count tehai
	haisuu=len(tehai1)
	tehai9=[0]*38
	for i in tehai1:
		tehai9[i]+=1

	if haisuu==0:
		print()
		return

	#show tehai
	if not dahai:
		print()
		print(s.tehai,end=s.colon)
		output_hais(tehai1,is_number_only,False,"\n\n")
		
		if any(i>4 for i in tehai9):
			print(s.more_than_4.format(s.ideographic_comma.join([output_hai(i) for i in range(38) if tehai9[i]>4])))

		if haisuu>14:
			print(s.more_than_14.format(str(haisuu)))
			print()
		if haisuu<13:
			print(s.less_than_13.format(str(haisuu)))
			print()

	mentsusuu=haisuu//3
	is_tenpai=False
	is_beginning_of_the_cosmos=False
	kouten=[]

	if haisuu==tehai9[35]==18:
		is_beginning_of_the_cosmos=True
		did_tsumo=True
	elif haisuu%3==2:
		did_tsumo=True
	elif haisuu%3==1:
		did_tsumo=False
		haisuu+=1
		agarihais=[]
	elif haisuu%3==0:
		did_tsumo=None
		print(s.taapai_or_shaopai.format(str(haisuu)))
		return

	if not dahai and 50<haisuu:
		if input(s.low_speed)!='':
			return
	start_time=time.time()

	for tsumohai in range(1,10 if is_number_only else 38):
		if tsumohai%10==0:
			continue

		is_karaten=False
		if did_tsumo==False:
			tehai9[tsumohai]+=1
			if tehai9[tsumohai]==5:
				is_karaten=True

		is_hoora=False
		hoorakeis=[]
		hansuu=[]

		#kokushimusou
		if haisuu==14 and not any(tehai9[2:9]) and not any(tehai9[12:19]) and not any(tehai9[22:29]) and tehai9[1] and tehai9[9] and tehai9[11] and tehai9[19] and tehai9[21] and tehai9[29] and all(tehai9[31:]):
			is_hoora=True
			hoorakeis.append([['j',tehai9.index(2),tehai9.index(2),None]]+[['tp',i,None,None] for i in range(38) if tehai9[i]==1])
			hansuu.append(yaku_and_output(tehai9,hoorakeis[-1],did_tsumo,is_karaten,tsumohai,dahai,is_number_only))

		#chiitoitsu
		if haisuu==14 and tehai9.count(2)==7:
			is_hoora=True
			hoorakeis.append([['t',i,i,None] for i in range(38) if tehai9[i]==2])
			hansuu.append(yaku_and_output(tehai9,hoorakeis[-1],did_tsumo,is_karaten,tsumohai,dahai,is_number_only))

		#analyse tehai
		#jantou
		for jantou_i in range(38):
			if tehai9[jantou_i]>=2:
				hoorakei_temp=[['j',jantou_i,jantou_i,None]]
				tehai9_temp=tehai9.copy()
				tehai9_temp[jantou_i]-=2
			else:
				continue

			#mentsu
			for mentsu_i in range(mentsusuu+1):
				if tehai9_temp==None:
					break
				elif sum(tehai9_temp)==0:
					is_hoora=True
					hoorakei_temp.sort()
					if hoorakei_temp not in hoorakeis:
						hoorakeis.append(hoorakei_temp)
						hansuu.append(yaku_and_output(tehai9,hoorakei_temp,did_tsumo,is_karaten,tsumohai,dahai,is_number_only))
						#if sanrenkoo then change to 3-shuntsu
						hoorakei_new_num=1
						while hoorakei_new_num:
							hoorakei_new_num_temp=hoorakei_new_num
							hoorakei_new_num=0
							for hoorakei_i in hoorakeis[-hoorakei_new_num_temp:]:
								for mentsu_picked_i in hoorakei_i[1:]:
									if mentsu_picked_i[0]=='k':
										kootsu_hai=mentsu_picked_i[1]
										if kootsu_hai%10<=7 and kootsu_hai<30 and ['k',kootsu_hai+1,kootsu_hai+1,kootsu_hai+1] in hoorakei_i and ['k',kootsu_hai+2,kootsu_hai+2,kootsu_hai+2] in hoorakei_i:
											hoorakei_temp=hoorakei_i.copy()
											hoorakei_temp.remove(mentsu_picked_i)
											hoorakei_temp.remove(['k',kootsu_hai+1,kootsu_hai+1,kootsu_hai+1])
											hoorakei_temp.remove(['k',kootsu_hai+2,kootsu_hai+2,kootsu_hai+2])
											hoorakei_temp.extend([['s',kootsu_hai,kootsu_hai+1,kootsu_hai+2]]*3)
											hoorakei_temp.sort()
											if hoorakei_temp not in hoorakeis:
												hoorakeis.append(hoorakei_temp)
												hoorakei_new_num+=1
												hansuu.append(yaku_and_output(tehai9,hoorakei_temp,did_tsumo,is_karaten,tsumohai,dahai,is_number_only))
					continue
				for hai_picked in range(38):
					if tehai9_temp[hai_picked]==0:
						continue
					elif tehai9_temp[hai_picked]>=3:#kootsu exists
						tehai9_temp[hai_picked]-=3
						hoorakei_temp.append(['k',hai_picked,hai_picked,hai_picked])
						break
					elif hai_picked<28 and all(tehai9_temp[hai_picked:hai_picked+3]):#shuntsu exists
						tehai9_temp[hai_picked]-=1
						tehai9_temp[hai_picked+1]-=1
						tehai9_temp[hai_picked+2]-=1
						hoorakei_temp.append(['s',hai_picked,hai_picked+1,hai_picked+2])
						break
					else:#neither kootsu nor shuntsu exists
						tehai9_temp=None
						break

		if did_tsumo==False and is_hoora:
			is_tenpai=True
			if not is_karaten:
				agarihais.append(tsumohai)
				if max(hansuu)>=13:
					kouten.append(max(hansuu)//13*13)
				else:
					kouten.append(max(hansuu))

		if did_tsumo and not is_hoora:
			if is_beginning_of_the_cosmos:
				print(s.hoora+" | 55z 5555z 5555z 5555z 5555z | "+s.beginning_of_the_cosmos+"(140"+s.fuu+"105"+s.han+" 90865195024359483499283685761351700"+s.ten+")"+s.colon+s.tsuuiisoo+s.ideographic_comma+s.sanankoo+s.ideographic_comma+s.suukantsu+s.ideographic_comma+s.rinshankaihou+s.ideographic_comma+s.yakuhai_haku+"4"+s.ideographic_comma+s.dora+"72")
			else:
				print(s.not_hoora)
				#dahai
				for sutehai_i in range(10 if is_number_only else 38):
					if sutehai_i in tehai1:
						tehai1_new=tehai1.copy()
						tehai1_new.remove(sutehai_i)
						main(tehai1=tehai1_new,dahai=sutehai_i,is_number_only=is_number_only)

		if did_tsumo:
			break
		if did_tsumo==False:
			tehai9[tsumohai]-=1

	#tenpai
	if not dahai and is_tenpai and agarihais:
		print()
		print(s.tenpai,end=s.colon)
		if not is_number_only:
			agarihai_han=list(zip(agarihais,kouten))
			agarihai_han.sort(key=lambda elem: (elem[1],elem[0]))

			for agarihai_han_i in range(len(agarihai_han)):
				print(output_hai(agarihai_han[agarihai_han_i][0],is_number_only),end=" ")
				if(agarihai_han_i!=len(agarihai_han)-1 and agarihai_han[agarihai_han_i][1]!=agarihai_han[agarihai_han_i+1][1]) or agarihai_han_i==len(agarihai_han)-1 and haisuu<=14:
					if agarihai_han[agarihai_han_i][1]>=13:
						print("("+s.yakuman_level_list[agarihai_han[agarihai_han_i][1]//13],end=") ")
					else:
						print("("+str(agarihai_han[agarihai_han_i][1])+s.han,end=") ")
		else:
			for agarihai_i in agarihais:
				print(output_hai(agarihai_i,is_number_only),end=" ")
		print()

	if not dahai and did_tsumo==False and not is_tenpai:
		print(s.nooten)

	#time spent
	end_time=time.time()
	time_spent=end_time-start_time
	if not dahai and time_spent>1.0:
		print(s.time_spent.format(round(time_spent,1)))

while True:
	main()
	print("\n**************\n")
