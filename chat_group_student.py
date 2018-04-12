S_ALONE = 0
S_TALKING = 1

#==============================================================================
# Group class:
# member fields: 
#   - An array of items, each a Member class
#   - A dictionary that keeps who is a chat group
# member functions:
#    - join: first time in
#    - leave: leave the system, and the group
#    - list_my_peers: who is in chatting with me?
#    - list_all: who is in the system, and the chat groups
#    - connect: connect to a peer in a chat group, and become part of the group
#    - disconnect: leave the chat group but stay in the system
#==============================================================================

class Group:
    
    def __init__(self):
        self.members = {}
        self.chat_grps = {}
        self.grp_ever = 0
        
    def join(self, name):
        self.members[name] = S_ALONE
        return
        
        
    #implement        
    def is_member(self, name):
        if name in self.members:
            return True
        else:
            return False
            
    #implement
    def leave(self, name):
        if name in self.chat_grps.values:
            self.chat_grps.remove(name)
        else:
            self.members.remove(name)

        return self.members,self.chat_grps
        
    #implement                
    def find_group(self, name):
        found = False
        group_key = 0
        for k in self.chat_grps.keys():
            if name in self.chat_grps[k] :
                found = True
                group_key = k
            
        return found, group_key
        
    #implement                
    def connect(self, me, peer):
        
        #if peer is in a group, join it
        
        peer_in_group, group_key = self.find_group(peer)
        me_in_group,group_key2 = self.find_group(me)

        if peer_in_group == True:
            self.chat_grps[group_key].append(me)
            self.members[me] = S_TALKING
        elif me_in_group == True:
            self.chat_grps[group_key2].append(peer)
            self.members[peer] = S_TALKING
        # otherwise, create a new group with you and your peer 
        else:
            self.grp_ever += 1
            self.chat_grps[self.grp_ever]=[me,peer]
            self.members[me] = S_TALKING
            self.members[peer] = S_TALKING
        
        
        return self.chat_grps,self.grp_ever,self.members

    #implement                
    def disconnect(self, me):
        # find myself in the group, quit
        in_group, group_num = self.find_group(me)
        if in_group == True:
            self.chat_grps[group_num].pop(self.chat_grps[group_num].index(me))
            self.members[me] = S_ALONE
            if len(self.chat_grps[group_num]) == 1:
                last_one = self.chat_grps[group_num][0]
                self.members[last_one] = S_ALONE
                self.chat_grps.pop(group_num)
                
        return self.chat_grps,self.members
        
    def list_all(self):
        # a simple minded implementation
        full_list = "Users:" + "\n"
        full_list += str(self.members) + "\n"
        full_list += "Groups:" + "\n"
        full_list += str(self.chat_grps) + "\n"
        return full_list

    #implement
    def list_me(self, me):
        # return a list, "me" followed by other peers in my group
        my_list = []
        my_list.append(me)
        peer_in, group = self.find_group(me)
        my_list.append(self.chat_grps[group])
        return my_list

if __name__ == "__main__":
	g = Group()
	g.join('a')
	g.join('b')
   
    
	print(g.list_all())

	g.connect('a', 'b')
	print(g.list_all())
    
