# -*- coding: utf-8 -*-
#!/usr/bin/python3
#python 3.7.2 3.7.3

"""
translated by Hu Xiangyou on February 20, 2019
translated by Hu Xiangyou on June 6, 2019
"""
title="麻雀計算機"

ask_input_tehai="手牌を入力"
help="README.mdをご覧ください"
language_switched="言語は日本語に変更されました"
has_0="「0」含み。「5」としました"
has_0m="「0m」含み。「5m」としました"
has_0p="「0p」含み。「5p」としました"
has_0s="「0s」含み。「5s」としました"
has_invalid_input="無効な入力"
low_speed="手牌が多すぎ。続行してもよろしいですか？（直接Enterキーを押して続行します）"

yakuman_level_list=('','役満','ダブル役満','トリプル役満','四倍役満','五倍役満','六倍役満','七倍役満')
kazoeyakuman='数え役満'
tehai="手牌"
more_than_4="{}は4枚以上"
more_than_14="{}枚の手牌は14枚以上"
less_than_13="{}枚の手牌は13枚以下（副露ありかも）"
taapai_or_shaopai="{}枚の手牌は多牌または少牌"
dora='ドラ'

kokushimusoujuusanmen='国士無双十三面待ち'
kokushimusou='国士無双'
chiitoitsu='七対子'
tanyaochuu='断么九'
yakuhai_ton='東'
yakuhai_nan='南'
yakuhai_shaa='西'
yakuhai_pei='北'
yakuhai_haku='白'
yakuhai_hatsu='発'
yakuhai_chun='中'
pinfu='平和'
iipeekoo='一盃口'
rinshankaihou='嶺上開花'
sanshokudoujun='三色同順'
ikkitsuukan='一気通貫'
honchantaiyaochuu='混全帯么九'
toitoihoo='対々和'
sanankoo='三暗刻'
honroutou='混老頭'
sanshokudookoo='三色同刻'
shousangen='小三元'
honiisoo='混一色'
junchantaiyaochuu='純全帯么九'
ryanpeekoo='二盃口'
chiniisoo='清一色'
suuankootanki='四暗刻単騎'
suuankoo='四暗刻'
daisangen='大三元'
tsuuiisoo='字一色'
shousuushii='小四喜'
ryuuiisoo='緑一色'
chinroutou='清老頭'
junseichuurenpouton='純正九蓮宝燈'
chuurenpouton='九蓮宝燈'
daisuushii='大四喜'
sankantsu='三槓子'
suukantsu='四槓子'
beginning_of_the_cosmos='天地創世'

hoora="和了"
fuu="符"
han="飜"
ten="点"
not_hoora="和了なし"
da="打"
karaten="空聴"
tenpai="聴牌"
nooten="不聴"

colon="："
ideographic_comma="・"
question_mark="？"
time_spent="計算は{}秒を掛かりました"

has_koyaku="古役を有効にしました"
not_has_koyaku="古役を無効にしました"
koyaku="古役"
uumensai="五門斉"
sanrenkoo="三連刻"
isshokusanjun="一色三順"
daisharin="大車輪"
daichikurin="大竹林"
daisuurin="大数隣"
daichisei="大七星"

ok="確認"
clear="取り除く"
