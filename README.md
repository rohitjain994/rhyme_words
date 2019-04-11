# rhyme_words

## Test Case: POST 
### Case 1 : When data formmat is wrong
  
```
$ curl --request POST --header "Content-Type: application/json" --data '{"word":["Disputing","Shooting"]}'  http://localhost:5000/rhyme/api/rhyme
{
  "error": "Bad request"
}

```
### Case 2 : When data is empty

```
$ curl --request POST \
>   --header "Content-Type: application/json" \
>   --data '{"words":[]}' \
>   http://localhost:5000/rhyme/api/rhyme

{}

```

### Case 3 : When data is correct format

```
$ curl --request POST \
>   --header "Content-Type: application/json" \
>   --data '{"words":["Disputing","Shooting"]}' \
>   http://localhost:5000/rhyme/api/rhyme
{
  "Disputing": [
    "Computing"
  ],
  "Shooting": [
    "Computing",
    "Polluting",
    "Diluting",
    "Commuting",
    "Recruiting"
  ]
}
```

### Case 4: When data field is missed

```
$ curl --request POST \
>   --header "Content-Type: application/json" \
>   http://localhost:5000/rhyme/api/rhyme
{
  "error": "Bad request"
}
```
## Test Case: GET 
### Case 1: 

```
$ curl --request GET http://localhost:5000/rhyme/api/word
{
  "words": [
    "Computing",
    "Polluting",
    "Diluting",
    "Commuting",
    "Recruiting",
    "Drooping"
  ]
}

```
