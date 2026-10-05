class Solution:

    def encode(self, strs: List[str]) -> str:
        word = 0
        encode = ""
        for index, value in enumerate(strs):
            for sub_index, sub_value in enumerate(value):
                word += ord(sub_value) + 6848
                word = str(word) + "%"
                encode += word
                word = 0
            encode+= "^"
            word = 0 
        return encode 


    def decode(self, s: str) -> List[str]:
        decode = []
        letter = ""
        word = ""
        for character in s:
            if character == "^":
                decode.append(word)
                word = ""
            elif character == "%":
                letter = int(letter) - 6848
                word += chr(letter)
                letter = ""
            else:
                letter += character

        return decode




