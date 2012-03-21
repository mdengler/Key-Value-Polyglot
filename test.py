import memcache

mc = memcache.Client(["127.0.0.1:11211"])

# Check empty behavior
result = mc.get(str(-1))
assert(result is None), "instead of exception got %s" % result

# Check \r\n in data
desired = 'one\r\ntwo'
mc.set('br', desired)
result = mc.get('br')
assert(result == 'one\r\ntwo'), "instead of [%s] got [%s]" % (desired, result)

# set
for i in range(500):
    mc.set(str(i), i)          # This hashmap syntax writes to memcached
# get
for i in range(500):
    val = mc.get(str(i))        # Hashmap syntax reads from memcached
    assert(int(val) == i)
