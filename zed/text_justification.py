from collections import defaultdict
from typing import *

"""
# Hi, -> 3
# how -> 7
# you -> 11
# ..
# ..


width = 12
text = "Hi, how are you doing today?"

# mid_way_result = [["Hi,", "how", "are",], ["you", "doing"], ["today?"]]

def justify(text, width):
    all_words = text.split()
    cum_length=0
    curr_list=[]
    mid_way_result=[]

    for each in all_words:
        cum_length+=len(each)
        if cum_length>12:
            mid_way_result.append(curr_list.copy())
            cum_length=len(each)
            curr_list=[]
            curr_list.append(each)
        else:
            cum_length+=1
            curr_list.append(each)
    mid_way_result.append(curr_list)

    line_length={}
    extra_space_needed={}
    for i,each_line in enumerate(mid_way_result):
        line_length[i]=sum([len(line) for line in each_line])
        extra_space_needed[i]=width-line_length[i]+(len(each_line)-1)

    result=[] #list of string

    for each_list, length, extra_space in zip(mid_way_result, line_length, extra_space_needed):
        ret_string=""
        sp_every,sp_last=divmod(extra_space, length-1)
        for i,each_str in enumerate(each_list):
            ret_string+=each_str
            ret_string+=' '
            if i==len(each_list)-1:
                ret_string+= extra_space_needed//sp_every
            else:
                ret_string+= extra_space_needed//sp_last





    
# 0: "Hi, " 
# 1: "how"
# 2: "are"

        
justify(text, width)
"""


class TextJustification:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        mid_list = []
        curr_length = 0
        curr_list = []
        for word in words:
            curr_length += len(word)
            if curr_length >= maxWidth:
                mid_list.append(curr_list)
                curr_length = len(word)
                curr_length += 1
                curr_list = [word]
            else:
                curr_list.append(word)
                curr_length += 1
        mid_list.append(curr_list)

        line_length, spaces = {}, {}
        for i, each in enumerate(mid_list):
            line_length[i] = sum([len(word) for word in each])
            spaces[i] = maxWidth - (len(each) - 1) - line_length[i]

        result = []
        for i, curr_list in enumerate(mid_list):
            each_str = self.justify_line(maxWidth, curr_list, line_length[i], spaces[i], i == len(mid_list) - 1)
            result.append(each_str)
        return result

    def justify_line(self, max_width, curr_list, line_length, spaces, last):
        if len(curr_list) == 1 or last:
            return ' '.join(curr_list) + ' ' * spaces
        all_spaces = max_width - line_length
        insert_locations = len(curr_list) - 1
        spaces_inserted = [all_spaces // insert_locations] * insert_locations
        for i in range(all_spaces % insert_locations):
            spaces_inserted[i] += 1

        result = ''
        for i in range(len(curr_list) - 1):
            result += curr_list[i]
            result += ' ' * spaces_inserted[i]
        result += curr_list[-1]
        return result


if __name__ == "__main__":
    init = TextJustification()
    print(init.fullJustify(words=["This", "is", "an", "example", "of", "text", "justification."],
                           maxWidth=16))  # ["This    is    an","example  of text","justification.  "]
    print(init.fullJustify(words=["What", "must", "be", "acknowledgment", "shall", "be"],
                           maxWidth=16))  # ["What   must   be","acknowledgment  ","shall be        "]
    print(init.fullJustify(
        words=["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain", "to", "a", "computer.", "Art", "is", "everything",
               "else", "we", "do"],
        maxWidth=20))  # ["Science  is  what we","understand      well","enough to explain to","a  computer.  Art is","everything  else  we","do                  "]
