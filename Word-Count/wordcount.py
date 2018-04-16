def words(rob_list):
   # function called word with argument rob_list
   try:
       rob_count = {}
       for word in [r for r in rob_list.split()]:
           try:
               word = int(word)
               try:
                   if rob_count[word]:
                       rob_count[word] += 1
               except KeyError:
                   rob_count[word] = 1
           except ValueError:
               try:
                   if rob_count[word]:
                       rob_count[word] += 1
               except KeyError:
                   rob_count[word] = 1
       return rob_count
   except:
       return "Invalid Input"
#print(words(1 2 3 1 3))
print(words("my desire right now, my biggest desire, wait for it... 1 1 2 2 3 Is to be and Andelan"))
