# Get the top events according to power points
def get_top_n_events(n, times):
    
    ranked_events = []
    for event in times.keys():
        # Get the best time in highschool
        best = sorted(times[event])[0]
        # Append the best highschool events POWER POINTS and then the name
        ranked_events.append((best[1], event))

    # Sort by power points so the front is the most
    ranked_events = sorted(ranked_events, reverse=True)
    # Return list of events
    return [event for _, event in ranked_events[0:n]]


def average_percentage_improvement(highschool_times, college_times):
    
    n = 0
    total_percentage = 0
    # Loop through every event in highschool
    for event in highschool_times.keys():
        # If we did NOT swim this event in college, skip.
        if not event in college_times:
            continue

        # Get the best time in highschool compared to the best time in college
        best_highschool = sorted(highschool_times[event])[0][0]
        best_college = sorted(college_times[event])[0][0]

        # A negative percentage indicates improvement
        percentage = (best_college - best_highschool) / best_highschool
        total_percentage += percentage
        n += 1

    if n == 0:
        return -1

    return (total_percentage / n + 1) * 100

def average_improvement_top_n(n, highschool_times, college_times):

    valid_events = 0
    total_percentage = 0
    # Get top events FROM highschool
    top_events = get_top_n_events(n, highschool_times)
    for event in top_events:
        if not event in college_times:
            continue

        # Get the best time in highschool compared to the best time in college
        best_highschool = sorted(highschool_times[event])[0][0]
        best_college = sorted(college_times[event])[0][0]

         # A negative percentage indicates improvement
        percentage = (best_college - best_highschool) / best_highschool
        total_percentage += percentage
        valid_events += 1

    if valid_events == 0:
        return -1

    return (total_percentage / valid_events + 1) * 100

def average_ratio_top_n(n, highschool_times, college_times):

    valid_events = 0
    total_ratio = 0
    # Get top events FROM highschool
    top_events = get_top_n_events(n, highschool_times)
    for event in top_events:
        if not event in college_times:
            continue

        # Get the best time in highschool compared to the best time in college
        best_highschool = sorted(highschool_times[event])[0][0]
        best_college = sorted(college_times[event])[0][0]

         # A negative percentage indicates improvement
        ratio = best_college / best_highschool
        total_ratio += ratio
        valid_events += 1

    if valid_events == 0:
        return -1

    return (total_ratio / valid_events) * 100

def average_power_points_top_n(n, highschool_times, college_times):

    valid_events = 0
    total_power_points = 0
    # Get top events FROM highschool
    top_events = get_top_n_events(n, highschool_times)
    for event in top_events:
        if not event in college_times:
            continue

        # Get the best time in highschool compared to the best time in college
        best_college = sorted(college_times[event])[0][1]
         # A negative percentage indicates improvement
        total_power_points += best_college
        valid_events += 1

    if valid_events == 0:
        return -1

    return (total_power_points / valid_events)