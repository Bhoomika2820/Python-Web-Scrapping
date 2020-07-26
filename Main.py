from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import pandas as pd
import re
from urllib.request import Request, urlopen


# step 1

class Dte_Details:
    # Scrapping one site of dte website and getting the result
    def __init__(self, url, ):
        self.my_url = url
        self.uClient = uReq(self.my_url)
        self.page_html = self.uClient.read()
        self.uClient.close()
        self.page_soup = soup(self.page_html, "html.parser")
        self._ID = (self.page_soup.findAll("span", {"id": "ctl00_ContentPlaceHolder1_lblInstituteCode"}))[0].text
        self._ClgName = self.page_soup.findAll("span", {"id": "ctl00_ContentPlaceHolder1_lblInstituteNameEnglish"})[
            0].text
        self._Address = (self.page_soup.findAll("span", {"id": "ctl00_ContentPlaceHolder1_lblAddressEnglish"}))[0].text
        self._Email = (self.page_soup.findAll("span", {"id": "ctl00_ContentPlaceHolder1_lblEMailAddress"}))[0].text

        self._district = (self.page_soup.findAll("span", {"id": "ctl00_ContentPlaceHolder1_lblDistrict"}))[0].text

        self._Website_link = (self.page_soup.findAll("span", {"id": "ctl00_ContentPlaceHolder1_lblWebAddress"}))[0].text
        self._Office_Number = (list(
            (self.page_soup.findAll("span", {"id": "ctl00_ContentPlaceHolder1_lblOfficePhoneNo"}))[0].text.split(
                " "))[0])
        self._Personal_Number = (
            list(((self.page_soup.findAll("span", {"id": "ctl00_ContentPlaceHolder1_lblPersonalPhoneNo"}))[
                      0].text).split(" "))[0])

        # self._course = (self.page_soup.findAll("", {"": ""}))[0].text

    # College Name
    def ClgName(self):
        return self._ClgName.strip()

    def Address(self):
        if '\n' or "\\n" in self._Address:
            self._Address.replace('\n', '|n')
            self._Address.replace('\\n', '|n')

        return self._Address.strip()

    def Email(self):
        return self._Email.strip()

    def district(self):
        return self._district.strip()

    def state(self):
        return "Maharashtra"

    def Website_Link(self):
        return self._Website_link.strip()

    def Office_Number(self):
        return self._Office_Number.strip() + "//" + self._Personal_Number.strip()

    # Course to identify which colleges fall under engineering colleges
    def course(self):
        if "engineering" in self._ClgName.lower() or "technology" in self._ClgName.lower() or "technological" in self._ClgName.lower() or "technical" in self._ClgName.lower():
            return "Engineering"
        else:
            return None


# step 2
class Dte_mainsite:
    # Scrapping links for each college information
    def __init__(self):
        self.filename = "Colleges.csv"
        f = open(self.filename, "w")
        self.headers = "COLLEGE_NAME,ADDRESS,DISTRICT,STATE,OFFICE_NUMBER,EMAIl,WEBSITE_LINK\n"
        f.write(self.headers)
        print(self.headers)
        print("---" * 60)
        # my_url contains all the urls present in dte maharashtra site
        self.my_url = ["http://dtemaharashtra.gov.in/frmInstituteList.aspx?RegionID=3&RegionName=Mumbai",
                       "http://dtemaharashtra.gov.in/frmInstituteList.aspx?RegionID=1&RegionName=Amravati",
                       "http://dtemaharashtra.gov.in/frmInstituteList.aspx?RegionID=2&RegionName=Aurangabad",
                       "http://dtemaharashtra.gov.in/frmInstituteList.aspx?RegionID=4&RegionName=Nagpur",
                       "http://dtemaharashtra.gov.in/frmInstituteList.aspx?RegionID=5&RegionName=Nashik"]

        for urls in self.my_url:
            uClient = uReq(urls)
            page_html = uClient.read()
            uClient.close()
            self.page_soup = soup(page_html, "html.parser")
            self.containers1 = self.page_soup.findAll("td", {"class": "Item"})

            for i in range(1, len(self.containers1)):
                for link in self.containers1[i].findAll('a'):
                    if link.get('href') is not None:
                        # lite is the link of the site
                        self.lite = "http://dtemaharashtra.gov.in/" + link.get('href')
                        self.site1 = Dte_Details(self.lite)
                        if self.site1.course() == "Engineering":
                            self.row = (self.site1.ClgName().replace(",", "|") + "," + self.site1.Address().replace(",",
                                                                                                                    "|") + "," + self.site1.district().replace(
                                ",", "|") + "," + self.site1.state() + "," + self.site1.Office_Number() + "," +
                                        self.site1.Email() + "," + self.site1.Website_Link() + "\n")
                            print(self.row)
                            f.write(self.row)

        f.close()
        # check for error in csv file and correct them manually(Mostly alignment issue only  and "//" in phone nos)


