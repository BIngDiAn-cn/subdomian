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
def generateSubdomain(subs):
    f2=open("jd_subdomain_0.txt","w+")
    domains=["jd"]
    subdomains_str=""
    subdomain_count=0
    k=0
    for sub in subs:
            for domain in domains:
                for test in tests:
                    for digit in digits:
                        for split in splits:
                            for rule in rules:
                                subdomain=rule
                                sub_str=sub.strip()
                                if "{domain}" in rule:

                                        subdomain=subdomain.replace("{domain}",domain)
                                if "{sub}" in rule:
                                        subdomain=subdomain.replace("{sub}",sub_str)

                                if "{test}" in rule:
                                        subdomain=subdomain.replace("{test}",test)

                                if "{split}" in rule:
                                        subdomain=subdomain.replace("{split}",split)

                                if "{digit}" in rule:
                                        subdomain=subdomain.replace("{digit}",digit)
                                subdomains_str+=subdomain+"\n"
                                subdomain_count+=1
                                if subdomain_count==10000:
                                    k+=1
                                    print(k)
                                    if k%1000==0:
                                        f2.close()
                                        f2=open("jd_subdomain_"+str(int(k/1000))+".txt","w+")
                                    subdomain_count=0
                                    f2.write(subdomains_str)
                                    subdomains_str=""


    f2.close()
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    with open("dic.txt","r") as f:
        generateSubdomain(f)
