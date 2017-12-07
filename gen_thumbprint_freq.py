import matplotlib.pyplot as plt

def gen_empty_set():
    array_set = []
    for i in range(0, 26):
        array_set.append(0)

    return array_set;

file_obj = open("text1.txt", "r")

print ("Name of file :", file_obj.name)
print ("Closed or not :", file_obj.closed)
print ("Opening mode :", file_obj.mode)


def gen_thumbprint_freq():
    frequency_set = gen_empty_set()
    text = file_obj.read().lower()

    for char in text:
        if(ord(char)>96 and ord(char)<123):
            index = ord(char) - 97
            print(index)

            frequency_set[index] += 1

    print(text)

    # plt.scatter(range(1,27), frequency_set)
    plot = plt.xticks(range(1,27))
    plt.bar(range(1,27), frequency_set)
    plt.show()

    return frequency_set;

print(gen_thumbprint_freq())
