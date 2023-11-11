# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import jieba
import jieba.posseg as pseg
from collections import Counter
jieba.load_userdict("C:/Users/Lenovo/Desktop/ai实训/dictionary.txt")

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
cunchu1 = []#演唱
cunchu2 = []#作词
cunchu3 = []#作曲
cunchu4 = []#编曲
cunchu5 = []#歌曲名
cunchu6 = []#专辑名
textnew1 = []
textnew2 = []
textnew3 = []
textnew4 = []
textnew6 = []
outword = ""
xxx = []
wenben1 = "《晴天》是周杰伦作词、作曲、编曲并演唱的歌曲，收录在周杰伦2003年7月31日发行的专辑《叶惠美》中。"
wenben2 = "《爱在西元前》是周杰伦演唱的一首歌曲，由方文山作词，周杰伦作曲，林迈可编曲，收录在周杰伦2001年9月14日发行的专辑《范特西》中"
wenben3 = "《花海》是古小力、黄淩嘉作词，黄雨勋编曲，周杰伦作曲并演唱的歌曲，收录在周杰伦2008年10月15日发行的专辑《魔杰座》中"
wenben4 = "《青花瓷》是周杰伦演唱的一首歌曲，由方文山作词，周杰伦作曲，钟兴民编曲，收录于周杰伦2007年11月2日发行的专辑《我很忙》中"
###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 950,600 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"中文提取与整合", wx.DefaultPosition, wx.Size( -1,40 ), 0 )
		self.m_staticText1.Wrap( -1 )

		self.m_staticText1.SetFont( wx.Font( 18, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "宋体" ) )
		self.m_staticText1.SetForegroundColour( wx.Colour( 0, 185, 185 ) )

		bSizer1.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		gbSizer1 = wx.GridBagSizer( 0, 0 )
		gbSizer1.SetFlexibleDirection( wx.BOTH )
		gbSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		gbSizer2 = wx.GridBagSizer( 0, 0 )
		gbSizer2.SetFlexibleDirection( wx.BOTH )
		gbSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"提取字段1", wx.DefaultPosition, wx.DefaultSize, 0|wx.BORDER_THEME )
		self.m_staticText2.Wrap( -1 )

		self.m_staticText2.SetFont( wx.Font( 11, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Yu Gothic" ) )
		self.m_staticText2.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOTEXT ) )
		self.m_staticText2.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )

		gbSizer2.Add( self.m_staticText2, wx.GBPosition( 0, 8 ), wx.GBSpan( 1, 1 ), wx.TOP|wx.BOTTOM|wx.LEFT, 5 )

		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"提取字段2", wx.DefaultPosition, wx.DefaultSize, 0|wx.BORDER_THEME )
		self.m_staticText3.Wrap( -1 )

		self.m_staticText3.SetFont( wx.Font( 11, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Yu Gothic" ) )
		self.m_staticText3.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.m_staticText3.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )

		gbSizer2.Add( self.m_staticText3, wx.GBPosition( 0, 29 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )


		bSizer2.Add( gbSizer2, 0, wx.EXPAND, 5 )

		gbSizer3 = wx.GridBagSizer( 0, 0 )
		gbSizer3.SetFlexibleDirection( wx.BOTH )
		gbSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.tiqu1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 240,160 ), wx.TE_MULTILINE|wx.TE_NO_VSCROLL )
		gbSizer3.Add( self.tiqu1, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.tiqu2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 240,160 ), wx.TE_MULTILINE|wx.TE_NO_VSCROLL )
		gbSizer3.Add( self.tiqu2, wx.GBPosition( 0, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )


		bSizer2.Add( gbSizer3, 1, wx.EXPAND, 5 )

		gbSizer4 = wx.GridBagSizer( 0, 0 )
		gbSizer4.SetFlexibleDirection( wx.BOTH )
		gbSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText21 = wx.StaticText( self, wx.ID_ANY, u"提取字段3", wx.DefaultPosition, wx.DefaultSize, 0|wx.BORDER_THEME )
		self.m_staticText21.Wrap( -1 )

		self.m_staticText21.SetFont( wx.Font( 11, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Yu Gothic" ) )
		self.m_staticText21.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOTEXT ) )
		self.m_staticText21.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )

		gbSizer4.Add( self.m_staticText21, wx.GBPosition( 0, 8 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_staticText31 = wx.StaticText( self, wx.ID_ANY, u"提取字段4", wx.DefaultPosition, wx.DefaultSize, 0|wx.BORDER_THEME )
		self.m_staticText31.Wrap( -1 )

		self.m_staticText31.SetFont( wx.Font( 11, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Yu Gothic" ) )
		self.m_staticText31.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.m_staticText31.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )

		gbSizer4.Add( self.m_staticText31, wx.GBPosition( 0, 29 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )


		bSizer2.Add( gbSizer4, 0, wx.EXPAND, 5 )

		gbSizer5 = wx.GridBagSizer( 0, 0 )
		gbSizer5.SetFlexibleDirection( wx.BOTH )
		gbSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.tiqu3 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 240,160 ), wx.TE_MULTILINE|wx.TE_NO_VSCROLL )
		gbSizer5.Add( self.tiqu3, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.tiqu4 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 240,160 ), wx.TE_MULTILINE|wx.TE_NO_VSCROLL )
		gbSizer5.Add( self.tiqu4, wx.GBPosition( 0, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )


		bSizer2.Add( gbSizer5, 1, wx.EXPAND, 5 )

		self.m_button1 = wx.Button( self, wx.ID_ANY, u"知识提取", wx.DefaultPosition, wx.Size( 150,35 ), 0 )
		self.m_button1.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "华文中宋" ) )

		bSizer2.Add( self.m_button1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		gbSizer1.Add( bSizer2, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )

		self.m_staticline1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 1,-1 ), wx.LI_HORIZONTAL )
		gbSizer1.Add( self.m_staticline1, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.EXPAND |wx.ALL, 5 )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		gbSizer6 = wx.GridBagSizer( 0, 0 )
		gbSizer6.SetFlexibleDirection( wx.BOTH )
		gbSizer6.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText22 = wx.StaticText( self, wx.ID_ANY, u"提取处理显示2", wx.DefaultPosition, wx.Size( 90,25 ), 0|wx.BORDER_SIMPLE )
		self.m_staticText22.Wrap( -1 )

		self.m_staticText22.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOTEXT ) )
		self.m_staticText22.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )

		gbSizer6.Add( self.m_staticText22, wx.GBPosition( 0, 17 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, u"提取处理显示1", wx.DefaultPosition, wx.Size( 90,25 ), 0|wx.BORDER_SIMPLE )
		self.m_staticText13.Wrap( -1 )

		self.m_staticText13.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOTEXT ) )
		self.m_staticText13.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )

		gbSizer6.Add( self.m_staticText13, wx.GBPosition( 0, 5 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )


		bSizer3.Add( gbSizer6, 0, wx.EXPAND, 5 )

		gbSizer7 = wx.GridBagSizer( 0, 0 )
		gbSizer7.SetFlexibleDirection( wx.BOTH )
		gbSizer7.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.show1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,150 ), wx.TE_MULTILINE|wx.TE_READONLY )
		self.show1.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "宋体" ) )
		self.show1.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOTEXT ) )
		self.show1.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		gbSizer7.Add( self.show1, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.show2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,150 ), wx.TE_MULTILINE|wx.TE_READONLY )
		self.show2.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "宋体" ) )
		self.show2.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOTEXT ) )
		self.show2.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		gbSizer7.Add( self.show2, wx.GBPosition( 0, 8 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )


		bSizer3.Add( gbSizer7, 0, wx.EXPAND, 5 )

		gbSizer8 = wx.GridBagSizer( 0, 0 )
		gbSizer8.SetFlexibleDirection( wx.BOTH )
		gbSizer8.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText221 = wx.StaticText( self, wx.ID_ANY, u"提取处理显示3", wx.DefaultPosition, wx.Size( 90,25 ), 0|wx.BORDER_SIMPLE )
		self.m_staticText221.Wrap( -1 )

		self.m_staticText221.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOTEXT ) )
		self.m_staticText221.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )

		gbSizer8.Add( self.m_staticText221, wx.GBPosition( 0, 5 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_staticText131 = wx.StaticText( self, wx.ID_ANY, u"提取处理显示4", wx.DefaultPosition, wx.Size( 90,25 ), 0|wx.BORDER_SIMPLE )
		self.m_staticText131.Wrap( -1 )

		self.m_staticText131.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOTEXT ) )
		self.m_staticText131.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )

		gbSizer8.Add( self.m_staticText131, wx.GBPosition( 0, 17 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )


		bSizer3.Add( gbSizer8, 0, wx.EXPAND, 5 )

		gbSizer9 = wx.GridBagSizer( 0, 0 )
		gbSizer9.SetFlexibleDirection( wx.BOTH )
		gbSizer9.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.show3 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,150 ), wx.TE_MULTILINE|wx.TE_READONLY )
		self.show3.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "宋体" ) )
		self.show3.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOTEXT ) )
		self.show3.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		gbSizer9.Add( self.show3, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.show4 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,150 ), wx.TE_MULTILINE|wx.TE_READONLY )
		self.show4.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "宋体" ) )
		self.show4.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOTEXT ) )
		self.show4.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		gbSizer9.Add( self.show4, wx.GBPosition( 0, 8 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )


		bSizer3.Add( gbSizer9, 0, wx.EXPAND, 5 )

		bSizer5 = wx.BoxSizer( wx.VERTICAL )


		bSizer5.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		gbSizer10 = wx.GridBagSizer( 0, 0 )
		gbSizer10.SetFlexibleDirection( wx.BOTH )
		gbSizer10.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )


		gbSizer10.Add( ( 130, 0 ), wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )

		self.m_button2 = wx.Button( self, wx.ID_ANY, u"知识合并", wx.Point( 20,60 ), wx.Size( 150,35 ), 0 )
		self.m_button2.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "华文中宋" ) )

		gbSizer10.Add( self.m_button2, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )


		bSizer5.Add( gbSizer10, 1, wx.EXPAND, 5 )


		bSizer3.Add( bSizer5, 1, wx.EXPAND, 5 )


		gbSizer1.Add( bSizer3, wx.GBPosition( 0, 3 ), wx.GBSpan( 1, 1 ), 0, 5 )


		bSizer1.Add( gbSizer1, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button1.Bind( wx.EVT_BUTTON, self.chuli )
		self.m_button2.Bind( wx.EVT_BUTTON, self.hebing )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def chuli( self, event ):
         self.tian1 = self.tiqu1.GetValue()
         self.tian2 = self.tiqu2.GetValue()
         self.tian3 = self.tiqu3.GetValue()
         self.tian4 = self.tiqu4.GetValue()
         #---------------------------------------
         #放处理代码
         global gequword
         global gequpos
         global i
         global longword
         global flag_wen
         global jishu
         global flag1
         global flag2
         global flag3
         global flag4
         global name1
         global name2
         global name3
         global name4
         global name5
         global name6
         global wenben1
         global wenben2
         global wenben3
         global wenben4
         global outword
         wenben1 = self.tian1
         wenben2 = self.tian2
         wenben3 = self.tian3
         wenben4 = self.tian4
         cunchu1.clear()#演唱
         cunchu2.clear()#作词
         cunchu3.clear()#作曲
         cunchu4.clear()#编曲
         cunchu5.clear()#歌曲名
         cunchu6.clear()#专辑名
         #textnew1.clear()#演唱
         #textnew2.clear()#作词
         #textnew3.clear()#作曲
         #textnew4.clear()#编曲
         #textnew6.clear()#专辑名
         outword = ""
         xxx.clear()

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
                 print(gequword[i],end = " ")
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
                          if (gequword[j] == "作词" or gequword[j] == "填词")and flag2 == 0:
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
           if flag_wen != 1:
              if jishu == 0:
                  self.show1.SetValue("")
              if jishu == 1:
                  self.show2.SetValue("")
              if jishu == 2:
                  self.show3.SetValue("")
              if jishu == 3:
                  self.show4.SetValue("")
           if flag_wen == 1:
              
              if jishu == 0:
                  cunchu1.append(name1)
                  cunchu2.append(name2)
                  cunchu3.append(name3)
                  cunchu4.append(name4)
                  cunchu5.append(name5)
                  cunchu6.append(name6)
                  print(cunchu1[0],cunchu2[0],cunchu3[0],cunchu4[0],cunchu5[0],cunchu6[0])
                  self.tian1 = "《"+name5 + "》：\n" + name1+"演唱\n"+ name2+"作词\n"+name3+"作曲\n"+name4+"编曲\n"+"收录于" + "《"+name6 + "》" 
                  self.show1.SetValue(self.tian1)
                  print("《"+name5 + "》：" , name1+"演唱",name2+"作词",name3+"作曲",name4+"编曲","收录于" + "《"+name6 + "》" )
              if jishu == 1:
                  cunchu1.append(name1)
                  cunchu2.append(name2)
                  cunchu3.append(name3)
                  cunchu4.append(name4)
                  cunchu5.append(name5)
                  cunchu6.append(name6)
                  self.tian2 = "《"+name5 + "》：\n" + name1+"演唱\n"+ name2+"作词\n"+name3+"作曲\n"+name4+"编曲\n"+"收录于" + "《"+name6 + "》" 
                  self.show2.SetValue(self.tian2)
                  print("《"+name5 + "》：" , name1+"演唱",name2+"作词",name3+"作曲",name4+"编曲","收录于" + "《"+name6 + "》" )
              if jishu == 2:
                  cunchu1.append(name1)
                  cunchu2.append(name2)
                  cunchu3.append(name3)
                  cunchu4.append(name4)
                  cunchu5.append(name5)
                  cunchu6.append(name6)
                  self.tian3 = "《"+name5 + "》：\n" + name1+"演唱\n"+ name2+"作词\n"+name3+"作曲\n"+name4+"编曲\n"+"收录于" + "《"+name6 + "》" 
                  self.show3.SetValue(self.tian3)
                  print("《"+name5 + "》：" , name1+"演唱",name2+"作词",name3+"作曲",name4+"编曲","收录于" + "《"+name6 + "》" )
              if jishu == 3:
                  cunchu1.append(name1)
                  cunchu2.append(name2)
                  cunchu3.append(name3)
                  cunchu4.append(name4)
                  cunchu5.append(name5)
                  cunchu6.append(name6)
                  self.tian4 = "《"+name5 + "》：\n" + name1+"演唱\n"+ name2+"作词\n"+name3+"作曲\n"+name4+"编曲\n"+"收录于" + "《"+name6 + "》" 
                  self.show4.SetValue(self.tian4)
                  print("《"+name5 + "》：" , name1+"演唱",name2+"作词",name3+"作曲",name4+"编曲","收录于" + "《"+name6 + "》" )
              
                #print("《"+name5 + "》：" , name1+"演唱",name2+"作词",name3+"作曲",name4+"编曲","收录于" + "《"+name6 + "》" )
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
         outword = ""
         textnew1 = dict(Counter(cunchu1))
         textnew2 = dict(Counter(cunchu2))
         textnew3 = dict(Counter(cunchu3))
         textnew4 = dict(Counter(cunchu4))
         textnew6 = dict(Counter(cunchu6)) 
         for key , value in textnew1.items() :
            xxx.append(key + "演唱了：")
            for num1 in range(len(cunchu1)) :
                if key == cunchu1[num1]:
                  xxx.append("《" + cunchu5[num1] + "》")
            xxx.append("\n")
         for key , value in textnew2.items() :
            xxx.append(key + "作词了：")
            for num1 in range(len(cunchu1)) :
                if key == cunchu2[num1]:
                  xxx.append("《"+cunchu5[num1] + "》")
            xxx.append("\n")
         for key , value in textnew3.items() :
            xxx.append(key + "作曲了：")
            for num1 in range(len(cunchu1)) :
                if key == cunchu3[num1]:
                  xxx.append("《"+cunchu5[num1] + "》")
            xxx.append("\n")
         for key , value in textnew4.items() :
            xxx.append(key + "编曲了：")
            for num1 in range(len(cunchu1)) :
                if key == cunchu4[num1]:
                  xxx.append("《"+cunchu5[num1] + "》")
            xxx.append("\n")
         for key , value in textnew6.items() :
            xxx.append("《"+key + "》"+ "收录了：")
            for num1 in range(len(cunchu1)) :
                if key == cunchu6[num1]:
                  xxx.append("《"+cunchu5[num1] + "》")
            xxx.append("\n")
        
         for nei in xxx:
            outword = outword + nei
         print(outword)
         #---------------------------------------
         wenben1 = outword
         event.Skip()

	def hebing(self,event ):
         global wenben1
         application = wx.PySimpleApp()
        
         frame1 = MyFrame2(None)
        
        # show the frame
        
         frame1.Show(True)
        
        # start the event loop
        
         application.MainLoop()
         event.Skip()
		




class MyFrame2 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 350,520 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText20 = wx.StaticText( self, wx.ID_ANY, u"合并处理结果显示", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText20.Wrap( -1 )

		self.m_staticText20.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "华文行楷" ) )
		self.m_staticText20.SetForegroundColour( wx.Colour( 250, 196, 52 ) )
		self.m_staticText20.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer4.Add( self.m_staticText20, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_textCtrl19 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 350,480 ),  wx.TE_MULTILINE|wx.TE_READONLY)
		self.m_textCtrl19.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOTEXT ) )
		self.m_textCtrl19.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer4.Add( self.m_textCtrl19, 0, wx.ALL, 5 )
		self.m_textCtrl19.SetValue(wenben1)

		self.SetSizer( bSizer4 )
		self.Layout()


		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


        
if __name__ == '__main__':

    
    app = wx.App()

    main_win = MyFrame1(None)

    main_win.Show()

    app.MainLoop()
    
    
    
    