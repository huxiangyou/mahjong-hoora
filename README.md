# 麻将[和了](#hoora)吗？ Mahjong [Hoora](#hoora) or not?

麻雀[和了](#hoora)かい？
マージャン[ホーラ](#hoora)かい？

此文档使用中文和英语。其中英语中的专有名词使用日语的罗马字，而非英语中的对应词。  
This document is in Chinese and English. The proper nouns in English use Romaji of Japanese, not the corresponding words in English.

## 概况 Overview

![version: 2.0.1](https://img.shields.io/badge/version-2.0.1-lightgrey.svg)
![python 3.7.1](https://img.shields.io/badge/python-3.7.1-blue.svg?logo=python)
![python 3.7.2](https://img.shields.io/badge/python-3.7.2-blue.svg?logo=python)
![python 3.7.3](https://img.shields.io/badge/python-3.7.3-blue.svg?logo=python)  
![tests: passed](https://img.shields.io/badge/tests-100%25_passed,_0%25_failed-brightgreen.svg)
![checks: passed](https://img.shields.io/badge/checks-100%25_passed,_0%25_errors-brightgreen.svg)
![build: passing](https://img.shields.io/badge/build-passing-brightgreen.svg)  
![quality: good](https://img.shields.io/badge/quality-good-brightgreen.svg)
![performance: good](https://img.shields.io/badge/performance-good-brightgreen.svg)
![coverge: not tested](https://img.shields.io/badge/coverge-not_tested-lightgrey.svg)
![techdebt: little](https://img.shields.io/badge/techdebt-little-yellowgreen.svg)
![dependencies: none](https://img.shields.io/badge/dependencies-none-brightgreen.svg)
![vulnerability: not tested](https://img.shields.io/badge/vulnerability-not_tested-lightgrey.svg)  
[![issues: as many as expected](https://img.shields.io/badge/issues-as_many_as_expected-red.svg)](#已知问题-known-issues)
![bugs: 0](https://img.shields.io/badge/bugs-0-brightgreen.svg)
![errors: 0](https://img.shields.io/badge/errors-0-brightgreen.svg)
![warnings: 0](https://img.shields.io/badge/warnings-0-brightgreen.svg)  
![release date: June 2019](https://img.shields.io/badge/release_date-June_2019-lightgrey.svg)
![maintenance: yes](https://img.shields.io/badge/maintenance-yes-brightgreen.svg)  
![code size: 21.3 kB](https://img.shields.io/badge/code_size-21.3_kB-green.svg)
![coded on Visual Studio Code](https://img.shields.io/badge/coded_on-Visual_Studio_Code-lightgrey.svg?logo=Visual%20Studio%20Code)
![coded on Sublime](https://img.shields.io/badge/coded_on-Sublime-lightgrey.svg?logo=sublime%20text)
![coded on Atom](https://img.shields.io/badge/coded_on-Atom-lightgrey.svg?logo=atom)
![coded on python IDLE](https://img.shields.io/badge/coded_on-python_IDLE-lightgrey.svg?logo=python)  
[![license: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/mit-license.php)

此应用程序的功能是查看日本麻将中[手牌](#tehai)的[听牌](#tenpai)及[和牌](#hoora)的情况。  
An application that checks whether it's [tenpai](#tenpai) and [hoora](#hoora) of a [tehai](#tehai) in Japanese Mahjong.

`version 0.0` 胡祥又写于2018年12月17日；  
`version 1.0` 胡祥又写于2019年2月9日；  
`version 1.1` 胡祥又写于2019年2月20日；  
`version 1.2` 胡祥又写于2019年3月20日；  
`version 2.0` 胡祥又写于2019年4月14日。  
`version 0.0` coded by Hu Xiangyou on December 17, 2018;  
`version 1.0` coded by Hu Xiangyou on February 9, 2019;  
`version 1.1` coded by Hu Xiangyou on February 20, 2019;  
`version 1.2` coded by Hu Xiangyou on March 20, 2019;  
`version 2.0` coded by Hu Xiangyou on April 14, 2019.

## 注意 Note

* 此程序只能简单分析[听牌](#tenpai)及[和牌](#hoora)的情况，而不能分析对局场上的情况，比如不能知道[场风](#chanfon)和[自风](#menfon)，不能判断是否有[立直](#riichi)、[抢杠](#chankan)等[役](#yaku)，不能准确判断[平和](#pinfu)中的[雀头](#jantou)是否为[场风](#chanfon)或[自风](#menfon)。同时，因为不能输入[副露](#fuuro)，包含[杠子](#kantsu)，也就不能准确判断[三暗刻](#sanankoo)、[三杠子](#sankantsu)等[役](#yaku)。详情请见下文[已知问题](#已知问题-Known-Issues)一节。  
This program can only analyze the [tenpai](#tenpai) and [hoora](#hoora), but not the details of the game. For example, it can not get the [chanfon](#chanfon) or the [menfon](#menfon), can not get whether [riichi](#riichi), [chankan](#chankan), or other [yaku](#yaku), can not accurately get whether the [jantou](#jantou) in a [pinfu](#pinfu) is [chanfon](#chanfon) or the [menfon](#menfon) or not. Besides, you cannot enter [fuuro](#fuuro), including [kantsu](#kantsu), so it can not accurately get  [sanankoo](#sanankoo), [sankantsu](#sankantsu), and other [yaku](#yaku). See the [Known Issues](#已知问题-Known-Issues) section below for details.

## 文件 Files

* `mahjong.py` (`version 1.2`)（可能不可用）(Maybe not available)
* `mahjong20.py` (`version 2.0`)
* `mahjong201.py` (`version 2.0.1`)
* `mahjong201.exe` （可执行文件）(Executable file)
* `sansoo.png` （图标原图）(Original picture of the icon)
* `test.py` （测试库）(Test database)
* `lang/` （语言库）(Language databases)
* `sansoo.ico` （图标）(The icon)
* `README.md` （说明文件）(Description file)

## 使用方法 Instructions

* 如果你完全不懂什么GitHub啊什么Python啊而却又想使用此程序：  
If you don't know anything about GitHub or Python or something, but want to use this application:
    * 你需要从GitHub下载此应用的文件。点击此项目右上方的`Clone or download`，然后点击[`Download ZIP`](https://github.com/huxiangyou/mahjong-hoora/archive/master.zip)，下载文件。下载完成后，解压该压缩文件。  
    You need to download the files for this application from GitHub. Click on `Clone or download` at the top right of the repository, then click [`Download ZIP`](https://github.com/huxiangyou/mahjong-hoora/archive/master.zip) to download the file. After the download is complete, extract the compressed file.
    * 在解压出的文件中，找到`mahjong201.exe`，即为程序的可执行文件，打开它即可直接运行程序。  
    In the extracted files, find `mahjong201.exe`, which is the executable file of the program. Open it to run the program directly.
    * 程序默认为简体中文（因为我说中文）。如果需要切换至其他语言，在输入[手牌](#tehai)的地方，直接输入语言对应的代码。
        * 现提供的语言如下：
            * `zh` 中文（简体）
            * `romaji` 日语（罗马字）
            * `kanji` 日语（汉字）
            * `katakana` 日语（片假名）
            * `ja` 日语（通常用语）
    * The program defaults to Simplified Chinese (because I speak Chinese). If you need to switch to another language, input the code of other languages directly at where you input the [tehai](#tehai).
        * The languages available are as follows:
            * `zh` Chinese (Simplified)
            * `romaji` Japanese (Romaji)
            * `kanji` Japanese (Kanji)
            * `katakana` Japanese (Katakana)
            * `ja` Japanese (General)

下面为程序的使用方法。  
The following is the instruction on how to use the program.

* 输入[手牌](#tehai)：
    * 用数字`1`到`9`表示[数牌](#suupai)，[花色](#shurui)用小写字母`m`表示“[万](#manzu)”、`p`表示“[筒](#pinzu)”、`s`表示“[索](#soozu)”，写在数字后面。如`3s`表示“三索”。
    * 用`1z`到`7z`分别表示[字牌](#jihai)中的“[东](#ton)”、“[南](#nan)”、“[西](#shaa)”、“[北](#pei)”、“[白](#haku)”、“[发](#hatsu)”、“[中](#chun)”。也可以使用大写字母`E`、`S`、`W`、`N`、`P`、`F`、`C`分别表示。
    * 同种[花色](#shurui)的[牌](#hai)可以合并输入。如`1233s`表示“一索、二索、三索、三索”。
    * 要一次性输入全部[手牌](#tehai)。例如，输入`1112345678999m`即为[万字](#manzu)[纯正九莲宝灯](junseichuurenpouton)[听牌](#tenpai)时的[手牌](#tehai)； `123m456p789s111zCC`即表示“一二三万、四五六筒、七八九索、东东东、中中”。
    * 注意：不能输入[杠子](#kantsu)；如果手牌中有[杠子](#kantsu)，按[刻子](#kootsu)输入，或者不输入。
    * 输入完成后，按回车(`Enter`)。
* Input [tehai](#tehai):
    * Use number `1` to `9` for [suupai](#suupai); and a lower-case letter after the number for [shurui](#shurui), `m` for "[manzu](#manzu)", `p` for "[pinzu](#pinzu)", `s` for "[soozu](#soozu)"。E.g., `3s` means "sansoo".
    * Use `1z` to `7z` for [jihai](#jihai) "[ton](#ton)", "[nan](#nan)", "[shaa](#shaa)", "[pei](#oei)", "[haku](#haku)", "[hatsu](#hatsu)", "[chun](#chun)". Upper-case letters `E`, `S`, `W`, `N`, `P`, `F`, `C` are also for these.
    * [Hai](#hai) with the same [shurui](#shurui) can be input together. E.g., `1233s` for "iisoo, ryansoo, sansoo, sansoo".
    * Enter all [tehai](#tehai) in a line. For example, `1112345678999m` is the [tehai](#tehai) of [manzu](#manzu) [junseichuurenpouton](#junseichuurenpouton) [tenpai](#tenpai); `123m456p789s111zCC` is for "ii-ryan-sanman, suu-uu-roopin, chii-paa-chuusoo, ton-ton-ton, chun-chun".
    * Note: Do not input [kantsu](#kantsu); if [tehai](#tehai) has [kantsu](#kantsu), input it as a [kootsu](#kootsu), or just omit it.
    * After the input, press `Enter`。
* 输入`exit`退出。
* Input `exit` to exit.
* 输入语言对应的代码来切换语言。
    * 现提供的语言如下：
        * `zh` 中文（简体）
        * `romaji` 日语（罗马字）
        * `kanji` 日语（汉字）
        * `katakana` 日语（片假名）
        * `ja` 日语（通常用语）
* Input the code of other languages to switch to other languages.
    * The languages available are as follows:
        * `zh` Chinese (Simplified)
        * `romaji` Japanese (Romaji)
        * `kanji` Japanese (Kanji)
        * `katakana` Japanese (Katakana)
        * `ja` Japanese (General)
* 当输入的[手牌](#tehai)为14张或(3n+2)张时，则判断是否[和了](#hoora)。
    * 如果[和了](#hoora)，则输出[和牌型](#hoorakei)及可能的[役](#yaku)。
    * 如果没有[和了](#hoora)，但已[听牌](#tenpai)，则判断[舍张](#sutehai)是哪张即可[听牌](#tenpai)，并输出[听牌型](#tenpaikei)及可能的[役](#yaku)。
* 当输入的[手牌](#tehai)为13张或(3n+1)张时，则判断是否[听牌](#tenpai)。
    * 如果[听牌](#tenpai)，则输出[听牌型](#tenpaikei)及可能的[役](#yaku)。
* [手牌](#tehai)多于14张时将不输出[役](#yaku)。
* If [tehai](#tehai) is 14 or (3n+2), then check whether [hoora](#hoora).
    * If [hoora](#hoora), then output the [hoorakei](#hoorakei) and possible [yaku](#yaku).
    * If not [hoora](#hoora), but [tenpai](#tenpai), then check which [tehai](#tehai) is the [sutehai](#sutehai) to [tenpai](#tenpai), and then output the [tenpaikei](#tenpaikei) and possible [yaku](#yaku).
*  If [tehai](#tehai) is 13 or (3n+1), then check whether [tenpai](#tenpai).
    * If [tenpai](#tenpai), then output the [tenpaikei](#tenpaikei) and possible [yaku](#yaku).
* [Yaku](#yaku) will not be output if [tehai](#tehai) is more than 14.

程序正确工作的输入输出举例：  
Examples when the application works fine:

```
输入手牌：123m789p45888s33z

手牌：123m 789p 45888s 西西

听牌 [3s] | 33z 888s 123m 789p 345s |
听牌 [6s] | 33z 888s 123m 789p 456s |

听牌：3s 6s (0番)

**************

输入手牌：345m345p1134567s

手牌：345m 345p 1134567s

听牌 [2s] | 11s 345m 345p 234s 567s |  1番：平和
听牌 [5s] | 11s 345m 345p 345s 567s |  3番：平和、三色同顺
听牌 [8s] | 11s 345m 345p 345s 678s |  3番：平和、三色同顺

听牌：2s (1番) 5s 8s (3番)

**************

输入手牌：1112345678999m

手牌：1112345678999m

听牌 [1m] | 99m 111m 123m 456m 789m | 两倍役满：一气通贯、纯正九莲宝灯
听牌 [2m] | 22m 111m 999m 345m 678m | 两倍役满：纯正九莲宝灯
听牌 [3m] | 11m 999m 123m 345m 678m | 两倍役满：纯正九莲宝灯
听牌 [4m] | 99m 111m 234m 456m 789m | 两倍役满：纯正九莲宝灯
听牌 [5m] | 55m 111m 999m 234m 678m | 两倍役满：纯正九莲宝灯
听牌 [6m] | 11m 999m 123m 456m 678m | 两倍役满：纯正九莲宝灯
听牌 [7m] | 99m 111m 234m 567m 789m | 两倍役满：纯正九莲宝灯
听牌 [8m] | 88m 111m 999m 234m 567m | 两倍役满：纯正九莲宝灯
听牌 [9m] | 11m 999m 123m 456m 789m | 两倍役满：一气通贯、纯正九莲宝灯

听牌：1m 2m 3m 4m 5m 6m 7m 8m 9m (两倍役满)

**************

输入手牌：22223333444457m

手牌：22223333444457m

没有和了
打 [2m] 听牌 [6m] | 22m 333m 444m 234m 567m |  7番：断幺九、清一色
打 [2m] 听牌 [7m] | 77m 222m 333m 444m 345m |  9番：断幺九、三暗刻、清一色
打 [2m] 听牌 [7m] | 77m 234m 234m 234m 345m |  8番：断幺九、一杯口、清一色
打 [3m] 听牌 [6m] | 33m 222m 444m 234m 567m |  7番：断幺九、清一色
打 [4m] 听牌 [6m] | 44m 222m 333m 234m 567m |  7番：断幺九、清一色
打 [5m] 听牌 [7m] | 77m 222m 333m 444m 234m |  9番：断幺九、三暗刻、清一色
打 [5m] 听牌 [7m] | 77m 234m 234m 234m 234m | 10番：断幺九、二杯口、清一色
打 [7m] 听牌 [1m] | 33m 222m 444m 123m 345m |  6番：清一色
打 [7m] 空听 [2m] | 22m 222m 333m 444m 345m |  9番：断幺九、三暗刻、清一色
打 [7m] 空听 [2m] | 22m 234m 234m 234m 345m |  9番：断幺九、平和、一杯口、清一色
打 [7m] 空听 [3m] | 44m 222m 333m 234m 345m |  7番：断幺九、清一色
打 [7m] 空听 [4m] | 33m 222m 444m 234m 345m |  7番：断幺九、清一色
打 [7m] 听牌 [5m] | 22m 234m 234m 345m 345m | 11番：断幺九、平和、二杯口、清一色
打 [7m] 听牌 [5m] | 55m 222m 333m 444m 234m |  9番：断幺九、三暗刻、清一色
打 [7m] 听牌 [5m] | 55m 234m 234m 234m 234m | 10番：断幺九、二杯口、清一色
打 [7m] 听牌 [6m] | 44m 222m 333m 234m 456m |  7番：断幺九、清一色

**************

输入手牌：exit
```
* 输入`test`来从测试库中随机取出一项测试。  
Input `test` to pick one test from the test database to test.

## 名词表 Nouns

注：以下列出的词语中部分为动词。以下列出的词语中部分没有在程序中使用。  
Note: Some of the words below are verbs. Some of the words below are not used in programming.

| 罗马字<br>Romaji<br> | 日语<br>Japanese | 中文<br>Chinese | 英语<br>English | 备注 Note |
|:--:|:--:|:--:|:--:|:--:|
| <a name="hai">hai</a> | 牌 | 牌 | tile | |
| <a name="shurui">shurui</a> | 種類 | 花色 | | |
| m<br><a name="manzu">manzu</a> | 萬 | 万 | character | 程序中使用`manzu`来用表示[手牌](#tehai)中有哪些[万子](#manzu)，用`manzu9`来表示1到9万各有几张。<br>In programming, `manzu` is used to list what [manzu](#manzu) are there in the [tehai](#tehai), and `manzu9` is used to list how many iiman to chuuman are there. |
| p<br><a name="pinzu">pinzu</a> | 筒 | 筒<br>饼 | dot | 程序中使用`pinzu`来用表示[手牌](#tehai)中有哪些[筒子](#pinzu)，用`pinzu9`来表示1到9筒各有几张。<br>In programming, `pinzu` is used to list what [pinzu](#pinzu) are there in the [tehai](#tehai), and `pinzu9` is used to list how many from iipin to chuupin are there. |
| s<br><a name="soozu">soozu</a> | 索 | 索<br>条 | bamboo | 程序中使用`soozu`来用表示[手牌](#tehai)中有哪些[索子](#soozu)，用`soozu9`来表示1到9索各有几张。<br>In programming, `soozu` is used to list what [soozu](#soozu) are there in the [tehai](#tehai), and `soozu9` is used to list how many from iisoo to chuusoo are there. |
| <a name="ton">ton</a> | 東 | 东<br>东风 | East | |
| <a name="nan">nan</a> | 南 | 南<br>南风 | South | |
| <a name="shaa">shaa</a> | 西 | 西<br>西风 | West | |
| <a name="pee">pee</a> | 北 | 北<br>北风 | North | |
| <a name="haku">haku</a> | 白 | 白<br>白板 | White | |
| <a name="hatsu">hatsu</a> | 發 | 发<br>发财 | Green | |
| <a name="chun">chun</a> | 中 | 中<br>红中 | Red | |
| <a name="suupai">suupai</a> | 数牌 | 序数牌 | suit | |
| <a name="yaochuupai">yaochuupai</a> | 么九牌 | 幺九牌 | terminal and honor | |
| <a name="chunchanpai">chunchanpai</a> | 中張牌 | 中张牌 | simple | |
| <a name="routouhai">routouhai</a> | 老頭牌 | 老头牌 | terminal | |
| <a name="jihai">jihai</a> | 字牌 | 字牌 | honor | |
| <a name="kazepai">kazepai</a> | 風牌 | 风牌 | wind | |
| <a name="sangenpai">sangenpai</a> | 三元牌 | 三元牌 | dragon | |
| <a name="tehai">tehai</a> | 手牌 | 手牌 | hand | |
| <a name="fuuro">fuuro</a> | 副露 | 鸣牌 | call | |
| <a name="juntehai">juntehai</a> | 純手牌 | | | 除[鸣牌](#fuuro)外的[手牌](#tehai)。<br>[Tehai](#tehai) except [fuuro](#fuuro) ones. |
| <a name="agarihai">agarihai</a> | 和了牌 | | | |
| <a name="taapai">taapai</a> | 多牌 | 大相公 | | |
| <a name="shaopai">shaopai</a> | 少牌 | 小相公 | | |
| <a name="hoorakei">hoorakei</a> | 和了形 | 和牌型 | | |
| <a name="ippankei">ippankei</a> | 一般形 | 普通型 | | 不是国士无双和七对子的和牌型。<br>[Hoorakei](#hoorakei) that is not [kokushimusou](#kokushimusou) or [chiitoitsu](#chiitoitsu). |
| <a name="tenpaikei">tenpaikei</a> | 聴牌形 | 听牌型 | | |
| <a name="mentsu">mentsu</a> | 面子 | 顺刻杠子 | set | |
| <a name="kootsu">kootsu</a> | 刻子 | 刻子 | triplet | |
| <a name="shuntsu">shuntsu</a> | 順子 | 顺子 | sequence | |
| <a name="kantsu">kantsu</a> | 槓子 | 杠子 | kong | |
| <a name="toitsu">toitsu</a> | 対子 | 对子 | pair | |
| <a name="jantou">jantou</a> | 雀頭 | 将牌 | head | |
| <a name="tanpai">tanpai</a> | 単牌 | 单张 | orphan | |
| <a name="tsumo">tsumo</a> | 自摸 | 摸牌 | draw | |
| <a name="dahai">dahai</a> | 打牌 | 出牌 | discard | |
| <a name="tsumohai">tsumohai</a> | 自摸牌 | 进张 | | |
| <a name="sutehai">sutehai</a> | 捨て牌 | 舍张 | | |
| <a name="chii">chii</a> | 吃 | 吃 | chow | |
| <a name="pon">pon</a> | 碰 | 碰 | pung | |
| <a name="kan">kan</a> | 槓 | 杠 | kong | |
| <a name="tsumohoo">tsumohoo</a> | 自摸和 | 自摸 | self drawn | |
| <a name="ronhoo">ronhoo</a> | 栄和 | 点和 | on a discard | |
| <a name="tenhai">tenpai</a> | 聴牌 | 听牌 | ready | |
| <a name="nooten">nooten</a> | 不聴 | 没有听牌 | not ready | |
| <a name="hoora">hoora</a> | 和了 | 和牌 | win | |
| <a name="keishikitenpai">keishikitenpai</a> | 形式聴牌 | 形式听牌 | | |
| <a name="karaten">karaten</a> | 空聴 | 空听 | | |
| <a name="chanfon">chanfon</a> | 圏風 | 场风 | prevalent wind | |
| <a name="menfon">menfon</a> | 門風 | 自风 | seat wind | |
| <a name="yaku">yaku</a> | 役 | 役 | | |
| <a name="han">han</a> | 飜 | 番 | | |
| <a name="hansuu">hansuu</a> | 飜数 | 番数 | | |
| <a name="koutenhou">koutenhou</a> | 高点法 | 就高不就低原则 | | |
| <a name="kouten">kouten</a> | 高点 | 高分 | | |
| <a name="takame">takame</a> | 高目 | 高分和牌 | | |
| <a name="yasume">yasume</a> | 安目 | 低分和牌 | | |
| <a name="dotakame">dotakame</a> | ド高目 | 最高分和牌 | | |
| <a name="mangan">mangan</a> | 満貫 | 满贯 | | |
| <a name="haneman">haneman</a> | 跳満 | 跳满 | | |
| <a name="baiman">baiman</a> | 倍満 | 倍满 | | |
| <a name="sanbaiman">sanbaiman</a> | 三倍満 | 三倍满 | | |
| <a name="yakuman">yakuman</a> | 役満 | 役满 | | |
| <a name="kazoeyakuman">kazoeyakuman</a> | 数え役満 | 累计役满 | | |
| <a name="daburuyakuman">daburuyakuman</a> | ダブル役満 | 两倍役满 | | |
| <a name="toripuruyakuman">toripuruyakuman</a> | トリプル役満 | 三倍役满 | | |
| <a name="yonbaiyakuman">yonbaiyakuman</a> | 四倍役満 | 四倍役满 | | |
| <a name="gobaiyakuman">gobaiyakuman</a> | 五倍役満 | 五倍役满 | | |
| <a name="rokubaiyakuman">rokubaiyakuman</a> | 六倍役満 | 六倍役满 | | |
| <a name="menzenchin">menzenchin</a> | 門前清 | 门前清 | concealed | |
| <a name="kuisagari">kuisagari</a> | 喰い下がり | 副露减一番 | | |
| <a name="menzenyaku">menzenyaku</a> | 門前役 | 门前清限定役 | | |
| <a name="kuisagariyaku">kuisagariyaku</a> | 喰い下がり役 | 副露减一番的役 | | |
| <a name="dora">dora</a> | ドラ | 宝牌 | | |
| <a name="akadora">akadora</a> | 赤ドラ | 红宝牌 | red tile | |
| <a name="riichi">riichi</a> | 立直 | 立直 | | |
| <a name="ippatsu">ippatsu</a> | 一発 | 一发 | one shot | |
| <a name="menzenchintsumohoo">menzenchintsumohoo</a> | 門前清自摸和 | 不求人 | fully concealed hand | |
| <a name="tanyaochuu">tanyaochuu</a> | 断么九 | 断幺九 | all simples | |
| <a name="pinfu">pinfu</a> | 平和 | 平和 | all chows | |
| <a name="iipeekoo">iipeekoo</a> | 一盃口 | 一般高 | pure double chow | |
| <a name="yakuhai">yakuhai</a> | 役牌 | 役牌 | | |
| <a name="chanfonpai">chanfonpai</a> | 圏風牌 | 场风牌 | prevalent wind | |
| <a name="menfonpai">menfonpai</a> | 門風牌 | 自风牌 | seat wind | |
| <a name="renfonpai">renfonpai</a> | 連風牌 | 连风牌 | | |
| <a name="rinshankaihou">rinshankaihou</a> | 嶺上開花 | 岭上开花 | out on a replacement | |
| <a name="chankan">chankan</a> | 槍槓 | 抢杠 | robbing the kong | |
| <a name="haiteimooyue">haiteimooyue</a> | 海底摸月 | 妙手回春 | last tile draw | |
| <a name="hooteiraoyui">hooteiraoyui</a> | 河底撈魚 | 海底捞月 | last tile discard | |
| <a name="dabururiichi">dabururiichi</a> | ダブル立直 | 二重立直 | | |
| <a name="sanshokudookoo">sanshokudoujun</a> | 三色同順 | 三色三同顺 | mixed triple chow | |
| <a name="ikkitsuukan">ikkitsuukan</a> | 一気通貫 | 一条龙 | pure straight | |
| <a name="honchantaiyaochuu">honchantaiyaochuu</a> | 混全帯么九 | 全带幺 | outside hand | |
| <a name="chiitoitsu">chiitoitsu</a> | 七対子 | 七将 | seven pairs | |
| <a name="toitoihoo">toitoihoo</a> | 対々和 | 碰碰和 | all pungs | |
| <a name="sanankoo">sanankoo</a> | 三暗刻 | 三暗刻 | three concealed pungs | |
| <a name="honroutou">honroutou</a> | 混老頭 | 混老头 | all terminals and honors | |
| <a name="sanshokudookoo">sanshokudookoo</a> | 三色同刻 | 三同刻 | triple pung | |
| <a name="sankantsu">sankantsu</a> | 三槓子 | 三杠 | three kongs | |
| <a name="shousangen">shousangen</a> | 小三元 | 小三元 | little three dragons | |
| <a name="honiisoo">honiisoo</a> | 混一色 | 混一色 | half flush | |
| <a name="junchantaiyaochuu">junchantaiyaochuu</a> | 純全帯么九 | 纯全带幺九 | terminals in all sets | |
| <a name="ryanpeekoo">ryanpeekoo</a> | 二盃口 | 二般高 | twice pure double chow | |
| <a name="chiniisoo">chiniisoo</a> | 清一色 | 清一色 | full flush | |
| <a name="kokushimusou">kokushimusou</a> | 国士無双 | 十三幺 | thirteen orphans | |
| <a name="sanankoo">suuankoo</a> | 四暗刻 | 四暗刻 | four concealed pungs | |
| <a name="daisangen">daisangen</a> | 大三元 | 大三元 | big three dragons | |
| <a name="tsuuiisoo">tsuuiisoo</a> | 字一色 | 字一色 | all honors | |
| <a name="shousuushii">shousuushii</a> | 小四喜 | 小四喜 | little four winds | |
| <a name="ryuuiisoo">ryuuiisoo</a> | 緑一色 | 绿一色 | all green | |
| <a name="chinroutou">chinroutou</a> | 清老頭 | 清幺九 | all terminals | |
| <a name="suukantsu">suukantsu</a> | 四槓子 | 四杠 | four kongs | |
| <a name="chuurenpouton">chuurenpouton</a> | 九蓮宝燈 | 九莲宝灯 | nine gates | |
| <a name="tenhou">tenhou</a> | 天和 | 天和 | blessing of heaven | |
| <a name="chiihou">chiihou</a> | 地和 | 地和 | blessing of earth | |
| <a name="daisuushii">daisuushii</a> | 大四喜 | 大四喜 | big four winds | |
| <a name="suuankootanki">suuankootanki</a> | 四暗刻単騎 | 四暗刻单钓将 | four concealed pungs with single wait | |
| <a name="kokushimusoujuusanmen">kokushimusoujuusanmen</a> | 国士無双十三面 | 国士无双十三面听牌 | pure thirteen orphans | |
| <a name="junseichuurenpouton">junseichuurenpouton</a> | 純正九蓮宝燈 | 纯正九莲宝灯 | pure nine gates | |
| <a name="fu">fu</a> | 符 | 符 | | |
| <a name="fusuu">fusuu</a> | 符数 | 符数 | | |
| <a name="tensuu">tensuu</a> | 点数 | 分数 | score | |

## 版本更新 What's New

### version 0.0
2018年12月17日  
December 17, 2018

1. 完成程序框架。  
Built the frame of the program.

### version 1.0
2019年2月9日  
February 9, 2019

1. 完成程序。  
Completed.

### version 1.1
2019年2月20日  
February 20, 2019

1. 改进了[高目](#takame)的输出方式。  
Improved the way to output [tekame](#takame).
2. 添加了一些语言。  
Added languages.
3. 增加了一个彩蛋。参见[彩蛋](#彩蛋-easter-eggs)。  
Added an easter egg. Check [Easter eggs](#彩蛋-easter-eggs).

### version 1.2
2019年3月20日  
March 20, 2019

1. 可切换语言。  
Switchable languages.
2. 支持更多种[手牌](#tehai)输入表示方法。  
Supported more ways to input [tehai](#tehai).

### version 1.2.1
2019年4月9日  
April 9, 2019

1. 一个很小的优化。  
A very small improvement.

### version 2.0
2019年4月14日  
April 14, 2019

1. 对性能做出了大幅度优化。  
A big improvement on the performance.
2. 增加测试功能。可随机生成[手牌](#tehai)进行测试。  
Added the test function. A [tehai](#tehai) can be randomly generated for testing.
3. 增加计时功能。当计算耗时超过1秒时，显示计算用时。  
Added the timing function. When the calculation takes more than 1 second, the calculation time will be displayed.

### version 2.1
2019年4月21日  
April 21, 2019

1. 对性能做出了优化。  
An improvement on the performance.

## 已知问题 Known issues

[i1]: https://img.shields.io/badge/issue-solved-brightgreen.svg
[i2]: https://img.shields.io/badge/issue-improved-green.svg
[i3]: https://img.shields.io/badge/issue-improving-yellowgreen.svg
[i4]: https://img.shields.io/badge/issue-not_to_be_solved-red.svg

| | |
| -- | -- |
| ![solved][i1] | 此问题已解决。<br>This issue has been solved. |
| ![improved][i2] | 此问题已尽可能改善。<br>This issue has been improved as much as possible. |
| ![improving][i3] | 正在尝试改善。<br>I'm trying to improve it. |
| ![not to be solved][i4] | 这个问题将不会解决。<br>This issue will not be solved. |

1. 输入[手牌](#tehai)时，不能区分[纯手牌](#juntehai)和[副露](#fuuro)。  
When inputting [tehai](#tehai), can not distinguish [juntehai](#juntehai) and [fuuro](#fuuro).  
![not to be solved][i4]
2. 输入[手牌](#tehai)时，可能会输入奇怪的符号，而这些符号可能无法被正确处理。  
When inputting [tehai](#tehai), strange symbols may be input, and these symbols may not be processed correctly.  
![improved][i2]  
    * 输入中的下列符号将被忽略：  
    The following symbols in the input will be ignored:  
    `!` `"` `#` `$` `%` `&` `'` `(` `)` `*` `+` `,` `-` `.` `/` `:` `;` `<` `=` `>` `?` `@` `[` `\` `]` `^` `_` `` ` `` `{` `|` `}` `~`
    * 无法处理的符号将出现提示：  
    A prompt will appear for symbols that can not be processed:  
    `手牌含有无效输入`  
    `Tehai has invalid input`
3. 输入[手牌](#tehai)时，如果含有此程序不能理解的输入，则不能正确处理。  
When inputting [tehai](#tehai), if it has input that can not be understood by this program, it will not be processed correctly.  
![improved][i2]  
    * 可以用`w`表示[万](#manzu)，但不能用`t`表示[筒](#pinzu)或[条](#soozu)。  
    `w` is for [wanzu](#manzu), but `t` is not for [tonzu](#pinzu) or [tiaozi](#soozu).
        * 也可以用汉字`万`、`萬`，`筒`、`饼`、`餠`、`餅`，`索`、`条`、`條`。  
        Kanji `万`, `萬`, `筒`, `饼`, `餠`, `餅`, `索`, `条`, `條` can also be used. (Not in the English language mode.)
    * 不能用`T`表示[东](#ton)或[中](#chun)；不能用`N`（[北](#pee)）表示[南](#nan)；不能用`S`（[南](#nan)）表示[西](#shaa)；不能用`P`（[发](#hatsu)）表示[北](#pee)。  
    `T` is not for [ton](#ton) or [chun](#chun); `N` is for [north](#pee) instead of [nan](#nan); `S` is for [south](#nan) instead of [shaa](#shaa); `P` is for [hatsu](#hatsu) instead of [pee](#pee).
        * 可以用`D`表示[白](#hatsu)；可以用`H`或`R`表示[发](#hatsu)。  
        `D` is for [hatsu](#hatsu); `H` and `R` are for [hatsu](#hatsu).
        * 也可以用汉字`東`、`东`、`南`、`西`、`北`、`白`、`發`、`発`、`发`、`中`。
        Kanji `東`, `东`, `南`, `西`, `北`, `白`, `發`, `発`, `发`, `中` can also be used.
    * `0m`、`0p`、`0s`用来表示[红宝牌](#akadora)，但不能计入[番数](#hansuu)。  
    `0m`, `0p`, `0s` are used for [akadora](#akadora), but are not counted into the [hansuu](#hansuu).
        * 但`0z`、`8z`、`9z`为无效输入。  
        But `0z`, `8z`, `9z` are invalid inputs.
    * 可以使用全角数字(`０`、`１`、`２`、`３`、`４`、`５`、`６`、`７`、`８`、`９`)和全角英语字母(`ｍ`、`ｐ`、`ｓ`等)。  
    Full-width numbers (`０`, `１`, `２`, `３`, `４`, `５`, `６`, `７`, `８`, `９`)  and full-width English letters (`ｍ`, `ｐ`, `ｓ`, etc.) can be used.
4. [听牌型](#tenpaikei)或[和牌型](#hoorakei)的输出顺序没有规律。  
The order of [tenpaikei](#tenpaikei) or [hoorakei](#hoorakei) outputs are not regular.  
![improving][i4]
    * 在`version 1`中，[听牌型](#tenpaikei)或[和牌型](#hoorakei)是按照[雀头](#jantou)和[面子](#mentsu)排序并输出的。但这样会非常占用内存，导致计算时间变长。在`version 2`中，取消了这种输出方式，改为按照计算顺序输出。  
    In `version 1`, [tenpaikei](#tenpaikei) or [hoorakei](#hoorakei) are output sorted by [jantou](#jantou) and [mentsu](#mentsu). But this will take up a lot of memory, which will make the calculation time longer. In `version 2`, this output mode was canceled, and outputs are in the order of calculation.
5. 此程序不能准确分析部分[役](#yaku)。  
Some [yaku](#yaku) cannot be analyzed accurately.  
![improving][i4]
    * 关于[场风](#chanfon)和[自风](#menfon)。  
    About [chanfon](#chanfon) or the [menfon](#menfon).
        * [役牌](#yakuhai)中的[东](#ton)、[南](#nan)、[西](#shaa)、[北](#pee)。只要[手牌](#tehai)中出现了[役牌](#yakuhai)的[刻子](#kootsu)，就会被判断为[役牌](#yakuhai)。但当同时出现了多个[场风](#chanfon)和[自风](#menfon)时，最多只会计2个。同时，[连风牌](#renfonpai)只会计1次。  
        [Ton](#ton), [nan](#nan), [shaa](#shaa), [pee](#pee), as [yakuhai](#yakuhai). As long as [yakuhai](#yakuhai)'s [kootsu](#kootsu) are in [tehai](#tehai), they will be taken as [yakuhai](#yakuhai). But if there are more than 2 [chanfon](#chanfon) or the [menfon](#menfon), only 2 of them will be counted. Besides, [renfonpai](#renfonpai) will only be counted once.
        * [平和](#pinfu)。[雀头](#jantou)为[东](#ton)、[南](#nan)、[西](#shaa)、[北](#pee)，都会判断为[平和](#pinfu)。  
        [Pinfu](#pinfu). It will be taken as [pinfu](#pinfu), no longer the [jantou](#jantou) is [ton](#ton), [nan](#nan), [shaa](#shaa), or [pee](#pee).
    * 关于[门前清](#menzenchin)。  
    About [menzenchin](#menzenchin).
        * 不论是否为[门前清](#menzenchin)，都会计算这些[役](#yaku)：[平和](#pinfu)、[一杯口](#iipeekoo)、[七对子](#chiitoitsu)、[二杯口](#ryanpeekoo)、[四暗刻](#suuankoo)、[九莲宝灯](#chuurenpouton)、[纯正九莲宝灯](#junseichuurenpouton)。  
        No longer it is [menzenchin](#menzenchin) or not, these [yaku](#yaku) will be calculated: [pinfu](#pinfu), [iipeekoo](#iipeekoo), [chiitoitsu](#chiitoitsu), [ryanpeekoo](#ryanpeekoo), [suuankoo](#suuankoo), [chuurenpouton](#chuurenpouton), [junseichuurenpouton](#junseichuurenpouton).
        * 不论是否为[门前清](#menzenchin)，这些[役](#yaku)都会按照[门前清](#menzenchin)计算[番数](#hansuu)：[一气通贯](#ikkitsuukan)、[三色同顺](#sanshokudoujun)、[混全带幺九](#honchantaiyaochuu)、[纯全带幺九](#junchantaiyaochuu)、[混一色](#honiisoo)、[清一色](#chiniisoo)。  
        No longer it is [menzenchin](#menzenchin) or not, these [yaku](#yaku)'s [hansuu](#hansuu) will be calculated as [menzenchin](#menzenchin): [ikkitsuukan](#ikkitsuukan), [sanshokudoujun](#sanshokudoujun), [honchantaiyaochuu](#honchantaiyaochuu), [junchantaiyaochuu](#junchantaiyaochuu), [honiisoo](#honiisoo), [chiniisoo](#chiniisoo).
    * 关于[杠子](#kantsu)。  
    About [kantsu](#kantsu).
        * 不能判断下列[役](#yaku)：[三杠子](#sankantsu)、[四杠子](#suukantsu)。  
        Cannot analyze these [yaku](#yaku): [sankantsu](#sankantsu), [suukantsu](#suukantsu).
    * 关于偶然役。  
    About guuzenyaku.
        * 不能判断下列[役](#yaku)：[立直](#riichi)、[一发](#ippatsu)、[门前清自摸和](#menzenchintsumohoo)、[海底摸月](#haiteimooyue)、[河底捞鱼](#hooteiraoyui)、[抢杠](#chankan)、[岭上开花](#rinshankaihou)、[双立直](#dabururiichi)、[天和](#tenhou)、[地和](#chiihou)。  
        Cannot analyze these [yaku](#yaku): [riichi](#riichi), [ippatsu](#ippatsu), [menzenchintsumohoo](#menzenchintsumohoo), [haiteimooyue](#haiteimooyue), [hooteiraoyui](#hooteiraoyui), [chankan](#chankan), [rinshankaihou](#rinshankaihou), [dabururiichi](#dabururiichi), [tenhou](#tenhou), [chiihou](#chiihou)。  
6. 此程序暂无英语版。  
This program has no English version now.  
![improving][i3]
    * 部分内容在英语中没有对应的翻译。  
    Some nouns have no translation in English.
    * 罗马字版中的文字部分亦为英语，可暂时使用它代替。  
    The texts in Romaji are also in English. Temporarily use it as an alternative.

如果你发现了其他问题，请在[Issues](https://github.com/huxiangyou/mahjong-hoora/issues)中反馈。  
If you find any other issues, plear tell me at [Issues](https://github.com/huxiangyou/mahjong-hoora/issues).

## 性能 Performance

`version 2.0`后，性能已有大幅改善。此处不再赘述。  
After `version 2.0`, performance has dramatically improved. So I won't go into details here.

我使用如下输入进行测试。在`version 1.2`中，完整计算时间为数分钟；而在`version 2.0`中，只需数秒。  
I used the following input to test. In `version 1.2`, the full calculation time is a few minutes; in `version 2.0,` it takes only a few seconds.

输入：Input:
`11111111111122222222222233333333333344444444444455555555555666666777777888888999999`

## 彩蛋 Easter eggs

* 输入18个[白](#haku)(`P`)，除正常的计算外，还会出现“天地创世”(`beginning of the cosmos`)的[听牌型](#tenpaikei)或[和牌型](#hoorakei)，并计算[点数](#tensuu)。  
When input 18 [haku](#haku)'s, in addition to the normal calculations, the [tenpaikei](#tenpaikei) or [hoorakei](#hoorakei) of the `beginning of the cosmos` will appear, with the calculated [tensuu](#tensuu).

```
输入手牌：PPPPPPPPPPPPPPPPPP

手牌：白 白 白 白 白 白 白 白 白 白 白 白 白 白 白 白 白 白 (18)

白多于4张
18张手牌，多于14张

和了：
55z 5555z 5555z 5555z 5555z | 天地创世(140符105番 90865195024359483499283685761351700点)：字一色、三暗刻、四杠子、岭上开花、役牌白4、宝牌72
```

## 许可 License

[![license: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/mit-license.php)

此程序使用[MIT许可协议](https://opensource.org/licenses/mit-license.php)授权。  
This program is licensed under The [MIT License](https://opensource.org/licenses/mit-license.php).
