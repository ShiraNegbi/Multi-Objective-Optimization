import datetime
import random

# The class represents job position and its characteristics that are relevant for someone who looks for a job
class job():
    def __init__(self, id_number, salary_per_month, distance, entrance_date,
                 working_hours):
        self.id_number = id_number
        self.salary_per_month = salary_per_month
        self.distance = distance
        self.entrance_date = entrance_date
        self.working_hours = working_hours

        dictionary = {}
        dictionary["id_number"] = id_number
        dictionary["salary_per_month"] = salary_per_month
        dictionary["distance"] = distance
        dictionary["entrance_date"] = entrance_date
        dictionary["working_hours"] = working_hours
        self.dictionary = dictionary

    # Description
    def __str__(self):
        ret = ""
        for i in self.dictionary:
            ret += "\n" + i + " " + str(self.dictionary[i])
        return ret


# Keep only the jobs which have the proper number of working hours, and minimal entrance date.
# The jobs can be later chosen by their salary and distance.
def screen_jobs(jobs_list, max_working_hours, max_enter_date):
    return [a for a in jobs_list if (a.working_hours <= max_working_hours and a.entrance_date <= max_enter_date)]

# Generate a list of jobs
def get_jobs(num_jobs):
    result = []
    for i in range(num_jobs):
        id_number = i
        # constrains
        entrance_date = random.randrange(1, 12)
        working_hours = random.randrange(5, 12)
        # objectives
        distance = random.randrange(10, 50)
        salary_per_month = random.randrange(1000,
                                            1500) * working_hours

        result.append(job(id_number, salary_per_month, distance, entrance_date, working_hours))
    return result

# Calculate the value by the given weights for the objectives
def get_objective_value(job, salary_weight, dist_weight):
    return salary_weight * job.salary_per_month + dist_weight * job.distance

# Sort a list of jobs by the objective value
def sort_by_objectives(jobs, salary_weight, dist_weight):
    jobs.sort(key=lambda apartment: get_objective_value(apartment, salary_weight, dist_weight),
              reverse=True)

# Choose the optimal job
def main():

    # Generate a list of open positions
    job_list = get_jobs(100)
    for job in job_list:
        print(job)

    start = datetime.datetime.now()

    # Screen the jobs by the constraints
    relevant_jobs = (screen_jobs(job_list, 8, 4))
    print("\nRelevant:")
    for job in relevant_jobs:
        print(job)

    # Define the weights of the objectives and sort the jobs by them
    weight_salary = 5
    weight_dist = -3

    sort_by_objectives(relevant_jobs, weight_salary, weight_dist)
    print("\nSorted by objectives:")
    for job in relevant_jobs:
        print(job)
        print("Objective value = " + str(get_objective_value(job, weight_salary, weight_dist)))
        print()

    # Choose the best job from the list
    print("Optimal job:")
    optimal = relevant_jobs[0]
    print(optimal)

    end = datetime.datetime.now()
    print(end - start)


if __name__ == '__main__':
    main()

