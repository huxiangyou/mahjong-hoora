# -*- coding: utf-8 -*-
#!/usr/bin/python3
#python 3.7.3

"""
tests for mahjong
Hu Xiangyou, April 27, 2019
"""
import random

def test():
	test_=random.choice((
		"1112345678999m",#junseichuurenpouton
		"19m19p19s1234567z",#kokushimusoujuusanmen
		"19m19p19s1234566z",#kokushimusou
		"234m234m234m222p5m",
		"1112223334445z",#daisuushii suankootanki tsuuiisoo
		"2233445566778s",#daichikurin
		"2223334446668s",#ryuuiisoo suankootanki
		"11p11155566677z",#shousangen or daisangen
		"1122334455667z",#daichisei
		"1234445677889p",#from majsoul 2018 TOP 14 by Yezhicha
		"22266688m22p222s",#from majsoul 2018 TOP 5 by Longling
		"22223334445556",
		"1112233778899",
		"123m11233p999s44z",
		"123m1123399p999s",
		"22406m34p123567s",#from majsoul introduction
		"123456789p1112s",#from majsoul introduction
		"22406m34p123567s 4s",#from majsoul introduction
		"1111111111111",
		"11111111111122222222222233333333333344444444444455555555555666666777777888888999999",
		"Hu Xiangyou",#random string
		"1145141919810",#random numbers
		"114 514 1919 810 893 931 889 464 364 721",
	))
	return test_