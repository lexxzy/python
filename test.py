#QUICK TASK:
# -> loop through each data in the collection and perform the following below:
#   - if banana is found, remove it and replace it with tomato
#   - if mango is found, remove it and replace it with corn
#   - if either banana or mango is not found, let the data remain the same
#   - Once looping has completed for above criteria, print the collection using loop.

collection = {"apple", "banana", "orange", "mango", "grape"} 

for item in collection:
    if item == "banana":
        collection.remove("banana")
        collection.add("tomato")
    elif item == "mango":
        collection.remove("mango")
        collection.add("corn")
    else:
        item = item

for item in collection:
    print(item)


    
