# WriteUp

## Q1:Get_post
get输入直接在url后面加a=1

关于post的，第一反应是curl，但是因为这台电脑还没装kali或者Ubuntu，所以说用powershell查了资料直接发包

也可以直接用chrome里面hackbar，打开post模式输入b=2直接发送

见图片t1p2q1.png

## Q2:ezhttp

这道题我觉得有点点意思，很有ctf题目onion一样的特征，有很多个stage

### 1：观察

题目首先提示try post，检查代码没有信息，于是尝试post一个东西

使用hackbar随意post一个值后，提示try imoau=sb

### 2.参数

再次post指定参数后，直接在hackbar处决（execute)提示需要尝试参数xt=大帅b，再次GET，url直接加?xt=大帅b，处决

### 3.source

提示source为The source must be https://www.xidian.edu.cn/，修改referer：https://www.xidian.edu.cn/，处决

### 4.饼干

需要设置cookie，user=admin，发现右侧头没有cookie头，于是新增头，改值为user=admin，处决

### 5.浏览器
依据提示修改user-agent,处决


### 6.localhost

X-host-for赋值为127.0.0.1

得到flag

