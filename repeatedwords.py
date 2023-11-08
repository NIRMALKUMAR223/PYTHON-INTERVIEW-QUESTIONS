def most_frequent_words(words):
    new=[]
    for i in words:
        if i not in new:
            new.append(i)
    return new

words = ["apple", "banana", "apple", "cherry", "banana", "date", "date"]
# words=list(map(str,input().split()))
final=most_frequent_words(words)
print(final)