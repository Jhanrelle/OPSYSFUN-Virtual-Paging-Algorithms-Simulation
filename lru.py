def run_lru(pages, frames_count):
    frames = []
    last_used = {}
    page_faults = 0
    hits = 0
    steps = []

    for i, page in enumerate(pages):
        if page in frames:
            hits += 1
            result = "HIT"
        else:
            page_faults += 1
            result = "FAULT"

            if len(frames) < frames_count:
                frames.append(page)
            else:
                lru_page = min(frames, key=lambda p: last_used[p])
                frames[frames.index(lru_page)] = page

        last_used[page] = i

        steps.append({
            "page": page,
            "frames": frames.copy(),
            "result": result
        })

    return steps, page_faults, hits