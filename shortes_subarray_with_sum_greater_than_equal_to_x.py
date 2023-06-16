def dynamic_sliding_window(arr: List[int], x:int)->int:
    #Track min value
    min_length=float('inf')
    
    #The current range and sum of our sliding window
    start=0
    end=0
    current_sum=0
    
    #Extend the sliding window until our criteria is met
    while end<len(arr):
        curr_sum+=arr[end]
        end+=1
        
        #Then contract the sliding window until it no lenoger meets our condition
        while start<end and curr_sum>=x:
            curr_sum-=arr[start]
            start+=1
            
#         update the min_length if this is shorter than current min
            min_length= min(min_length, end-start+1)
    
    return min_length
