def count_substring(string, sub_string):
    res = 0
    for i in range(len(string)):
       if string[i:i+len(sub_string)] == sub_string:
         res+=1
    return res