import JSON

print("Setup Search Engine Helper")
print("Coded by @XRYong on GitHub")
print("https://xryong.github.io")
print("Setup API Keys for services")

google_key = input("Enter Google API key: ")
facebook_key = input("Enter Facebook API key: )
twitter_key = input("Enter X (formally Twitter) API Key")

api_keys = {
 "google": google_key
 "twitter": twitter_key
 "Facebook": facebook_key
}


with open("config.json" as "w") as json_file:
 json.dump(api_keys, json_file)