import instaloader


ig = instaloader.Instaloader()

user = input("Enter the instagram user name:")

ig.download_profile(user,profile_pic_only=False)