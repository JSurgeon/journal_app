from activity import Activity, Habit

hike = Activity("hike", "1pm", "3pm", "good", "forrest park")

print(f"Hike: {hike.name} {hike.startime}, {hike.endtime}, {hike.quality}, {hike.location}")

hike.name = "basketball"
hike.startime = "10pm"
hike.endtime = "11pm"
hike.quality = "bad"
hike.location = "somewhere else"

print(f"Hike: {hike.name} {hike.startime}, {hike.endtime}, {hike.quality}, {hike.location}")

hike = Habit("hike", "1pm", "3pm", "good", "forrest park", 5)

print(f"Hike: {hike.name} {hike.startime}, {hike.endtime}, {hike.quality}, {hike.location}, {hike.amount}")
