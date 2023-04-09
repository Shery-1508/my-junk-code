class Users:
    # create user
    def __init__(self,name):
        self.name = name
        self.followers = []
        self.posts = []
    # follow
    def follow(self,followed):
        followed.followers.append(self)
        print(f"{self.name} just followed {followed.name}")
    # post
    def post(poster,content):
        poster.posts.append(content)
        for f in poster.followers:
            f.notify(poster,content)
        
    # notify
    def notify(follower,poster,content):
        print(f"heloooo {follower.name} , {poster.name} has added foloowing post\n \"{content}\" ")
    
    def aboutUser(self,users):
        followerstextlist = []
        for f in self.followers:
            followerstextlist.append(str(f.name))
        for u in users:
            return (f"Name: {self.name}   Followers:{followerstextlist}\nPosts : {self.posts}")

class SocialMedia:
    # init
    def __init__(self) -> None:
        self.users = []
    # add_user
    def add_user(self,newuser):
        self.users.append(newuser)
    # get_users
    def get_users(self):
        pass

# creating social media object
network = SocialMedia()


# Creating new Users and adding to social media ----
Shery = Users('Shery')
network.add_user(Shery)

Wasif = Users('Wasif')
network.add_user(Wasif)

Ahmed = Users('Ahmed')
network.add_user(Ahmed)

Ali = Users('Ali')
network.add_user(Ali)
########################################################


## Users following each other ##
Ahmed.follow(Shery)
Wasif.follow(Ahmed)
Wasif.follow(Shery)
Ali.follow(Shery)

################################


##             Users Posting            ##
Shery.post("Hey this project is fun")
Ahmed.post("This is getting intense at every step ")
Wasif.post("But a little hardwork and concentration is need and we could achieve our goals")

###############################################



myfile = open('user_data.txt','w+')
myfile.write("\n\n"+Shery.aboutUser(network.users))
myfile.write("\n\n"+Ahmed.aboutUser(network.users))
myfile.write("\n\n"+Wasif.aboutUser(network.users))
myfile.write("\n\n"+Ali.aboutUser(network.users))


















# class User:
#     def __init__(self, username):
#         self.username = username
#         self.followers = []
#         self.posts = []
#         self.following = []
#         self.feed = []
        
#     def follow(self, user):
#         user.followers.append(self)
        
#     def post(self, message):
#         self.posts.append(message)
#         for follower in self.followers:
#             follower.notify(self.username + ": " + message)
            
#     def notify(self, message):
#         print(self.username + ": " + message)
    
#     def print_user_details(self):
#         return (f"name :{self.username}\t posts:{self.posts}\n followers:{self.followers}")
    
# class SocialNetwork:
#     def __init__(self):
#         self.users = []
        
#     def add_user(self, username):
#         self.users.append(username)
    
#     def get_user(self):
#         for usr in self.users:
#             print(usr)
#         return self.users
    
# network = SocialNetwork()

# userss = {}
# # create users
# network.add_user("Alice")
# alice = User("alice")
# network.add_user("Bob")
# bob = User("bob")
# network.add_user("Charlie")
# charlie = User("charlie")

# # alice follows bob and charlie
# alice.follow(bob)
# alice.follow(charlie)

# # bob and charlie post messages
# bob.post("Hello, World!")
# charlie.post("Python is fun!")


# # print(alice.username)
# # print(bob.followers)
# # print(alice.followers)
# # print(charlie.posts)