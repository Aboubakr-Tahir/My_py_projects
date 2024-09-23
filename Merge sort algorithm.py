string_list=input('pls enter the sequence of numbers that u want to be sort_merged , put space between the numbers : ')
my_list=[int(x) for x in string_list.split()]

def merge_sort_algo (my_list):
    if len(my_list) <= 1:
        return my_list
    
    mid_index=len(my_list)//2
    first_half=my_list[:mid_index]
    last_half=my_list[mid_index:]
    
    left_list= merge_sort_algo(first_half)
    right_list=merge_sort_algo(last_half)  
    
    i=0
    j=0
    result=[]
    
    while i<len(left_list) and j<len(right_list):
        if left_list[i] < right_list[j]:
            result.append(left_list[i])
            i+=1
        else: 
            result.append(right_list[j])  
            j+=1
    while i < len(left_list):
        result.append(left_list[i])
        i+=1
    while j < len(right_list):
        result.append(right_list[j])
        j+=1
    return result
print (merge_sort_algo (my_list))                
             
              
            
    

    








    


