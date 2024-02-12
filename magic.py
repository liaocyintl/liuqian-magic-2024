import random
from enum import Enum
random.seed(2024)

TRUMP = "A23456789TJQK"

class YouFrom(Enum):
    NORTH = "北方人"
    SOUTH = "南方人"
    UNKNOWN = "不清楚哪里人"
    
    
class Gender(Enum):
    FEMALE = "女"
    MALE = "男"

def magic(number_of_words_in_your_name: int=3, 
          you_from: YouFrom=YouFrom.NORTH,
          gender: Gender=Gender.FEMALE
        ):
    # 随机抽取4张牌
    cards = random.sample(TRUMP, 4)
    print(cards, "随机抽四张卡牌")
    
    # 把牌撕成两半，然后摞起来
    cards = cards * 2
    print(cards, "撕成两半以后摞起来的卡牌")
    
    # 如果你的名字是N个字，你就从牌堆里抽N张牌，放在最下面
    for i in range(number_of_words_in_your_name):
        cards.append(cards.pop(0))
        print(cards, "因为你的名字是{}个字，抽了第{}张牌放在最下面".format(number_of_words_in_your_name, i+1))
    
    # 拿起最上面的三张牌，随便查到剩下的卡片的中间，任何一个位置都可以
    top_3 = cards[:3]
    rest = cards[3:]
    position = random.randint(1, len(rest) - 1)
    cards = rest[:position] + top_3 + rest[position:]
    print(cards, "把最上面的三张牌插入到剩下的卡片的中间，任何一个位置都可以")
    
    # 把最上面的一张牌藏起来
    hidden = cards.pop(0)
    print(cards, "把最上面的一张牌藏起来, 你藏起来的牌是{}".format(hidden))
    
    # 如果你是南方人，从上面拿起一张；
    # 如果你是北方人，从上面拿起两张；
    # 如果你是不知道哪儿的人，从上面拿起三张。
    # 随便查到剩下的卡片的中间，任何一个位置都可以
    if you_from == YouFrom.NORTH:
        top = cards[:2]
        rest = cards[2:]
    elif you_from == YouFrom.SOUTH:
        top = cards[:1]
        rest = cards[1:]
    elif you_from == YouFrom.UNKNOWN:
        top = cards[:3]
        rest = cards[3:]
    else:
        raise ValueError("you_from must be one of the YouFrom")
    position = random.randint(1, len(rest) - 1)
    cards = rest[:position] + top + rest[position:]
    print(cards, "因为你是{}，所以你抽了{}张牌插在下面的随机位置".format(you_from.value, len(top)))
    
    # 如果你是男生，把最上面的一张牌扔掉；
    # 如果你是女生，把最上面的两张牌扔掉；
    if gender == Gender.MALE:
        cards = cards[1:]
    elif gender == Gender.FEMALE:
        cards = cards[2:]
    else:
        raise ValueError("gender must be one of the Gender")
    print(cards, "因为你是{}生，所以你扔掉了{}张牌".format(gender.value, 1 if gender == Gender.MALE else 2))
        
    # “见证奇迹的时刻” 每念一个字，就把牌堆顶部的一张牌放到最下面
    for char in "见证奇迹的时刻":
        cards.append(cards.pop(0))
        print(cards, "念了一个字'{}'，把牌堆顶部的一张牌放到最下面".format(char))
    
    # 说“好运留下来”，把牌堆顶部的一张牌放到最下面
    # 说“烦恼丢出去”，把牌堆顶不的一张牌扔掉
    # 一直循环到剩下最后一张牌
    while len(cards) > 1:
        cards.append(cards.pop(0))
        print(cards, "说'好运留下来'，把牌堆顶部的一张牌放到最下面")
        cards.pop(0)
        print(cards, "说'烦恼丢出去'，把牌堆顶部的一张牌扔掉")
    
    # 最后一张牌就是你藏起来的那张牌
    assert cards[0] == hidden
    print(cards[0], "=" , hidden, "最后一张牌就是你藏起来的那张牌")
    
if __name__ == "__main__":
    for number_of_words_in_your_name in range(1, 6):
        for you_from in [YouFrom.NORTH, YouFrom.SOUTH, YouFrom.UNKNOWN]:
            for gender in [Gender.FEMALE, Gender.MALE]:
                print("==========")
                print("你的名字是{}个字，你是{}，你是{}生".format(number_of_words_in_your_name, you_from.value, gender.value))
                magic(number_of_words_in_your_name, you_from, gender)

