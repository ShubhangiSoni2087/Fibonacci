from asyncio import events
import json, time
def fibonacci_index(num):
    fibo_list = []
    first_val, sum = 0,0
    second_val = 1
    while(sum <= num):
        fibo_list.append(sum)
        first_val = second_val
        second_val = sum
        sum = first_val+second_val
    return fibo_list
def lambda_handler(event, context):
    dataset = event['params']['querystring']['data']
    data = int(dataset)
    data_list = []
    if (data==0):
        data_list.append(data)
        index = fibonacci_index(data)
        return{
                'statusCode':200,
                'body':json.dumps("{} is a Fibonacci Number. Its the {}th Number in the Fibonacci Series ".format(data,len(index)))
            }
    elif (data>0):
        value = [5*data**2+4,5*data**2-4]
        for i in range(0,len(value)):
            square_root = value[i]**0.5
            modulus = square_root % 1
            if(modulus==0):
                data_list.append(value[i])
        if not data_list:
            return{
                'statusCode':200,
                'body': json.dumps("{} is not a Fibonacci number".format(data))
            }
        else: 
            index = fibonacci_index(data)
            return{
                'statusCode':200,
                'body':json.dumps("{} is a Fibonacci Number. Its the {}th Number in the Fibonacci Series ".format(data,len(index)))
            }
