def risk(x): return "High" if x<15 else ("Moderate" if x<25 else "Low")
print([risk(x) for x in [12,20,30]])
