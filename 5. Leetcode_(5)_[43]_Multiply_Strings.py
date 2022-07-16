# -*- coding: utf-8 -*-
"""
Created on Sat Jul 16 19:28:58 2022

@author: eliem
"""

class Multiply_Strings:
    
    global number_digits
    number_digits = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9
}
    
    

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        
    def driver(self):
        
        def to_zip_lists(list_1,list_2):
            return list(zip(list_1,list_2))
    
        def num1():

            def digits_in_num1_str(num1_str):
                length = len(num1_str)
                for i in num1_str:
                    digits_of_num1_str.append(i)
                return digits_of_num1_str

            def digits_in_num1_int(num1_list):
                for i in range(len(num1_list)):
                    dig = num1_list[i]
                    dig_int = number_digits[dig]
                    digits_of_num1_list_int.append(dig_int)
                return digits_of_num1_list_int

            def factor_of_10_num1(num_str):               
                digits = len(num_str)
                for i in range(digits-1,-1,-1):
                    num1_of_zeros_num_1_list.append(i)
                return num1_of_zeros_num_1_list
            
            def num1_composition(num_details):

                def num1_by_ten_factor():
                    for i in range(len(num1_details)):
                        ten_factor = num1_details[i][1]
                        v = 10 ** ten_factor
                        ten_factor_list.append(v)
                    return ten_factor_list

                def num1_composition_step_0():
                    for i in range(len(num1_details)):
                        num_resultant = num1_details[i][0] * ten_factor_list[i]
                        num_components_result.append(num_resultant)

                    return num_components_result

                def num1_as_int():
                    value_num_as_int = 0
                    for i in call_inner_fun_2:
                        value_num_as_int += i
                    return value_num_as_int
                

                ten_factor_list = []
                num_components_result = []

                call_inner_fun_1 = num1_by_ten_factor()
                call_inner_fun_2 = num1_composition_step_0()
                call_inner_fun_3 = num1_as_int()

                return call_inner_fun_3
            
            num1_of_zeros_num_1_list = []
            digits_of_num1_list_int = []
            digits_of_num1_str = []
            
            num1_zeros = factor_of_10_num1(self.num1)
            
            num1_str = digits_in_num1_str(self.num1)
            num1_int = digits_in_num1_int(num1_str)
            num1_details = to_zip_lists(num1_int,num1_zeros)
            
            
            
            num1_details = to_zip_lists(num1_int,num1_zeros)
            
            
            num1_as_int = num1_composition(num1_details)

            return num1_as_int

        def num2():

            def digits_in_num2_str(num2_str):
                length = len(num2_str)
                for i in num2_str:
                    digits_of_num2_str.append(i)
                return digits_of_num2_str

            def digits_in_num2_int(num2_list):
                for i in range(len(num2_list)):
                    dig = num2_list[i]
                    dig_int = number_digits[dig]
                    digits_of_num2_list_int.append(dig_int)
                return digits_of_num2_list_int

            def factor_of_10_num2(num_str):
                digits = len(num_str)
                for i in range(digits-1,-1,-1):
                    num_of_zeros_num2_list.append(i)
                return num_of_zeros_num2_list

            def num2_composition(num_details):

                def num2_by_ten_factor():
                    for i in range(len(num2_details)):
                        ten_factor = num2_details[i][1]
                        v = 10 ** ten_factor
                        ten_factor_list.append(v)
                    return ten_factor_list

                def num2_composition_step_0():
                    for i in range(len(num2_details)):
                        num_resultant = num2_details[i][0] * ten_factor_list[i]
                        num_components_result.append(num_resultant)

                    return num_components_result

                def num2_as_int():
                    value_num_as_int = 0
                    for i in call_inner_fun_5:
                        value_num_as_int += i
                    return value_num_as_int
                
            
                call_inner_fun_4 = num2_by_ten_factor()
                call_inner_fun_5 = num2_composition_step_0()
                call_inner_fun_6 = num2_as_int()


                
                num2_zeros = factor_of_10_num2(self.num2)

                return call_inner_fun_6

            num_of_zeros_num2_list = []
            digits_of_num2_str = []
            digits_of_num2_list_int = []
            ten_factor_list = []
            num_components_result = []
            num2_zeros = []
            
            num2_str = digits_in_num2_str(self.num2)
            num2_int = digits_in_num2_int(num2_str)
            num2_zeros = factor_of_10_num2(self.num2)

            num2_details = to_zip_lists(num2_int,num2_zeros)
            num2_as_int = num2_composition(num2_details)
            
            return num2_as_int

        num1_as_int_final = num1()
        num2_as_int_final = num2()
        final_value = num1_as_int_final * num2_as_int_final
        return final_value
    
a = Multiply_Strings('10526','246')
a.driver()
b = a.driver()
print(b)