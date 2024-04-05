def count_unique_characters(filename):
    my_dict = {}

    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            if line in my_dict:
                my_dict[line] += 1
            else:
                my_dict[line] = 1

    unique_characters = len(my_dict)

    # 印出統計結果
    print("總共有 {} 個不重複的英文字。".format(unique_characters))
    print("每個英文字出現次數如下:")
    for char, count in my_dict.items():
        print("英文字 '{}' 出現了 {} 次。".format(char, count))

# 執行函式
count_unique_characters("hw2_data.txt")
