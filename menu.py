import RoundRobin
import NonPreempPrio
import PreempPrio
import ShortestJob


def menu():
    choice = ""
    while True:
        print("\nPlease input what Algorithm You want to use: \n [1] Round-Robin Algorithm \n [2] Non-Preemptive Priority Algorithm \n [3] Preemptive Priority Algorithm \n [4] Shortest Job First Algorithm \n [0] Exit")
        choice = input("Enter your choice: ")
        if choice == "0":
            print("Exiting the program.")
            break
        process = int(input("Enter the number of processes: "))
        processList = [0] * process
        priorityList = [0] * process
        burstList = [0] * process
        arrivalList = [0] * process
        takingInput(processList, priorityList, burstList, arrivalList, process)
        if "1" in choice:
            print("\nYou have selected Round-Robin Algorithm")
            quantum = int(input("Enter the time quantum: "))
            RoundRobin.Algo(processList, priorityList, burstList, arrivalList, process, quantum)
        if "2" in choice:
            print("\nYou have selected Non-Preemptive Priority Algorithm")
            NonPreempPrio.Algo(processList, priorityList, burstList, arrivalList, process)
        if "3" in choice:
            print("\nYou have selected Preemptive Priority Algorithm")
            PreempPrio.Algo(processList, priorityList, burstList, arrivalList, process)
        if "4" in choice:
            print("\nYou have selected Shortest Job First Algorithm")
            ShortestJob.Algo(processList, priorityList, burstList, arrivalList, process)
        if choice not in ['1', '2', '3', '4']:
            print("Invalid choice. Please try again.")



def takingInput(processList, priorityList, burstList, arrivalList, process):
        print("Enter details for each process (Lower number = higher priority):")
        for i in range(process):
            processList[i] = f"P{i+1}"
            arrivalList[i]  = int(input(f"Arrival time for {processList[i]}: "))
            burstList[i]    = int(input(f"Burst time for {processList[i]}: "))
            priorityList[i] = int(input(f"Priority for {processList[i]} (Enter 0 if not applicable):  "))





if __name__ == "__main__":
    try:
        print("Welcome to the CPU Scheduling Simulator!")
        menu()
    except Exception as e:
        print("An error occurred:", e)










