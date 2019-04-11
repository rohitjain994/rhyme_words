#!flask/bin/python
from flask import Flask, jsonify, request, abort, make_response

app = Flask(__name__)

word_list = ["Computing","Polluting","Diluting","Commuting","Recruiting","Drooping"]

def word_match(word1,word2):
  n = len(word1)
  m = len(word2)
  i = 1
  while(word1[n-i]==word2[m-i]):
    i = i+1
  return i-1

def get_rhyme(matching_word):
    match_word = {}
    for word in word_list:
        cnt = word_match(matching_word,word)
        if cnt != 0:
            if cnt not in match_word:
                l = []
                l.append(word)
                match_word[cnt] = l
            else:
                match_word[cnt].append(word)
    if match_word:
        k=list(match_word)
        k.sort(reverse = True)
        return match_word[k[0]]
    else: 
        return None

@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify( { 'error': 'Bad request' } ), 400)

@app.route('/rhyme/api/word', methods=['GET'])
def get_tasks():
    return jsonify({'words': word_list})


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
