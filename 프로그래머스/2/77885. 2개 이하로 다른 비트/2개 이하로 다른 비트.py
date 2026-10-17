def solution(numbers):
    answer = []
    
    for number in numbers:
        if number % 2 == 0:
            answer.append(number + 1)
            
        else:
            binary = list('0' + bin(number)[2:])
            
            idx = ''.join(binary).rfind('0')
            
            binary[idx] = '1'
            binary[idx+1] = '0'
            
            answer.append(int(''.join(binary), 2))
            
    return answer