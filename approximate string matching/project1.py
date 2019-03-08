"""
COMP90049 Knowledge Technologies Project1
author: Yiming Zhang

"""
import editdistance
import nltk
import jellyfish

# files are at python workspace

f0 = open("./dict.txt")
my_dict = f0.readlines()
f0.close()

f1 = open('./wiki_misspell.txt')
wiki_misspell = f1.readlines()
f1.close()

f2 = open('./wiki_correct.txt')
correct_words = open('./wiki_correct.txt').readlines()
f2.close()

f3 = open('./birkbeck_misspell.txt')
f4 = open('./birkbeck_correct.txt')

# method1: global edit distance
def global_edit_distance():
    """first method - GED"""
    fw1 = open('global_edit_distance_result.txt', 'w')
    for line in wiki_misspell:
        string = line.strip()
        dis = 100000000
        bests = ""
        for entry in my_dict:
            tem_dis = editdistance.eval(string, entry.strip())
            if tem_dis < dis:
                dis = tem_dis
                bests = " "
                bests = entry.strip()
            elif tem_dis == dis:
                bests += ' ' + entry.strip()
        print(dis,string, bests)
        fw1.write(bests + "\n")
    fw1.close()


# method2: local edit distance
def local_edit_distance():
    fw2 = open('local_edit_distance_result.txt', 'w')

    for line in wiki_misspell:
        string = line.strip()
        dis = -1000000
        bests = ""

        for entry in my_dict:

            len_entry = len(entry)+1
            len_string = len(string)+1
            distance_m = [[0 for i in range(len_string)] for i in range(len_entry)]
            for i in range(0, len_entry):
                distance_m[i][0] = 0
            for i in range(0, len_string):
                distance_m[0][i] = 0

            max_dis = 0
            for i in range(1, len_entry):
                for j in range(1, len_string):
                    if entry[i-1] == string[j-1]:
                        distance_m[i][j] = max(
                            distance_m[i - 1][j - 1] + 1,
                            distance_m[i - 1][j] - 1,
                            distance_m[i][j - 1] - 1,
                            0
                        )
                    else:
                        distance_m[i][j] = max(
                            distance_m[i - 1][j - 1] - 1,
                            distance_m[i - 1][j] - 1,
                            distance_m[i][j - 1] - 1,
                            0
                        )

                    if distance_m[i][j] > max_dis:
                        max_dis = distance_m[i][j]
            if max_dis > dis:
                dis = max_dis
                bests = " "
                bests = entry.strip()
            elif max_dis == dis:
                bests += ' ' + entry.strip()
        print(dis,string, bests)
        fw2.write(bests + "\n")
    fw2.close()

# method3: 2-gram method
def two_gram_distance():
    fw3 = open('two_gram_distance_result.txt', 'w')

    for line in wiki_misspell:
        string = line.strip()
        dis = 1000000
        bests = ""
        string_2gram = list(nltk.bigrams(string))
        len_string = len(string_2gram)

        for entry in my_dict:
            entry_2gram = list(nltk.bigrams(entry))
            len_entry = len(entry_2gram)

            visit = [0 for i in range(len_entry)]
            intersection = 0
            for i in range(len_string):
                for j in range(len_entry):
                    if string_2gram[i] == entry_2gram[j] and visit[j] != 1:
                        intersection += 1
                        visit[j] = 1

            tem_dis = len_entry + len_string - 2 * intersection

            if tem_dis < dis:
                dis = tem_dis
                bests = " "
                bests = entry.strip()
            elif tem_dis == dis:
                bests += ' ' + entry.strip()

        print(dis, string, bests)
        fw3.write(bests + "\n")
    fw3.close()

# method4: 3-gram method
def three_gram_distance():
    fw4 = open('three_gram_distance_result.txt', 'w')

    for line in wiki_misspell:
        string = line.strip()
        dis = 1000000
        bests = ""
        string_3gram = list(nltk.trigrams(string))
        len_string = len(string_3gram)

        for entry in my_dict:
            entry_3gram = list(nltk.trigrams(entry))
            len_entry = len(entry_3gram)

            visit = [0 for i in range(len_entry)]
            intersection = 0
            for i in range(len_string):
                for j in range(len_entry):
                    if string_3gram[i] == entry_3gram[j] and visit[j] != 1:
                        intersection += 1
                        visit[j] = 1

            tem_dis = len_entry + len_string - 2 * intersection

            if tem_dis < dis:
                dis = tem_dis
                bests = " "
                bests = entry.strip()
            elif tem_dis == dis:
                bests += ' ' + entry.strip()

        print(dis, string, bests)
        fw4.write(bests + "\n")
    fw4.close()


