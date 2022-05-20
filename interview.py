def interview(tim, max):
    
  if (max > 120):
     return("disqualified")
     
  for i in tim:

    if (i >= 0 and i <= 1):
      if (tim[i] > 5):
        return("disqualified")
      
    elif (i >= 2 and i <= 3):
      if (tim[i] > 10):
        return("disqualified")

    elif (i >= 4 and i <= 5):
      if (tim[i] > 15):
        return("disqualified")
        
    else:
      if (tim[i] > 20):
        return("disqualified")


    return("qualified")

tim=[5,5,10,10,10,10,20,20]
max=115
interview(tim,max)
