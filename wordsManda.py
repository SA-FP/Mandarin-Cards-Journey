"""
wordsManda.py
-----------------------------------------
The Mandarin vocabulary itself: 21 themes, 250 words.

Each word is a list of three things: [characters, pinyin, english]

This file is pure DATA. It never reads or writes anything, which makes it
the easiest file in the project to edit safely — add your own words here.
"""

THEMES = [
 {
  "zh": "数字",
  "py": "Shùzì",
  "en": "Numbers",
  "seal": "数",
  "words": [
   [
    "一",
    "yī",
    "one"
   ],
   [
    "二",
    "èr",
    "two"
   ],
   [
    "三",
    "sān",
    "three"
   ],
   [
    "四",
    "sì",
    "four"
   ],
   [
    "五",
    "wǔ",
    "five"
   ],
   [
    "六",
    "liù",
    "six"
   ],
   [
    "七",
    "qī",
    "seven"
   ],
   [
    "八",
    "bā",
    "eight"
   ],
   [
    "九",
    "jiǔ",
    "nine"
   ],
   [
    "十",
    "shí",
    "ten"
   ],
   [
    "百",
    "bǎi",
    "hundred"
   ],
   [
    "零",
    "líng",
    "zero"
   ]
  ]
 },
 {
  "zh": "时间",
  "py": "Shíjiān",
  "en": "Time",
  "seal": "时",
  "words": [
   [
    "今天",
    "jīntiān",
    "today"
   ],
   [
    "明天",
    "míngtiān",
    "tomorrow"
   ],
   [
    "昨天",
    "zuótiān",
    "yesterday"
   ],
   [
    "现在",
    "xiànzài",
    "now"
   ],
   [
    "点",
    "diǎn",
    "o'clock"
   ],
   [
    "分钟",
    "fēnzhōng",
    "minute"
   ],
   [
    "小时",
    "xiǎoshí",
    "hour"
   ],
   [
    "早上",
    "zǎoshang",
    "morning"
   ],
   [
    "中午",
    "zhōngwǔ",
    "noon"
   ],
   [
    "晚上",
    "wǎnshang",
    "evening"
   ],
   [
    "几点",
    "jǐ diǎn",
    "what time"
   ],
   [
    "时候",
    "shíhou",
    "time / moment"
   ]
  ]
 },
 {
  "zh": "日期与季节",
  "py": "Rìqī yǔ Jìjié",
  "en": "Days & Seasons",
  "seal": "日",
  "words": [
   [
    "星期一",
    "xīngqīyī",
    "Monday"
   ],
   [
    "星期六",
    "xīngqīliù",
    "Saturday"
   ],
   [
    "星期天",
    "xīngqītiān",
    "Sunday"
   ],
   [
    "月",
    "yuè",
    "month"
   ],
   [
    "年",
    "nián",
    "year"
   ],
   [
    "号",
    "hào",
    "day (date)"
   ],
   [
    "春天",
    "chūntiān",
    "spring"
   ],
   [
    "夏天",
    "xiàtiān",
    "summer"
   ],
   [
    "秋天",
    "qiūtiān",
    "autumn"
   ],
   [
    "冬天",
    "dōngtiān",
    "winter"
   ],
   [
    "周末",
    "zhōumò",
    "weekend"
   ],
   [
    "生日",
    "shēngrì",
    "birthday"
   ]
  ]
 },
 {
  "zh": "家人",
  "py": "Jiārén",
  "en": "Family",
  "seal": "家",
  "words": [
   [
    "爸爸",
    "bàba",
    "dad"
   ],
   [
    "妈妈",
    "māma",
    "mom"
   ],
   [
    "哥哥",
    "gēge",
    "older brother"
   ],
   [
    "姐姐",
    "jiějie",
    "older sister"
   ],
   [
    "弟弟",
    "dìdi",
    "younger brother"
   ],
   [
    "妹妹",
    "mèimei",
    "younger sister"
   ],
   [
    "爷爷",
    "yéye",
    "grandpa"
   ],
   [
    "奶奶",
    "nǎinai",
    "grandma"
   ],
   [
    "儿子",
    "érzi",
    "son"
   ],
   [
    "女儿",
    "nǚ'ér",
    "daughter"
   ],
   [
    "父母",
    "fùmǔ",
    "parents"
   ],
   [
    "家",
    "jiā",
    "home / family"
   ]
  ]
 },
 {
  "zh": "人称",
  "py": "Rénchēng",
  "en": "People & Pronouns",
  "seal": "人",
  "words": [
   [
    "我",
    "wǒ",
    "I / me"
   ],
   [
    "你",
    "nǐ",
    "you"
   ],
   [
    "他",
    "tā",
    "he / him"
   ],
   [
    "她",
    "tā",
    "she / her"
   ],
   [
    "我们",
    "wǒmen",
    "we / us"
   ],
   [
    "他们",
    "tāmen",
    "they / them"
   ],
   [
    "人",
    "rén",
    "person"
   ],
   [
    "男人",
    "nánrén",
    "man"
   ],
   [
    "女人",
    "nǚrén",
    "woman"
   ],
   [
    "孩子",
    "háizi",
    "child"
   ],
   [
    "朋友",
    "péngyou",
    "friend"
   ],
   [
    "名字",
    "míngzi",
    "name"
   ]
  ]
 },
 {
  "zh": "问候",
  "py": "Wènhòu",
  "en": "Greetings & Courtesy",
  "seal": "礼",
  "words": [
   [
    "你好",
    "nǐ hǎo",
    "hello"
   ],
   [
    "您好",
    "nín hǎo",
    "hello (polite)"
   ],
   [
    "早上好",
    "zǎoshang hǎo",
    "good morning"
   ],
   [
    "谢谢",
    "xièxie",
    "thank you"
   ],
   [
    "不客气",
    "bú kèqi",
    "you're welcome"
   ],
   [
    "对不起",
    "duìbuqǐ",
    "sorry"
   ],
   [
    "没关系",
    "méi guānxi",
    "it's okay"
   ],
   [
    "再见",
    "zàijiàn",
    "goodbye"
   ],
   [
    "请",
    "qǐng",
    "please"
   ],
   [
    "请问",
    "qǐng wèn",
    "excuse me"
   ],
   [
    "欢迎",
    "huānyíng",
    "welcome"
   ],
   [
    "没问题",
    "méi wèntí",
    "no problem"
   ]
  ]
 },
 {
  "zh": "学校",
  "py": "Xuéxiào",
  "en": "Classroom & School",
  "seal": "学",
  "words": [
   [
    "学校",
    "xuéxiào",
    "school"
   ],
   [
    "老师",
    "lǎoshī",
    "teacher"
   ],
   [
    "学生",
    "xuésheng",
    "student"
   ],
   [
    "同学",
    "tóngxué",
    "classmate"
   ],
   [
    "教室",
    "jiàoshì",
    "classroom"
   ],
   [
    "上课",
    "shàng kè",
    "to attend class"
   ],
   [
    "下课",
    "xià kè",
    "class is over"
   ],
   [
    "作业",
    "zuòyè",
    "homework"
   ],
   [
    "考试",
    "kǎoshì",
    "exam"
   ],
   [
    "问题",
    "wèntí",
    "question / problem"
   ],
   [
    "学习",
    "xuéxí",
    "to study"
   ],
   [
    "上学",
    "shàng xué",
    "to go to school"
   ]
  ]
 },
 {
  "zh": "学科与文具",
  "py": "Xuékē yǔ Wénjù",
  "en": "Subjects & Stationery",
  "seal": "书",
  "words": [
   [
    "语文",
    "yǔwén",
    "Chinese (class)"
   ],
   [
    "数学",
    "shùxué",
    "mathematics"
   ],
   [
    "英语",
    "yīngyǔ",
    "English"
   ],
   [
    "书",
    "shū",
    "book"
   ],
   [
    "课本",
    "kèběn",
    "textbook"
   ],
   [
    "笔",
    "bǐ",
    "pen"
   ],
   [
    "铅笔",
    "qiānbǐ",
    "pencil"
   ],
   [
    "本子",
    "běnzi",
    "notebook"
   ],
   [
    "纸",
    "zhǐ",
    "paper"
   ],
   [
    "黑板",
    "hēibǎn",
    "blackboard"
   ],
   [
    "书包",
    "shūbāo",
    "schoolbag"
   ],
   [
    "字",
    "zì",
    "character / word"
   ]
  ]
 },
 {
  "zh": "身体",
  "py": "Shēntǐ",
  "en": "The Body",
  "seal": "体",
  "words": [
   [
    "头",
    "tóu",
    "head"
   ],
   [
    "眼睛",
    "yǎnjing",
    "eye"
   ],
   [
    "耳朵",
    "ěrduo",
    "ear"
   ],
   [
    "鼻子",
    "bízi",
    "nose"
   ],
   [
    "嘴",
    "zuǐ",
    "mouth"
   ],
   [
    "手",
    "shǒu",
    "hand"
   ],
   [
    "脚",
    "jiǎo",
    "foot"
   ],
   [
    "头发",
    "tóufa",
    "hair"
   ],
   [
    "脸",
    "liǎn",
    "face"
   ],
   [
    "牙",
    "yá",
    "tooth"
   ],
   [
    "肚子",
    "dùzi",
    "belly / stomach"
   ],
   [
    "身体",
    "shēntǐ",
    "body"
   ]
  ]
 },
 {
  "zh": "食物",
  "py": "Shíwù",
  "en": "Food",
  "seal": "食",
  "words": [
   [
    "米饭",
    "mǐfàn",
    "cooked rice"
   ],
   [
    "面条",
    "miàntiáo",
    "noodles"
   ],
   [
    "面包",
    "miànbāo",
    "bread"
   ],
   [
    "鸡蛋",
    "jīdàn",
    "egg"
   ],
   [
    "肉",
    "ròu",
    "meat"
   ],
   [
    "鱼",
    "yú",
    "fish (food)"
   ],
   [
    "菜",
    "cài",
    "dish / vegetable"
   ],
   [
    "饺子",
    "jiǎozi",
    "dumplings"
   ],
   [
    "早饭",
    "zǎofàn",
    "breakfast"
   ],
   [
    "午饭",
    "wǔfàn",
    "lunch"
   ],
   [
    "晚饭",
    "wǎnfàn",
    "dinner"
   ],
   [
    "饭",
    "fàn",
    "meal"
   ]
  ]
 },
 {
  "zh": "饮食",
  "py": "Yǐnshí",
  "en": "Drinks & Eating",
  "seal": "喝",
  "words": [
   [
    "水",
    "shuǐ",
    "water"
   ],
   [
    "茶",
    "chá",
    "tea"
   ],
   [
    "牛奶",
    "niúnǎi",
    "milk"
   ],
   [
    "咖啡",
    "kāfēi",
    "coffee"
   ],
   [
    "果汁",
    "guǒzhī",
    "juice"
   ],
   [
    "吃",
    "chī",
    "to eat"
   ],
   [
    "喝",
    "hē",
    "to drink"
   ],
   [
    "饿",
    "è",
    "hungry"
   ],
   [
    "渴",
    "kě",
    "thirsty"
   ],
   [
    "好吃",
    "hǎochī",
    "delicious (food)"
   ],
   [
    "好喝",
    "hǎohē",
    "tasty (drink)"
   ],
   [
    "杯子",
    "bēizi",
    "cup / glass"
   ]
  ]
 },
 {
  "zh": "水果蔬菜",
  "py": "Shuǐguǒ Shūcài",
  "en": "Fruits & Vegetables",
  "seal": "果",
  "words": [
   [
    "苹果",
    "píngguǒ",
    "apple"
   ],
   [
    "香蕉",
    "xiāngjiāo",
    "banana"
   ],
   [
    "橙子",
    "chéngzi",
    "orange"
   ],
   [
    "葡萄",
    "pútáo",
    "grapes"
   ],
   [
    "西瓜",
    "xīguā",
    "watermelon"
   ],
   [
    "草莓",
    "cǎoméi",
    "strawberry"
   ],
   [
    "水果",
    "shuǐguǒ",
    "fruit"
   ],
   [
    "蔬菜",
    "shūcài",
    "vegetables"
   ],
   [
    "土豆",
    "tǔdòu",
    "potato"
   ],
   [
    "西红柿",
    "xīhóngshì",
    "tomato"
   ],
   [
    "胡萝卜",
    "húluóbo",
    "carrot"
   ],
   [
    "白菜",
    "báicài",
    "cabbage"
   ]
  ]
 },
 {
  "zh": "颜色",
  "py": "Yánsè",
  "en": "Colors",
  "seal": "色",
  "words": [
   [
    "红色",
    "hóngsè",
    "red"
   ],
   [
    "橙色",
    "chéngsè",
    "orange"
   ],
   [
    "黄色",
    "huángsè",
    "yellow"
   ],
   [
    "绿色",
    "lǜsè",
    "green"
   ],
   [
    "蓝色",
    "lánsè",
    "blue"
   ],
   [
    "紫色",
    "zǐsè",
    "purple"
   ],
   [
    "黑色",
    "hēisè",
    "black"
   ],
   [
    "白色",
    "báisè",
    "white"
   ],
   [
    "粉色",
    "fěnsè",
    "pink"
   ],
   [
    "灰色",
    "huīsè",
    "gray"
   ],
   [
    "棕色",
    "zōngsè",
    "brown"
   ],
   [
    "颜色",
    "yánsè",
    "color"
   ]
  ]
 },
 {
  "zh": "动物",
  "py": "Dòngwù",
  "en": "Animals",
  "seal": "物",
  "words": [
   [
    "狗",
    "gǒu",
    "dog"
   ],
   [
    "猫",
    "māo",
    "cat"
   ],
   [
    "鸟",
    "niǎo",
    "bird"
   ],
   [
    "鱼",
    "yú",
    "fish"
   ],
   [
    "马",
    "mǎ",
    "horse"
   ],
   [
    "牛",
    "niú",
    "cow"
   ],
   [
    "猪",
    "zhū",
    "pig"
   ],
   [
    "鸡",
    "jī",
    "chicken"
   ],
   [
    "兔子",
    "tùzi",
    "rabbit"
   ],
   [
    "老虎",
    "lǎohǔ",
    "tiger"
   ],
   [
    "熊猫",
    "xióngmāo",
    "panda"
   ],
   [
    "动物",
    "dòngwù",
    "animal"
   ]
  ]
 },
 {
  "zh": "家居",
  "py": "Jiājū",
  "en": "Home & Furniture",
  "seal": "居",
  "words": [
   [
    "房间",
    "fángjiān",
    "room"
   ],
   [
    "门",
    "mén",
    "door"
   ],
   [
    "窗户",
    "chuānghu",
    "window"
   ],
   [
    "桌子",
    "zhuōzi",
    "table"
   ],
   [
    "椅子",
    "yǐzi",
    "chair"
   ],
   [
    "床",
    "chuáng",
    "bed"
   ],
   [
    "厨房",
    "chúfáng",
    "kitchen"
   ],
   [
    "厕所",
    "cèsuǒ",
    "bathroom / toilet"
   ],
   [
    "电视",
    "diànshì",
    "TV"
   ],
   [
    "电脑",
    "diànnǎo",
    "computer"
   ],
   [
    "手机",
    "shǒujī",
    "cellphone"
   ],
   [
    "灯",
    "dēng",
    "lamp / light"
   ]
  ]
 },
 {
  "zh": "衣服",
  "py": "Yīfu",
  "en": "Clothing",
  "seal": "衣",
  "words": [
   [
    "衣服",
    "yīfu",
    "clothes"
   ],
   [
    "衬衫",
    "chènshān",
    "shirt"
   ],
   [
    "裤子",
    "kùzi",
    "pants"
   ],
   [
    "鞋",
    "xié",
    "shoes"
   ],
   [
    "帽子",
    "màozi",
    "hat"
   ],
   [
    "袜子",
    "wàzi",
    "socks"
   ],
   [
    "裙子",
    "qúnzi",
    "skirt"
   ],
   [
    "外套",
    "wàitào",
    "coat"
   ],
   [
    "手表",
    "shǒubiǎo",
    "watch"
   ],
   [
    "眼镜",
    "yǎnjìng",
    "glasses"
   ],
   [
    "穿",
    "chuān",
    "to wear (clothes)"
   ],
   [
    "戴",
    "dài",
    "to wear (accessories)"
   ]
  ]
 },
 {
  "zh": "天气与自然",
  "py": "Tiānqì yǔ Zìrán",
  "en": "Weather & Nature",
  "seal": "天",
  "words": [
   [
    "天气",
    "tiānqì",
    "weather"
   ],
   [
    "太阳",
    "tàiyáng",
    "sun"
   ],
   [
    "月亮",
    "yuèliang",
    "moon"
   ],
   [
    "雨",
    "yǔ",
    "rain"
   ],
   [
    "风",
    "fēng",
    "wind"
   ],
   [
    "雪",
    "xuě",
    "snow"
   ],
   [
    "云",
    "yún",
    "cloud"
   ],
   [
    "天空",
    "tiānkōng",
    "sky"
   ],
   [
    "山",
    "shān",
    "mountain"
   ],
   [
    "河",
    "hé",
    "river"
   ],
   [
    "热",
    "rè",
    "hot"
   ],
   [
    "冷",
    "lěng",
    "cold"
   ]
  ]
 },
 {
  "zh": "城市地点",
  "py": "Chéngshì Dìdiǎn",
  "en": "Places in Town",
  "seal": "市",
  "words": [
   [
    "医院",
    "yīyuàn",
    "hospital"
   ],
   [
    "商店",
    "shāngdiàn",
    "shop"
   ],
   [
    "饭店",
    "fàndiàn",
    "restaurant"
   ],
   [
    "银行",
    "yínháng",
    "bank"
   ],
   [
    "公园",
    "gōngyuán",
    "park"
   ],
   [
    "图书馆",
    "túshūguǎn",
    "library"
   ],
   [
    "超市",
    "chāoshì",
    "supermarket"
   ],
   [
    "车站",
    "chēzhàn",
    "station"
   ],
   [
    "机场",
    "jīchǎng",
    "airport"
   ],
   [
    "路",
    "lù",
    "road"
   ],
   [
    "城市",
    "chéngshì",
    "city"
   ],
   [
    "中国",
    "Zhōngguó",
    "China"
   ]
  ]
 },
 {
  "zh": "交通",
  "py": "Jiāotōng",
  "en": "Transport & Travel",
  "seal": "车",
  "words": [
   [
    "车",
    "chē",
    "vehicle / car"
   ],
   [
    "公交车",
    "gōngjiāochē",
    "bus"
   ],
   [
    "火车",
    "huǒchē",
    "train"
   ],
   [
    "飞机",
    "fēijī",
    "airplane"
   ],
   [
    "自行车",
    "zìxíngchē",
    "bicycle"
   ],
   [
    "地铁",
    "dìtiě",
    "subway"
   ],
   [
    "出租车",
    "chūzūchē",
    "taxi"
   ],
   [
    "船",
    "chuán",
    "boat"
   ],
   [
    "坐",
    "zuò",
    "to ride / sit"
   ],
   [
    "开车",
    "kāichē",
    "to drive"
   ],
   [
    "走",
    "zǒu",
    "to walk / go"
   ],
   [
    "旅游",
    "lǚyóu",
    "to travel"
   ]
  ]
 },
 {
  "zh": "动词",
  "py": "Dòngcí",
  "en": "Common Verbs",
  "seal": "动",
  "words": [
   [
    "是",
    "shì",
    "to be"
   ],
   [
    "有",
    "yǒu",
    "to have"
   ],
   [
    "去",
    "qù",
    "to go"
   ],
   [
    "来",
    "lái",
    "to come"
   ],
   [
    "看",
    "kàn",
    "to look / read"
   ],
   [
    "听",
    "tīng",
    "to listen"
   ],
   [
    "说",
    "shuō",
    "to speak"
   ],
   [
    "写",
    "xiě",
    "to write"
   ],
   [
    "买",
    "mǎi",
    "to buy"
   ],
   [
    "想",
    "xiǎng",
    "to want / think"
   ],
   [
    "喜欢",
    "xǐhuan",
    "to like"
   ],
   [
    "做",
    "zuò",
    "to do / make"
   ]
  ]
 },
 {
  "zh": "描述与提问",
  "py": "Miáoshù yǔ Tíwèn",
  "en": "Describing & Asking",
  "seal": "问",
  "words": [
   [
    "大",
    "dà",
    "big"
   ],
   [
    "小",
    "xiǎo",
    "small"
   ],
   [
    "好",
    "hǎo",
    "good"
   ],
   [
    "多",
    "duō",
    "many"
   ],
   [
    "少",
    "shǎo",
    "few"
   ],
   [
    "新",
    "xīn",
    "new"
   ],
   [
    "什么",
    "shénme",
    "what"
   ],
   [
    "谁",
    "shéi",
    "who"
   ],
   [
    "哪儿",
    "nǎr",
    "where"
   ],
   [
    "怎么",
    "zěnme",
    "how"
   ]
  ]
 }
]


