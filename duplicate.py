important = set()

with open('videos.txt', 'r') as f:
    for line in f:
        if len(line.strip('\n')) != 1:
            important.add(line.strip('\n'))

with open('videos_set', 'a') as f:
    for i in important:
        f.write(i + '\n')

f.close()
