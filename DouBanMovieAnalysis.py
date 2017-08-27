#-*-coding:utf-8-*-
'''
基于Python2.7编写。不依赖任何第三方库。
例如《中国有嘻哈（2017）》的电影主页为：https://movie.douban.com/subject/27037043/
短评页为：https://movie.douban.com/subject/27037043/comments?status=P
长评页为：https://movie.douban.com/subject/27037043/reviews
'''
import sys
import urllib
import HTMLParser
from sgmllib import SGMLParser
if(len(sys.argv)<2 or len(sys.argv)>2):
    print '输入格式不对！'
    exit(0)
homepage=sys.argv[1]
commentsPage=homepage+'comments?status=P'
reviewsPage=homepage+'reviews'
commentsHtml=urllib.urlopen(commentsPage).read()


# commentsHtml=commentsHtml.decode('unicode_escape')
# eval("u"+"\'"+commentsHtml+"\'")
# commentsHtml=commentsHtml.decode('utf-8')
# commentsHtml=commentsHtml.decode('unicode_escape').encode('utf-8')
# print commentsHtml


class MyCommentsParser(HTMLParser.HTMLParser):

    a_t=False

    #处理开始标签，比如<xx>
    def handle_starttag(self, tag, attrs):
        # print("yujing-TAG:",tag)
        if str(tag).startswith("p"):
            self.a_t=True
        for attr in attrs:
            print("yujing-attrs：",attr)
       # print()

    #处理<xx>data</xx>中间的那些数据
    def handle_data(self, data):
        if self.a_t is True:
            print("yujing-data: ",data)

    #处理结束标签，比如</xx>或者<……/>
    def handle_endtag(self, tag):
        self.a_t=False
        print("yujing-endtag:",tag)
        print()

parser=MyCommentsParser()
parser.feed(commentsHtml)
parser.close()
# print bs(resp.read().decode('utf-8'),'html.parser')

# parser=htmllib.HTMLParser()
# parser.feed(resp.read().decode('utf-8'))

