# Lecture 8 Problems - exceptions and assertions

# L8 Problem 2


          
def FancyDivide(list_of_numbers, index):
    try:
        try:
            denom = list_of_numbers[index]
            for i in range(len(list_of_numbers)):
                list_of_numbers[i] /= denom
        finally:
            raise Exception("0")
    except Exception, e:
        print e


# L8 Problem 3

def FancyDivide(list_of_numbers, index):
   denom = list_of_numbers[index]
   return [SimpleDivide(item, denom)
               for item in list_of_numbers]


def SimpleDivide(item, denom):

    try:
        return item / denom
    except ZeroDivisionError, e:
        return 0

      
          
