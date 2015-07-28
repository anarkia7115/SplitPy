#!/usr/bin/env python
#

import zlib

CHUNK = 1

gz1 = "./ss.gz"
gz2 = "../data/sample_n2.gz"
w = "./output"

f1 = open(gz1, "rb")
fw = open(w, "w")

dobj = zlib.decompressobj(16 + zlib.MAX_WBITS)

buf = f1.read(CHUNK)

while buf:
	os = dobj.decompress(buf)
	fw.write(os)
	fw.write("==")

	buf = f1.read(CHUNK)

fw.write("\n\n\n===============flush=============\n\n\n")
os = dobj.flush()
fw.write(os)

f1.close()
fw.close()
