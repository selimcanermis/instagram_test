from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ChromeOptions
import time
from termcolor import colored
import requests


class Instagram:
    def __init__(self):
        option = ChromeOptions()
        option.add_argument("--disable-infobars")
        option.add_argument("start-maximized")
        option.add_argument("--disable-extensions")
        option.add_argument("--disable-notifications")

        self.driver = webdriver.Chrome(chrome_options=option)

        self.is_public = True
        self.url = "https://www.instagram.com/"
        self.script()
        self.logIn()

    # ✔ ✔ ✔ ✔ ✔ ✔ ✔ ✔ ✔ ✔ ✔ ✔
    # Uygulama acilisinda cikacak olan script yazi
    def script(self):
        print("#"*50)
        print("#                  INSTAGRAM BOT                 #")
        print("#"*50)
        print("#author           :Selim Can ERMİŞ               #")
        print("#email            :ermisselimcan<@>gmail.com     #")
        print("#date             :06.11.2020                    #")
        print("#python_version   :3.8.6                         #")
        print("#selenium_version :3.141.0                       #")
        print("#"*50)

    # ✔ ✔ ✔ ✔ ✔ ✔ ✔ ✔ ✔ ✔ ✔ ✔
    # Giris fonksiyonu. username ve password yazarak buton ile giris sagliyor.
    def logIn(self):
        print("-"*50)
        self.username = input("lutfen kullanici adinizi giriniz: ")
        self.password = input("lutfen sifrenizi giriniz: ")

        

        login_url = "https://www.instagram.com/"
        self.driver.get(login_url)
        time.sleep(3)

        usernameInput = self.driver.find_element_by_name("username").send_keys(self.username)
        passwordInput = self.driver.find_element_by_name("password").send_keys(self.password)
        loginbuttonInput = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button").click()
        time.sleep(3)

        try:
            not_now = self.driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/div/div/button")
            not_now.click()
        except:
            pass

        time.sleep(3)
        print("-"*50)
        self.warningMessage("Girisiniz yapilmistir.", 1)
        print("-"*50)
        self.Menu()

    # ✔ ✔ ✔ ✔ ✔ ✔ ✔ ✔ ✔ ✔ ✔ ✔
    # instagram.com sayfasi = base sayfamiz
    def homePage(self):
        home_url = "https://www.instagram.com/"
        self.driver.get(home_url)

    # ✔ ✔ ✔ ✔ ✔ ✔ ✔ ✔ ✔ ✔ ✔ ✔
    # kullaniciya renkli uyari mesaji veren fonksiyon yapisi
    def warningMessage(self, mesaj, durum):
        if int(durum) == 1:
            warning = colored(mesaj, "green")
        elif int(durum) == 2:
            warning = colored(mesaj, "red")
        elif int(durum) == 3:
            warning = colored(mesaj, "blue")
        print(warning)

    # ✔ ✔ ✔ ✔ ✔ ✔ ✔ ✔ ✔ ✔ ✔ ✔
    # Arama fonksiyonu kullanicidan aranacak kelimeyi alip
    # arama kutusuna yaziyor ve ilk gelen sonuca tikliyor.
    def search(self, hashtag):
        self.homePage()
        self.hashtag = hashtag
        searchInput = self.driver.find_element_by_class_name("XTCLo").send_keys(self.hashtag, Keys.ENTER)
        time.sleep(3)
        searchAccount = self.driver.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[2]/div[4]/div/a[1]/div/div[2]")
        searchAccount.click()
        time.sleep(5)

    # Anasayfaya donerek sirayla story izlemeye basliyor.
    def watchStory(self):
        self.homepage()
        time.sleep(3)
        self.warningMessage("Story sekmesindeyim.", 3)
        #stories = self.driver.find_element_by_xpath("//*[@id='react-root']/section/main/section/div[1]/div[1]/div/div/div/div/ul/li[3]")
        stories = self.driver.find_element_by_xpath("//*[@id='react-root']/section/main/section/div[1]/div[1]/div/div/div/div/ul/li[3]/div/button")
        stories.click()
        self.warningMessage("izliyorum", 3)
        time.sleep(100)

    # ✔ ✔ ✔ ✔ ✔ ✔ ✔ ✔ ✔ ✔ ✔ ✔
    # kullanici ismi isteyerek profilindeki son postu begenen fonksiyon yapisi
    def lastPostLike(self):
        userPost = input("Begenmek istediginiz kullanici: ")
        self.search(userPost)
        self.warningMessage("({0}) => Kullanıcı bulundu.".format(userPost), 1)
        userLikePost = self.driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div[3]/article/div[1]/div/div[1]/div[1]/a").click()
        time.sleep(3)
        likeButton = self.driver.find_element_by_xpath("/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[1]/button/div/span").click()
        self.warningMessage("({0}) => Foto begenildi.".format(userPost), 1)
        

        exit_button = self.driver.find_element_by_xpath("/html/body/div[5]/div[3]/button")
        exit_button.click()

    # ✔ ✔ ✔ ✔ ✔ ✔ ✔ ✔ ✔ ✔ ✔ ✔
    # kullanici ismi isteyerek profilindeki postlari gezen fonksiyon yapisi
    def photoSorf(self):
        userPost = input("Kullanici adi: ")
        self.search(userPost)
        self.warningMessage("({0}) => Kullanici bulundu.".format(userPost), 1)

        posts_numbers = self.driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[1]/span/span").text
        posts_numbers = int(posts_numbers)
        print(posts_numbers)

        self.isPublic()

        if (self.is_public == True):
            userLikePost = self.driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div[3]/article/div[1]/div/div[1]/div[1]/a").click()
            time.sleep(3)

            if (posts_numbers >= 10):
                for i in range(10):
                    time.sleep(5)
                    self.nextPost(i)
            elif (posts_numbers < 10):
                for i in range(posts_numbers-1):
                    time.sleep(5)
                    self.nextPost(i)
            elif (posts_numbers == 1):
                self.nextPost(0)
            else:
                self.warningMessage("({0}) => Kullanicinin herhangi bir gonderisi yoktur.".format(userPost), 2)
            exit_button = self.driver.find_element_by_xpath("/html/body/div[5]/div[3]/button")
            exit_button.click()
            self.warningMessage("Postlari gezdim.", 1)
        else:
            self.warningMessage("({0}) => Bu hesap gizlidir.".format(userPost), 2)


    # ✔ ✔ ✔ ✔ ✔ ✔ ✔ ✔ ✔ ✔ ✔ ✔
    # kullanici istatistiklerini alan fonksiyon yapisi
    # kullanici bilgisi karsidan alinir. (search metodu ile bulunur)
    # stats olarak (username - post sayisi - takipci- takip edilen - )
    def userStats(self):
        userStat = input("Aradiginiz kullanici: ")
        self.search(userStat)
        print("-"*50)
        self.warningMessage("({0}) => Kullanici bulundu.".format(userStat), 1)
        print("-"*50)

        self.isPublic()

        if(self.is_public == True):
            self.isFollowing()
            if(self.is_following == True):
                # Takip edilen durum
                userName = self.driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/div[1]/h2").text
                userBio = self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/div[2]/span').text
                posts_numbers = self.driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[1]/span/span").text
                followers_numbers = self.driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a/span").text
                following_numbers = self.driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[3]/a/span").text

                self.warningMessage("Kullanici...:   " + userName + " (Takip ediliyor) ", 3)
                print("Bio.........:   " + userBio)
                print("Gonderi.....:   " + posts_numbers)
                print("Takipci.....:   " + followers_numbers)
                print("Takip.......:   " + following_numbers)
            else:
                # Takip edilmeyen durum
                userName = self.driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/div[1]/h2").text
                posts_numbers = self.driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[1]/span/span").text
                followers_numbers = self.driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a/span").text
                following_numbers = self.driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[3]/a/span").text

                self.warningMessage("Kullanici...:   " + userName + " (Takip edilmiyor) ", 2)
                print("Gonderi.....:   " + posts_numbers)
                print("Takipci.....:   " + followers_numbers)
                print("Takip.......:   " + following_numbers)
        else:
            self.warningMessage("({0}) => Bu hesap gizlidir.".format(userStat), 2)

    # ✔ ✔ ✔ ✔ ✔ ✔ ✔ ✔ ✔ ✔ ✔ ✔
    # takip edilip edilmeme kontrolü yapan fonksiyon yapisiu
    def isFollowing(self):
        follow_button = self.driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/div[1]/div[2]/div/div/div/span/span[1]/button").text
        #follow_button = self.driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/div[1]/div[2]/div/div[2]/div/span/span[1]/button").text
        if (follow_button == "Takip Et"):
            self.is_following = False
        else:
            self.is_following = True

    # ✔ ✔ ✔ ✔ ✔ ✔ ✔ ✔ ✔ ✔ ✔ ✔
    # photoSorf() fonksiyon icinde bir sonraki posta gecen yardimci fonksiyon yapisi
    def nextPost(self, i):
        if(i == 0):
            next_post = self.driver.find_element_by_xpath("/html/body/div[5]/div[1]/div/div/a")
        else:
            next_post = self.driver.find_element_by_xpath("/html/body/div[5]/div[1]/div/div/a[2]")
        next_post.click()

    # ✔ ✔ ✔ ✔ ✔ ✔ ✔ ✔ ✔ ✔ ✔ ✔
    # public - private durumu kontrolu yapan fonksiyon yapisi
    def isPublic(self):
        self.is_public = True

        if "Bu Hesap Gizli" in self.driver.page_source:
            self.is_public = False
        else:
            self.is_public = True

    # ✔ ✔ ✔ ✔ ✔ ✔ ✔ ✔ ✔ ✔ ✔ ✔
    # kullanici ismi isteyerek takip ettiklerinin listesini veren fonksiyon yapisi
    def followingList(self):
        _user = input("Aradiginiz kullanici: ")
        self.search(_user)
        print("-"*50)
        self.warningMessage("({0}) => Kullanici bulundu.".format(_user), 1)
        print("-"*50)
    
        self.isPublic()

        if (self.is_public == True):
            flistbutton = self.driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[3]/a")
            flistbutton.click()
            time.sleep(3)
            fbody  = self.driver.find_element_by_xpath("//div[@class='isgrP']")
            scroll = 0
            while scroll < 20: 
                self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', fbody)
                time.sleep(1)
                scroll += 1
            time.sleep(3)
            flist = self.driver.find_elements_by_css_selector('div.PZuss > li ')
            
            index = 0
            while (index <len(flist)):
                temp = flist[index].text
                fsplit = temp.split()
                print("{0}- {1}".format(index, fsplit[0]))
                index += 1

            exit_button = self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div[1]/div/div[2]/button")
            exit_button.click()
        else:
            self.warningMessage("({0}) => Bu hesap gizlidir.".format(_user), 2)
     
    # ✔ ✔ ✔ ✔ ✔ ✔ ✔ ✔ ✔ ✔ ✔ ✔
    # kullanıcı urlsinin calisip calismadigini kontrol eden fonksiyon yapisi
    def accountControl(self, account):
        self.account_url = self.url + account
        print(self.account_url)  # sil
        response = requests.get(self.account_url)
        if (response.status_code == 404):
            print("False")  # sil
            return False
        else:
            print("True")  # sil
            return True

    # ✔ ✔ ✔ ✔ ✔ ✔ ✔ ✔ ✔ ✔ ✔ ✔
    def follow(self, account):
        self.account_url = self.url + account
        self.driver.get(self.account_url)
        self.isPublic()

        if (self.is_public == True):
            self.isFollowing()
            if (self.is_following == True):
                self.warningMessage("({0}) => Takip ediyorsun.".format(account), 1)
                time.sleep(3)
            else:
                print("Takip etmiyorsun")
                follow_button = self.driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/div[1]/div[2]/div/div/div/span/span[1]/button")
                follow_button.click()
                self.warningMessage("({0}) => Takip edildi.".format(account), 3)
        else:
            self.warningMessage("({0}) => Bu hesap gizlidir.".format(account), 2)

    # ✔ ✔ ✔ ✔ ✔ ✔ ✔ ✔ ✔ ✔ ✔ ✔
    def followList(self, account_list):
        for item in range(len(account_list)):
            self.account_url = self.url + account_list[item]
            print(self.account_url)
            self.driver.get(self.account_url)
            self.isFollowing()
            print("1")

            if(self.is_following == True):
                self.warningMessage("({0}) => Takip ediyorsun.".format(account_list[item]), 1)

            else:
                self.warningMessage("({0}) => Takip etmiyorsun.".format(account_list[item]), 2)

                follow_button = self.driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/div[1]/div[2]/div/div/div/span/span[1]/button")
                follow_button.click()
                self.warningMessage("({0}) => Takip edildi.".format(account_list[item]), 3)

    # ✔ ✔ ✔ ✔ ✔ ✔ ✔ ✔ ✔ ✔ ✔ ✔
    # private olayini ayarla
    def unfollow(self, account):
        self.account_url = self.url + account
        self.driver.get(self.account_url)
        self.isPublic()
        

        if (self.is_public == True):
            self.isFollowing()
            if (self.is_following == False):
                self.warningMessage("({0}) => Takip etmiyorsun.".format(account), 2)
                time.sleep(3)
            else:
                print("Takip ediyosun")
                unf_button = self.driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/div[1]/div[2]/div/div[2]/div/span/span[1]/button")
                unf_button.click()
                time.sleep(2)
                unf_button2 = self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div/div[3]/button[1]")
                time.sleep(2)

                if unf_button2.text == "Takibi Birak":
                    unf_button2.click()
                    time.sleep(2)
                    self.warningMessage("({0}) => Takipten ciktiniz.".format(account), 1)
                else:
                    self.warningMessage("Hata aldiniz", 2)
        else:
            self.warningMessage("({0}) => Bu hesap gizlidir.".format(account), 2)

    # ✔ ✔ ✔ ✔ ✔ ✔ ✔ ✔ ✔ ✔ ✔ ✔  
    def myProfilStats(self):
        self.homePage()
        profil = self.driver.find_element_by_class_name("gmFkV").send_keys(Keys.ENTER)
        time.sleep(3)
        userName = self.driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/div[1]/h2").text
        userBio = self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/div[2]').text
        posts_numbers = self.driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[1]/span/span").text
        followers_numbers = self.driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a/span").text
        following_numbers = self.driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[3]/a/span").text

        self.warningMessage("Kullanici...:   " + userName , 3)
        print("Bio.........:   " + userBio)
        print("Gonderi.....:   " + posts_numbers)
        print("Takipci.....:   " + followers_numbers)
        print("Takip.......:   " + following_numbers)

    # ✔ ✔ ✔ ✔ ✔ ✔ ✔ ✔ ✔ ✔ ✔ ✔  
    def Menu(self):
        while True:
            print("#"*50)
            print("#            \u2714 1- Arama Yap                      #")
            print("#             2- Story İzle                       #")
            print("#            \u2714 3- Postlari Gez                   #")
            print("#            \u2714 4- Son Post Begen                 #")
            print("#            \u2714 5- Kullanici İstatistikleri       #")
            print("#            \u2714 6- Takip Listesi?                 #")
            print("#            \u2714 7- Kendi Profil Istatistiklerin   #")
            print("#            \u2714 8- Cikis Yap                      #")
            print("#            \u2714 9- url kontrol                    #")
            print("#            \u2714 10- follow                        #")
            print("#            \u2714 11- unfollow                      #")
            print("#            \u2714 12- toplu follow                  #")
            print("#"*50)
            choice = input("Lütfen seciminizi yapiniz: ")

            if(choice == "1"):
                hashtag = input("Lutfen aramak istediginiz kelimeyi giriniz: ")
                self.warningMessage("Arama Yapiliyor...", 3)
                self.search(hashtag)
                self.warningMessage("Arama Yapildi.", 1)

            elif(choice == "2"):
                self.warningMessage("Story izleme islemi basladi.", 3)
                self.watchStory()

            elif(choice == "3"):
                self.photoSorf()

            elif(choice == "4"):
                self.warningMessage("Girdim buraya", 1)
                self.lastPostLike()
                self.warningMessage("Basardim", 1)

            elif(choice == "5"):
                self.warningMessage("Girdim buraya", 1)
                self.userStats()
                self.warningMessage("Stats Basarili", 1)

            elif(choice == "6"):
                self.followingList()

            elif(choice == "7"):
                self.myProfilStats()

            elif(choice == "8"):
                self.driver.quit()
                exit()

            elif(choice == "9"):
                self.accountControl("merthakanyandas")

            # follow
            elif(choice == "10"):
                self.follow("dimitrispelkas")
                self.follow("stevengerrard")
                self.follow("selim_caan")

            # unfollow
            elif(choice == "11"):
                self.unfollow("dimitrispelkas")
                self.unfollow("laclippers")
                self.unfollow("selim_caan")

            # toplu follow
            elif(choice == "12"):
                follow_list = ["ozan", "dimitrispelkas", "merthakanyandas", "fcbayern", "fenerbahce", "laclippers"]
                self.followList(follow_list)

            else:
                self.warningMessage("Yanlis secim yaptiniz.", 2)
                self.Menu()


instagramBot = Instagram()
# instagramBot.logIn()
