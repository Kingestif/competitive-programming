from queue import deque
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # queue = deque(students)
        # count = 0
        # for i in sandwiches:
        #     while len(queue) > 0:
        #         if queue[0] == sandwiches[0]:
        #             count += 1
        #             queue.popleft()
        #         else:
        #             queue.append(queue.popleft())

        x = Counter(students)
        counter = 0
        for i in sandwiches:
            if x[i] > 0:
                counter += 1
                x[i] -= 1
            else:
                break
        return len(students) - counter
            








        # start = 0
        # while len(queue) > 0:
        #     if queue[0] == sandiwiches[start]:
        #         queue.popleft()
        #         start += 1
        #     else:
        #         queue.append(queue.popleft())