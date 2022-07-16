# -*- coding: utf-8 -*-
"""
Created on Sat Jul 16 19:04:48 2022

@author: eliem
"""

class Solution():
        
    def driver(self):
    
        def FizzBuzz_list_creation():
            
            for i in range(1,10**4+1,1):
                if i % 3 == 0 and i % 15 != 0:
                    FizzBuzz_list.append('Fizz')

                if i % 5 == 0 and i % 15 != 0:
                    FizzBuzz_list.append('Buzz')

                if i % 15 == 0:
                    FizzBuzz_list.append('FizzBuzz')
                else:
                    FizzBuzz_list.append(i)
            return FizzBuzz_list

        def FizzBuzz_elements_to_be_removed():
            
            for i in range(1,10**4+1,1):
                if i % 3 == 0 and i % 15 != 0:
                    FizzBuzz_list_values_remove.append(i)

                if i % 5 == 0 and i % 15 != 0:

                    FizzBuzz_list_values_remove.append(i)

            return FizzBuzz_list_values_remove

        def final_solution():
            final_list = [x for x in FizzBuzz_list if x not in FizzBuzz_list_values_remove]
            return final_list
        
        FizzBuzz_list = []
        FizzBuzz_list_values_remove = []
        
        call_fun_1 = FizzBuzz_list_creation()
        call_fun_2 = FizzBuzz_elements_to_be_removed()
        call_fun_3 = final_solution()
        return call_fun_3

    

a = Solution()
a.driver()
b = a.driver()
print(b)