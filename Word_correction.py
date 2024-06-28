import streamlit as st
def levenshein_distance(word1,word2):
  
  arr = [[0 for _ in range(len(word1)+1)] for _ in range(len(word2)+1)]
  for i in range(len(word2)):
    arr[i][-1] = len(word2)-i
  for j in range(len(word1)):
    arr[-1][j] = len(word1)-j
  for i in range(len(word2)-1, -1, -1):
    for j in range(len(word1)-1,-1,-1):
      if word1[j] == word2[i]:
        arr[i][j] = arr[i+1][j+1]
      else:
        arr[i][j] = min(arr[i+1][j+1],arr[i+1][j], arr[i][j+1]) +1

  return arr[0][0]

st.title("Word correction")
text = st.text_input("Word: ")
button = st.button("compute")
def load_vocabs(path):
    with open(path, 'r') as f:
        lines = f.readlines()
    words = sorted(set([line.strip().lower() for line in lines]))
    return words
vocabs= load_vocabs("./source/vocab.txt")
if button:
    distance = dict()
    for vocab in vocabs:

        distance[vocab] = levenshein_distance(vocab,text)
    sorted_distance = dict(sorted(distance.items(),key= lambda x:x[1]))
    correct_word = list(sorted_distance.keys())[0]
    st.write("Correct word:",correct_word)
    col1,col2 = st.columns(2)
    col1 = st.write(vocabs)
    col2 = st.write(sorted_distance)
    