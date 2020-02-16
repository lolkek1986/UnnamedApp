

class GrantParser(object):
    
    def __init__(self):
        self.file_name = "grants"
        
    def parse_grants(self):
        self.grants_file = open(self.file_name, "r")
        self.grants = []
        for line in self.grants_file.readlines():
            self.grants.append([line.split(", ")[0], line.split(", ")[1]])
        self.grants_file.close()
        return self.grants
    def search_grants(self, keyword):
        grants = self.parse_grants()
        grants_found = []
        for grant in grants:
            if grant[0] == keyword:
                grants_found.append(grant[0] + " - " + grant[1])
        return grants_found


