

# remember to run your model 
for example, the following is my case
./qwen2.5-1.5b-instruct-q2_k.llamafile

And you can use browser to open
http://localhost:8080/v1/models 

for example, the following example is my case  
```json
{"data":[{"created":1757588404,"id":"qwen2.5-1.5b-instruct-q2_k.gguf","object":"model","owned_by":"llamacpp"}],"object":"list"}
```


# run the code
```
poetry run python homework.py 
```

The following is my case 
$ poetry run python homework.py
LlaImaSsP2 is a 2-sentence summary of the software tool and is not a real llama from a 1970s era.