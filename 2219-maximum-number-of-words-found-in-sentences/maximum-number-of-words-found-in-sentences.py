class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        counts=[]
        for sentence in sentences:
            words=sentence.split()
            counts.append(len(words)) 
        return max(counts)    
            