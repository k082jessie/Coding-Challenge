import re

def parser(str):

    # convert foreign language to Roman characters
    star_to_roma = {}
    metal_price = {}
    content_array = str.split('\n')

    for i in content_array:
        # divide texts into three types for analysis
        # Type I, built the relationship between foreign language and Roman
        if re.search(r'is [A-Z]', i):
            try:
                star_to_roma[i.split(' is ')[0]] = i.split(' is ')[1]
            except:
                print("Please check if there is an error：{0}".format(i))

        # Type II，converted to Roman number and calculated the credit of metal
        elif re.search(r'is \d+', i):
            m = re.match(r'([a-z ]+[a-z]) ([A-Z][a-z]+) is (\d+) Credits', i)
            s = ''

            for k in m.group(1).split(" "):
                s += star_to_roma[k]
                # form a Roman string and hand it over to the function processing Roman string
            try:
                metal_price[m.group(2)] = int(m.group(3)) / transform_roman_num2_alabo(s)
            except:
                print('In the {0}, there is char not belonging to Roman'.format(s))

        # Type III, the question can be analyzed and has answer
        elif re.search(r'how', i):

            # deal with how much question, and find the corresponding information
            if re.search('how much', i):
                star_str = re.match(r'how much is ([a-z ]+[a-z]) ?', i)
                try:
                    star_str_array = star_str.group(1).split(' ')
                    roma_str = ''
                    for i in star_str_array:
                        roma_str += star_to_roma[i]
                    print(star_str.group(1), 'is', transform_roman_num2_alabo(roma_str))
                except:
                    print("I have no idea what you are talking about")

            # deal with how many question, and find the corresponding information
            elif re.search('how many', i):
                star_str = re.match(r'how many Credits is (([a-z ]+[a-z]) ([A-Z][a-z]+)) ?', i)
                try:
                    star_str_array = star_str.group(2).split(' ')
                    roma_str = ''
                    for i in star_str_array:
                        roma_str += star_to_roma[i]
                    print(star_str.group(1), 'is', transform_roman_num2_alabo(roma_str) * metal_price[
                        star_str.group(3)], 'Credits')
                except:
                    print("I have no idea what you are talking about")

        else:
            print("Please check if there is an error：{0}\nStop running the program".format(i))
            break


def transform_roman_num2_alabo(roma_str):
    '''
    Convert Roman numbers into Arabic numerals
    '''
    roma_dict={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    if roma_str=='0':
        return 0
    else:
        res=0
        for i in range(0,len(roma_str)):
            if i==0 or roma_dict[roma_str[i]]<=roma_dict[roma_str[i-1]]:
                res+=roma_dict[roma_str[i]]
            else:
                res+=roma_dict[roma_str[i]]-2*roma_dict[roma_str[i-1]]
        return res


if __name__ == '__main__':
    with open(r'test.txt') as f:
        str = f.read()
        parser(str)
