# -*- coding: utf-8 -*-
#!/usr/bin/python3
#python 3.7.2 3.7.3

"""
translated by Hu Xiangyou on February 20, 2019
translated by Hu Xiangyou on June 6, 2019
"""
title="麻将计算器"

ask_input_tehai="输入手牌"
help="输入手牌：m=万，p=筒，s=索，z=字。1~7z=东、南、西、北、白、发、中\n输入test查看示例\n详细内容请查看README.md"
language_switched="语言已切换至中文"
has_0="手牌含有0，按5处理"
has_0m="手牌含有0m，按5m处理"
has_0p="手牌含有0p，按5p处理"
has_0s="手牌含有0s，按5s处理"
has_invalid_input="手牌含有无效输入"
low_speed="手牌过多，确定继续吗？（直接按回车继续）"

yakuman_level_list=('','役满','两倍役满','三倍役满','四倍役满','五倍役满','六倍役满','七倍役满')
kazoeyakuman='累计役满'
tehai="手牌"
more_than_4="{}多于4张"
more_than_14="{}张手牌，多于14张"
less_than_13="{}张手牌，少于13张（可能有副露）"
taapai_or_shaopai="{}张手牌，大相公或小相公"
dora='宝牌'

kokushimusoujuusanmen='国士无双十三面'
kokushimusou='国士无双'
chiitoitsu='七对子'
tanyaochuu='断幺九'
yakuhai_ton='东'
yakuhai_nan='南'
yakuhai_shaa='西'
yakuhai_pei='北'
yakuhai_haku='白'
yakuhai_hatsu='发'
yakuhai_chun='中'
pinfu='平和'
iipeekoo='一杯口'
rinshankaihou='岭上开花'
sanshokudoujun='三色同顺'
ikkitsuukan='一气通贯'
honchantaiyaochuu='混全带幺九'
toitoihoo='对对和'
sanankoo='三暗刻'
honroutou='混老头'
sanshokudookoo='三色同刻'
shousangen='小三元'
honiisoo='混一色'
junchantaiyaochuu='纯全带幺九'
ryanpeekoo='二杯口'
chiniisoo='清一色'
suuankootanki='四暗刻单骑'
suuankoo='四暗刻'
daisangen='大三元'
tsuuiisoo='字一色'
shousuushii='小四喜'
ryuuiisoo='绿一色'
chinroutou='清老头'
junseichuurenpouton='纯正九莲宝灯'
chuurenpouton='九莲宝灯'
daisuushii='大四喜'
sankantsu='三杠子'
suukantsu='四杠子'
beginning_of_the_cosmos='天地创世'

hoora="和了"
fuu="符"
han="番"
ten="点"
not_hoora="没有和了"
da="打"
karaten="空听"
tenpai="听牌"
nooten="没有听牌"

colon="："
ideographic_comma="、"
question_mark="？"
time_spent="计算耗时{}秒"

has_koyaku="已开启古役"
not_has_koyaku="已关闭古役"
koyaku="古役"
uumensai="五门齐"
sanrenkoo="三连刻"
isshokusanjun="一色三同顺"
daisharin="大车轮"
daichikurin="大竹林"
daisuurin="大数邻"
daichisei="大七星"

ok="确定"
clear="清空"
