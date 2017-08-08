import re
import binascii
import wx
import cStringIO
f=open('columns.jpg','rb')
t=f.read().encode('hex')
f.close()
alist=re.findall(r'(.{2})',t)
alist.reverse()
str=''.join(alist)
#f=open('biu.txt','w')
f.write(str)
f.close()
img = binascii.a2b_hex(str)
image = wx.ImageFromStream(cStringIO.StringIO(img), wx.BITMAP_TYPE_JPEG)
image.SaveFile('temp.jpg', wx.BITMAP_TYPE_JPEG)