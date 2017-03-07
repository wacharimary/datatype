def data_type (x):
  
  if type(x) == str:
    
    return len(x)
    
  elif type(x) ==None:
     
     return "no value"
     
  elif type(x)== bool:
    
    return x
    
  elif type(x)== int:
      
      if x< 100:
        
        return "less than 100"
      
      elif x> 100:
        
        return "more than 100"
    
      else:
         return  "equal to 100"
  
  elif type(x)== list:
    
      if  len(x)>=3:
    
        return x [2]
    
      else:
        return None
  
  else:
    return "no value"
        
  
  
  data_type (None)
  data_type ([1,2,3])
  data_type ([1,2])
  data_type (True)
  data_type (3)
  data_type (200)
  data_type ("andela")
  

        
  