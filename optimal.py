def predict(pages, frames, total_pages, current_index):
    # Function to find the page that will not be used for the longest time in the future
    res = -1
    farthest = current_index
    for i in range(len(frames)):
        j = 0
        for j in range(current_index, total_pages):
            if frames[i] == pages[j]:
                if j > farthest:
                    farthest = j
                    res = i
                break
        
        # If a page is never referenced in future, return its index immediately
        if j == total_pages - 1:
            return i
            
    # If none of the frames appear in the future, replace the first one (index 0)
    return 0 if (res == -1) else res

def run_optimal(pages, frames_count):
    frames = []
    page_faults = 0
    hits = 0
    steps = []
    total_pages = len(pages)

    for i in range(total_pages):
        page = pages[i]
        
        if page in frames:
            hits += 1
            result = "HIT"
        else:
            page_faults += 1
            result = "FAULT"

            if len(frames) < frames_count:
                frames.append(page)
            else:
                # Predict which frame to replace
                replace_index = predict(pages, frames, total_pages, i + 1)
                frames[replace_index] = page

        # Record the state for the menu/UI
        steps.append({
            "page": page,
            "frames": frames.copy(),
            "result": result
        })

    return steps, page_faults, hits