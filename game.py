import json
import random
import time


with open('./idiom.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    f.close()

datasets = []
for line in data:
    datasets.append(line['word'])

len_dts = len(datasets)
first_char = [i[0] for i in datasets]
first_char = list(set(first_char))

start = random.randint(1, 30000)
idiom = datasets[start]
coun = 0


def check_idiom_pc(cy):    # 检查电脑提供的成语是否可接
    token = cy[0]
    while True:
        if cy[-1] not in first_char:
            cy = datasets[datasets.index(cy) + 1]
            if token != cy[0]:
                print('无成语可接，游戏结束')
                return
        if cy[-1] in first_char:
            return cy


idiom = check_idiom_pc(idiom)
suc = 0


while True:
    if coun == 0:
        print("成语接龙开始！ 我先来%s" % idiom)
        start_time = time.time()
        user_input = input()

    if user_input == '不玩了':
        print('你个憨批，爬爬爬')
        break
    if user_input[0] == idiom[-1] and (user_input in datasets):
        suc += 1
        end_time = time.time()
        use_time = int(end_time - start_time)
        print("接龙成功 !!!! <%s>, 耗时: %s秒， 目前答对了%s个" % (user_input, use_time, suc))

        if user_input[-1] not in first_char:
            print('无成语可接，游戏结束！')
        for i in datasets:
            if i[0] == user_input[-1]:
                idiom = i
                break
        idiom = check_idiom_pc(idiom)
        print('下一个成语: %s' % idiom)
        start_time = time.time()
        user_input = input()
    else:
        print('你是不是铁龙鸣？没有 ‘%s’ 这个成语！再想想。' % user_input)
        print('接龙成语: %s' % idiom)
        user_input = input()
    coun += 1



