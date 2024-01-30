import heapq

def heap_sum(nums):

    heapq.heapify(nums)

    if len(nums) == 0:
        print("Відсутні кабелі для об'єднання.")
        print('-'*30)	
    elif len(nums) == 1:
        print(f"Загальні витрати на з'єднання кабелів дорівнюють {nums[0]}")
        print('-'*30)
    else:
        step = 0
        while len(nums) > 1: 
            min_elem_1 = heapq.heappop(nums)
            min_elem_2 = heapq.heappop(nums)
            sum = min_elem_1 + min_elem_2
            step += 1
            print(f"{step}. Об'єднано кабелі {min_elem_1} та {min_elem_2}.\nДовжина кабелю {sum} додана до кількості кабелів {len(nums)}")	
            heapq.heappush(nums, sum)
            print(nums)
            print('-'*30)
        else:
            print(f"Загальні витрати на з'єднання кабелів дорівнюють {nums[0]}")
            print('-'*30)
nums = [4, 10, 3, 5, 12, 8, 6, 9, 7, 1]
heap_sum(nums)

nums = []
heap_sum(nums)

nums = [4]            
heap_sum(nums)
