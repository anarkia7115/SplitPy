#!/usr/bin/env python
#


import zlib

CHUNK = 1024

#fgz = "../data/sample_n1.gz"
fgz = "./WGC_20m_n1.fq.gz"
fwn = "./output"

def main():
	
	f = open(fgz)
	d = zlib.decompressobj(16 + zlib.MAX_WBITS)

	buf = f.read(CHUNK)
	fw = open("./output", "w")

	while buf:
		dbuf = d.decompress(buf)
		fw.write(dbuf)
		buf = f.read(CHUNK)



if __name__ == "__main__":
	main()