# step 3

class Study_guide_Detail_site:
    def __init__(self, url, ):
        self.my_url = url
        self.uClient = uReq(self.my_url)
        self.page_html = self.uClient.read()
        self.uClient.close()
        self.page_soup = soup(self.page_html, "html.parser")
        self.container = self.page_soup.findAll("div", {"id": "college_details-new"})
        self.container1 = self.container[0].findAll("div", {"id": "clg_dtl"})
        self.det = self.container1[0].findAll("tr")
        self._email = ""
        self._address = ""
        self._website = ""
        self._office_number = ""
        for each in self.det:
            k = each.findAll("td")
            if k[0].text.strip() == "Address":
                self._address = " ".join(k[1].text.strip().split())
                # print(address)
            if k[0].text.strip() == "Phone":
                self._office_number = k[1].text.strip()
                # print(phone)
            if k[0].text.strip() == "E-Mail":
                self._email = k[1].text.strip()
                # print(email)
            if k[0].text.strip() == "Website":
                self._website = k[1].text.strip()
                # print(website)

    def Address(self):
        if '\n' in self._address:
            self._address.replace('\n', ';')
        self._address.replace(",", " ; ")
        self._address.strip()
        return self._address

    def Email(self):
        return self._email

    def Website_Link(self):
        return self._website

    def Office_Number(self):
        return self._office_number.replace(",", "/")


# step 4
class Study_guide_middle_site:
    def __init__(self):
        self.site_url = "http://www.studyguideindia.com/Colleges/Engineering/default.asp?"
        self.filename = "Colleges1.csv"
        self.f = open(self.filename, "w")
        self.headers = "COLLEGE_NAME,ADDRESS,DISTRICT,STATE,OFFICE_NUMBER,EMAIl,WEBSITE_LINK\n"
        self.f.write(self.headers)
        print(self.headers)
        print("---" * 60)
        Study_guide_middle_site.details(self, self.site_url)
        self.f.close()

    def details(self, site_url):
        # print(self.site_url)
        uClient = uReq(site_url)
        self.page_html = uClient.read()
        uClient.close()
        self.page_soup = soup(self.page_html, "html.parser")
        self.containers1 = self.page_soup.findAll("table", {"class": "clg-listing"})
        self.con = self.containers1[0].findAll("td")
        self.con = self.con[3:]

        # print(len(con))
        for i in range(0, len(self.con), 3):
            self.college_name = (self.con[i].findAll("a"))[0].get("title").strip()
            self.link = (self.con[i].findAll("a"))[0].get("href")
            try:

                self.district = self.con[i + 1].text.strip()
                self.state = self.con[i + 2].text.strip()
                if self.state.lower() != "Maharashtra":
                    self.site1 = Study_guide_Detail_site(self.link)
                    self.row = self.college_name.replace(",", "|") + "," + self.site1.Address().replace(",",
                                                                                                        ";") + "," + self.district.replace(
                        ",", ";") \
                               + "," + self.state.replace(",", ";") + "," + self.site1.Office_Number().replace(",",
                                                                                                               " // ") + "," + self.site1.Email().replace(
                        ",", "// ") \
                               + "," + self.site1.Website_Link().replace(",", "//") + "\n"
                    print(self.row)
                    self.f.write(self.row)
            except:
                pass
        self.next1 = self.page_soup.findAll("a", {"class": "link"})
        self.next1[-1] = (self.next1[-1].get("href")).replace(";", "&")
        if self.college_name[0] == "Z":
            return
        self.details(self.next1[-1])


# check for manual error()
# step 4
# Merging the two data sets
# You can store in same data frame but for my convinience i ll store it in different csv
# Check whether the csv file is saved in utf-8 comma delimeted

class Combination:
    def __init__(self):
        self.df = pd.read_csv("Colleges1.csv")
        self.df1 = pd.read_csv("Colleges.csv")
        self.combined_data_frame = pd.concat([self.df, self.df1], ignore_index=True)
        self.combined_data_frame = self.combined_data_frame.sort_values(by=["STATE"])
        self.combined_data_frame.to_csv("combined_colleges.csv", index=False, encoding="utf-8")
        self.combined_data_frame = self.combined_data_frame.dropna()
        self.combined_data_frame.to_csv("combined_colleges_drop.csv", index=False, encoding="utf-8")
        # un comment this code if you want index in csv
        # self.df2 = pd.read_csv("combined_colleges.csv")
        # self.df2.to_csv("combined_colleges.csv")


