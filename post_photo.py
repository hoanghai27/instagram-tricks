from instagram import InstagramSession
import sys

username = sys.argv[1]
password = sys.argv[2]
file_path = sys.argv[3]
print "Uploading " + file_path

insta = InstagramSession()
if insta.login(username, password):
    media_id = insta.upload_photo(file_path)
    print media_id
    if media_id is not None:
        insta.configure_photo(media_id, "")
    else:
        raise Exception("Photo uploaded fail")