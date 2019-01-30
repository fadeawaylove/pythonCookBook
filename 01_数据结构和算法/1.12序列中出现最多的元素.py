from collections import Counter
words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the', 'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into', 'my', 'eyes', "you're", 'under'
]
word_counts = Counter(words)
# 出现频率最高的 3 个单词
top_three = word_counts.most_common(3) 
print(top_three)
# Outputs [('eyes', 8), ('the', 5), ('look', 4)]
