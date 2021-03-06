from twitter import Twitter
import time


tw = Twitter()

def start():
    print("Starting program...")
    dms = list()
    while True:
        if len(dms) is not 0:
            for i in range(len(dms)):
                message = dms[i]['message']
                sender_id = dms[i]['sender_id']
                id = dms[i]['id']

                if len(message) is not 0 and len(message) < 280:
                    if "-tabe" in message:
                        message = message.replace("-tabe ini", "")
                        if len(message) is not 0:
                            if dms[i]['media'] is None:
                                print("DM will be posted")
                                tw.post_tweet(message)

                            else:
                                print("DM will be posted with media")
                                print(dms[i]['shorted_media_url'])
                                tw.post_tweet_with_media(message, dms[i]['media'],dms[i]['shorted_media_url'], dms[i]['type'])

                        else:
                            print("DM deleted because its empty..")

                    else:
                        print("DM will be deleted because does not contains keyword..")
                        tw.delete_dm(id)


            dms = list()

        else:
            print("Direct message is empty...")
            dms = tw.read_dm()
            if len(dms) is 0:
                time.sleep(20)

if __name__ == "__main__":
    start()