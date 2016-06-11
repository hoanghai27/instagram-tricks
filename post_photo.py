from instagram import InstagramSession
import sys

# Get username, password and image path from arguments
username = sys.argv[1]
password = sys.argv[2]
file_path = sys.argv[3]

# NOTE: Image must be square
# Library is ported from PHP at http://lancenewman.me/posting-a-photo-to-instagram-without-a-phone/
# Thanks @lukecyca

print "Uploading " + file_path
insta = InstagramSession()
if insta.login(username, password):
    media_id = insta.upload_photo(file_path)
    print media_id
    if media_id is not None:
        insta.configure_photo(media_id, "")