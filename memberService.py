from repository import Repository


class MemberService:

    def get_memberList(self):
        return Repository.membersList

    def add_member(self, member):
        lastmemberKey = -1
        for memberKey in Repository.membersList:
            lastmemberKey = memberKey
        lastmemberKey = lastmemberKey + 1
        Repository.membersList[lastmemberKey] = member.__dict__
        return lastmemberKey

    def update_member(self, memberKey, member):
        if memberKey not in Repository.membersList:
            raise ValueError
        Repository.membersList[memberKey]['_name'] = member.name
        Repository.membersList[memberKey]['_surname'] = member.surname
        Repository.membersList[memberKey]['_age'] = member.age

    def delete_member(self, memberKey):
        if memberKey not in Repository.membersList:
            raise ValueError
        del Repository.membersList[memberKey]
