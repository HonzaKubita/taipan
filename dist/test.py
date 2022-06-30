
ifer = "hello"
items = ["helo", "hello", "HELLO", "Hello"]

if (ifer == "hello") 
{
  for (i in range(1, items.length)){
    print(ifer)
  }
} elif (ifer == "bye") 
{
  print(str([item for (item in items) if (item.islower())]))
}

print("\'te)st")