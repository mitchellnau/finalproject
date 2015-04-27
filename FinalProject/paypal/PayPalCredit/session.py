import shelve, Cookie, os

class Session(object):

   def __init__(self, expires=None, cookie_path=None):
      string_cookie = os.environ.get('HTTP_COOKIE','')
      self.cookie = Cookie.SimpleCookie()
      self.cookie.load(string_cookie)

      if self.cookie.get('sess'):
         sid = self.cookie['sess'].value
         # Clear session cookie from other cookies
         #self.cookie.clear()

      else:
         self.cookie.clear()
         sid = "sess123"

      self.cookie['sess'] = sid

      if cookie_path:
         self.cookie['sess']['path'] = cookie_path

      session_dir =  '/tmp/session'
      if not os.path.exists(session_dir):
         try:
            os.mkdir(session_dir, 02770)
         # If the apache user can't create it create it manualy
         except OSError, e:
            errmsg =  """%s when trying to create the session directory. \
Create it as '%s'""" % (e.strerror, os.path.abspath(session_dir))
            raise OSError, errmsg
      self.data = shelve.open(session_dir + '/sess_' + sid, writeback=True)
      os.chmod(session_dir + '/sess_' + sid, 0777)
      
      # Initializes the expires data
      if not self.data.get('cookie'):
        self.data['cookie'] = {'expires':' ','session':{}}

      self.set_expires(expires)
      #self.set_session(session)	

   def close(self):
      self.data.close()

   def set_expires(self, expires=None):
      if expires == '':
         self.data['cookie']['expires'] = ''
      elif isinstance(expires, int):
         self.data['cookie']['expires'] = expires
         
      self.cookie['sess']['expires'] = self.data['cookie']['expires']

   def set_session(self, session={}):
      if session == '':
         self.data['cookie']['session'] = ''
      else:
	self.data['cookie']['session'] = session
        #self.cookie['sess']['session'] = session
