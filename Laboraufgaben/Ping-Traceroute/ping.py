from icmplib import multiping
import matplotlib.pyplot as plt

hosts = [
    "www.htwg-konstanz.de",
    "www.stanford.edu",
    "www.sydney.edu.au",
    "www.ntt.co.jp",
    "www.cern.ch"
]

num_pings = 100
pings = multiping(hosts, privileged=False, count=num_pings)

results = []
for ping in pings:
    results.append(ping.rtts)

#print(results)

fig, ax = plt.subplots()
ax.set_ylabel("Ping rtts (ms)")
ax.yaxis.grid(True)

ax.boxplot(results)
ax.set_title("Pings")
ax.set_xticks([y + 1 for y in range(len(hosts))], labels=hosts)

plt.show()
