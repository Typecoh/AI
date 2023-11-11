import jieba
# import wx
jieba.load_userdict("C:/Users/Lenovo/Desktop/ai实训/dictionary.txt")
# jieba.add_word("爱在西元前")
# wordseg_all = jieba.cut("《爱在西元前》是周杰伦演唱的一首歌曲，由方文山作词，周杰伦作曲，林迈可编曲，收录在周杰伦2001年9月14日发行的专辑《范特西》中", cut_all=True)
# print("全模式: " + " ".join(wordseg_all))
# 精确模式分词
# wordseg = jieba.cut("《爱在西元前》是周杰伦演唱的一首歌曲，由方文山作词，周杰伦作曲，林迈可编曲，收录在周杰伦2001年9月14日发行的专辑《范特西》中", cut_all=False)
# # print("精确模式: " + " ".join(wordseg))
# print("《"+" ".join(wordseg)+"》")
# # 输出：精确模式: 我 爱 自然语言 处理 技术 ！

# 搜索引擎模式
# wordseg_search = jieba.cut_for_search("《爱在西元前》是周杰伦演唱的一首歌曲，由方文山作词，周杰伦作曲，林迈可编曲，收录在周杰伦2001年9月14日发行的专辑《范特西》中")  
# print("搜索引擎模式:" + " ".join(wordseg_search))
# # 输出：搜索引擎模式:我 爱 自然 语言 自然语言 处理 技术 ！


import jieba.posseg as pseg
gequword = [] 
gequpos = [] 
i = -1
longword = 0
flag_wen = 0
jishu = 0
flag1 = 0 #演唱
flag2 = 0 #作词
flag3 = 0 #作曲
flag4 = 0 #编曲
name1 = "" #演唱
name2 = "" #作词
name3 = "" #作曲
name4 = "" #编曲
name5 = "" #歌曲名
name6 = "" #专辑名
wenben1 = "《晴天》是周杰伦作词、作曲、编曲并演唱的歌曲，收录在周杰伦2003年7月31日发行的专辑《叶惠美》中。"
wenben2 = "《爱在西元前》是周杰伦演唱的一首歌曲，由方文山作词，周杰伦作曲，林迈可编曲，收录在周杰伦2001年9月14日发行的专辑《范特西》中"
wenben3 = "《花海》是古小力、黄淩嘉作词，黄雨勋编曲，周杰伦作曲并演唱的歌曲，收录在周杰伦2008年10月15日发行的专辑《魔杰座》中"
wenben4 = "《青花瓷》是周杰伦演唱的一首歌曲，由方文山作词，周杰伦作曲，钟兴民编曲，收录于周杰伦2007年11月2日发行的专辑《我很忙》中"
# wenben2 = ""
# wenben3 = ""
# wenben4 = ""

for jishu in range(4):
   if jishu == 0 and wenben1 != "":
      words = pseg.cut(wenben1)
      flag_wen = 1
   if jishu == 1 and wenben2 != "":
      words = pseg.cut(wenben2)
      flag_wen = 1
   if jishu == 2 and wenben3 != "":
      words = pseg.cut(wenben3)
      flag_wen = 1
   if jishu == 3 and wenben4 != "":
      words = pseg.cut(wenben4)
      flag_wen = 1
   if flag_wen == 1:
      for word ,pos in words:
         gequword.append(word)
         gequpos.append(pos)
         longword = longword + 1
      for i in range(longword):
         if gequpos[i] == "x":
            if gequword[i] == "《":
               
               while 1:
                  i = i + 1
                  if gequpos[i] == "nr" and name6 == "" and name5 != "" : #找到专辑名了
                     name6 = gequword[i]
                  if gequword[i] == "》": #结束
                     break 
                  if gequpos[i] == "nr" and name5 == "" : #找到歌曲名了
                     name5 = gequword[i]
                  if gequword[i] == "》": #结束
                     break 
            if gequword[i] == "，":
               j = i
               cnt = 0
               while 1:
                  j = j - 1
                  if j <= 1 :
                     cnt = cnt + 1
                     j = i 
                  if gequword[j] == "，":
                     j = i
                     cnt = cnt + 1
                  if cnt >= 4:
                     cnt  = 0
                     # flag1 = 0
                     # flag2 = 0
                     # flag3 = 0
                     # flag4 = 0
                     break

                  if gequword[j] == "演唱" and flag1 == 0:
                     flag1 = 1
                     j = i
                     while 1:
                        if j <= 0 :
                           cnt = cnt + 1
                           break
                        j = j - 1
                        if gequpos[j] == "nr":
                           name1 = gequword[j]
                           j = i
                           cnt = cnt + 1
                           break
                  if gequword[j] == "作词" and flag2 == 0:
                     flag2 = 1
                     j = i
                     while 1:
                        if j <= 0 :
                           cnt = cnt + 1
                           break
                        j = j - 1
                        if gequpos[j] == "nr":
                           name2 = gequword[j]
                           j = i
                           cnt = cnt + 1
                           break
                  if gequword[j] == "作曲" and flag3 == 0:
                     flag3 = 1
                     j = i
                     while 1:
                        if j <= 0 :
                           cnt = cnt + 1
                           break
                        j = j - 1
                        if gequpos[j] == "nr":
                           name3 = gequword[j]
                           j = i
                           cnt = cnt + 1
                           break 
                  if gequword[j] == "编曲" and flag4 == 0:
                     flag4 = 1
                     j = i
                     while 1:
                        if j <= 0 :
                           cnt = cnt + 1
                           break
                        j = j - 1
                        if gequpos[j] == "nr":
                           name4 = gequword[j]
                           j = i
                           cnt = cnt + 1
                           break
   if flag_wen == 1:
      wen = "《"+name5 + "》：\n" +name1+"演唱\n"+name2+"作词\n"+name3+"作曲\n"+name4+"编曲\n"+"收录于" + "《"+name6 + "》\n"
      print( wen )
      flag_wen = 0
      gequword = [] 
      gequpos = [] 
      i = -1
      longword = 0
      jishu = 0
      flag1 = 0 #演唱
      flag2 = 0 #作词
      flag3 = 0 #作曲
      flag4 = 0 #编曲
      name1 = "" #演唱
      name2 = "" #作词
      name3 = "" #作曲
      name4 = "" #编曲
      name5 = "" #歌曲名
      name6 = "" #专辑名
