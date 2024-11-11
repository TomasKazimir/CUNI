a= int(input())
b= int(input())
c= int(input())
d= int(input())

def spolmenovatel(b,d):
    if b%d==0 or d%b==0:
        if b>d:
            menovatel= b
        else:
            menovatel=d
    else:
        menovatel= b*d
    return menovatel
def scitanycitatel(a,b,c,d):
    x=(spolmenovatel(b,d)/b)*a
    y=(spolmenovatel(b,d)/d)*c
    citatel= x+y
    return citatel
citatel= scitanycitatel(a,c,b,d)
menovatel= spolmenovatel(b,d)
def nsd(citatel,menovatel):
    while citatel!=menovatel:
        if citatel>menovatel:
            citatel=citatel-menovatel
        if menovatel>citatel:
            menovatel=menovatel-citatel
    return citatel

print(scitanycitatel(a,b,c,d)/nsd(citatel,menovatel))
print(spolmenovatel(b,d)/nsd(citatel,menovatel))
