from collections import namedtuple

Process = namedtuple("Process", ["process_size", "block_size"])


def allocate_partitions(
    block_sizes: list[int], process_sizes: list[int]
) -> list[Process]:
    processes = []
    block_sizes.sort(reverse=True)
    process_sizes.sort(reverse=True)

    bs_gen = (bs for bs in block_sizes)

    bs = next(bs_gen, None)
    for ps in process_sizes:
        while bs is not None and bs < ps:
            bs = next(bs_gen, None)

        if bs is None:
            processes.append(Process(ps, -1))
        else:
            processes.append(Process(ps, bs))
            bs = next(bs_gen, None)

    return processes


print(
    allocate_partitions([100, 500, 200, 300, 600], [212, 417, 112, 426, 100, 105, 107])
)
