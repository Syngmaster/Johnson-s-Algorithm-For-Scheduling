
class Machine:

    def __init__(self, jobs):
        self.jobs = jobs


class Sequence:

    def __init__(self, machine1, machine2):
        self.machine1 = machine1
        self.machine2 = machine2

    def calculate_best_sequence(self):
        left_side = []
        right_side = []
        list_index = get_array_of_indexes()
        # get min of first machine

        while len(machine1.jobs) > 0:
            if min(machine1.jobs) > min(machine2.jobs):
                # min job is in machine 2
                index = machine2.jobs.index(min(machine2.jobs))
                right_side.insert(0, list_index[index])
                list_index.pop(index)
                machine1.jobs.pop(index)
                machine2.jobs.pop(index)
            else:
                # min job is in machine 1
                index = machine1.jobs.index(min(machine1.jobs))
                left_side.append(list_index[index])
                list_index.pop(index)
                machine1.jobs.pop(index)
                machine2.jobs.pop(index)

        return left_side + right_side


def get_array_of_indexes():
    array = []
    for i in range(len(machine1.jobs)):
        array.append(i + 1)
    return array


jobs1 = [3, 6, 4, 3, 4, 2, 7, 5, 5, 6, 12]
jobs2 = [4, 5, 5, 2, 3, 3, 6, 6, 4, 7, 2]
machine1 = Machine(jobs1)
machine2 = Machine(jobs2)
best_sequence = Sequence(machine1, machine2)
print best_sequence.calculate_best_sequence()