def all_words():
    """Return every word from every theme as one flat list."""
    out = []
    for t in THEMES:
        for w in t["words"]:
            out.append({"hanzi": w[0], "pinyin": w[1], "english": w[2], "theme": t["en"]})
    return out


def words_for_theme(theme_en):
    """Return the words of a single theme (by its English name)."""
    for t in THEMES:
        if t["en"] == theme_en:
            return [{"hanzi": w[0], "pinyin": w[1], "english": w[2], "theme": t["en"]} for w in t["words"]]
    return []


def theme_names():
    """Return a list of theme names for menus, e.g. 'Numbers (12)'."""
    return [t["en"] for t in THEMES]


# ---------------------------------------------------------------------------
# CHAPTERS
# ---------------------------------------------------------------------------
# The 21 themes above are grouped into 7 chapters, 3 themes each (~36 words).
# Study a chapter, then take its test. Add or rearrange chapters freely —
# just make sure every theme name matches one in THEMES exactly.
# ---------------------------------------------------------------------------

CHAPTERS = [
    {"n": 1, "title": "Animals & Food",   "icon": "\U0001F43C",
     "themes": ["Animals", "Food", "Fruits & Vegetables"]},
    {"n": 2, "title": "Family & People",  "icon": "\U0001F46A",
     "themes": ["Family", "People & Pronouns", "Greetings & Courtesy"]},
    {"n": 3, "title": "Numbers & Time",   "icon": "\U0001F551",
     "themes": ["Numbers", "Time", "Days & Seasons"]},
    {"n": 4, "title": "School Life",      "icon": "\U0001F393",
     "themes": ["Classroom & School", "Subjects & Stationery", "Common Verbs"]},
    {"n": 5, "title": "Body & Clothing",  "icon": "\U0001F455",
     "themes": ["The Body", "Clothing", "Colors"]},
    {"n": 6, "title": "Home & Eating",    "icon": "\U0001F3E0",
     "themes": ["Home & Furniture", "Drinks & Eating", "Describing & Asking"]},
    {"n": 7, "title": "Out In The World", "icon": "\U0001F30D",
     "themes": ["Weather & Nature", "Places in Town", "Transport & Travel"]},
]

# How many questions each chapter test asks, and the mark needed to pass.
TEST_LENGTH = 10
PASS_MARK = 80          # percent


def chapter_words(n):
    """Every word belonging to chapter number n."""
    ch = get_chapter(n)
    if not ch:
        return []
    out = []
    for theme in ch["themes"]:
        out.extend(words_for_theme(theme))
    return out


def get_chapter(n):
    """Look up one chapter by its number."""
    for ch in CHAPTERS:
        if ch["n"] == n:
            return ch
    return None


def chapter_label(n):
    """A tidy label like 'Chapter 1 - Animals & Food'."""
    ch = get_chapter(n)
    return f"Chapter {ch['n']} - {ch['title']}" if ch else f"Chapter {n}"
