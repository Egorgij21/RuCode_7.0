def read_file(filename: str):
    with open(filename) as f:
        data = f.readlines()
    
    out = []
    for line in data:
        out.append(line.replace("\n", ""))
    
    return out


if __name__ == "__main__":
    train = read_file("stresses/train_stresses_labels.txt")
    test = read_file("stresses/public_test_stresses.txt")

    print(max(len(x) for x in train))

    # train = sorted(set(''.join(train)))
    # test = ''.join(test)

    # print(ord(train[1]))
    # print(chr(1072 + 33))

    # for i in range(1072, 1072 + 34):
    #     print(chr(i), i)
    
    # print(train)


