details={"name":"soajn","place":"kottayam","age":23,"job":"onnulla"}
print(details)
details["course"]="python"
print(details)
details["age"]=24
print(details)
del details["age"]
details.pop("job")
print(details)