

# Calculate Minutes per mile
MPM =(((43.5 * 60)/(10 / 1.61))/60)

# Calculate Mile per hour
MPH = ((60 / 43.5) * MPM)

# Round our #'s to 2 decimals 
RMPM = round (MPM, 2)
RMPH = round (MPH, 2)

# Present our findings
print ("If you run a 10 kilometer race in 43 minutes 30 seconds, what is your average time per mile? What is your average speed in miles per hour?\n\n\t", RMPM, "Minutes per mile\n\t", RMPH, "Miles per hour")