import random
import tweepy
import urllib3
import re
import requests
from multiprocessing import Pool
from time import sleep
urllib3.disable_warnings()

invite = ""
def getDiscord(twitterName):
    consumer_key = "P73yodskHy8bgU7QpiSHyJEUj"
    consumer_secret = "7lDk9p2AdbV1GpefCu7hcJkZ2s60XF66zhmyRY1LB8Mnw0czC9"
    access_token = "816700206033014784-tTtZP4JLUa4gRCcbyCV0Vy1J5lnjwNv"
    access_token_secret = "Xhj9L61lwyTk3HzKR26dw4J9ET4WwtCbUGxeWMWYUCvdb"
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth, proxy='')

    last_tweet = api.user_timeline(screen_name=twitterName, count=1)[0]
    tweet_text = last_tweet._json['entities']['urls']
    for links in tweet_text:
        link = links['expanded_url']
        if re.fullmatch(r'((https?:\/\/)?(www\.)?(discord\.(gg|io|me|li)|discordapp\.com\/invite)\/([^\s\/]+))', link) is not None:
            inv_code = re.findall(r'((https?:\/\/)?(www\.)?(discord\.(gg|io|me|li)|discordapp\.com\/invite)\/([^\s\/]+))', link)[0][-1]
            return inv_code
def main(discordtoken):
    print("starting with", discordtoken)
    header = {"authorization": discordtoken
              "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"}
    sleep(random.random())
    r = requests.post("https://discord.com/api/v8/invites/{}".format(invite), headers=header, verify=False)
    print(r)
    print("finish with", discordtoken)

if __name__ == '__main__':
    print("Bot by Lyonya feat. Tern")
    twitterName = str(input("Аккаунт в твитере (после @) "))
    timeout = int(input("Частота обновления в сек "))

    while True:
        sleep(timeout)
        print("waiting...")
        if getDiscord(twitterName):
            invite = getDiscord(twitterName)
            print("INVITE IS", invite)
            break
    discordtokens = []
    with open("tokens.txt") as f:
        for tokens in f:
            discordtokens.append(tokens.replace("\n", ""))
    print(discordtokens)
    print("Starting profiles")
    p = Pool(processes=len(discordtokens))
    p.map(main, discordtokens)

