import pickle
import json


a_list = ["hello", "world", 1, "åäö", 3]
print(type(a_list))

serialized_with_pickle = pickle.dumps(a_list)
print(type(serialized_with_pickle))
print(serialized_with_pickle)


serialized_with_json = json.dumps({"a_list": a_list})
print(type(serialized_with_json))
print(serialized_with_json)

json_to_bytes = serialized_with_json.encode()
print(json_to_bytes)
print(type(json_to_bytes))
