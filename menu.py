import optimal
import lru

def display_results(algo_name, steps, faults, hits):
    """Formats and prints the simulation results in a clean table."""
    print(f"\n{'='*20} {algo_name.upper()} RESULTS {'='*20}")
    print(f"{'Step':<5} | {'Page':<5} | {'Frames':<20} | {'Result':<10}")
    print("-" * 55)
    
    for idx, step in enumerate(steps):
        # Convert frame list to a clean string like [7, 0, 1]
        frames_display = str(step['frames'])
        print(f"{idx+1:<5} | {step['page']:<5} | {frames_display:<20} | {step['result']:<10}")
    
    print("-" * 55)
    print(f"Total Hits:   {hits}")
    print(f"Total Faults: {faults}")
    
    if len(steps) > 0:
        hit_ratio = (hits / len(steps)) * 100
        print(f"Hit Ratio:    {hit_ratio:.2f}%")
    print("=" * 50)

def get_input():
    """Handles user input for pages and frames with error checking."""
    try:
        raw_pages = input("Enter page reference string (space-separated, e.g., 7 0 1 2): ")
        if not raw_pages.strip():
            return None, None
        pages = [int(x) for x in raw_pages.split()]
        frames_count = int(input("Enter number of frames: "))
        return pages, frames_count
    except ValueError:
        print("\n[!] Invalid input. Please ensure pages are integers separated by spaces.")
        return None, None

def main_menu():
    while True:
        print("\n===== PAGE REPLACEMENT ALGORITHM SIMULATOR =====")
        print("[1] LRU (Least Recently Used)")
        print("[2] Optimal (Belady's Algorithm)")
        print("[0] Exit")
        
        choice = input("Select an algorithm: ")

        if choice == "0":
            print("Exiting Simulator. Goodbye!")
            break
        
        if choice not in ['1', '2']:
            print("\n[!] Invalid choice or Algorithm not yet implemented.")
            continue

        pages, frames_count = get_input()
        if pages is None:
            continue

        if choice == "1":
            # Calling run_lru from lru.py
            steps, faults, hits = lru.run_lru(pages, frames_count)
            display_results("LRU", steps, faults, hits)
        elif choice == "2":
            # Calling run_optimal from optimal.py
            steps, faults, hits = optimal.run_optimal(pages, frames_count)
            display_results("Optimal", steps, faults, hits)

if __name__ == "__main__":
    main_menu()