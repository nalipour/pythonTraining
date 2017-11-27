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

sorted(data)
data
