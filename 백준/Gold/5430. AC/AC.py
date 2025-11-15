from collections import deque
import sys

n=int(input())
out=[]


def parse_list(nums):
    nums = nums.replace('[', '').replace(']', '')
    return nums.split(',')
    

for i in range(n):
    reverse=False
    error=False
    cmds = sys.stdin.readline().rstrip()
    len_nums=int(sys.stdin.readline())
    nums=sys.stdin.readline().rstrip()
    parsed_nums=parse_list(nums) # 리스트로 변환
    
    if len_nums > 0:
        parsed_nums=list(map(int,parsed_nums)) # str -> int
        queue=deque(parsed_nums)
    
    else:
        # "[]" -> "" 으로 들어가 len이 1이 되는 현상을 방지
        queue=deque([])

    # R | D 입력 처리

    for cmd in cmds:
        # 여러번 뒤집으면 비효율적이니까 deque으로 양쪽에서 pop하는 방식으로 구현
            


        if cmd=='D':
            
            if len(queue) == 0:
                out.append("error")
                error=True
                break
            
            # 반전인 경우 배열 뒤에서 pop
            if reverse:
                queue.pop()
                
            else:
                queue.popleft()

        else:
            reverse = not reverse



    if error:
        continue

    if reverse:
        queue.reverse()

    # out.append((str(list(queue))).replace(" ",""))
    out.append("["+",".join(map(str,queue))+"]")

sys.stdout.write("\n".join(out))

