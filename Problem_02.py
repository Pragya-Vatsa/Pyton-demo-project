from collections import Counter
  
# initializing list
test_list = ["Red color is best for you ",
             "All love memes", 
             "Game is best for fitness",
             "It is raining outside"]
               
# printing original list
print("The original list is : " + str(test_list))
  
# concatenating using join 
joined = " ".join(ele for ele in test_list)
  
# mapping using Counter()
mappd = Counter(joined.split())
  
# getting total using sum 
total_val = sum(mappd.values())
  
# getting share of each word
res = {key: val / total_val for key,
       val in mappd.items()}
  
# printing result
print("Percentage share of each word : " + str(res))
