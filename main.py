import os
import pandas as pd

import dfg_visualizer


def pretty_print_dict(dictionary, indent=0):
    for key, value in dictionary.items():
        if isinstance(value, dict):
            print(" " * indent + f"{key}:")
            pretty_print_dict(value, indent + 4)
        else:
            print(" " * indent + f"{key}: {value}")


event_log_path = os.path.join("data", "blasting_with_rework_event_log.csv")

event_log = pd.read_csv(event_log_path, sep=";")

event_log = dfg_visualizer.log_formatter(event_log)

(
    multi_perspective_dfg,
    start_activities,
    end_activities,
) = dfg_visualizer.discover_multi_perspective_dfg(event_log)

pretty_print_dict(multi_perspective_dfg)

multi_perspective_dfg_string = dfg_visualizer.get_multi_perspective_dfg_string(
    multi_perspective_dfg, start_activities, end_activities
)


print("START ACTIVITIES")
print(start_activities)

print("END ACTIVITIES")
print(end_activities)
