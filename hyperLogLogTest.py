import redis

client = redis.StrictRedis()
# client.pfadd()
# client.pfadd()
client.pfadd("codehole", "user1")
print(client.pfcount("codehole"))

for i in range(1000):
    client.pfadd("codehole", "user%d" % i)
    total = client.pfcount("codehole")
    if total != i + 1:
        print(total, i + 1)
        break
