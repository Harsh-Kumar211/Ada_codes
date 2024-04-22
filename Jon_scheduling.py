def job_scheduling(deadlines, profit):
    jobs = [(i+1, deadlines[i], profit[i]) for i in range(len(deadlines))]
    
    jobs.sort(key=lambda x: -x[2])
    
    selected_jobs = []
    selected_deadlines = set()
    max_profit = 0
    for job in jobs:
        deadline = job[1]
        p = job[2]
        if deadline not in selected_deadlines:
            selected_jobs.append(job)
            selected_deadlines.add(deadline)
            max_profit += p
    
    return selected_jobs, max_profit

def get_input():
    deadlines = tuple(map(int, input("Enter deadlines separated by space: ").split()))
    profit = tuple(map(int, input("Enter profits separated by space: ").split()))
    return deadlines, profit

def main():
    deadlines, profit = get_input()
    selected_jobs, max_profit = job_scheduling(deadlines, profit)
    print("Selected Jobs:", selected_jobs)
    print("Maximum Profit:", max_profit)

if __name__ == "__main__":
    main()
