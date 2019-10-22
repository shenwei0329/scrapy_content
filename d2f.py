#coding=utf-8
#
#
import hashlib
import os
import p2d

ascii={'a':10,'b':11,'c':12,'d':13,'e':14,'f':15}

def findDir(path,fn):
    flist = os.listdir(path)
    if fn in flist:
        return True
    return False

def getIdx(fname):
    global ascii
    md5 = hashlib.md5()
    _c = 0
    _idx = 0
    _hex = md5.update(fname)
    _hex = md5.hexdigest()
    for _cc in _hex:
        if _cc in 'abcdef':
            _c += (ascii[_cc] * (10 ** _idx))
        elif _cc in '0123456789':
            _c += (int(_cc) * (10 ** _idx))
        _idx += 1
    #print(_c % 512)
    return _c % 512

lists = os.listdir('pic/full')
for list in lists:
    _k = getIdx(list)
    _str = "-> %d : " % _k
    if not findDir('../art/pic_%d' % _k,list):
        _str += ">>> add[%d][%s] <<<" % (_k,list)
        p2d.moveIT(list)
    else:
        _cmd = "rm pic/full/%s" % list
        ret = os.system(_cmd)
        if ret!=0:
            _str += '<rm ERR>'
        else:
            _str += '<rm OK>'
    print _str

#
# Eof
#
