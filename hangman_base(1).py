
# Hangman Game
# -----------------------------------
# begin 補助関数
# この定義には授業で扱っていない関数も含まれます
# 指示に従って関数を使ってください
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns 答えになる単語のリストを返す. 全て小文字.
    """
    print("ファイルから単語を読み込み中...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "単語読み込み完了．")
    return wordlist

# -----------------------------------

# 単語の読み込みを実行しておく
wordlist = load_words()

# -----------------------------------

def choose_word():
    """
    wordlist (list): 単語のリスト (strings)
    Returns リストからランダムに選択した単語
    """
    return random.choice(wordlist)

# -----------------------------------

