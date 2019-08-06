class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        email_set = set()
        
        for email in emails:
            at_index = email.index('@')
            local_name = email[:at_index]
            filter_local_name = ''
            for c in local_name:
                if c == '.': continue
                elif c == '+': break
                else: filter_local_name += c
            
            email_set.add(filter_local_name + email[at_index:])
            
        return len(email_set)
