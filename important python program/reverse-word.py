sent = input("enter:")
def reverse(string):
    words = string.split()
    words.reverse()
    new_sent = ' '.join(words)
    print(new_sent)

reverse(sent)