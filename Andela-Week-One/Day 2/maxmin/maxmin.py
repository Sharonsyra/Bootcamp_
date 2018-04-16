def find_max_min(rob):
  #function to create method find_max_min with an argument rob
    rob_list=[]
    if min(rob)!=max(rob):
        rob_list.append(min(rob))
        rob_list.append(max(rob))
        return rob_list
    else:
        rob_list.append(len(rob))
        return rob_list
      
