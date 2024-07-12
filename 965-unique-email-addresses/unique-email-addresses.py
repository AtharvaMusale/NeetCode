class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = set()
        for email in emails:
            local, domain = email.split("@")
            local = local.split("+")[0]
            local = local.replace(".","")
            email_add = local + "@" + domain
            unique.add(email_add)
        return len(unique)