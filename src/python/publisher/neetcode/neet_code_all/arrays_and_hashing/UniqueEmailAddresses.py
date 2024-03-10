from typing import List


class UniqueEmailAddresses:

    def nunUniqueEmailAddresses(self, emails: List[str]) -> int:
        uniqueList = set()
        test = []
        for email in emails:
            isValid = self.processLocalEmailPlusSign(email)
            if isValid != "-1":
                uniqueList.add(isValid)
                test.append(isValid)
        print(isValid)
        return len(uniqueList)

    def processLocalEmailPlusSign(self, email: str) -> str:
        localName = ""
        atIndex = email.index("@")
        localName = email[0: atIndex]
        domainName = email[atIndex: len(email) + 1]

        hasPlus = localName.find("+")
        if hasPlus != -1:
            localName = localName[0: hasPlus]

        localName = localName.replace(".", "")
        if localName and domainName:
            return localName + domainName

        return "-1"

    def neetProcessLocalEmailPlusSign(self, emails: str) -> str:
        uniqueSet = set()

        for email in emails:
            i = 0
            local = ""
            while email[i] not in ["@", "+"]:
                if email[i] != ".":
                    local = local + email[i]
                i += 1

            domain = ""
            j = len(email) - 1
            while email[j] != "@":
                domain = email[j] + domain
                j -= 1

            uniqueSet.add((local, domain))

        return len(uniqueSet)
        # return uniqueSet

    def neetCheatProcessLocalEmailPlusSign(self, emails: str) -> str:
        uniqueList = set()

        for email in emails:
            localName, domain = email.split("@")
            localName = localName.split("+")[0]
            localName = localName.replace(".", "")
            uniqueList.add((localName, domain))

        return len(uniqueList)



uniqueEmailAddresses = UniqueEmailAddresses()
print(uniqueEmailAddresses.neetCheatProcessLocalEmailPlusSign(["test.email+alex@leetcode.com",
                                                          "test.e.mail+bob.cathy@leetcode.com",
                                                          "testemail+david@lee.tcode.com"]))
print(uniqueEmailAddresses.neetCheatProcessLocalEmailPlusSign(["a@leetcode.com", "b@leetcode.com", "c@leetcode.com"]))
print(uniqueEmailAddresses.neetCheatProcessLocalEmailPlusSign([
                                                            "r.cyo.g+d.h+b.ja@tgsg.z.com",
                                                            "r.cyo.g+ng.r.iq@tgsg.z.com",
                                                            "r.cyo.g+n.h.e+n.g@tgsg.z.com",
                                                            "r.cyo.g+x+d.c+f.t@tgsg.z.com",
                                                            "r.cyo.g+x+t.y.l.i@tgsg.z.com",
                                                            "r.cyo.g+brxxi@tgsg.z.com",
                                                            "r.cyo.g+z+dr.k.u@tgsg.z.com",
                                                            "r.cyo.g+d+l.c.n+g@tgsg.z.com",
                                                            "fg.r.u.uzj+vq.o@kziczvh.com",
                                                            "fg.r.u.uzj+uzq@kziczvh.com",
                                                            "fg.r.u.uzj+mvz@kziczvh.com",
                                                            "fg.r.u.uzj+taj@kziczvh.com",
                                                            "fg.r.u.uzj+fek@kziczvh.com",
                                                            "fg.r.u.uzj+o.f.d@kziczvh.com",
                                                            "fg.r.u.uzj+o.pw@kziczvh.com",
                                                            "fg.r.u.uzj+k+p.j@kziczvh.com",
                                                            "fg.r.u.uzj+w.y+b@kziczvh.com",
                                                            "fg.r.u.uzj+lp.k@kziczvh.com"]))
