import tornado.web
import tornado.ioloop

#创建处理类
class IndexHangler(tornado.web.RequestHandler):
	def get(self,*args,**kwargs):
		self.write('hello world')

#创建Application对象
app = tornado.web.Application([
	(r'/',IndexHangler)
	])

#绑定监听端口号
app.listen(8888)

#启动监听
tornado.ioloop.IOLoop.instance().start()
