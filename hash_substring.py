# python3

def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    
    text_input = input()
    if "I" in text_input: 
#         pattern = input()
#         text = input()
        return (input().rstrip(), input().rstrip())

    if "F" in text_input:
        filename = "06"
        if "a" in filename:
           return
        else:
            filename = "tests/" + filename
            f = open(filename)
#             pattern = f.readline()
#             text = f.readline()
            return (f.readline().rstrip(), f.readline().rstrip())
            f.close()
           
    
    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    
    # return both lines in one return
    
    # this is the sample return, notice the rstrip function
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm 
    p_len = len(pattern)
    t_len = len(text)
    prime = 101
    mod = 10**9 + 7
    p_hash = 0
    t_hash = 0
    power = 1

    for i in range(p_len):
        p_hash = (p_hash + ord(pattern[i]) * power) % mod
        t_hash = (t_hash + ord(text[i]) * power) % mod
        power = (power * prime) % mod

    result = []
    for i in range(t_len - p_len + 1):
        if p_hash == t_hash and text[i:i + p_len] == pattern:
            result.append(i)

        if i < t_len - p_len:
            t_hash = (t_hash - ord(text[i]) * power // prime) % mod
            t_hash = (t_hash * prime + ord(text[i + p_len])) % mod
            t_hash = (t_hash + mod) % mod

    return result


    # and return an iterable variable
#     return [0]


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

# # python3

# def read_input():
#     # this function needs to aquire input both from keyboard and file
#     # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    
    
#     # after input type choice
#     # read two lines 
#     # first line is pattern 
#     # second line is text in which to look for pattern 
    
#     # return both lines in one return
    
#     # this is the sample return, notice the rstrip function
#     return (input().rstrip(), input().rstrip())

# def print_occurrences(output):
#     # this function should control output, it doesn't need any return
#     print(' '.join(map(str, output)))

# def get_occurrences(pattern, text):
#     # this function should find the occurances using Rabin Karp alghoritm 

#     # and return an iterable variable
#     return [0]


# # this part launches the functions
# if __name__ == '__main__':
#     print_occurrences(get_occurrences(*read_input()))

