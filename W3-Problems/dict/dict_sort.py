sample_dict = {'name' : { 'James', 'Donna', 'Bella', 'Isabella', 'Josh', 'Donald'}}
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

# Nested values

sorted_list = []
for first in sample_dict.itervalues():
    for second in first:
        sorted_list.append(second)

print sorted(sorted_list)

# Unnested values

print sorted([i for i in d.itervalues()])

