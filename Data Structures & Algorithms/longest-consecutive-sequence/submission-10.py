class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #if the next element is greater than the previous element 
        #add to counter 
        #store the highest counter to the end of the list 
        #if counter breaks reset counter
        #return highest counter

        #sort the array
        nums.sort()

        #find the unique elements in the array
        unique_elements = []
        for i in nums:
            if i not in unique_elements:
                unique_elements.append(i)

        #start a counter with 1 for lowest element
        highest_counter = 1
        count = 1

        #[9,1,4,7,3,-1,0,5,8,-1,6]
        #[-1,0,1,3,4,5,6,7,8,9]
        if nums == []:
            return 0
        for i in range(len(unique_elements)-1):
            #if the next element is greater than prev element
            #increment counter
            #and increment highest count
            if unique_elements[i + 1] == unique_elements[i]+1:
                count+=1

            #if new current count is greater than old count
            #then change highest count to be older count
            #reset count.
            else:
                if highest_counter < count:
                    highest_counter = count
                
                count=1

        if highest_counter < count:
                highest_counter = count

        return (highest_counter)

        
            
        