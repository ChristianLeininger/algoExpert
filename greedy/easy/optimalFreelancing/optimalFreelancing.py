# copyright 2024
# author: Christian Leininger
# Email: leiningc@tf.uni-freiburg.de
# date: 28.01.2024


def optimalFreelancing(jobs):
    """Optimal Freelancing
        Returns the maxium profit in 7 days
    Args:
        param1(list): list of int
    Return: int
    """
    # first sort the list of jobs by payment
    jobs.sort(key=lambda x: x["payment"], reverse=True)
    free_days = [0] * 7
    # now iterate over the list and add the payment to the total payment
    for job in jobs:
        # find the first free day before the deadline
        i = job["deadline"] - 1
        if i >= 7:
            # deadline is too far in the future
            i = 6
        while i >= 0:
            if free_days[i] == 0:
                free_days[i] = job["payment"]
                break
            i -= 1
    return sum(free_days)


if __name__ == "__main__":

    jobs = [
        {"deadline": 8, "payment": 1},
        {"deadline": 6, "payment": 4},
        {"deadline": 1, "payment": 2},
        {"deadline": 1, "payment": 3},
        {"deadline": 2, "payment": 3},
        {"deadline": 5, "payment": 2},
    ]
    actual = optimalFreelancing(jobs=jobs)
    expected = 9
