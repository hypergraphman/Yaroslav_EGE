f = open('26.txt')
n = int(f.readline())
start = 1633305600
end = start + 60 * 60 * 24 * 7
unlim_proc = 0
processes = []
for i in range(n):
    s, e = map(int, f.readline().split())
    if s < start:
        s = start
    if e > end or e == 0:
        e = end
    if s == start and e == end:
        unlim_proc += 1
    elif s <= end and e >= start:
        processes.append(s)
        processes.append(-e)
processes.sort(key=abs)
lim_proc = 0
mx_proc = 0
for proc in processes:
    if proc > 0:
        lim_proc += 1
    else:
        lim_proc -= 1
    if lim_proc > mx_proc:
        mx_proc = lim_proc
print(unlim_proc + mx_proc)