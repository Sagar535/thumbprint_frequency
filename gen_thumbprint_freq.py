
def gen_empty_set():
    array_set = []
    for i in range(0,26):
        array_set.append(0)

    print(array_set)
    print(len(array_set))

gen_empty_set()

file_obj = open("text1.txt", "r")

print "Name of file :" , file_obj.name 
print "Closed or not :" ,file_obj.closed
print "Opening mode :" , file_obj.mode
print "Softspace flag :" , file_obj.softspace

def gen_thumbprint_freq():
    text = file_obj.read()
    

gen_thumbprint_freq()
