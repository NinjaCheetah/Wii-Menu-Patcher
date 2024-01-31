sysmenu_versions = [
    ["34903cf8c6806c7c97de14377dd18ce4", "2.0", "E"],
    ["40cdaf6ba065eaaf8069a20f58171bfb", "2.1", "E"],
    ["f17ee211c55bf436cb4664e1ad3c4dc4", "2.2", "E"],
    ["744d38b0638e1b4ed381c5fa96c6bb46", "3.0", "E"],
    ["4d4c6435b0a491d17fd9fbf030b02b66", "3.1", "E"],
    ["0395ec39f8e353623e1620c5711af985", "3.2", "E"],
    ["ca0a2a5521389d050efdef342e83de9d", "3.3", "E"],
    ["7a2df3293672660e5c3ba366afedddae", "3.4", "E"],
    ["87f011d525b7acfbf7956cc2a452ffcb", "4.0", "E"],
    ["d19af34181c46645002efb130f6ea44c", "4.1", "E"],
    ["fe100d54129cb413029e8b5d501698c6", "4.2", "E"],
    ["cad93ca3ca41704b15bbee95b2e6aae2", "4.3", "E"],
    ["3634007279b3c3bbc286034e90fbe928", "2.0", "J"],
    ["2fc2361766692b4c0919453d9c2d69ae", "2.2", "J"],
    ["b742a8b2a8c45ca15b0fd62ceebd252d", "3.0", "J"],
    ["45885b693a9ea81ca96ddeb47e487f99", "3.1", "J"],
    ["8bb64a90874cc634dafb8b03fbcdb193", "3.2", "J"],
    ["a845fbae6d9de4f2f6fea5f8d2691540", "3.3", "J"],
    ["eb03d6f1640283931a3e5088e32dc64f", "3.4", "J"],
    ["d5b57cb3810c80149f6bfa192795d004", "4.0", "J"],
    ["64b846931dc7d790347827125c8c9509", "4.1", "J"],
    ["9552e63c8e0b6688e788639fb1c14e13", "4.3", "J"],
    ["a6b3cb6c6e11a8507c7e2736376a1726", "2.0", "U"],
    ["504d002f9225280456c9a8c41784c450", "2.2", "U"],
    ["879f69e25f517afc8c67b559672ba89f", "3.0", "U"],
    ["a0b076c7dd21a30945b64961c53d8745", "3.1", "U"],
    ["7c6a74820882936ca07d87637f9efaf0", "3.2", "U"],
    ["bfa616243e00df7627e915f6079e2bcc", "3.3", "U"],
    ["faf38cf46a62007badd82a5fada5e2ef", "3.4", "U"],
    ["ecd92d623872d556287eb1120c0d9204", "4.0", "U"],
    ["555d2c0bc92ccd05c6f6a57412ebbd37", "4.1", "U"],
    ["b4eda5b30d090c9256b60441d83c9d65", "4.2", "U"],
    ["417358284cce02dbb0fed3ef30b0b59d", "4.3", "U"],
]


def getMenuVersionCode(wadHash):
    for version in sysmenu_versions:
        if wadHash == version[0]:
            return version[1]
    return "Unknown Version"


def getMenuRegionCode(wadHash):
    for version in sysmenu_versions:
        if wadHash == version[0]:
            return version[2]
    return "Unknown Region"
