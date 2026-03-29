#from fifo import run_fifo
from lru import run_lru
#from mru import run_mru
#from optimal import run_optimal
#from second_chance import run_second_chance


def print_results(name, steps, faults, hits, pages, frames_count):
    print(f"\n--- {name} RESULT ---")
    print(f"Number of pages: {len(pages)}")
    print(f"Number of frames: {frames_count}")
    print(f"Reference string: {' '.join(map(str, pages))}")
    print("-" * 60)
    print(f"{'Step':<5}{'Page':<8}{'Frames':<25}{'Result'}")
    print("-" * 60)

    for i, step in enumerate(steps, start=1):
        print(f"{i:<5}{step['page']:<8}{str(step['frames']):<25}{step['result']}")

    total = len(pages)
    failure_rate = (faults / total) * 100 if total > 0 else 0
    success_rate = (hits / total) * 100 if total > 0 else 0

    print("-" * 60)
    print(f"Page Interrupts / Faults: {faults}")
    print(f"Hits / Successes: {hits}")
    print(f"Failure Rate: {failure_rate:.2f}%")
    print(f"Success Rate: {success_rate:.2f}%")
    print("-" * 60)


def get_input():
    pages = list(map(int, input("Enter pages (space-separated): ").split()))
    frames = int(input("Enter number of frames: "))
    return pages, frames


def main():
    while True:
        print("\n===== PAGE REPLACEMENT MENU =====")
        print("1. FIFO")
        print("2. LRU")
        print("3. MRU")
        print("4. OPTIMAL")
        print("5. SECOND CHANCE")
        print("6. Exit")

        choice = input("Choose an algorithm: ")

        if choice == "1":
            pages, frames = get_input()
            steps, faults, hits = run_fifo(pages, frames)
            print_results("FIFO", steps, faults, hits, pages, frames)

        elif choice == "2":
            pages, frames = get_input()
            steps, faults, hits = run_lru(pages, frames)
            print_results("LRU", steps, faults, hits, pages, frames)

        elif choice == "3":
            pages, frames = get_input()
            steps, faults, hits = run_mru(pages, frames)
            print_results("MRU", steps, faults, hits, pages, frames)

        elif choice == "4":
            pages, frames = get_input()
            steps, faults, hits = run_optimal(pages, frames)
            print_results("OPTIMAL", steps, faults, hits, pages, frames)

        elif choice == "5":
            pages, frames = get_input()
            steps, faults, hits = run_second_chance(pages, frames)
            print_results("SECOND CHANCE", steps, faults, hits, pages, frames)

        elif choice == "6":
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()