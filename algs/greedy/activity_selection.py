# You are given n activities with their start and finish times. Select the maximum number of activities that can be
# performed by a single person, assuming that a person can only work on a single activity at a time.
from dataclasses import dataclass

# Input: `jobs[start -> end]`  =  `[10 -> 20, 12 -> 25, 20 -> 30]`
# Output: `[10 -> 20, 20 -> 30]`
#
# Input: `jobs[start -> end]`  =  `[1 -> 2, 3 -> 4, 0 -> 6, 5 -> 7, 8 -> 9, 5 -> 9]`
# Output: `[1 -> 2, 3 -> 4, 5 -> 7, 8 -> 9]`


@dataclass(frozen=True, slots=True)
class Job:
    start_time: int
    end_time: int

    def __repr__(self) -> str:
        return f"{self.start_time} -> {self.end_time}"


def select_activities(jobs: list[Job]) -> list[Job]:
    results: list[Job] = []
    current_job = Job(0, 0)
    # sort by end_time
    for job in sorted(jobs, key=lambda job: job.end_time):
        # pick job that starts closest to current end_time
        if job.start_time >= current_job.end_time:
            current_job = job
            results.append(job)

    return results


print(select_activities([Job(10, 20), Job(12, 25), Job(20, 30)]))
print(
    select_activities(
        [Job(1, 2), Job(3, 4), Job(0, 6), Job(5, 7), Job(8, 9), Job(5, 9)]
    )
)
print(select_activities([]))
