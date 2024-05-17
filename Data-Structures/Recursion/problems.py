#Capital words

def capitalize(arr):
    res = []
    if len(arr)==0:
        return res
    res.append(arr[0].upper())
    return res + capitalize(arr[1:])

words = ['i', 'am', 'learning', 'recursion']
print(capitalize(words)) # ['I', 'AM', 'LEARNING', 'RECURSION']

#Capitalize first

def captilaizef(arr):
    res = []
    if len(arr)==0:
        return res
    res.append(arr[0][0].upper()+arr[0][1:])
    return res + captilaizef(arr[1:])

print(captilaizef(['car', 'taco', 'banana'])) # ['Car','Taco','Banana']

#Collectstrings

def collectstrings(obj):
    res = []
    for key in obj:
        
        if type(obj[key]) is str:
            res.append(obj[key])
        if type(obj[key]) is dict:
            res = res + collectstrings(obj[key])
    return res
    
obj = {
  "stuff": 'foo',
  "data": {
    "val": {
      "thing": {
        "info": 'bar',
        "moreInfo": {
          "evenMoreInfo": {
            "weMadeIt": 'baz'
          }
        }
      }
    }
  }
}

print(collectstrings(obj)) # ['foo', 'bar', 'baz'])

            
    
