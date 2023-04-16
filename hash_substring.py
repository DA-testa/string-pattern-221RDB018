
def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    text_input = input()
    if "I" in text_input: 
        return (input().rstrip(), input().rstrip())
    if "F" in text_input:
        filename = "06"
        if "a" in filename:
           return
        else:
            filename = "tests/" + filename
            f = open(filename)
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
    pattern_length = len(pattern)
    text_length = len(text)
    prime = 101
    q = 10000007
    h = pow(prime, pattern_length - 1) % q

    pattern_hash = 0
    current_text_hash = 0
    result = []

    for i in range(pattern_length):
        pattern_hash = (prime * pattern_hash + ord(pattern[i])) % q
        current_text_hash = (prime * current_text_hash + ord(text[i])) % q

    for i in range(text_length - pattern_length + 1):
        if pattern_hash == current_text_hash:
            for j in range(pattern_length):
                if text[i + j] != pattern[j]:
                    break
            else:
                result.append(i)

        if i < text_length - pattern_length:
            current_text_hash = (prime * (current_text_hash - ord(text[i]) * h) + ord(text[i + pattern_length])) % q

    return result

# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
