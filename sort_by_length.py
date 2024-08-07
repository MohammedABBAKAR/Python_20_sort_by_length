# Sort a List by String Length

# Create a function that takes a list of strings and return a list, 
# sorted from shortest to longest.
# Examples

# sort_by_length(["Google", "Apple", "Microsoft"])
# ➞ ["Apple", "Google", "Microsoft"]

# sort_by_length(["Leonardo", "Michelangelo", "Raphael", "Donatello"])
# ➞ ["Raphael", "Leonardo", "Donatello", "Michelangelo"]

# sort_by_length(["Turing", "Einstein", "Jung"])
# ➞ ["Jung", "Turing", "Einstein"]



# def length(lst):
#     for item in lst:
#      return len(item)
   
# print(length(["Michelangelo", "Raphael", "Donatello"]))
#/////////////////////////////////////////////////////

def length(lst):
    lengths = []
    for item in lst:
        lengths.append(len(item))
    return lengths

print(length(["Michelangelo", "Raphael", "Donatello"]))

#/////////////////////////////////////////////////////

# def length(lst):
#     return [len(item) for item in lst]

# print(length(["Michelangelo", "Raphael", "Donatello"]))



def sort_by_length(lst):
    return sorted(lst, key=len)

# Test cases
print(sort_by_length(["Google", "Apple", "Microsoft"]))
# ➞ ["Apple", "Google", "Microsoft"]

print(sort_by_length(["Leonardo", "Michelangelo", "Raphael", "Donatello"]))
# ➞ ["Raphael", "Leonardo", "Donatello", "Michelangelo"]

print(sort_by_length(["Turing", "Einstein", "Jung"]))
# ➞ ["Jung", "Turing", "Einstein"]




def sort_by_length(lst):
    # Implementing bubble sort
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if len(lst[j]) > len(lst[j+1]):
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst

# Test cases
print(sort_by_length(["Google", "Apple", "Microsoft"]))
# ➞ ["Apple", "Google", "Microsoft"]

print(sort_by_length(["Leonardo", "Michelangelo", "Raphael", "Donatello"]))
# ➞ ["Raphael", "Leonardo", "Donatello", "Michelangelo"]

print(sort_by_length(["Turing", "Einstein", "Jung"]))
# ➞ ["Jung", "Turing", "Einstein"]
