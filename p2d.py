#coding=utf-8
#
#
import hashlib
import os

kv = {}

ascii={'a':10,'b':11,'c':12,'d':13,'e':14,'f':15}

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

def buildKV(fname):
    global kv
    _k = getIdx(fname)
    if _k not in kv.keys():
        kv[_k] = [fname]
    else:
        kv[_k].append(fname)

def moveIT(fn):

    _k = getIdx(fn)
    _dirn = 'pic_%d' % _k
    _cmd = 'mv pic/full/%s ../art/%s/' % (fn,_dirn)
    print _cmd
    ret =os.system(_cmd)
    if ret==0:
        print 'OK'
    else:
        print 'Error'

#
# Eof
#
