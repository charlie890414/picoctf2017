import md5 
#id
seed = "8505"

hashc = seed

#hash
while md5.new(hashc).hexdigest()!="bd084e77956dedff145de252327b58ac" :
	hashc = md5.new(hashc).hexdigest()
 
print hashc
