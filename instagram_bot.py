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

    #Uygulam açılışında çıkacak olan script yazı
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

    #Giriş fonksiyonu. username ve password yazarak buton ile giriş sağlıyor.
    def logIn(self):
        print("-"*50)
        #self.username = input("Lütfen kullanıcı adınızı giriniz: ")
        #self.password = input("Lütfen şifrenizi giriniz: ")

        self.username = "jamorant001@gmail.com"
        self.password = "123fb123"

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
        self.warningMessage("Girişiniz yapılmıştır.", 1)
        print("-"*50)
        self.Menu()

    #instagram.com sayfası base sayfamız
    def homePage(self):
        home_url = "https://www.instagram.com/"
        self.driver.get(home_url)

    #kullanıcıya renkli uyarı mesajı veren fonksiyon yapısı
    def warningMessage(self, mesaj, durum):
            if int(durum) == 1:
                warning= colored(mesaj, "green")
            elif int(durum) == 2:
                warning=  colored(mesaj, "red")
            elif int(durum) == 3:
                warning=  colored(mesaj, "blue")
            print(warning)

    #Arama fonksiyonu kullanıcıdan aranacak kelimeyi alıp 
    #arama kutusuna yazıyor ve ilk gelen sonuca tıklıyor.
    def search(self, hashtag):
        self.homePage()
        self.hashtag = hashtag
        searchInput = self.driver.find_element_by_class_name("XTCLo").send_keys(self.hashtag, Keys.ENTER)
        time.sleep(3)
        searchAccount = self.driver.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[2]/div[4]/div/a[1]/div/div[2]")
        #searchAccount = self.driver.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[2]/div[3]/div[2]/div/a[1]/div")
        searchAccount.click()
        time.sleep(5)

    #Anasayfaya dönerek sırayla story izlemeye başlıyor.
    def watchStory(self):
        home_url = "https://www.instagram.com/"
        self.driver.get(home_url)
        time.sleep(3)
        self.warningMessage("Story sekmesindeyim.", 3)
        #stories = self.driver.find_element_by_xpath("//*[@id='react-root']/section/main/section/div[1]/div[1]/div/div/div/div/ul/li[3]")
        stories = self.driver.find_element_by_xpath("//*[@id='react-root']/section/main/section/div[1]/div[1]/div/div/div/div/ul/li[3]/div/button")
        stories.click()
        self.warningMessage("izliyorum", 3)
        time.sleep(100)

    #kullanıcı ismi isteyerek profilindeki son postu beğenen fonksiyon yapısı
    def lastPostLike(self):
        userPost = input("Beğenmek istediğiniz kullanıcı: ")
        self.search(userPost)
        self.warningMessage("Kullanıcı bulundu.", 1)
        userLikePost = self.driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div[3]/article/div[1]/div/div[1]/div[1]/a").click()
        time.sleep(3)
        likeButton = self.driver.find_element_by_xpath("/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[1]/button/div/span").click()
        self.warningMessage("Foto beğenildi.", 1)

        exit_button = self.driver.find_element_by_xpath("/html/body/div[5]/div[3]/button")
        exit_button.click()

    #kullanıcı ismi isteyerek profilindeki postları gezen fonksiyon yapısı
    def photoSorf(self):
        userPost = input("Kullanıcı adı: ")
        self.search(userPost)
        self.warningMessage("Kullanıcı bulundu.", 1)

        posts_numbers = self.driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[1]/span/span").text
        posts_numbers = int(posts_numbers)
        print(posts_numbers)

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
            print("Kullanıcının herhangi bir gönderisi yoktur.")

        exit_button = self.driver.find_element_by_xpath("/html/body/div[5]/div[3]/button")
        exit_button.click()

    #kullanıcı istatistiklerini alan fonksiyon yapısı
    #kullanıcı bilgisi karşıdan alınır. (search metodu ile bulunur)
    #stats olarak (username - post sayısı - takipçi- takip edilen - )
    def userStats(self):
        userStat = input("Aradığınız kullanıcı: ")
        self.search(userStat)
        print("-"*50)
        self.warningMessage("Kullanıcı bulundu.", 1)
        print("-"*50)

        self.isPublic()
        
        if(self.is_public == True):
            self.isFollowing()
            if(self.is_following == True):
                #Takip edilen durum
                userName = self.driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/div[1]/h2").text
                posts_numbers = self.driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[1]/span/span").text
                followers_numbers = self.driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a/span").text
                following_numbers = self.driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[3]/a/span").text

                self.warningMessage("Kullanıcı...:   " + userName + " (Takip ediliyor) ", 3)
                print("Gönderi.....:   " + posts_numbers)
                print("Takipçi.....:   " + followers_numbers)
                print("Takip.......:   " + following_numbers)
            else:
                #Takip edilmeyen durum
                userName = self.driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/div[1]/h2").text
                posts_numbers = self.driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[1]/span/span").text
                followers_numbers = self.driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a/span").text
                following_numbers = self.driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[3]/a/span").text

                self.warningMessage("Kullanıcı...:   " + userName + " (Takip edilmiyor) ", 2)
                print("Gönderi.....:   " + posts_numbers)
                print("Takipçi.....:   " + followers_numbers)
                print("Takip.......:   " + following_numbers)
        else:
            self.warningMessage("Bu hesap gizlidir.", 2)

    #takip edilip edilmeme kontrolü yapan fonksiyon yapısı
    def isFollowing(self):
        follow_button = self.driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/div[1]/div[2]/div/div/div/span/span[1]/button").text
        #follow_button = self.driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/div[1]/div[2]/div/div[2]/div/span/span[1]/button").text
        if (follow_button == "Takip Et"):
            self.is_following = False
        else:
            self.is_following = True
    
    #photoSorf() fonksiyo içinde bir sonraki posta geçen yardımcı fonksiyon yapısı
    def nextPost(self, i):
        if(i==0):
            next_post = self.driver.find_element_by_xpath("/html/body/div[5]/div[1]/div/div/a")
        else:
            next_post = self.driver.find_element_by_xpath("/html/body/div[5]/div[1]/div/div/a[2]")
        next_post.click()

    #public - private durumu kontrolü yapan fonksiyon yapısı
    def isPublic(self):
        self.is_public = True
        """
        userPost = input("Kullanıcı: ")
        self.search(userPost)
        self.warningMessage("Kullanıcı bulundu.", 1)
        """
        if "Bu Hesap Gizli" in self.driver.page_source:
            self.is_public = False
        else:
            self.is_public = True

    #kullanıcı ismi isteyerek takip ettiklerinin listesini veren fonksiyon yapısı
    def followingList(self):

        """
        userStat = input("Aradığınız kullanıcı: ")
        self.search(userStat)
        print("-"*50)
        self.warningMessage("Kullanıcı bulundu.", 1)
        print("-"*50)
        """

        self.isPublic()

        if (self.is_public==True):
            flistbutton = self.driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[3]/a")
            flistbutton.click()
            time.sleep(3)

            for index in range(1,11):
                #time.sleep(3)
                flist = self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]/ul/div/li[{0}]/div/div[2]/div/div/div/span/a".format(index)).text
                print("{0}-  {1}".format(index, flist))
            exit_button = self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div[1]/div/div[2]/button")
            exit_button.click()
        else:
            self.warningMessage("Bu hesap gizli olduğu için takipçilerini listenemez.", 2)


    #kullanıcı urlsinin çalışıp çalışmadığını kontrol eden fonksiyon yapısı
    def accountControl(self, account):
        self.account_url = self.url + account
        print(self.account_url) #sil
        response = requests.get(self.account_url)
        if (response.status_code == 404):
            print("False")  #sil
            return False
        else:
            print("True")   #sil
            return True

    def follow(self, account):
        self.account_url = self.url + account
        print(self.account_url) #sil
        self.driver.get(self.account_url)
        self.isFollowing()

        if (self.is_following == True):
            self.warningMessage("Takip ediyorsun", 1)
            time.sleep(3)
        else:
            print("Takip etmiyosun")
            self.isPublic()

            if (self.is_public == True):
                follow_button = self.driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/div[1]/div[2]/div/div/div/span/span[1]/button")
                follow_button.click()
                self.warningMessage("Takip ettim patron", 3)
            else:
                self.warningMessage("Bu hesap gizlidir", 2)

    def followList(self, account_list):
        for item in range(len(account_list)):
            self.account_url = self.url + account_list[item]
            print(self.account_url)
            self.driver.get(self.account_url)
            self.isFollowing()
            print("1")

            if(self.is_following == True):
                self.warningMessage("Takip ediyorsun", 1)
            
            else:
                self.warningMessage("Takip etmiyorsun", 2)

                follow_button = self.driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/div[1]/div[2]/div/div/div/span/span[1]/button")
                follow_button.click()
                self.warningMessage("Takip ettim patron", 3)

    #private olayını ayarla
    def unfollow(self, account):
        self.account_url = self.url + account
        print(self.account_url) #sil
        self.driver.get(self.account_url)
        self.isFollowing()

        if (self.is_following == False):
            self.warningMessage("Takip etmiyosun", 2)
            time.sleep(3)
        else: 
            print("Takip ediyosun")
            unf_button = self.driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/div[1]/div[2]/div/div[2]/div/span/span[1]/button")
            unf_button.click()
            time.sleep(1)
            unf_button2 = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[1]")
            unf_button2.click()
            self.warningMessage("Takipten çıktınız", 1)
    
    def Menu(self):
        while True:
            print("#"*50)
            print("#               1- Arama Yap                     #")
            print("#               2- Story İzle                    #")
            print("#               3- Postları Gez                  #")
            print("#               4- Son Post Beğen                #")
            print("#               5- Kullanıcı İstatistikleri      #")
            print("#               6- Hesap Gizli Mi?               #")
            print("#               7- Takip Listesi?                #")
            print("#               8- Çıkış Yap                     #")
            print("#               9- url kontrol                   #")
            print("#               10- follow                       #")
            print("#               11- unfollow                     #")
            print("#               12- toplu follow                 #")
            print("#"*50)
            choice = input("Lütfen seçiminizi yapınız: ")
            
            if(choice == "1"):
                hashtag = input("Lütfen aramak istediğiniz kelimeyi giriniz: ")
                self.search(hashtag)
                self.warningMessage("Arama Yapılıyor...", 3)
                time.sleep(3)
                self.warningMessage("Arama Yapıldı.", 1)
            
            elif(choice == "2"):
                self.warningMessage("Story izleme işlemi başladı.", 3)
                self.watchStory()

            elif(choice == "3"):
                self.photoSorf()
                self.warningMessage("Postları gezdim.", 1)

            elif(choice == "4"):
                self.warningMessage("Girdim buraya", 1)
                self.lastPostLike()
                self.warningMessage("Başardım", 1)

            elif(choice == "5"):
                self.warningMessage("Girdim buraya", 1)
                self.userStats()
                self.warningMessage("Stats Başarılı", 1)
            
            elif(choice == "6"):
                self.isPublic()

            elif(choice == "7"):
                self.followingList()

            elif(choice == "8"):
                self.driver.quit()
                exit()
            
            elif(choice == "9"):
                self.accountControl("merthakanyandas")
            
            #follow
            elif(choice == "10"):
                self.follow("dimitrispelkas")
                #self.follow("selim_caan")
            
            #unfollow
            elif(choice == "11"):
                self.unfollow("dimitrispelkas")
                self.unfollow("laclippers")
                #self.unfollow("selim_caan")

            #toplu follow
            elif(choice == "12"):
                follow_list = ["ozan", "dimitrispelkas", "merthakanyandas", "fcbayern", "fenerbahce", "laclippers"]
                self.followList(follow_list)

            else:
                self.warningMessage("Yanlış seçim yaptınız.", 2)
                self.Menu()


instagramBot = Instagram()
#instagramBot.logIn()
