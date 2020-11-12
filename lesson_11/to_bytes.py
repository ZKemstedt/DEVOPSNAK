import pickle
import json


a_list = ["hello", "world", 1, "åäö", 3]
print(1, type(a_list))

serialized_with_pickle = pickle.dumps(a_list)
print(2, type(serialized_with_pickle))
print(3, serialized_with_pickle)
print("3a", len(serialized_with_pickle))


serialized_with_json = json.dumps({"a_list": a_list})
print(4, type(serialized_with_json))
print(5, serialized_with_json)

json_to_bytes = serialized_with_json.encode()
print(6, json_to_bytes)
print(7, type(json_to_bytes))
print(8, len(json_to_bytes))
