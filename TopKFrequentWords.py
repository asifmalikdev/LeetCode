class Solution(object):
    def topKFrequent(self, words, k):
        dict1 = {}
        for word in words:
            dict1[word] = dict1.get(word, 0) + 1
        
        sorted_words = sorted(dict1.items(), key=lambda x: (-x[1], x[0]))
        print(sorted_words)
        res = [item[0] for item in sorted_words[:k]]
        return res

words = ["the","day","is","sunny","the","the","the","sunny","is","is"]
k = 4
obj = Solution()
print(obj.topKFrequent(words, k))