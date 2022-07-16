# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 06:38:49 2022

@author: eliem
"""

class Roman:
    
    global int_input_str
    
    
    def __init__(self,int_input):
        self.int_input = int_input
        
    def driver(self):
        def to_zip_lists(list_1,list_2):
            return list(zip(list_1,list_2))
        
        def digit_heads_str():
            int_input_str = str(self.int_input)
            for i in range(len(int_input_str)):
                digit_head = int_input_str[i]
                digit_head_list_str.append(digit_head)
            return digit_head_list_str
        
        def digit_heads_int():
            int_input_str = str(self.int_input)
            for i in range(len(int_input_str)):
                digit_head = int(int_input_str[i])
                digit_head_list_int.append(digit_head)
            return digit_head_list_int

        def number_of_zeros():
            for i in range(len(digit_head_list_str)-1,-1,-1):
                num_of_zeros_list.append(i)
            return num_of_zeros_list

        def value_of_num_breakdown():
            value_of_digit_head_to_num_of_zeros = to_zip_lists(digit_head_list_str,num_of_zeros_list)
            for i in range (len(value_of_digit_head_to_num_of_zeros)):

                v = 10 ** value_of_digit_head_to_num_of_zeros[i][1]
                values_breakdown.append(v)
            return values_breakdown

        def components_of_num():
            value_of_digit_head_to_factor_of_10_str = to_zip_lists(digit_head_list_str,values_breakdown)
            for i in range(len(value_of_digit_head_to_factor_of_10_str)):
                respective_values = int(value_of_digit_head_to_factor_of_10_str[i][0]) * value_of_digit_head_to_factor_of_10_str[i][1]
                components_list.append(respective_values)
            return components_list
        
        def filtration_lists():
            for i in range(0,9,1):
                if i not in range(4,8):
                    rn_head.append(i+1)
                else:
                    rn_middle.append(i+1)
                    
        def rn_head_or_middle():
            value_of_digit_head_to_factor_of_10_int = to_zip_lists(digit_head_list_int,values_breakdown)
            for i in range(len(value_of_digit_head_to_factor_of_10_int)):
                if value_of_digit_head_to_factor_of_10_int[i][0] in rn_head:
                    trial_list.append('head')
                else:
                    trial_list.append('middle')
            return trial_list

        
        def rn_digit_first_digit_of_rn_block():
    
            def rn_digit_first_digit_head():

                for j in range(len(rn_symbols_head_by_zeros)):
                    if rn_head_or_middle_list[i][0] == 'head' and rn_head_or_middle_list[i][1] == rn_symbols_head_by_zeros[j][1]:
                        rn_block_head.append(rn_symbols_head_by_zeros[j])
                return rn_block_head

            def rn_digit_first_digit_middle():
                

                for j in range(len(rn_symbols_middle_by_zeros)):
                    if rn_head_or_middle_list[i][0] == 'middle'and rn_head_or_middle_list[i][1] == rn_symbols_middle_by_zeros[j][1]:
                        rn_block_middle.append(rn_symbols_middle_by_zeros[j])
                return rn_block_middle
            rn_head_or_middle_list = to_zip_lists(trial_list,num_of_zeros_list)
            for i in range(len(rn_head_or_middle_list)):
                if rn_head_or_middle_list[i][0] == 'head':
                    call_inner_fun_1 = rn_digit_first_digit_head()

                else:
                    call_inner_fun_2 = rn_digit_first_digit_middle()
   
        def reorder_list():
            rn_head_or_middle_list = to_zip_lists(trial_list,num_of_zeros_list)
            list_with_symbol_head = rn_block_head + rn_block_middle 
            for j in range(len(rn_head_or_middle_list)):
                for i in range(len(list_with_symbol_head)):
                    if list_with_symbol_head[i][1] == rn_head_or_middle_list[j][1]:
                        list_with_symbol_head_pair.append(list_with_symbol_head[i])
                        list_with_symbol_head_final.append(list_with_symbol_head[i][0])


        def director():

            def for_val_1_3():
                for i in range(len(value_of_digit_head_to_factor_of_10_int)):
                    if value_of_digit_head_to_factor_of_10_int[i][0] <= 3:
                        rn_block_1_to_3 = list_with_symbol_head_final[i] * value_of_digit_head_to_factor_of_10_int[i][0]
                        rn_blocks_list.append(rn_block_1_to_3)
                return rn_blocks_list

            def for_val_4():
                for i in range(len(value_of_digit_head_to_factor_of_10_int)):
                    for k in range(len(rn_symbols_by_zeros)):
                        if value_of_digit_head_to_factor_of_10_int[i][0] == 4 and list_with_symbol_head_pair[i][1] == rn_symbols_by_zeros[k][1]:
                            rn_block_4 = rn_symbols_by_zeros[k][0] + rn_symbols_by_zeros[k+1][0]
                            rn_blocks_list.append(rn_block_4)
                            break
                return rn_blocks_list

            def for_val_5():
                for i in range(len(value_of_digit_head_to_factor_of_10_int)):
                    if value_of_digit_head_to_factor_of_10_int[i][0] == 5:
                        rn_block_5 = list_with_symbol_head_final[i]
                        rn_blocks_list.append(rn_block_5)
                return rn_blocks_list

            def for_val_6_8():
                for i in range(len(value_of_digit_head_to_factor_of_10_int)):
                    for k in range(len(rn_symbols_by_zeros)):
                        if 6 <= value_of_digit_head_to_factor_of_10_int[i][0] <= 8:
                            if list_with_symbol_head_pair[i][1] == rn_symbols_by_zeros[k][1]:

                                rn_block_multiple = (value_of_digit_head_to_factor_of_10_int[i][0] - 5)     
                                rn_block_6_8 = rn_symbols_by_zeros[k+1][0] + rn_block_multiple * rn_symbols_by_zeros[k][0]

                                rn_blocks_list.append(rn_block_6_8)
                                break


                return rn_blocks_list 


            def for_val_9():
                def first_symbol():
                    value_of_digit_head_to_factor_of_10_int = to_zip_lists(digit_head_list_int,values_breakdown)
                    for i in range(len(value_of_digit_head_to_factor_of_10_int)):
                        for k in range(len(rn_symbols_by_zeros)):
                            
                            if value_of_digit_head_to_factor_of_10_int[i][0] == 9:
                                if list_with_symbol_head_pair[i][1] == rn_symbols_by_zeros[k][1]:

                                    rn_block_9_symbol_1 = rn_symbols_by_zeros[k][0]
                                    rn_blocks_list_5_first_symbol.append(rn_block_9_symbol_1)

                                    break

                    return rn_blocks_list_5_first_symbol


                def second_symbol():
                    for i in range(len(rn_blocks_list_5_first_symbol)):
                        for k in range(len(rn_symbols_by_zeros)):
                            if rn_blocks_list_5_first_symbol[i] == rn_symbols_by_zeros[k][0]:
                                rn_block_9_symbol_2 = rn_symbols_by_zeros[k+2][0]
                                rn_blocks_list_5_second_symbol.append(rn_block_9_symbol_2)
                    return rn_blocks_list_5_second_symbol




                call_inner_fun_3 = first_symbol()
                call_inner_fun_4 = second_symbol()

                concat_func = lambda x,y: x + "" + str(y)
                rn_block_9 = list(map(concat_func,rn_blocks_list_5_first_symbol,rn_blocks_list_5_second_symbol))
                for i in rn_block_9:
                    rn_blocks_list.append(i)
                return rn_blocks_list



            value_of_digit_head_to_factor_of_10_int = to_zip_lists(digit_head_list_int,values_breakdown)
            
            for i in range(len(value_of_digit_head_to_factor_of_10_int)):
                if value_of_digit_head_to_factor_of_10_int[i][0] <= 3:
                    call_inner_fun_1 = for_val_1_3()
                elif value_of_digit_head_to_factor_of_10_int[i][0] == 4:
                    call_inner_fun_2 = for_val_4()
                elif value_of_digit_head_to_factor_of_10_int[i][0] == 5:
                    call_inner_fun_3 = for_val_5()
                elif value_of_digit_head_to_factor_of_10_int[i][0] >= 6 and value_of_digit_head_to_factor_of_10_int[i][0] <= 8:
                    call_inner_fun_4 = for_val_6_8()
                else:
                    call_inner_fun_5 = for_val_9()
                
        
        def reorder_final_list():
            for i in range(len(list_with_symbol_head_pair)):
                    for j in range(len(rn_blocks_list)):
                        if list_with_symbol_head_pair[i][0] == rn_blocks_list[j][0]:
                            final_list.append(rn_blocks_list[j])
            return final_list
        
        rn_symbols = ['I','V','X','L','C','D','M']
        rn_values = [1,5,10,50,100,500,1000]

        rn_symbols_head = ['I','X','C','M']
        rn_symbols_head_by_zeros = [0,1,2,3]
        rn_symbols_to_digit_head_list = ['head','head','head','head'] 

        rn_symbols_middle = ['V', 'L', 'D',]
        rn_symbols_middle_by_zeros = [0,1,2]
        rn_symbols_to_digit_middle_list = ['middle','middle','middle']

        rn_symbols = ['I','V','X','L','C','D','M']
        rn_head_and_middle_list = ['head','middle','head','middle','head','middle','head']
        rn_symbols_head_and_middle_by_zeros_list = [0,0,1,1,2,2,3]
        
        
        rn_sym_to_value = to_zip_lists(rn_symbols,rn_values)

        rn_symbols_head_by_zeros = to_zip_lists(rn_symbols_head,rn_symbols_head_by_zeros)
        rn_symbols_middle_by_zeros = to_zip_lists(rn_symbols_middle,rn_symbols_middle_by_zeros)

        rn_symbols_to_digit_head = to_zip_lists(rn_symbols_head,rn_symbols_to_digit_head_list)
        rn_symbols_to_digit_middle_list = to_zip_lists(rn_symbols_middle,rn_symbols_to_digit_middle_list)

        rn_head_and_middle = to_zip_lists(rn_symbols,rn_head_and_middle_list)
        rn_symbols_head_and_middle_by_zeros = to_zip_lists(rn_head_and_middle_list,rn_symbols_head_and_middle_by_zeros_list)

        rn_symbols_by_zeros = to_zip_lists(rn_symbols,rn_symbols_head_and_middle_by_zeros_list)

        digit_head_list_str = []
        digit_head_list_int = []
        num_of_zeros_list = []
        values_breakdown = []
        components_list = []

        rn_head = []
        rn_middle = []

        trial_list = []
        rn_block_head = []
        rn_block_middle = []
        list_with_symbol_head_pair = []
        list_with_symbol_head_final = []
        
        rn_blocks_list_5_first_symbol = []
        rn_blocks_list_5_second_symbol = []
        
        rn_blocks_list = []

        final_list = []

        call_fun_1 = digit_heads_str()
        call_fun_2 = digit_heads_int()
        call_fun_3 = number_of_zeros()
        call_fun_4 = value_of_num_breakdown()
        call_fun_5 = components_of_num()
        call_fun_6 = filtration_lists()
        call_fun_7 = rn_head_or_middle()

        call_fun_8 = rn_digit_first_digit_of_rn_block()
        call_fun_9 = reorder_list()
        call_fun_10 = director()
        
        rn_blocks_list = list(set(rn_blocks_list))
        
        call_fun_11 = reorder_final_list()
        
        int_input_str = str(self.int_input)
        value_of_digit_head_to_num_of_zeros = to_zip_lists(digit_head_list_str,num_of_zeros_list)
        value_of_digit_head_to_factor_of_10_str = to_zip_lists(digit_head_list_str,values_breakdown)
        value_of_digit_head_to_factor_of_10_int = to_zip_lists(digit_head_list_int,values_breakdown)

        rn_head_or_middle_list = to_zip_lists(trial_list,num_of_zeros_list)
        list_with_symbol_head = rn_block_head + rn_block_middle 

       
        result = ''.join(final_list)
        
        
        return result
    
integer_to_roman = Roman(3999)
integer_to_roman.driver()
b = integer_to_roman.driver()
print(b)