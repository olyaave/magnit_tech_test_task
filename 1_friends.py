
class Friend:
    def __init__(self, name: str):
        self.name = name
        self._invites = []
    
    def invite(self, invite_message: str):
        self._invites.append(invite_message)
        
    def show_invite(self):
        if self._invites:
            return self._invites[-1]
        return "No party..."
    
class Party:
    def __init__(self, place: str):
        self.place = place
        self._friends = []
    
    def add_friend(self, friend: Friend):
        self._friends.append(friend)
    
    def del_friend(self, friend: Friend):
        if friend in self._friends:
            self._friends.remove(friend)
    
    def send_invites(self, date_text: str):
        for friend in self._friends:
            friend.invite(f"{self.place}: {date_text}")
            
    
if __name__ == "__main__":
    party = Party("Midnight Pub")
    nick = Friend("Nick")
    john = Friend("John")
    lucy = Friend("Lucy")
    chuck = Friend("Chuck")
    
    party.add_friend(nick)
    party.add_friend(john)
    party.add_friend(lucy)
    party.send_invites("Friday, 9:00 PM")
    party.del_friend(nick)
    party.send_invites("Saturday, 10:00 AM")
    party.add_friend(chuck)

    print(john.show_invite())

    assert(john.show_invite() == "Midnight Pub: Saturday, 10:00 AM")
    assert(lucy.show_invite() == "Midnight Pub: Saturday, 10:00 AM")
    assert(nick.show_invite() == "Midnight Pub: Friday, 9:00 PM")
    assert(chuck.show_invite() == "No party...")