from ledDisplay import preDisplay,ledDisplay


#This is the seven segments display codification
#Each number is formed by 7 segments
#1 means turn on the LED of the segment, 0 means ramain dark
#https://sites.google.com/site/tanglindigitalelectronics/basic-digital-circuits/bcd-to-seven-segment-display
leds=["1111110",          #This represents 0
		"0110000",		  #This represents 1
		"1101101",		  #This represents 2
		"1111001",		  #Same logic...
		"0110011",
		"1011011",
		"1011111",
		"1110000",
		"1111111",
		"1111011"
]



def numToLed(digits):
	lines = [ '' for l in range(5) ]	
	for num in digits:
		parttern = leds[int(num)]
		#Each segment has 3 "leds"
		segment = [[" "," "," "] for s in range (5)]
		#depending each digit of the parttern, turning each led of the segment ON (assigning the # to the segment.)
		if parttern[0] == "1":
			segment[0][0] = segment[0][1] = segment[0][2] = "#"

		if parttern[1] == "1":
			segment[0][2] = segment[1][2] = segment[2][2] = "#"

		if parttern[2] == "1":
			segment[2][2] = segment[3][2] = segment[4][2] = "#"

		if parttern[3] == "1":
			segment[4][0] = segment[4][1] = segment[4][2] = "#"

		if parttern[4] == "1":
			segment[2][0] = segment[3][0] = segment[4][0] = "#"

		if parttern[5] == "1":
			segment[0][0] = segment[1][0] = segment[2][0] = "#"

		if parttern[6] == "1":
			segment[2][0] = segment[2][1] = segment[2][2] = "#"

		#putting segments of each digit to a list called lines
		#lines is a 5 element list, which each element represents the row should be printed out on the console
		preDisplay(lines,segment)
	else:
		ledDisplay(lines)
