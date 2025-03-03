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
    letters = line.split(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z)
    for l in letters:
      letterCount = letterCount + 1
  print("Lines:", lineCount)
  print("Words:", wordCount)
  print("Characters:", letterCount)
if __name__ == '__main__':
  main()
