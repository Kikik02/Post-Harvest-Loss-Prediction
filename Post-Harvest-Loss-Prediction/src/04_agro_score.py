def score(moisture,temp,humidity,rain,ph,nitrogen):
    return .28*moisture-.22*abs(temp-28)+.1*humidity+.06*rain-1.5*abs(ph-6.7)+.04*nitrogen
print(round(score(55,29,70,60,6.6,90),2))
