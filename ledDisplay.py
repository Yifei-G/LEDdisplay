def preDisplay(lines,ledSegments):
	for l in range(5):
			lines[l] += "".join(ledSegments[l]) + " "


def ledDisplay(lines):
	for line in lines:
		print(line)	