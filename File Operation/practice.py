#Find in which line of the file does the word "python" occur first.

def check_for_line():
  word = "open"
  data = True
  line_no = 1
  with open("File Operation/demo.txt","r") as f:
    while data:
      data = f.readline()
      if(word in data):
        print(line_no)
        return
      line_no +=1
  
  return print("Not found")
check_for_line()