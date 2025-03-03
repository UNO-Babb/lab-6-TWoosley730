#WordCount.py
#Name: Trevor Woosley
#Date: 03/02/2025
#Assignment: Wordcount

def main():
  textFile = open("gettysberg.txt", 'r')
  lineCount = 0
  wordCount = 0
  letterCount = 0

  
  for line in textFile:
    lineCount = lineCount + 1
    words = line.split()
    for w in words:
      wordCount = wordCount + 1
    words = line.split
  print("Lines:", lineCount)
  print("Words:", wordCount)

if __name__ == '__main__':
  main()
