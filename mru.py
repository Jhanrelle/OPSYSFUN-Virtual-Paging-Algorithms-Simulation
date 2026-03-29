# =====================================================
# MRU (MOST RECENTLY USED) PAGE REPLACEMENT SIMULATOR
# =====================================================

def print_results(hits, faults, total):
    hit_ratio = (hits / total) * 100

    print("-----------------------------------------------------")
    print(f"Total Hits: {hits}")
    print(f"Total Faults: {faults}")
    print(f"Hit Ratio: {hit_ratio:.2f}%")
    print("=====================================================")


def mru_simulation(pages, capacity):

    frames = []
    last_used = {}   # keeps track of most recent usage
    hits = 0
    faults = 0

    print("\n==================== MRU RESULTS ====================")
    print("Step | Page | Frames        | Result")
    print("-----------------------------------------------------")

    for step, page in enumerate(pages, start=1):

        # PAGE HIT
        if page in frames:
            hits += 1
            result = "HIT"

        # PAGE FAULT
        else:
            faults += 1
            result = "FAULT"

            # If frames not full
            if len(frames) < capacity:
                frames.append(page)

            # Replace MOST RECENTLY USED page
            else:
                mru_page = max(last_used, key=last_used.get)
                replace_index = frames.index(mru_page)
                frames[replace_index] = page
                del last_used[mru_page]

        # Update last used time
        last_used[page] = step

        # Display step (same format as your screenshot)
        print(f"{step:<4} | {page:<4} | {str(frames):<13} | {result}")

    print_results(hits, faults, len(pages))


# ================= MAIN PROGRAM =================
def main():

    print("====== PAGE REPLACEMENT ALGORITHM SIMULATOR ======")
    print("[1] MRU (Most Recently Used)")
    print("[0] Exit")

    choice = input("Select an algorithm: ")

    if choice == "1":
        ref_string = input(
            "Enter page reference string (space-separated, e.g., 7 0 1 2): "
        )

        pages = list(map(int, ref_string.split()))
        frames = int(input("Enter number of frames: "))

        mru_simulation(pages, frames)

    else:
        print("Program ended.")


# RUN PROGRAM
main()