## Twitter-un-follower
A simple python script to follow or unfollow users on twitter using the tweepy api

# Step 1.
The easiest way to install the latest version is by using pip/easy_install to pull it from PyPI:
- [python](https://www.python.org/downloads/)
- [tweepy](https://github.com/tweepy/tweepy) (`pip install tweepy`)
- [Twitter app and keys](https://apps.twitter.com/), with appropriate permissions (usually read and write)
- [un/follower] (`git clone https://github.com/ManoloArevalo/Twitter-un-follower`)

# Step 2.
Head over to https://apps.twitter.com and register an application!
After you register, grab your applications ``Consumer Key`` and ``Consumer Secret`` from the application details tab.

Make sure to give read and write permission!

# Step 3.
Create a python file with the name "keys.py" and add the following with your new keys:

    keys = dict(
        screen_name = "your twitter-name comes here",
        consumer_key = "your consumer-key comes here",
        consumer_secret = "your consumer-secret comes here",
        access_token = "your acces-token comes here",
        access_token_secret = "your acces-token-secret comes here",
    )

# Run the script
There are two scripts that you can use:

##Follow your followers (follows every follower you currently have if you not already are following them)

    python follow.py
    
##Unfollow people that are not following you back

    python unfollow.py
    
#Thats all! have fun!
