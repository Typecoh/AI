def find_word(self):
    wlist=[]
    #测试大词典下的效果，forcelist词典本身70个词，wlist扩大10000倍
    for i in range(10000):
        wlist.extend(self.forcelist)
    import datetime
    sentence='《钢铁是怎样炼成的》的主演是谁电影《钢铁是怎样炼成的》的主演是谁'

    de_sentence= sentence.decode('utf8')
    begin = datetime.datetime.now()
    a=0
    for fi in wlist:
        fw = fi.get_text()
        if sentence.find(fw)>-1:
            a += 1

    end = datetime.datetime.now()
    k = end - begin
    print 'find方法-找到次数：%s,耗时：%s' %(a, k.total_seconds())

    begin = datetime.datetime.now()
    a = 0
    for fi in wlist:
        fw = fi.get_text()
        if (fw in sentence):
            a+=1

    end = datetime.datetime.now()
    k=end-begin
    # print 'in方法-找到次数：%s,耗时：%s' %(a, k.total_seconds())


    compilelist=[]
    y=0
    xlen=60#每个编译语句中包含词的数量，根据词典大小调整可以进一步调高效率
    stop=False
    while not stop:
        comstr='(?:'
        for x in range(xlen):
            z=y*xlen+x
            if z>len(wlist)-1:
                stop=True
                break
            if x>0:
                comstr+='|'
            comstr+=wlist[z].get_text()
        comstr+=')'
        compilelist.append(re.compile(comstr.decode('utf8')))
        y+=1

    begin = datetime.datetime.now()
    a = 0
    for compilestr in compilelist:
        result=compilestr.search(de_sentence)
        if result:
            g=result.group()
            a += 1

    end = datetime.datetime.now()
    k = end - begin
    # print '正则方法-找到次数：%s,耗时：%s' %(a, k.total_seconds())
