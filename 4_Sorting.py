# Keys for sorting

d = dict()
with open('/etc/passwd') as f:
    for line in f:
        if len(line.split(':')) > 3:
            uname, _, uid, _ = line.split(':', 3)
            d[uid] = uname

sorted(d.keys())
d

# Use list for sorting

data = list()

with open('/etc/passwd') as f:
    for line in f:
        if len(line.split(':')) > 3:
            uname, _, uid, _ = line.split(':', 3)
            data.append((int(uid), uname))

for uid, uname in sorted(data):
    print(uid, uname)


# Define key for the sorting


def mykey(pair):
    return pair[1]


data = []
with open('/etc/passwd') as f:
    for line in f:
        if len(line.split(':')) > 3:
            uname, _, uid, _ = line.split(':', 3)
            data.append((uname, int(uid)))

sorted(data, key=mykey)

# Use of nested functions


def my_key(n):
    def mykey(pair):
        return pair[n]
    return mykey


data = []
with open('/etc/passwd') as f:
    for line in f:
        if len(line.split(':')) > 3:
            uname, _, uid, _ = line.split(':', 3)
            data.append((uname, int(uid)))

sorted(data, key=my_key(1))
