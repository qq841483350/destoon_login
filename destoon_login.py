#coding:utf8
#模拟登陆destoon程序网站后台自动发布文章
import urllib2,urllib,re,cookielib
def test(domain,domain_hz,username,password,catid,title,content):
    #——— 模拟头部信息  ———————
    header={
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; rv:42.0) Gecko/20100101 Firefox/42.0",
    }
    cookie=cookielib.CookieJar()
    opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    urllib2.install_opener(opener)
    #---- 模拟头部信息结束------
    login_data={
        "username":username,
        "password":password,
        "submit":"登陆"
    }
    #-----模拟后台用户登陆信息---------------------------
    login_url="http://%s/%s?file=login&forward=http://%s/%s"%(domain,domain_hz,domain,domain_hz)#登陆url
    # print urllib.unquote(login_url)
    login_data=urllib.urlencode(login_data)
    req1=urllib2.Request(url=login_url,data=login_data,headers=header)
    html=urllib2.urlopen(req1).read()
    if "Powered By DESTOON B2B" in html:
        print u"模拟登陆成功"
    else:
        print html
    #————————模拟登陆结束————————————————————
    post_data={
        "post[catid]":catid,
        "post[title]":title,
        "post[content]":content,
        "post[status]":"3",
        "post[save_remotepic]":"1",
        "post[thumb_no]":"1",
        "post[clear_link]":"1",
        "submit":"确定"
    }
    #———————模拟文章发布数据结束———————————————
    post_url="http://%s/%s?rand=64&moduleid=21&action=add&catid=%s"%(domain,domain_hz,catid) #发布URL
    post_data=urllib.urlencode(post_data)
    req2=urllib2.Request(url=post_url,data=post_data,headers=header)
    if urllib2.urlopen(req2).read():
        print u'文章发布成功,标题是：',title
if __name__=="__main__":
    domain="www.test.com"  #域名
    domain_hz="admin_test.php" #网站后台登陆地址后缀
    username="admin"  #用户名
    password="jy18980916"   #密码
    catid="5"  #分类ID
    title="title"    #文章标题
    content="content"   #文章内容
    test(domain,domain_hz,username,password,catid,title,content)
