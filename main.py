# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import requests
from itertools import combinations,permutations
rules=[
    "{domain}-{sub}",
    "{sub}-{domain}",
    "{domain}_{sub}",
    "{sub}_{domain}",
    "{domain}-{sub}{split}{test}",
    "{sub}-{domain}{split}{test}",
    "{domain}_{sub}{split}{test}",
    "{sub}_{domain}{split}{test}",
    "{test}{split}{domain}-{sub}",
    "{test}{split}{sub}-{domain}",
    "{test}{split}{domain}_{sub}",
    "{test}{split}{sub}_{domain}",
    "{test}{split}{sub}",
    "{sub}{split}{test}",
    "{domain}-{sub}-{digit}",
    "{domain}_{sub}_{digit}",
]
tests=[
    "test",
    "beta",
    "beta2",
    "pre",
    "dev",
]
splits={
    "-",
    "_",
    ".",
    ""
}
digits={
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9"
}
def generateSubdomain():
    domains=["jd"]
    subs=["admin"]
    for sub in subs:
            for domain in domains:
                for test in tests:
                    for digit in digits:
                        for split in splits:
                            for rule in rules:
                                subdomain=rule
                                if "{domain}" in rule:

                                        subdomain=subdomain.replace("{domain}",domain)
                                if "{sub}" in rule:
                                        subdomain=subdomain.replace("{sub}",sub)

                                if "{test}" in rule:
                                        subdomain=subdomain.replace("{test}",test)

                                if "{split}" in rule:
                                        subdomain=subdomain.replace("{split}",split)

                                if "{digit}" in rule:
                                        subdomain=subdomain.replace("{digit}",digit)


                                print(subdomain)
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    generateSubdomain()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
