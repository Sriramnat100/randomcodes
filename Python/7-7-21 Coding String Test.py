available_parts = ["computer",
                   "monitor",
                   "keyboard",
                   "mouse",
                   "hdmi cable",
                   "dvd drive"
                   ]
for i in available_parts:
    available_parts[3:] = "trackball"

print(available_parts)