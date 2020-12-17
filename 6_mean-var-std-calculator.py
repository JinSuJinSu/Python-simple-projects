
#import numpy to create martix
import numpy as np

#  create calculate function
def calculate(list):
    if(len(list)<9):
        raise ValueError("List must contain nine numbers.")

    else:
        martix = np.asmatrix(list).reshape(3,3)


    # create calculation function to convert martix to list
    def range_calculation(value,value_list):
        for i in range(len(value)):
            value_list.append(value[i])

    #1.mean value calculation

    mean_value1 = np.mean(martix,axis=0)
    mean_value2 = np.mean(martix,axis=1)
    mean_value3 = np.mean(martix)

    result_mean_value1 = np.ravel(mean_value1, order='C')
    result_mean_value2 = np.ravel(mean_value2, order='F')
    result_mean_value3 = mean_value3

    result_mean_value1_list=[]
    result_mean_value2_list=[]

    range_calculation(result_mean_value1,result_mean_value1_list)
    range_calculation(result_mean_value2,result_mean_value2_list)

    final_mean_value = [result_mean_value1_list,result_mean_value2_list,result_mean_value3]

    #2. var value calculation

    var_value1 = np.var(martix,axis=0)
    var_value2 = np.var(martix,axis=1)
    var_value3 = np.var(martix)

    result_var_value1 = np.ravel(var_value1, order='C')
    result_var_value2 = np.ravel(var_value2, order='F')
    result_var_value3 = var_value3

    result_var_value1_list=[]
    result_var_value2_list=[]

    range_calculation(result_var_value1,result_var_value1_list)
    range_calculation(result_var_value2,result_var_value2_list)

    final_var_value = [result_var_value1_list,result_var_value2_list,result_var_value3]


    #3. std value calculation

    std_value1 = np.std(martix,axis=0)
    std_value2 = np.std(martix,axis=1)
    std_value3 = np.std(martix)

    result_std_value1 = np.ravel(std_value1, order='C')
    result_std_value2 = np.ravel(std_value2, order='F')
    result_std_value3 = std_value3

    result_std_value1_list=[]
    result_std_value2_list=[]

    range_calculation(result_std_value1,result_std_value1_list)
    range_calculation(result_std_value2,result_std_value2_list)

    final_std_value = [result_std_value1_list,result_std_value2_list,result_std_value3]


    #4.max value calculation

    max_value1 = np.max(martix,axis=0)
    max_value2 = np.max(martix,axis=1)
    max_value3 = np.max(martix)

    result_max_value1 = np.ravel(max_value1, order='C')
    result_max_value2 = np.ravel(max_value2, order='F')
    result_max_value3 = max_value3

    result_max_value1_list=[]
    result_max_value2_list=[]

    range_calculation(result_max_value1,result_max_value1_list)
    range_calculation(result_max_value2,result_max_value2_list)

    final_max_value = [result_max_value1_list,result_max_value2_list,result_max_value3]


    #5. min value calculation

    min_value1 = np.min(martix,axis=0)
    min_value2 = np.min(martix,axis=1)
    min_value3 = np.min(martix)

    result_min_value1 = np.ravel(min_value1, order='C')
    result_min_value2 = np.ravel(min_value2, order='F')
    result_min_value3 = min_value3

    result_min_value1_list=[]
    result_min_value2_list=[]

    range_calculation(result_min_value1,result_min_value1_list)
    range_calculation(result_min_value2,result_min_value2_list)

    final_min_value = [result_min_value1_list,result_min_value2_list,result_min_value3]


    #6. sum value calculation

    sum_value1 = np.sum(martix,axis=0)
    sum_value2 = np.sum(martix,axis=1)
    sum_value3 = np.sum(martix)

    result_sum_value1 = np.ravel(sum_value1, order='C')
    result_sum_value2 = np.ravel(sum_value2, order='F')
    result_sum_value3 = sum_value3

    result_sum_value1_list=[]
    result_sum_value2_list=[]


    range_calculation(result_sum_value1,result_sum_value1_list)
    range_calculation(result_sum_value2,result_sum_value2_list)

    final_sum_value = [result_sum_value1_list,result_sum_value2_list,result_sum_value3]

    # finish code and return final results

    return {
          'mean': final_mean_value,
          'variance': final_var_value,
          'standard deviation': final_std_value,
          'max': final_max_value,
          'min': final_min_value,
          'sum': final_sum_value
                                                }

print(calculate([0,1,2,3,4,5,6,7,8]))








