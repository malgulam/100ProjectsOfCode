echo "ensure you have inserted your api key where your_api_key_goes_here is"
curl https://quizapi.io/api/v1/questions -G \
-d apiKey=your_api_key_goes_here \
-d limit=10 -o quizoutput.txt #where limit is the number of questions