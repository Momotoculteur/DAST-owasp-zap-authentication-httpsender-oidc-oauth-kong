import java.net.HttpCookie as HttpCookie
import org.openqa.selenium.By as By
from synchronize import make_synchronized
import org.openqa.selenium.firefox.FirefoxDriver as FirefoxDriver;
import org.openqa.selenium.firefox.FirefoxOptions as FirefoxOptions;
import org.openqa.selenium.support.ui.WebDriverWait as WebDriverWait;
import org.openqa.selenium.support.ui.ExpectedConditions as ExpectedConditions;
import org.zaproxy.zap.extension.script.ScriptVars as GlobalVariables


# GLOBAL VARIABLES
COOKIE_NAME = "session"
URL_LOGIN = "https://monsite.fr/login"
COOKIE = "COOKIE"


def sendingRequest(msg, initiator, helper):
    '''
    Appelé a chaque requête, lors d'en envoi
    '''

    print('sendingRequest called for url=' +
          msg.getRequestHeader().getURI().toString())

    cookieInCurrentSession = GlobalVariables.getGlobalCustomVar(COOKIE)

    if cookieInCurrentSession is None:
        login()

    setCookieInRequest(msg)


def responseReceived(msg, initiator, helper):
    '''
    Appelé a chaque requête, lors des réponses
    Non utile pour le cadre de notre cours
    '''

    print('responseReceived called for url=' +
          msg.getRequestHeader().getURI().toString())


def login():
    '''
    Fonction permettant se récupérer le cookie de session après une connexion via selenium
    '''
    
    firefoxOptions = FirefoxOptions()
    #firefoxOptions.addArguments("--window-size=1920,1080")
    #firefoxOptions.addArguments("--disable-gpu")
    #firefoxOptions.addArguments("--disable-extensions")
    #firefoxOptions.addArguments("--proxy-server='direct://'")
    #firefoxOptions.addArguments("--proxy-bypass-list=*")
    #firefoxOptions.addArguments("--start-maximized")
    firefoxOptions.addArguments("--headless")
    webDriver = FirefoxDriver(firefoxOptions)

    webDriver.get(URL_LOGIN)

    timeOut = 3
    waiter = WebDriverWait(webDriver, timeOut)

    waiter.until(ExpectedConditions.visibilityOfElement(By.id("login-form")))
    webDriver.findElement(By.name("email")).sendKeys("bastien@hotmail.com")
    webDriver.findElement(By.name("pass")).sendKeys("123")
    webDriver.findElement(By.name("login-button")).click()

    waiter.until(ExpectedConditions.visibilityOfElement(By.id("welcome-page")))

    GlobalVariables.setGlobalCustomVar(COOKIE, 
                                        str(webDriver.manage().getCookieNamed(COOKIE_NAME).getValue()))


def setCookieInRequest(msg):
    '''
    Injection du cookie de session stocké en var global dans chaque requête
    '''

    msg.getRequestHeader().setCookies([GlobalVariables.getGlobalCustomVar(COOKIE)])

def setBearerInRequest(msg):
    '''
    Injection Json Web Token(bearer) de session stocké en var global dans chaque requête
    '''
    
    msg.getRequestHeader().setHeader("Authorization", "Bearer " + GlobalVariables.getGlobalCustomVar(ACCESS_TOKEN));
    
'''
NON TESTé

# Custom pour injecter le bearer token en header de requête
def sendingRequest(msg, initiator, helper):
    accessToken = GlobalVariables.getGlobalCustomVar(ACCESS_TOKEN)

    # Token KO ou expiré
    if accessToken is None or tokenHasExpired():
        login()
        
    #Token OK
    setTokenInRequest(msg)
    
# Custom afin de vérifier le refresh de l'access token
def tokenHasExpired(accessToken):
    accessTokenCreation = GlobalVariables.getGlobalCustomVar(ACCESS_TOKEN_CREATION);

    currentTime = time.time();
    difference = currentTime - accessTokenCreation;

    accessTokenExpiryInSeconds = GlobalVariables.getGlobalCustomVar(ACCESS_TOKEN_EXPIRY);
    if difference > accessTokenExpiryInSeconds:
        print "token expiré"
        return True;
    else:
      print "token OK"
      return False;
'''