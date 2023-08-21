from datetime import datetime

def get_birthday(age):
  year = datetime.today().year
  return year - int(age)
