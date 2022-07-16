# -*- coding: utf-8 -*-
"""
Created on Sat Jul 16 18:46:12 2022

@author: eliem
"""

class Solution:
    
    global roman_numerals_dict
    roman_numerals_dict = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000 
}
    

    

    

    def __init__(self,roman_numeral_input):
        self.roman_numeral_input = roman_numeral_input
        
    def driver(self):

        def exceptions_identifier():
            for i in range(0,len(self.roman_numeral_input),1):
                for j in range(1,len(self.roman_numeral_input),1):
                    if roman_numerals_dict[self.roman_numeral_input[i]] < roman_numerals_dict[self.roman_numeral_input[j]]:
                         exceptions_list.append(self.roman_numeral_input[i:j+1])
            return exceptions_list

        def exceptions_arithmetic_rnb():
            for i in range (len(exceptions_list_proper)):
                v_1, v_2 = exceptions_list_proper[i][0:2]
                v_of_exception_rnb = roman_numerals_dict[v_2] - roman_numerals_dict[v_1]
                exceptions_rnb_values.append(v_of_exception_rnb)
            return exceptions_rnb_values

        def rn_to_char(rn_str):
            return [char for char in rn_str]

        def indices_first_of_exceptions():
            for i in range(len(exceptions_list_proper)):
                for j in range(len(input_as_char)):
                    if input_as_char[j] == exceptions_list_proper[i][0] and input_as_char[j + 1] == exceptions_list_proper[i][1]:
                        indices_exception_first.append(j)
            return indices_exception_first

        def indices_second_of_exceptions():
            for i in indices_exception_first:
                z = i + 1
                indices_exception_second.append(z)
            return indices_exception_second

        def indices_of_exceptions_final():
            third_list = indices_exception_first + indices_exception_second
            indices_exception_final_list = sorted(third_list)
            return indices_exception_final_list

        def remainder_list_after_deduction():
            for index, element in enumerate(input_as_char_dup):
                if index not in final_list_for_exceptions:
                    remainder_list.append(element)
            return remainder_list

        def rn_to_int_total_sum():
            def remainder():
                for i in range (len(remainder_list)):
                    value_of_remainder = roman_numerals_dict[remainder_list[i]]
                    value_total_of_remainder.append(value_of_remainder)
                    total_value_of_remainder = sum(value_total_of_remainder)
                return total_value_of_remainder
            def exceptions():
                total_value_of_exceptions = sum(exceptions_rnb_values)
                return total_value_of_exceptions
            total_value_from_remainder = remainder()
            total_value_from_exceptions = exceptions()
            total_sum = total_value_from_remainder + total_value_from_exceptions
            return total_sum
        


        exceptions_list = []
        exceptions_rnb_values = []
        remainder_list = []
        value_total_of_remainder = []
        indices_exception_first = []
        indices_exception_second = []
        final_list_for_exceptions = []
        
        roman_numeral_input_dup = self.roman_numeral_input
        input_as_char = rn_to_char(roman_numeral_input_dup)
        input_as_char_dup = input_as_char
        
        
        call_fun_1 = exceptions_identifier()
        exceptions_list_proper = list(filter(None, exceptions_list))
        call_fun_2 = exceptions_arithmetic_rnb()
        
        input_as_char = rn_to_char(roman_numeral_input_dup)
        
        
        
        call_fun_3 = indices_first_of_exceptions()
        call_fun_4 = indices_second_of_exceptions()
        call_fun_5 = indices_of_exceptions_final()
        final_list_for_exceptions = call_fun_5
        
        call_fun_6 = remainder_list_after_deduction()
        call_fun_7 = rn_to_int_total_sum()
        final_value = call_fun_7
        return final_value

complete = Solution('DCCLXXXIII')
complete.driver()
b = complete.driver()
print(b)