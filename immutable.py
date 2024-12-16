result = False
another_result = result

print(id(result))          # ID of the singleton object False
print(id(another_result))  # Same ID as result, because both point to False

result = True              # result now points to the singleton object True

well_what_about_me = False
print(id(well_what_about_me))

print(result is another_result)  # False, because they now point to different objects


# True and False are singletons
#A singleton is a design pattern where only
# one instance of an object exists in memory throughout the program's lifetime. In Python:
