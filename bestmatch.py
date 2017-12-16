count = [0, 0, 0, 0, 0, 0]
percent = [0.00, 0.00, 0.00, 0.00, 0.00, 0.00]
dataset = ['education_set', 'entertainment_set', 'songs_set', 'sports_set', 'news_set', 'videos_set']
words = set()
max = 0
threshold = 15.0
k = 0

def category(argument):
    switcher = {
        0: "education",
        1: "entertainment",
        2: "songs",
        3: "sports",
        4: "news",
        5: "videos"
    }
    return switcher.get(argument, "invalid index")

with open('top50.txt', 'r') as f:
    for line in f:
        words.add(line.strip('\n'))
for i in dataset:
    with open(i, 'r') as file:
        for l in file:
            for element in words:
                if l.strip('\n') == element:
                    count[k] += 1
    k += 1

for x in range(0, 6):
    percent[x] = round((count[x] / 50)*100.00, 2)

for i in range(0, 6):
    if percent[max] < percent[i]:
        max = i
    print(str(percent[i]) + '%')

#print("max is " + str(percent[max]))
if percent[max] <= 15.0:
    with open('bookmark.txt', 'r') as f:
        x = f.read()
    f.close()
    with open('/mnt/sda9/classified_bookmark/others' + '/' + x + '.desktop', 'w') as f:
        with open('url.txt', 'r') as file:
            y = file.read()
        file.close()
        f.write('[Desktop Entry]' + '\n' + 'Encoding=UTF-8' + '\n' + 'Name=' + x + '\n' + 'Type=Link' + '\n' + 'URL=' + y + '\n' + 'Icon=text-html')
    f.close()
    print("Bookmark was added to others category")
else :
    with open('bookmark.txt', 'r') as f:
        x = f.read()
    f.close()
    with open('/mnt/sda9/classified_bookmark/' + category(max) + '/' + x + '.desktop', 'w') as f:
        with open('url.txt', 'r') as file:
            y = file.read()
        file.close()
        f.write('[Desktop Entry]' + '\n' + 'Encoding=UTF-8' + '\n' + 'Name=' + x + '\n' + 'Type=Link' + '\n' + 'URL=' + y + '\n' + 'Icon=text-html')
    f.close()
    print("Bookmark " + x + " was added to the " + category(max) + " category")