"""


# step 5
# Finding tpo data and storing them in an another file
"""


class tpo_data_site:

    def __init__(self, my_url):
        self.mail_list = []
        self.uClient = uReq(my_url)
        self.page_html = self.uClient.read()
        self.uClient.close()
        self.page_soup = soup(self.page_html, "html.parser")
        self.data = (self.page_soup.text.strip())
        self.TPO_MAIL = (re.findall('([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+)', self.data))
        self.phone = re.findall(".*?(\(?\d{3}\D{0,3}\d{3}\D{0,3}\d{4}).*?/", self.data)
        self.phone = (each.replace(" ", "") for each in self.phone)
        self.phone1 = re.findall("^((\+){1}91){1}[1-9]{1}[0-9]{9}$", self.data)
        self.regex_name = re.findall('(?:Mr\.|Mrs\.|Dr\.|Prof\.) ([A-Z]\w+(?=[\s\-][A-Z])(?:[\s\-][A-Z]\w+)+)',
                                     self.data)

    def tpo_email(self):
        for each in list(set(self.TPO_MAIL)):
            if ".in" in each:
                k = each.split(".in")
                self.mail_list.append(k[0] + ".in")
            else:
                self.mail_list.append(each)
        # print("//".join(self.mail_list)
        return "//".join(self.mail_list)

    def tpo_name(self):
        Name = list(set(self.regex_name))
        Name = list(each.replace("\n", " ") for each in Name)
        if len(Name) > 2:
            return "//".join(Name[0:2])
        else:
            return "//".join(Name)

    def tpo_contact(self):
        self.phone_no = list(set(self.phone).union(set(self.phone1)))
        for each in self.phone_no:
            if len(each) < 8:
                self.phone_no.remove(each)
        return "//".join(self.phone_no)


class tpo_link:
    def __init__(self, college_name, link1, ):
        college_name = college_name.replace("|", "%2C")
        self.req = Request(
            'https://www.google.com/search?q=' + 'training+and+placement+contact+of+' + college_name.replace(" ",
                                                                                                             "+") + '+',
            headers={'User-Agent': 'Chrome/5.0'})
        self.web_page = urlopen(self.req).read()
        self.page_soup = soup(self.web_page, "html.parser")
        self.page = str(self.page_soup.prettify(encoding='utf-8'))
        self.page = self.page[2:-1].replace(str("\\n"), "")
        self.page1 = soup(self.page, "html.parser")
        self.containers = self.page1.findAll("div", {"class": "kCrYT"})
        for each in self.containers[:len(self.containers) // 3]:
            try:
                self.t1 = (each.findAll("a")[0])
                self.link = (self.t1.get("href")[7:].split("&"))[0]
                # print(link)
                if link1 in self.link:
                    self.details = tpo_data_site(self.link)
                    self.detail1 = str(self.details.tpo_name().replace('\n',
                                                                       ' ') + ',' + self.details.tpo_contact() + ',' + self.details.tpo_email() + '\n')
                # print(self.details.tpo_name().replace("\n", " "), self.details.tpo_contact(), self.details.tpo_email())
                break
            except:
                pass

    def detail(self):
        return self.detail1


class Tpo_main_site:
    def __init__(self):
        self.df = pd.read_csv("combined_colleges_drop.csv", )
        # print(self.df.info())
        self.df[["COLLEGE_NAME", "WEBSITE_LINK"]].to_csv("colleges_name.csv", index=False, header=True)
        self.f1 = open("colleges_name.csv", 'r')
        self.c = self.f1.readlines()
        self.f2 = open("tpo_contact_details.csv", "w")
        self.f2.write("COLLEGE_NAME,TPO_NAME,TPO_CONTACT,TPO_EMAIL\n")
        for each in self.c[1:]:
            try:
                self.row = each[0] + ",,,\n"
                each = (each.strip("\n")).split(",")
                j = tpo_link(each[0].strip("\n"), each[1])
                self.row = each[0].strip("\n") + "," + j.detail()
            except:
                self.row = each[0] + ",,,\n"
            finally:
                self.f2.write(self.row)
            print(self.row)
        self.f2.close()
        self.f1.close()


if __name__ == "__main__":
    Dte_mainsite()
    Study_guide_middle_site()
    Combination()
    Tpo_main_site()
