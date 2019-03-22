#把一个字典扁平化
#源字典：{'a':{'b':1,'c':2},'d':{'e':3,'f':{'g':4}}}
#目标字典：{'a.b': 1, 'a.c': 2, 'd.e': 3, 'd.f.g': 4}

#1st
source = {'a':{'b':1,'c':2},'d':{'e':3,'f':{'g':4}}}
target = {}
def flatmap(src,prefix=''):
    for k,v in src.items():
        if isinstance(v,(list,tuple,set,dict)):
            flatmap(v,prefix+k+'.') #递归调用
        else:
            target[prefix+k] = v
flatmap(source)
print(target)

#2nd 内部创建dest字典
source = {'a':{'b':1,'c':2},'d':{'e':3,'f':{'g':4}}}

def flatmap(src,dest=None,prefix=''):
    if dest == None:
        dest = {}
    for k,v in src.items():
        if isinstance(v,(list,tuple,set,dict)):
            flatmap(v,dest,prefix=prefix+k+'.') #递归调用
        else:
            dest[prefix+k] = v
    return dest
print(flatmap(source))

#3rd
source = {'a':{'b':1,'c':2},'d':{'e':3,'f':{'g':4}}}
# 4th

def flatmap(src):
    def _flatmap(src,dest=None,prefix=''):
        for k,v in src.items():
            key = prefix + k
            if isinstance(v,(list,tuple,set,dict)):
                _flatmap(v,dest,key+'.') #递归调用
            else:
                dest[key] = v
    dest = {}
    _flatmap(src,dest)
    return dest
print(flatmap(source))
