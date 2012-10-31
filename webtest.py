import httplib2

print "imported"

def get_site_data(site):
    h = httplib2.Http(".cache")
    resp, content = h.request(site,"GET")
    return content


