#!flask/bin/python
from flask import Flask, jsonify, request, abort, make_response

app = Flask(__name__)

# Constant word list.
word_list = ["Computing","Polluting","Diluting","Commuting","Recruiting","Drooping"]

# get number of characters match between two words
"""
  count matched character from last
"""
def get_character_match(word1,word2):
  n = len(word1)
  m = len(word2)
  i = 1
  while(word1[n-i]==word2[m-i]):
    i = i+1
  return i-1

#get rhyming words for input word out of word_list
"""
  1. create a dict of list where key is cnt and value is the list of the words in word_list that match to word
  2. get key where key is maximum.
  3. return list of word w.r.t to max(key) 

"""

def get_rhyme(matching_word):
    match_word = {}
    for word in word_list:
        cnt = get_character_match(matching_word,word)
        if cnt != 0:
            if cnt not in match_word:
                match_word[cnt] = [word]
            else:
                match_word[cnt].append(word)
    if match_word:
        k=list(match_word)
        k.sort(reverse = True)
        return match_word[k[0]]
    else: 
        return None

#error handler
@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify( { 'error': 'Bad request' } ), 400)

#GET api to get reference of word list
@app.route('/rhyme/api/word', methods=['GET'])
def get_tasks():
    return jsonify({'words': word_list})

#Post api to get rhyme words w.r.t word_list
"""
Sample input json:  {"words": ["word1", "word2", "word3"]}

Sample output json: { "word1":[List of matching rhyming words],
                      "word2": [list of matching rhyming  words],
                      "word3": [List of matching rhyming  words]}

"""

@app.route('/rhyme/api/rhyme', methods=['POST'])
def create_task():
    if not request.json or not 'words' in request.json:
        abort(400)
    rhyme_list = {}
    for word in request.json['words']:
      rhyme_list[word] = get_rhyme(word)
    return jsonify(rhyme_list)


if __name__ == '__main__':
    app.run(debug=True)
