#!/usr/bin/env python
#
"""
	1. if no buf, read buf, get first line
	2. if has buf, if has line, get line
	3. if has buf, no line, get buf, paste to first line
"""

import zlib

CHUNK = 1024

#fgz = "../data/sample_n1.gz"
fgz = "./WGC_20m_n1.fq.gz"
fwn = "./output"

class gz:
	def __init__(self, fn):
		self.gz = fn
		self.f = open(self.gz, "rb")
		self.d = zlib.decompressobj(16 + zlib.MAX_WBITS)
		self.buf = ''
		self.readBuf()
	
	def readBuf(self):
		buf = self.f.read(CHUNK)
		if len(buf) > 0:
			self.buf += self.d.decompress(buf)
			return 0
		else:
			# file is empty
			return 1
	
	def readline(self):

		npos = self.buf.find('\n')
		#print npos

		if npos != -1:
			# split self.buf = ret + self.buf

			ret = self.buf[0:npos]
			self.buf = self.buf[npos+1:len(self.buf)]

			return ret

		else:
			# read next buf append to current buf
			isEmpty = self.readBuf()

			if isEmpty:
				return ''
			else:
				ret = self.readline()
				return ret

	def cutline(self):

		npos = self.buf.find('\n')
		print npos

		self.buf = self.buf[npos+1:len(self.buf) - 1]
		

	def close(self):
		self.f.close()

def main():

	fw = open(fwn, "w")

	g1 = gz(fgz)

	line = g1.readline()

	l = len(line)

	while l != 0:

		fw.write(line)
		fw.write('\n')

		line = g1.readline()

		l = len(line)

	g1.close()
	fw.close()

if __name__ == "__main__":
	main()
