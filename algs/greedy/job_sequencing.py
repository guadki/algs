# Given an array of jobs where every job has a deadline and associated profit if the job is finished before the
# deadline. It is also given that every job takes a single unit of time, so the minimum possible deadline for any job
# is 1. Maximize the total profit if only one job can be scheduled at a time.
from dataclasses import dataclass


@dataclass
class Job:
    job_id: str
    deadline: int
    profit: int

    def __repr__(self) -> str:
        return self.job_id


def job_sequence(jobs: list[Job]) -> list[Job]:
    result = []
    used_jobs = []
    max_deadline = max(jobs, key=lambda j: j.deadline).deadline
    # sort jobs by profit desc
    jobs = sorted(jobs, key=lambda j: j.profit, reverse=True)

    for i in range(max_deadline, 0, -1):
        for job in jobs:
            # pick the highest profit in currently checked deadline (for d=2 its deadlines 2,3,4...) that hasn't been
            # picked yet
            if max_deadline <= job.deadline and job.job_id not in used_jobs:
                result.append(job)
                used_jobs.append(job.job_id)
                max_deadline -= 1
                break

    return result


print(
    job_sequence([Job("a", 4, 20), Job("b", 1, 10), Job("c", 1, 40), Job("d", 1, 30)])
)
print(
    job_sequence(
        [
            Job("a", 2, 100),
            Job("b", 1, 19),
            Job("c", 2, 27),
            Job("d", 1, 25),
            Job("e", 3, 100),
        ]
    )
)
