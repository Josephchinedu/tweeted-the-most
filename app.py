from collections import Counter

no_tweet = int(input("no of tweets: "))
tweets = []

for i in range(1,no_tweet +1):
    user_tweets = input("enter tweet containing user name and tweet id separated by a space: ")
    tweets.append(user_tweets)


tweet_users = [pref_names.split()[0] for pref_names in tweets]
times = Counter(tweet_users)
repeat = times.values()
  
for element in set(repeat):
    dupl = ([(key, value) for
             key, value in sorted(times.items()) if
             value == element])
      
    if len(dupl) > 1:
        for (key, value) in dupl:
            print (key,'',value)
    max_value = max(times.values())
    temp_max_result = [(key, value) for 
                       key, value in sorted(times.items()) if
                       value == max_value]
      
    if temp_max_result != dupl:
        for (key,value) in temp_max_result:
            print (key,'',value)




