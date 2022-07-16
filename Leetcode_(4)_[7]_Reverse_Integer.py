# -*- coding: utf-8 -*-
"""
Created on Sat Jul 16 19:27:27 2022

@author: eliem
"""

class Solution:
    
    def __init__(self, number_as_integer):
        self.number_as_integer = number_as_integer
    
    def driver(self):
        def number_as_string():
            return str(self.number_as_integer)
        
        def working_digits_without_ending_zeros():
            
            def last_digit_0():
                for i in range(len(y)-1,0,-1):
                    if y[i] != '0':
                        not_zero = y[i]
                        not_zero_index_list.append(i)
                return not_zero_index_list

            def number_without_ending_zeros():
                for i in range(0,z,1):
                    digits = y[i]
                    digits_without_ending_zeros_list.append(digits)
                return digits_without_ending_zeros_list

            not_zero_index_list = []
            call_inner_fun_1 = last_digit_0()
            
            index_without_ending_zeros = max(not_zero_index_list)
            practical_range_max_without_ending_zeros = index_without_ending_zeros + 1
            z = practical_range_max_without_ending_zeros
            digits_without_ending_zeros_list = []
            call_inner_fun_2 = number_without_ending_zeros()

            return call_inner_fun_2
        
        def reversal():
            for i in range (len(y)-1,-1,-1):
                reversed_list_1.append(y[i])
            return reversed_list_1


        def working_number_digits():
            def working_number_digits_negative():
                reversed_list_1.remove(reversed_list_1[len(reversed_list_1)-1])
                return reversed_list_1

            def working_number_digits_positive():
                return reversed_list_1


            if original_list[len(original_list)-1] == '-':
                call_inner_fun_3 = working_number_digits_negative()
            else:
                call_inner_fun_4 = working_number_digits_positive()


        def number_formation():

            def number_formation_negative():
                number_reversed_str = ''.join(reversed_list_1)
                final_number_reversed_str = ('-' + number_reversed_str)
                final_number = int(final_number_reversed_str)
                return final_number

            def number_formation_positive():
                final_number_reversed_str = ''.join(reversed_list_1)
                final_number = int(final_number_reversed_str)
                return final_number


            if original_list[len(original_list)-1] == '-':
                call_inner_fun_5 = number_formation_negative()
                return call_inner_fun_5
            else:
                call_inner_fun_6 = number_formation_positive()
                return call_inner_fun_6





        call_fun_1 = number_as_string()
        y = call_fun_1
        call_fun_2 = working_digits_without_ending_zeros()
        working_digits_given = call_fun_2
        
        reversed_list_1 = []
        reversal()
        
        original_list = reversed_list_1.copy()
        call_fun_3 = working_number_digits()
        call_fun_5 = number_formation()
        final_digit_reversed = call_fun_5
        
        return final_digit_reversed
    
test_class = Solution(-120036436)
test_class.driver()
b = test_class.driver()
print(b)