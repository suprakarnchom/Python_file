# nested_array = [[i * j for j in range(1, 4)] for i in range(1, 6)]
import json
from rich import print

print(type(nested_array))


       

nested_array = [[[[(i * j * k * l) for l in range(1, 3)] for k in range(1, 4)] for j in range(1, 5)] for i in range(1, 6)]

for x in nested_array:
    print(x,type(x),"This is x.")
    for y in x:
        print("  ",y,type(y),"This is y.")
        for z in y:
            print("    ",z,type(z),"This is z.")
            for a in z:
                print("      ",a,type(a),"This is a.")

X = {'array_0': [{'key_1': 'value_0_0_1', 'key_2': 'value_0_0_2', 'key_3': 'value_0_0_3'}, {'key_1': 'value_0_1_1', 'key_2': 'value_0_1_2', 'key_3': 'value_0_1_3'}, {'key_1': 'value_0_2_1', 'key_2': 'value_0_2_2', 'key_3': 'value_0_2_3'}, {'key_1': 'value_0_3_1', 'key_2': 'value_0_3_2', 'key_3': 'value_0_3_3'}], 'array_1': [{'key_1': 'value_1_0_1', 'key_2': 'value_1_0_2', 'key_3': 'value_1_0_3'}, {'key_1': 'value_1_1_1', 'key_2': 'value_1_1_2', 'key_3': 'value_1_1_3'}, {'key_1': 'value_1_2_1', 'key_2': 'value_1_2_2', 'key_3': 'value_1_2_3'}, {'key_1': 'value_1_3_1', 'key_2': 'value_1_3_2', 'key_3': 'value_1_3_3'}], 'array_2': [{'key_1': 'value_2_0_1', 'key_2': 'value_2_0_2', 'key_3': 'value_2_0_3'}, {'key_1': 'value_2_1_1', 'key_2': 'value_2_1_2', 'key_3': 'value_2_1_3'}, {'key_1': 'value_2_2_1', 'key_2': 'value_2_2_2', 'key_3': 'value_2_2_3'}, {'key_1': 'value_2_3_1', 'key_2': 'value_2_3_2', 'key_3': 'value_2_3_3'}]}
print(type(X))
jso

list01 = []
list02 = []

for key, value in X.items():
    print(key, value)
    print(type(value))
    print(type(key))
    for v in value:
        print(v,type(v))
        for k2, v2 in v.items():
            print(k2,v2,type(v2))
            n = len(v2)
            print(n)
            # if v2[n-1] == str(2):
            #     list01.append(v2)
            if v2[6] == v2[8] == v2[10]:
                list02.append(v2)

print(list02)

json_string = json.dumps(X, indent=4)
print(json_string)



nested_dict = {'inner_dict_0': {'inner_dict_0': {'inner_dict_0': {'key1': 'value_0_0_0_1', 'key2': 'value_0_0_0_2', 'key3': 'value_0_0_0_3'}, 'inner_dict_1': {'key1': 'value_0_0_1_1', 'key2': 'value_0_0_1_2', 'key3': 'value_0_0_1_3'}}, 'inner_dict_1': {'inner_dict_0': {'key1': 'value_0_1_0_1', 'key2': 'value_0_1_0_2', 'key3': 'value_0_1_0_3'}, 'inner_dict_1': {'key1': 'value_0_1_1_1', 'key2': 'value_0_1_1_2', 'key3': 'value_0_1_1_3'}}, 'inner_dict_2': {'inner_dict_0': {'key1': 'value_0_2_0_1', 'key2': 'value_0_2_0_2', 'key3': 'value_0_2_0_3'}, 'inner_dict_1': {'key1': 'value_0_2_1_1', 'key2': 'value_0_2_1_2', 'key3': 'value_0_2_1_3'}}, 'inner_dict_3': {'inner_dict_0': {'key1': 'value_0_3_0_1', 'key2': 'value_0_3_0_2', 'key3': 'value_0_3_0_3'}, 'inner_dict_1': {'key1': 'value_0_3_1_1', 'key2': 'value_0_3_1_2', 'key3': 'value_0_3_1_3'}}}, 'inner_dict_1': {'inner_dict_0': {'inner_dict_0': {'key1': 'value_1_0_0_1', 'key2': 'value_1_0_0_2', 'key3': 'value_1_0_0_3'}, 'inner_dict_1': {'key1': 'value_1_0_1_1', 'key2': 'value_1_0_1_2', 'key3': 'value_1_0_1_3'}}, 'inner_dict_1': {'inner_dict_0': {'key1': 'value_1_1_0_1', 'key2': 'value_1_1_0_2', 'key3': 'value_1_1_0_3'}, 'inner_dict_1': {'key1': 'value_1_1_1_1', 'key2': 'value_1_1_1_2', 'key3': 'value_1_1_1_3'}}, 'inner_dict_2': {'inner_dict_0': {'key1': 'value_1_2_0_1', 'key2': 'value_1_2_0_2', 'key3': 'value_1_2_0_3'}, 'inner_dict_1': {'key1': 'value_1_2_1_1', 'key2': 'value_1_2_1_2', 'key3': 'value_1_2_1_3'}}, 'inner_dict_3': {'inner_dict_0': {'key1': 'value_1_3_0_1', 'key2': 'value_1_3_0_2', 'key3': 'value_1_3_0_3'}, 'inner_dict_1': {'key1': 'value_1_3_1_1', 'key2': 'value_1_3_1_2', 'key3': 'value_1_3_1_3'}}}, 'inner_dict_2': {'inner_dict_0': {'inner_dict_0': {'key1': 'value_2_0_0_1', 'key2': 'value_2_0_0_2', 'key3': 'value_2_0_0_3'}, 'inner_dict_1': {'key1': 'value_2_0_1_1', 'key2': 'value_2_0_1_2', 'key3': 'value_2_0_1_3'}}, 'inner_dict_1': {'inner_dict_0': {'key1': 'value_2_1_0_1', 'key2': 'value_2_1_0_2', 'key3': 'value_2_1_0_3'}, 'inner_dict_1': {'key1': 'value_2_1_1_1', 'key2': 'value_2_1_1_2', 'key3': 'value_2_1_1_3'}}, 'inner_dict_2': {'inner_dict_0': {'key1': 'value_2_2_0_1', 'key2': 'value_2_2_0_2', 'key3': 'value_2_2_0_3'}, 'inner_dict_1': {'key1': 'value_2_2_1_1', 'key2': 'value_2_2_1_2', 'key3': 'value_2_2_1_3'}}, 'inner_dict_3': {'inner_dict_0': {'key1': 'value_2_3_0_1', 'key2': 'value_2_3_0_2', 'key3': 'value_2_3_0_3'}, 'inner_dict_1': {'key1': 'value_2_3_1_1', 'key2': 'value_2_3_1_2', 'key3': 'value_2_3_1_3'}}}}
print(type(nested_dict))
print(nested_dict)