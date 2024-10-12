print("it's not pretty but it works.")
print("recurrings dont work")

def convert_to_frac(n): # sets numerator variable to the numerator and the denominator variable to the denominator. maybe this fraction should be represented as a dictionary e.g. {numerator:denominator}, i probably won't implement this though, even if it is neater.
    global numerator
    global denominator
    numerator=n
    denominator=1
    #while numerator != round(numerator):
        #numerator*=10
        #denominator*=10
    if n == round(n):
        n = int(n)
    for i in range(len(str(n))): # measure to avoid floating point errors
        if str(n)[i] == '.':
            denominator *= 10**( len(str(n)) - 1 - i)
            numerator = int(str(numerator).replace('.', ''))
                

def find_factors(n, key, dictionary):
    if type(dictionary.get(key)) != type([]): # two birds with one stone, true if the key isn't there and true if the key is there but the value is not a list!
        dictionary.update({key: []})
    for i in range(1,int(n/2+1)): # backwards range, half of numerator to 2
        if n % i == 0:
            dictionary.get(key).append(i)
    dictionary.get(key).append(int(n))

def find_common_factors(list1, list2, common_factors_list):
    for factor in list1:
        if factor in list2:
            common_factors_list.append(factor)

def simplify_frac(numeratorkey, denominatorkey, factors_dictionary, common_factors_list): # sets numerator and denominator variable to their simplified versions.
    global numerator
    global denominator
    find_factors(numerator, numeratorkey, factors_dictionary)
    find_factors(denominator, denominatorkey, factors_dictionary)
    
    find_common_factors(factors_dictionary.get(numeratorkey), factors_dictionary.get(denominatorkey), common_factors_list)
    
    numerator = int(numerator/max(common_factors_list))
    denominator = int(denominator/max(common_factors_list))

def convert_and_simplify(n):
    factors={"numerator": [], "denominator": []}
    common_factors=[]

    convert_to_frac(n)
    simplify_frac("numerator", "denominator", factors, common_factors)

    print("Converted and simplified:", int(numerator), "/", int(denominator))