# method5: soundex method
def soundex():
    fw5 = open('soundex_result.txt', 'w')
    for line in wiki_misspell:
        string = line.strip()
        dis = 100000
        bests = ""
        string_s = jellyfish.soundex(string)
        for entry in my_dict:
            entry.strip()
            entry_s = jellyfish.soundex(entry)

            # tem_dis = distance(entry_s, string_s)

            len_entry = len(entry_s) + 1
            len_string = len(string_s) + 1
            distance_m = [[0 for i in range(len_string)] for i in range(len_entry)]
            for i in range(0, len_entry):
                distance_m[i][0] = 0
            for i in range(0, len_string):
                distance_m[0][i] = 0

            for i in range(1, len_entry):
                for j in range(1, len_string):
                    if entry_s[i - 1] == string_s[j - 1]:
                        distance_m[i][j] = min(
                            distance_m[i - 1][j - 1] - 1,
                            distance_m[i - 1][j] + 1,
                            distance_m[i][j - 1] + 1,
                        )
                    else:
                        distance_m[i][j] = min(
                            distance_m[i - 1][j - 1] + 1,
                            distance_m[i - 1][j] + 1,
                            distance_m[i][j - 1] + 1,
                        )

            tem_dis = distance_m[len_entry-1][len_string-1]

            if tem_dis < dis:
                dis = tem_dis
                bests = " "
                bests = entry.strip()
            elif tem_dis == dis:
                bests += ' ' + entry.strip()

        print(dis, string, bests)
        fw5.write(bests + '\n')
    fw5.close()

#method6: Metaphone method
def metaphone():
    fw6 = open('metaphone_result.txt', 'w')
    for line in wiki_misspell:
        string = line.strip()
        dis = 100000
        bests = ""
        string_s = jellyfish.metaphone(string)
        for entry in my_dict:
            entry.strip()
            entry_s = jellyfish.metaphone(entry)

            len_entry = len(entry_s) + 1
            len_string = len(string_s) + 1
            distance_m = [[0 for i in range(len_string)] for i in range(len_entry)]
            for i in range(0, len_entry):
                distance_m[i][0] = 0
            for i in range(0, len_string):
                distance_m[0][i] = 0

            for i in range(1, len_entry):
                for j in range(1, len_string):
                    if entry_s[i - 1] == string_s[j - 1]:
                        distance_m[i][j] = min(
                            distance_m[i - 1][j - 1] - 1,
                            distance_m[i - 1][j] + 1,
                            distance_m[i][j - 1] + 1,
                        )
                    else:
                        distance_m[i][j] = min(
                            distance_m[i - 1][j - 1] + 1,
                            distance_m[i - 1][j] + 1,
                            distance_m[i][j - 1] + 1,
                        )

            tem_dis = distance_m[len_entry-1][len_string-1]

            if tem_dis < dis:
                dis = tem_dis
                bests = " "
                bests = entry.strip()
            elif tem_dis == dis:
                bests += ' ' + entry.strip()

        print(dis, string, bests)
        fw6.write(bests + '\n')
    fw6.close()

"calculate precision, recall"
def evaluation(predicted_words):

    num_correct_pre = 0
    num_total_pre = 0
    precision = 0

    num_correct_rec = 0
    num_total_rec = 0
    recall = 0

    for item in predicted_words:
        num_total_pre += len(item.split())

    "correct_words here is wiki-correct.txt"
    for predicted_word, correct_word in zip(predicted_words, correct_words):
        if correct_word.strip() in predicted_word.strip():
            num_correct_pre += 1

    for correct_word in correct_words:
        num_total_rec += 1

    for predicted_word, correct_word in zip(predicted_words, correct_words):
        if correct_word.strip() in predicted_word.strip():
            num_correct_rec += 1

    precision = (num_correct_pre / num_total_pre) * 100
    recall = (num_correct_rec / num_total_rec) * 100

    print("Precision:", str(float("{0:.2f}".format(precision))) + "%",
          "Recall:", str(float("{0:.2f}".format(recall))) + "%")

    print("precision correct number: ", str(num_correct_pre),
          "precision total number: ", str(num_total_pre),
          "recall correct number: ", str(num_correct_rec),
          "recall total number: ", str(num_total_rec))

"results"

# method1: global edit distance
global_edit_distance()
predicted_word_ged = open('global_edit_distance_result.txt').readlines()
print("Method1: Global Edit Distance")
evaluation(predicted_word_ged)
print("\n")


# method2: local edit distance
local_edit_distance()
predicted_word_led = open('local_edit_distance_result.txt').readlines()
print("Method2: Local Edit Distance")
evaluation(predicted_word_led)
print("\n")


# method3: two gram distance
two_gram_distance()
predicted_word_2gd = open('two_gram_distance_result.txt').readlines()
print("Method3: Two Gram Distance")
evaluation(predicted_word_2gd)
print("\n")

# method4: three gram distance
three_gram_distance()
predicted_word_3gd = open('three_gram_distance_result.txt').readlines()
print("Method4: Three Gram Distance")
evaluation(predicted_word_3gd)
print("\n")

# method5: soundex
soundex()
predicted_soundex = open('soundex_result.txt').readlines()
print("Method5: Soundex")
evaluation(predicted_soundex)
print("\n")

# method6: metaphone
metaphone()
predicted_metaphone = open('metaphone_result.txt').readlines()
print("Method6: Metaphone")
evaluation(predicted_metaphone)
print("\n")

